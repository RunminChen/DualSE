# DualSE

Public demo page for DualSE speech enhancement examples.

This repository is intentionally limited to project documentation, a lightweight demo page, processed audio examples, and spectrogram images. The research/source code will be released after acceptance.

## Demo

The static demo page is in `index.html`. It is designed to work with GitHub Pages from the repository root.

Current demo layout:

```text
audio/
  DNS2020/
    noreverb/
      noisy/
        sample_01.wav
      clean/
        sample_01.wav
      our/
        sample_01.wav

spectrograms/
  DNS2020/
    noreverb/
      noisy/
        sample_01.png
      clean/
        sample_01.png
      our/
        sample_01.png
```

Add more samples by keeping the same filename stem across `noisy`, `clean`, and `our`.

## Repository Scope

- Public now: README, demo page, processed audio examples, and spectrogram images.
- Not public yet: training code, inference code, model checkpoints, private datasets, and experiment logs.

## Audio Notes

Please keep uploaded demo audio compact and web-friendly. For GitHub, individual files should stay below the platform file-size limit; for larger audio or image collections, use a release asset, external storage, or Git LFS.
