"""Validador reproducible de integridad simbólica para EXP-003.

Uso:
    python tools/exp003/validate-exp003-freeze-v2.py experiments/EXP-003/EXP-003-item-freeze-manifest-v2.yaml

No genera MIDI/audio ni invoca music-engine.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml


PITCH_CLASS = {
    "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3,
    "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8,
    "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11,
}
QUALITY_INTERVALS = {
    "major triad": (0, 4, 7),
    "minor triad": (0, 3, 7),
    "major seventh": (0, 4, 7, 11),
    "minor seventh": (0, 3, 7, 10),
    "dominant seventh": (0, 4, 7, 10),
}


def h2_pitch_classes(identity: str) -> set[int]:
    match = re.match(r"^([A-G](?:#|b)?) (major triad|minor triad|major seventh|minor seventh|dominant seventh)", identity)
    if not match:
        raise ValueError(f"H2_identity no parseable: {identity!r}")
    root, quality = match.groups()
    return {(PITCH_CLASS[root] + interval) % 12 for interval in QUALITY_INTERVALS[quality]}


def pcs(pitches: list[int]) -> list[int]:
    return [pitch % 12 for pitch in pitches]


def feature_errors(family: dict, construction: dict) -> list[str]:
    errors: list[str] = []
    declared = [PITCH_CLASS[name] for name in family["doubling_pattern"].split(",")]
    declared_counter = Counter(declared)
    h2_set = h2_pitch_classes(family["H2_identity"])
    ranges = construction["voice_ranges_midi"]
    r1 = family["R1_pitches_midi"]

    if len(r1) != 4 or r1 != sorted(r1):
        errors.append("R1 voice order/voice count")

    endpoint_features = {}
    for condition in ("LOW", "HIGH"):
        key = f"R2_{condition}_pitches_midi"
        pitches = family[key]
        actual = pcs(pitches)
        if set(actual) != h2_set:
            errors.append(f"{condition} H2 pitch-class set")
        if Counter(actual) != declared_counter:
            errors.append(f"{condition} doubling/multiplicity")
        if len(pitches) != 4:
            errors.append(f"{condition} voice count")
        if any(not (ranges[f"V{i+1}"][0] <= pitch <= ranges[f"V{i+1}"][1]) for i, pitch in enumerate(pitches)):
            errors.append(f"{condition} voice ranges")
        spacing = [pitches[i + 1] - pitches[i] for i in range(3)]
        span = pitches[-1] - pitches[0]
        if any(not (construction["adjacent_spacing_semitones"][0] <= value <= construction["adjacent_spacing_semitones"][1]) for value in spacing):
            errors.append(f"{condition} spacing")
        if not (construction["total_span_semitones"][0] <= span <= construction["total_span_semitones"][1]):
            errors.append(f"{condition} span")
        if pitches != sorted(pitches):
            errors.append(f"{condition} crossing")
        motion = [b - a for a, b in zip(r1, pitches)]
        endpoint_features[condition] = {
            "pitches": pitches,
            "pcs": actual,
            "motion": motion,
            "total": sum(abs(value) for value in motion),
            "maximum": max(abs(value) for value in motion),
            "moving": sum(value != 0 for value in motion),
            "span": span,
            "centroid": sum(pitches) / 4,
            "spacing": spacing,
            "min_spacing": min(spacing),
            "max_spacing": max(spacing),
        }
        stored = {
            "motion_vector": family[f"motion_vector_{condition}"],
            "total_motion": family[f"total_motion_{condition}"],
            "max_motion": family[f"max_motion_{condition}"],
            "moving_voice_count": family[f"moving_voice_count_{condition}"],
            "span": family[f"span_{condition}"],
            "centroid": family[f"centroid_{condition}"],
            "spacing_profile": family[f"spacing_profile_{condition}"],
        }
        expected = endpoint_features[condition]
        for field, value in {
            "motion_vector": expected["motion"],
            "total_motion": expected["total"],
            "max_motion": expected["maximum"],
            "moving_voice_count": expected["moving"],
            "span": expected["span"],
            "centroid": expected["centroid"],
            "spacing_profile": expected["spacing"],
        }.items():
            if stored[field] != value:
                errors.append(f"{condition} derived {field}")

    if family["R2_LOW_pitches_midi"][0] % 12 != PITCH_CLASS[family["bass_pitch_class"]]:
        errors.append("LOW bass/inversion")
    if family["R2_HIGH_pitches_midi"][0] % 12 != PITCH_CLASS[family["bass_pitch_class"]]:
        errors.append("HIGH bass/inversion")
    if family["retained_exact_pitches_LOW"] != family["retained_exact_pitches_HIGH"]:
        errors.append("common-tone retention")
    if family["retaining_voices_LOW"] != family["retaining_voices_HIGH"]:
        errors.append("retaining voices")
    if endpoint_features["LOW"]["moving"] != endpoint_features["HIGH"]["moving"]:
        errors.append("moving_voice_count match")
    if endpoint_features["LOW"]["total"] >= endpoint_features["HIGH"]["total"]:
        errors.append("LOW/HIGH motion ordering")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--events", type=Path, help="validate one explicit EXP-003 event manifest")
    args = parser.parse_args()
    document = yaml.safe_load(args.manifest.read_text(encoding="utf-8"))
    if args.events:
        event_document = json.loads(args.events.read_text(encoding="utf-8"))
        return validate_exp003_events(document, event_document)
    failures = 0
    for family in document["families"]:
        errors = feature_errors(family, document["construction_space"])
        if errors:
            failures += 1
            print(f"{family['item_family_id']}: FAIL — {', '.join(errors)}")
        else:
            print(f"{family['item_family_id']}: PASS")
    print(f"SUMMARY: passed={len(document['families']) - failures} failed={failures}")
    return 1 if failures else 0


def validate_exp003_events(manifest: dict, event_document: dict) -> int:
    """Validate the exact eight-event contract for one EXP-003 stimulus."""
    errors: list[str] = []
    family_id = event_document.get("item_family_id")
    condition = event_document.get("condition")
    family = next((item for item in manifest["families"] if item["item_family_id"] == family_id), None)
    if family is None or condition not in {"LOW_SELECTED", "HIGH_SELECTED"}:
        errors.append("item_family_id/condition")
    events = event_document.get("events", [])
    if len(events) != 8:
        errors.append("exactly eight events")
    ids = [event.get("event_id") for event in events]
    if any(not event_id for event_id in ids) or len(ids) != len(set(ids)):
        errors.append("event_id presence/uniqueness")
    segments = [(event.get("segment") or str(event.get("event_id", "")).split("-")[0]) for event in events]
    if sum(segment == "R1" for segment in segments) != 4:
        errors.append("four R1 events")
    if sum(segment == "R2" for segment in segments) != 4:
        errors.append("four R2 events")
    expected_pitches = None
    if family is not None:
        suffix = "LOW" if condition == "LOW_SELECTED" else "HIGH"
        expected_pitches = family[f"R2_{suffix}_pitches_midi"]
    expected = {
        **({f"R1-V{i}": ("R1", family["R1_pitches_midi"][i - 1], 0.25) for i in range(1, 5)}
           if family is not None else {}),
        **({f"R2-V{i}": ("R2", expected_pitches[i - 1], 0.75) for i in range(1, 5)}
           if expected_pitches is not None else {}),
    }
    for event in events:
        event_id = event.get("event_id")
        if event_id not in expected:
            errors.append(f"unexpected event {event_id!r}")
            continue
        segment, pitch, onset = expected[event_id]
        actual_segment = event.get("segment") or str(event_id).split("-")[0]
        if actual_segment != segment or event.get("pitch_midi") != pitch:
            errors.append(f"event content {event_id}")
        if event.get("onset_seconds") != onset or event.get("duration_seconds") != 0.48:
            errors.append(f"event timing {event_id}")
        if event.get("velocity") != 96:
            errors.append(f"event velocity {event_id}")
    if event_document.get("sample_rate_hz") != 48000 or event_document.get("duration_seconds") != 2.0:
        errors.append("canonical sample rate/duration")
    if errors:
        print("EVENTS: FAIL — " + ", ".join(errors))
        return 1
    print("EVENTS: PASS — exactly 8 events, exact frozen pitches and timing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
