#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


DATASET = "DNS2020"
CONDITION = "noreverb"
KINDS = ("noisy", "clean", "our")
ROOT = Path(__file__).resolve().parents[1]
AUDIO_ROOT = ROOT / "audio" / DATASET / CONDITION
SPECTROGRAM_ROOT = ROOT / "spectrograms" / DATASET / CONDITION
MANIFEST_PATH = ROOT / "samples.json"


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def make_spectrogram(wav_path: Path, kind: str) -> Path:
    relative_wav = wav_path.relative_to(AUDIO_ROOT / kind)
    png_path = (SPECTROGRAM_ROOT / kind / relative_wav).with_suffix(".png")
    png_path.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        str(wav_path),
        "-lavfi",
        "showspectrumpic=s=1280x720:legend=disabled:scale=log:color=viridis",
        "-frames:v",
        "1",
        str(png_path),
    ]
    subprocess.run(command, check=True)
    return png_path


def collect_samples() -> dict:
    samples: dict[str, dict] = {}

    for kind in KINDS:
        kind_root = AUDIO_ROOT / kind
        if not kind_root.exists():
            continue

        for wav_path in sorted(kind_root.rglob("*.wav")):
            relative_stem = wav_path.relative_to(kind_root).with_suffix("").as_posix()
            sample = samples.setdefault(
                relative_stem,
                {"id": relative_stem, "audio": {}, "spectrograms": {}},
            )
            sample["audio"][kind] = relpath(wav_path)
            sample["spectrograms"][kind] = relpath(make_spectrogram(wav_path, kind))

    return {
        "dataset": DATASET,
        "condition": CONDITION,
        "versions": list(KINDS),
        "samples": [samples[key] for key in sorted(samples)],
    }


def main() -> None:
    SPECTROGRAM_ROOT.mkdir(parents=True, exist_ok=True)
    manifest = collect_samples()
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {relpath(MANIFEST_PATH)} with {len(manifest['samples'])} samples.")


if __name__ == "__main__":
    main()
