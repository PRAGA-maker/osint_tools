---
id: deepfake-detect
name: DeepFake-Detection (Dessa)
description: Use when you have an `image`/video and want to experiment with ML-based deepfake detection — returns a real/fake `image` classification score (research codebase, not a turnkey tool).
url: https://github.com/dessa-oss/DeepFake-Detection
category: image-video-face
path:
- image-video-face
- deepfake-detection
bestFor: A self-hosted research codebase for training and testing deepfake-detection models on face videos.
selectorsIn:
- image
selectorsOut:
- image
status: degraded
pricing: free
costNote: Free and open-source (Apache/MIT-style). No fees, but requires a GPU machine, datasets, and Docker to run — cost is in compute and setup, not licensing.
opsec: passive
opsecNote: Runs entirely on your own hardware — media you analyse never leaves your machine, so it is fully offline and leaks nothing. Ideal when you must not upload a sensitive image to a third-party detector.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: docker
trust: community
trustNote: Open-source research project by Dessa (2020), now unmaintained. Its own README concludes the models do NOT generalise well to real-world manipulations — treat outputs as experimental, not authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- DeepFake-Detect
- Dessa deepfake detection
tags:
- deepfake-detection
- ml
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# DeepFake-Detection (Dessa)

> An open-source research codebase for deepfake detection on face video — useful for offline experimentation, but explicitly a research demo, not a reliable production detector.

## When to use
You suspect a face image/video connected to a case is AI-manipulated and you need an *offline* way to experiment with detection — for example when the media is too sensitive to upload to a web-based detector. This repo lets a technical investigator run a trained model locally. Be clear-eyed: the authors found these models fail to generalise to real-world (YouTube-sourced) manipulations, so it is a starting point for hands-on research, not a verdict machine.

## How to use it (`bestInteractionPattern`: docker)
1. Clone `https://github.com/dessa-oss/DeepFake-Detection`; provision a machine with a GPU, 32GB+ RAM, nvidia-docker, and ffmpeg.
2. Obtain the datasets (FaceForensics++ requires a signed access form) and follow the repo's Docker/Atlas setup to build the environment.
3. Run inference on your face video/image; the model outputs a real-vs-fake classification score per sample.
4. **Manually review**: treat a "fake" score as a lead to corroborate — inspect frames for artefacts (warping, blending seams, inconsistent lighting/blink rate) yourself.
5. Pivot: combine with reverse-image search to find the source/original media and with EXIF/metadata analysis on the file.

## Inputs → Outputs
- **In:** `image` (face image or video frames)
- **Out:** `image` real/fake classification score
- **Empty/negative result looks like:** a low-confidence or "real" score — which given the model's poor generalisation is weak evidence either way; never treat a "real" output as proof the media is authentic.

## Gotchas & OpSec
- Heavy setup (GPU, datasets, Docker) and unmaintained — expect dependency friction; it is not a click-and-go tool.
- The authors themselves warn it does not generalise to real-world fakes — outputs are experimental. Always back with manual forensic review.
- Fully offline/self-hosted, so it is the safe choice for sensitive media you must not upload.

## Overlaps ("do both")
- Pairs with manual frame-forensics and reverse-image search — the model flags candidates, human review and source-finding confirm manipulation. For a quick check on non-sensitive media, a maintained hosted detector is faster.

## Trust & verifiability
`trust: community` — a real open-source project from a known team, but old and self-described as insufficient for real-world detection; use it as a research aid whose outputs must be independently verified, never as a sole authority.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deepfake-detect |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | yes (manual-review) |
