"""Adaptador genérico exacto para las 24 combinaciones de EXP-003.

Lee el manifiesto de ítems congelado y solo traduce la realización ya
seleccionada a eventos canónicos y SongPlanV2. No escribe MIDI/WAV ni invoca
el renderer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import yaml
from music_engine.domain import Duration, Position
from music_engine.songplan.v2 import song_plan_v2_from_dict, validate_song_plan_v2
from music_engine.timing import duration_to_ticks, position_to_ticks


EXPECTED_FREEZE_SHA256 = "940D317684BF17BCB5CAF3EA9E08CCE4FE8C428BC1CD63F4C2004D32739E5B64"
EXPECTED_CANARY_F01_LOW_SHA256 = "D25B504CF5CB57749B4ECC51C0145BA83827A7BC452AE4939218338A3C6E9BF2"
PPQ = 1000
TEMPO_BPM = 120
CONDITIONS = ("LOW_SELECTED", "HIGH_SELECTED")
FAMILY_IDS = tuple(f"EXP003-F{i:02d}" for i in range(1, 13))


def _condition_suffix(condition: str) -> str:
    if condition not in CONDITIONS:
        raise ValueError(f"condición no soportada: {condition}")
    return condition.removesuffix("_SELECTED")


def _load_manifest(path: Path) -> dict[str, Any]:
    actual = hashlib.sha256(path.read_bytes()).hexdigest().upper()
    if actual != EXPECTED_FREEZE_SHA256:
        raise ValueError(f"hash del item freeze incorrecto: {actual}")
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    if document.get("experiment_id") != "EXP-003":
        raise ValueError("manifiesto incorrecto")
    families = document.get("families")
    if not isinstance(families, list) or len(families) != 12:
        raise ValueError("el manifiesto debe contener 12 familias")
    return document


def _family(manifest: dict[str, Any], family_id: str) -> dict[str, Any]:
    if family_id not in FAMILY_IDS:
        raise ValueError(f"familia no soportada: {family_id}")
    matches = [family for family in manifest["families"] if family["item_family_id"] == family_id]
    if len(matches) != 1:
        raise ValueError(f"familia ausente o duplicada: {family_id}")
    return matches[0]


def _event(event_id: str, pitch: int, onset: str) -> dict[str, Any]:
    return {
        "event_id": event_id,
        "pitch_midi": pitch,
        "onset_seconds": float(Fraction(onset)),
        "duration_seconds": 0.48,
        "velocity": 96,
    }


def build_event_document(manifest_path: Path, family_id: str, condition: str) -> dict[str, Any]:
    manifest = _load_manifest(manifest_path)
    family = _family(manifest, family_id)
    suffix = _condition_suffix(condition)
    r1 = family["R1_pitches_midi"]
    r2 = family[f"R2_{suffix}_pitches_midi"]
    if len(r1) != 4 or len(r2) != 4:
        raise ValueError("cada realización debe contener exactamente cuatro pitches")
    events = [_event(f"R1-V{i}", pitch, "1/4") for i, pitch in enumerate(r1, 1)]
    events += [_event(f"R2-V{i}", pitch, "3/4") for i, pitch in enumerate(r2, 1)]
    return {
        "experiment_id": "EXP-003",
        "canary_id": None,
        "item_family_id": family_id,
        "condition": condition,
        "sample_rate_hz": 48000,
        "duration_seconds": 2.0,
        "events": events,
    }


def serialize_event_document(document: dict[str, Any]) -> bytes:
    """Serialización estable compatible con el artifact F01 LOW histórico."""
    lines = [
        "{",
        f'  "experiment_id": {json.dumps(document["experiment_id"])},',
        f'  "canary_id": {json.dumps(document["canary_id"])},',
        f'  "item_family_id": {json.dumps(document["item_family_id"])},',
        f'  "condition": {json.dumps(document["condition"])},',
        f'  "sample_rate_hz": {document["sample_rate_hz"]},',
        f'  "duration_seconds": {document["duration_seconds"]},',
        '  "events": [',
    ]
    lines.extend(
        "    " + json.dumps(event, ensure_ascii=False, separators=(", ", ": ")) + ("," if i < len(document["events"]) - 1 else "")
        for i, event in enumerate(document["events"])
    )
    lines.extend(["  ]", "}", ""])
    return "\n".join(lines).encode("utf-8")


def build_songplan_dict(document: dict[str, Any]) -> dict[str, Any]:
    events = document["events"]
    return {
        "schema_version": "2.0",
        "name": f"{document['item_family_id']}_{_condition_suffix(document['condition'])}",
        "tempo": TEMPO_BPM,
        "time_signature": "4/4",
        "tonic": "C",
        "mode": "ionian",
        "style": "exp003_canonical_verification",
        "arrangement": {"sections": [{"id": "stimulus", "start_bar": 1, "bar_count": 1, "energy": 0.5}], "harmony_assignments": []},
        "tracks": [{
            "id": "exp003_canonical_pitched",
            "type": "pitched",
            "role": "technical_verification",
            "motifs": [{
                "id": "canonical_events",
                "events": [
                    {"bar": 1, "beat": "3/2", "duration": "6/25", "pitches": [str(_pitch_name(e["pitch_midi"])) for e in events[:4]], "velocity": 96, "chromatic": True},
                    {"bar": 1, "beat": "5/2", "duration": "6/25", "pitches": [str(_pitch_name(e["pitch_midi"])) for e in events[4:]], "velocity": 96, "chromatic": True},
                ],
            }],
            "section_assignments": [{"section_id": "stimulus", "motif_id": "canonical_events"}],
        }],
    }


def _pitch_name(midi_pitch: int):
    from music_engine.domain import Pitch

    return Pitch.from_absolute_semitone(midi_pitch)


def build_songplan(manifest_path: Path, family_id: str, condition: str):
    document = build_event_document(manifest_path, family_id, condition)
    plan = song_plan_v2_from_dict(build_songplan_dict(document))
    return document, plan


def run_non_media_tests(manifest_path: Path) -> None:
    manifest = _load_manifest(manifest_path)
    all_ids: set[str] = set()
    all_event_ids: set[str] = set()
    for family_id in FAMILY_IDS:
        for condition in CONDITIONS:
            document, plan = build_songplan(manifest_path, family_id, condition)
            family = _family(manifest, family_id)
            suffix = _condition_suffix(condition)
            assert len(document["events"]) == 8
            assert [e["pitch_midi"] for e in document["events"][:4]] == family["R1_pitches_midi"]
            assert [e["pitch_midi"] for e in document["events"][4:]] == family[f"R2_{suffix}_pitches_midi"]
            assert all(e["velocity"] == 96 and e["duration_seconds"] == 0.48 for e in document["events"])
            assert [e["event_id"] for e in document["events"]] == [f"R{r}-V{v}" for r in (1, 2) for v in range(1, 5)]
            assert len({e["event_id"] for e in document["events"]}) == 8
            all_event_ids.update(e["event_id"] for e in document["events"])
            internal_id = f"{family_id}-{_condition_suffix(condition)}"
            assert internal_id not in all_ids
            all_ids.add(internal_id)
            validation = validate_song_plan_v2(plan)
            assert validation.valid, validation.issues
            assert plan.tempo.bpm == TEMPO_BPM
            for beat, expected_on, expected_off in (("3/2", 500, 1460), ("5/2", 1500, 2460)):
                position = Position(1, beat)
                assert position_to_ticks(position, ppq=PPQ, signature=plan.time_signature) == expected_on
                assert position_to_ticks(position, ppq=PPQ, signature=plan.time_signature) + duration_to_ticks(Duration(Fraction(6, 25)), ppq=PPQ) == expected_off
            assert duration_to_ticks(Duration(Fraction(6, 25)), ppq=PPQ) == 960

    assert len(all_ids) == 24
    assert len(all_event_ids) == 8  # event IDs are explicitly stimulus-local.
    f01 = build_event_document(manifest_path, "EXP003-F01", "LOW_SELECTED")
    f01["canary_id"] = "EXP003-CANARY-001"
    assert hashlib.sha256(serialize_event_document(f01)).hexdigest().upper() == EXPECTED_CANARY_F01_LOW_SHA256


def main() -> int:
    parser = argparse.ArgumentParser(description="Adaptador MIDI genérico EXP-003, sin salida multimedia")
    parser.add_argument("--manifest", type=Path, default=Path("experiments/EXP-003/EXP-003-item-freeze-manifest-v2.yaml"))
    parser.add_argument("--family")
    parser.add_argument("--condition", choices=CONDITIONS)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        run_non_media_tests(args.manifest)
        print("PASS: EXP-003 adapter v2 24/24 non-media tests")
        return 0
    if not args.family or not args.condition:
        parser.error("--family y --condition son obligatorios salvo con --self-test")
    document, plan = build_songplan(args.manifest, args.family, args.condition)
    print(json.dumps({"event_document": document, "songplan": build_songplan_dict(document), "ppq": PPQ}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
