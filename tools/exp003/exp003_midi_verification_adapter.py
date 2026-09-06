"""Adaptador exacto de verificación MIDI para EXP-003.

No escribe MIDI ni WAV. Lee el artefacto de eventos congelado, construye el
SongPlanV2 corregido y materializa un ``Song`` en memoria con PPQ explícito.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import replace
from fractions import Fraction
from pathlib import Path
from typing import Any

from music_engine.domain import Duration, Position
from music_engine.songplan.v2 import (
    materialize_song_plan_v2,
    song_plan_v2_from_dict,
    validate_song_plan_v2,
)
from music_engine.timing import duration_to_ticks, position_to_ticks


PPQ = 1000
TEMPO_BPM = 120
EVENT_SHA256 = "D25B504CF5CB57749B4ECC51C0145BA83827A7BC452AE4939218338A3C6E9BF2"


def _plan_dict(events: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[str, list[dict[str, Any]]] = {"R1": [], "R2": []}
    for event in events:
        group = event["event_id"].split("-", 1)[0]
        groups[group].append(event)
    if sorted(groups) != ["R1", "R2"] or any(len(value) != 4 for value in groups.values()):
        raise ValueError("el artefacto canónico no contiene exactamente R1 y R2 de cuatro voces")

    def chord(group: str, beat: str) -> dict[str, Any]:
        values = groups[group]
        if any(value["duration_seconds"] != 0.48 for value in values):
            raise ValueError("duración canónica inesperada")
        if any(value["velocity"] != 96 for value in values):
            raise ValueError("velocity canónica inesperada")
        return {
            "bar": 1,
            "beat": beat,
            "duration": "6/25",
            "pitches": [f"{_pitch_name(value['pitch_midi'])}" for value in values],
            "velocity": 96,
        }

    return {
        "schema_version": "2.0",
        "name": "EXP003_CANARY_002_F01_LOW",
        "tempo": TEMPO_BPM,
        "time_signature": "4/4",
        "tonic": "C",
        "mode": "ionian",
        "style": "exp003_technical_canary",
        "arrangement": {
            "sections": [{"id": "canary", "start_bar": 1, "bar_count": 1, "energy": 0.5}],
            "harmony_assignments": [],
        },
        "tracks": [{
            "id": "exp003_canary_pitched",
            "type": "pitched",
            "role": "technical_canary",
            "motifs": [{
                "id": "f01_low_events",
                "events": [chord("R1", "3/2"), chord("R2", "5/2")],
            }],
            "section_assignments": [{"section_id": "canary", "motif_id": "f01_low_events"}],
        }],
    }


def _pitch_name(midi_pitch: int) -> str:
    # This is a mechanical MIDI-pitch-to-domain-pitch conversion, not a
    # voicing decision. The event artifact remains the source of truth.
    from music_engine.domain import Pitch

    return str(Pitch.from_absolute_semitone(midi_pitch))


def load_canonical_events(path: Path) -> list[dict[str, Any]]:
    document = json.loads(path.read_text(encoding="utf-8"))
    if document["item_family_id"] != "EXP003-F01" or document["condition"] != "LOW_SELECTED":
        raise ValueError("artefacto canónico incorrecto para F01 LOW")
    return document["events"]


def build_song(events_path: Path):
    plan = song_plan_v2_from_dict(_plan_dict(load_canonical_events(events_path)))
    validation = validate_song_plan_v2(plan)
    if not validation.valid:
        raise AssertionError(f"SongPlanV2 inválido: {validation.issues}")
    song = materialize_song_plan_v2(plan)
    song = replace(song, ppq=PPQ)
    return plan, song


def run_non_media_tests(events_path: Path) -> None:
    plan, song = build_song(events_path)
    assert plan.tempo.bpm == TEMPO_BPM
    assert song.ppq == PPQ
    assert 1 <= song.ppq <= 32767

    notes = song.tracks[0].notes
    assert len(notes) == 8
    assert [note.pitch.absolute_semitone for note in notes] == [48, 52, 60, 67, 43, 55, 62, 71]
    assert [note.velocity for note in notes] == [96] * 8

    expected_positions = [500] * 4 + [1500] * 4
    expected_offs = [1460] * 4 + [2460] * 4
    assert [position_to_ticks(note.position, ppq=PPQ, signature=plan.time_signature) for note in notes] == expected_positions
    assert [position_to_ticks(note.position, ppq=PPQ, signature=plan.time_signature) + duration_to_ticks(note.duration, ppq=PPQ) for note in notes] == expected_offs
    assert duration_to_ticks(Duration(Fraction(6, 25)), ppq=PPQ) == 960

    assert [note.position.beat for note in notes[::4]] == [Fraction(3, 2), Fraction(5, 2)]
    assert [note.duration.whole_notes for note in notes] == [Fraction(6, 25)] * 8
    assert all(isinstance(value, int) for value in expected_positions + expected_offs)


def main() -> int:
    parser = argparse.ArgumentParser(description="Pruebas no multimedia del adaptador MIDI EXP-003")
    parser.add_argument("--events", type=Path, default=Path("experiments/EXP-003/technical-canary/EXP003-CANARY-001-F01-LOW.events.json"))
    args = parser.parse_args()
    run_non_media_tests(args.events)
    print("PASS: EXP-003 MIDI adapter non-media tests")
    print(f"PPQ={PPQ}; event_sha256={EVENT_SHA256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
