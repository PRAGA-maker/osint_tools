---
id: deepfaceui-github-com
name: deepfaceui (github.com)
description: Use when you have two face photos and want a local, offline same-person comparison/verification score — returns a match verdict and similarity distance.
url: https://github.com/GONZOsint/deepfaceui
category: image-video-face
path:
- image-video-face
bestFor: Local 1:1 face verification (same person?) between two images using the DeepFace library, via a GUI.
selectorsIn:
- face
- image
selectorsOut:
- face
status: live
pricing: free
costNote: Free, open-source; runs on your own hardware (no per-query cost).
opsec: passive
opsecNote: Runs entirely locally — images never leave your machine, so no third-party leakage. Strongest OpSec option for comparing sensitive faces.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: community
trustNote: Open-source GUI wrapping the well-known DeepFace library, authored by a recognized OSINT researcher (GONZO); results are a similarity score that still needs human judgment.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: true
registration: false
relatedTools: [diffchecker, copyseeker-net]
aliases:
- DeepFace UI
- deepfaceui
tags:
- facialcomparison
- Facial Comparison Sites
- face-verification
source: uk-osint
lastVerified: ''
enrichment: full
---

# deepfaceui (github.com)

> A local GUI front-end for the DeepFace library — load two face images and get an offline same-person verification score, with nothing leaving your machine.

## When to use
You have two `face`/`image` samples — e.g. a known photo of the missing person and a candidate from a profile or reverse-image hit — and need to judge whether they are the same individual. It runs DeepFace's verification models locally and returns a distance/similarity score, so you can compare faces without uploading anything to a third-party cloud.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Clone https://github.com/GONZOsint/deepfaceui and install the Python/DeepFace dependencies (the GUI launches as a local app/web UI).
2. Load image A (known) and image B (candidate).
3. Pick a model/backend and run the comparison.
4. Read the verdict + similarity distance; lower distance / "verified" = likely same person.
5. Pivot: confirm strong matches visually with `[[diffchecker]]`, and trace the candidate image's origin via `[[copyseeker-net]]`.

## Inputs → Outputs
- **In:** `face` / `image` (two photos)
- **Out:** `face` (a same-person verdict + similarity distance)
- **Empty/negative result looks like:** "not verified" / a high distance, OR a failure to detect a face at all (bad angle, occlusion, low resolution) — the latter is inconclusive, not a non-match.

## Gotchas & OpSec
- Human-in-the-loop: the score is a probability, not proof. Pose, lighting, age gap, and resolution skew results — a human must adjudicate, especially near the threshold.
- Setup requires Python and model downloads; first run pulls model weights.
- OpSec: passive and fully local — the best-privacy option here since images are never uploaded. Use this rather than a cloud face engine for sensitive comparisons.

## Overlaps ("do both")
- Pairs with `[[diffchecker]]` for a manual side-by-side and with `[[copyseeker-net]]` to source the candidate image. Use a cloud face-search engine to *find* candidates, then deepfaceui to *verify* them locally.

## Trust & verifiability
`trust: community` — open-source wrapper over the established DeepFace library by a recognized OSINT author. The math is reproducible and runs on your own data, but the output is a similarity score requiring human verification, never a legal identification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deepfaceui-github-com |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → face |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes |
