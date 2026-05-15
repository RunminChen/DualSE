# DualSE

Public demo page for DualSE speech enhancement examples.

This repository is intentionally limited to project documentation, a lightweight demo page, and processed audio examples. The research/source code will be released after acceptance.

## Demo

The static demo page is in `index.html`. It is designed to work with GitHub Pages from the repository root.

Suggested audio layout:

```text
audio/
  noisy_01.wav
  dualse_01.wav
  noisy_02.wav
  dualse_02.wav
  noisy_03.wav
  dualse_03.wav
```

You can replace the placeholder filenames in `index.html` with the final processed audio files.

## Repository Scope

- Public now: README, demo page, processed audio examples.
- Not public yet: training code, inference code, model checkpoints, private datasets, and experiment logs.

## Audio Notes

Please keep uploaded demo audio compact and web-friendly. For GitHub, individual files should stay below the platform file-size limit; for larger audio collections, use a release asset, external storage, or Git LFS.
