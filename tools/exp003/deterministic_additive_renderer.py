"""Renderer aditivo mono determinista para estímulos autorizados explícitamente.

Este módulo no lee el manifiesto de EXP-003 ni crea un plan de materialización.
Solo el subcomando explícito ``render-events`` escribe un WAV para un archivo
JSON de eventos proporcionado por el operador.

Contrato JSON mínimo:
{
  "sample_rate_hz": 48000,
  "duration_seconds": 2.0,
  "events": [
    {"event_id": "R1-V1", "pitch_midi": 60, "onset_seconds": 0.25,
     "duration_seconds": 0.48, "velocity": 96}
  ]
}
"""

from __future__ import annotations

import argparse
import json
import math
import wave
from dataclasses import dataclass
from pathlib import Path


SAMPLE_RATE_HZ = 48_000
BIT_DEPTH = 24
CHANNELS = 1
GLOBAL_GAIN = 1 / 16
VELOCITY = 96
VELOCITY_AMPLITUDE = VELOCITY / 127
RELEASE_SECONDS = 0.020
ATTACK_SECONDS = 0.010
# Fixed geometric harmonic spectrum: h1=1, h2=1/2, h3=1/4, h4=1/8.
HARMONIC_AMPLITUDES = (1.0, 0.5, 0.25, 0.125)


@dataclass(frozen=True)
class Event:
    event_id: str
    pitch_midi: int
    onset_seconds: float
    duration_seconds: float
    velocity: int = VELOCITY


def midi_to_frequency(pitch_midi: int) -> float:
    """12-TET frequency with A4 (MIDI 69) = 440 Hz."""
    return 440.0 * (2.0 ** ((pitch_midi - 69) / 12.0))


def seconds_to_sample(seconds: float, sample_rate_hz: int = SAMPLE_RATE_HZ) -> int:
    """Convert an approved decimal time to an integer frame index exactly."""
    index = round(seconds * sample_rate_hz)
    if not math.isclose(index / sample_rate_hz, seconds, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError(f"time is not exactly representable at sample rate: {seconds}")
    return index


def active_harmonics(frequency_hz: float, sample_rate_hz: int) -> tuple[tuple[int, float], ...]:
    """Keep only fixed partials strictly below Nyquist; no per-note tuning."""
    nyquist = sample_rate_hz / 2
    return tuple(
        (harmonic, amplitude)
        for harmonic, amplitude in enumerate(HARMONIC_AMPLITUDES, start=1)
        if harmonic * frequency_hz < nyquist
    )


def envelope(local_sample: int, note_off_sample: int, end_sample: int) -> float:
    """Linear attack, sustain, and release with exact zero at end_sample."""
    attack_samples = seconds_to_sample(ATTACK_SECONDS)
    release_samples = seconds_to_sample(RELEASE_SECONDS)
    if local_sample < attack_samples:
        return local_sample / attack_samples
    if local_sample < note_off_sample:
        return 1.0
    remaining = end_sample - local_sample
    return max(0.0, min(1.0, remaining / release_samples))


def validate_events(events: list[Event], duration_seconds: float, sample_rate_hz: int) -> None:
    if sample_rate_hz != SAMPLE_RATE_HZ:
        raise ValueError(f"sample_rate_hz must be {SAMPLE_RATE_HZ}")
    total_samples = seconds_to_sample(duration_seconds, sample_rate_hz)
    event_ids = [event.event_id for event in events]
    if len(event_ids) != len(set(event_ids)):
        raise ValueError("event_id must be unique within one rendered stimulus")
    for event in events:
        if not event.event_id:
            raise ValueError("event_id must be non-empty")
        if not 0 <= event.pitch_midi <= 127:
            raise ValueError("pitch_midi must be in 0..127")
        if event.velocity != VELOCITY:
            raise ValueError(f"velocity must be the fixed value {VELOCITY}")
        onset = seconds_to_sample(event.onset_seconds, sample_rate_hz)
        note_off = seconds_to_sample(event.onset_seconds + event.duration_seconds, sample_rate_hz)
        end = note_off + seconds_to_sample(RELEASE_SECONDS, sample_rate_hz)
        if event.duration_seconds <= RELEASE_SECONDS:
            raise ValueError("duration_seconds must exceed the fixed release")
        if onset < 0 or end > total_samples:
            raise ValueError("event lies outside the canonical output duration")


def render_pcm(events: list[Event], duration_seconds: float, sample_rate_hz: int = SAMPLE_RATE_HZ) -> list[int]:
    """Return mono signed 24-bit sample integers; does not write media."""
    validate_events(events, duration_seconds, sample_rate_hz)
    total_samples = seconds_to_sample(duration_seconds, sample_rate_hz)
    output = [0.0] * total_samples
    ordered_events = sorted(
        events,
        key=lambda event: (seconds_to_sample(event.onset_seconds, sample_rate_hz), event.event_id),
    )
    for event in ordered_events:  # Canonical order independent of input insertion order.
        onset = seconds_to_sample(event.onset_seconds, sample_rate_hz)
        note_off = seconds_to_sample(event.onset_seconds + event.duration_seconds, sample_rate_hz)
        end = note_off + seconds_to_sample(RELEASE_SECONDS, sample_rate_hz)
        frequency = midi_to_frequency(event.pitch_midi)
        partials = active_harmonics(frequency, sample_rate_hz)
        amplitude = event.velocity / 127.0
        for sample_index in range(onset, end):
            local = sample_index - onset
            phase_time = local / sample_rate_hz
            value = sum(
                partial_amplitude * math.sin(2.0 * math.pi * harmonic * frequency * phase_time)
                for harmonic, partial_amplitude in partials
            )
            output[sample_index] += GLOBAL_GAIN * amplitude * envelope(local, note_off - onset, end - onset) * value
    limit = (1 << 23) - 1
    return [max(-limit, min(limit, round(value * limit))) for value in output]


def write_wav_24_mono(samples: list[int], output_path: Path, sample_rate_hz: int = SAMPLE_RATE_HZ) -> None:
    """Write deterministic little-endian PCM-24 WAV with no metadata chunks."""
    packed = bytearray()
    for sample in samples:
        packed.extend(int(sample).to_bytes(3, byteorder="little", signed=True))
    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(3)
        wav_file.setframerate(sample_rate_hz)
        wav_file.writeframes(bytes(packed))


def load_events(path: Path) -> tuple[list[Event], float, int]:
    document = json.loads(path.read_text(encoding="utf-8"))
    sample_rate_hz = int(document.get("sample_rate_hz", SAMPLE_RATE_HZ))
    duration_seconds = float(document["duration_seconds"])
    events = [Event(**item) for item in document["events"]]
    return events, duration_seconds, sample_rate_hz


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    render_parser = subparsers.add_parser("render-events", help="render explicit JSON events")
    render_parser.add_argument("input_json", type=Path)
    render_parser.add_argument("output_wav", type=Path)
    args = parser.parse_args()
    if args.command == "render-events":
        events, duration_seconds, sample_rate_hz = load_events(args.input_json)
        samples = render_pcm(events, duration_seconds, sample_rate_hz)
        write_wav_24_mono(samples, args.output_wav, sample_rate_hz)
        return 0
    raise AssertionError("unreachable")


if __name__ == "__main__":
    raise SystemExit(main())
