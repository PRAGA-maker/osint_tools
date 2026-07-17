---
id: deepfakedetector
name: DeepfakeDetector
description: Use when you have an `image` or video and want a quick real/fake classification — returns a binary verdict with a confidence score, runnable locally or via a web UI.
url: https://github.com/TRahulsingh/DeepfakeDetector
category: image-video-face
path:
- image-video-face
- deepfake-detection
bestFor: A fast, self-hostable real/fake classifier for a single image or video.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: MIT-licensed, open-source; free to self-host. You provide the compute (Python/PyTorch).
opsec: passive
opsecNote: Run locally so the subject's media never leaves your machine — that keeps it passive. Any public web deployment you use may log the upload; prefer the local `classify.py`/self-hosted Gradio app for sensitive media.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: A small but real MIT open-source project (EfficientNet-B0 classifier) by student authors; single-model, so treat it as one opinion and corroborate with a second detector.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- deepsafe
- deepfakebench
- faceforensics-plus-plus
aliases:
- TRahulsingh/DeepfakeDetector
tags:
- deepfake
- media-verification
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# DeepfakeDetector

> A lightweight, self-hostable deepfake classifier: feed it an image or video and get a real/fake verdict with a confidence score, via a drag-and-drop web app or the command line.

## When to use
You want a quick first-pass authenticity check on a single image or short video tied to a subject, and you'd rather run it yourself than upload to a third-party service. DeepfakeDetector is a small PyTorch model (EfficientNet-B0) that classifies media as real or fake with a confidence score — fast (~200 ms/image) and easy to run locally. Use it as one signal among several, not a sole arbiter.

## How to use it (`bestInteractionPattern`: python-lib)
1. Clone `https://github.com/TRahulsingh/DeepfakeDetector` and install the Python/PyTorch requirements.
2. For a single image: `python classify.py <image>`. For a UI: `python web-app.py` (Gradio drag-and-drop). For video: `inference/video_inference.py` (samples ~10 frames).
3. Read the output: binary Real/Fake with a confidence score.
4. Corroborate: run the same media through a second detector before trusting the verdict.
5. Pivot: a "fake" flag redirects you to provenance/reverse-image checks; a "real" result still needs metadata/context verification.

## Inputs → Outputs
- **In:** an `image` or video file (no personal selector — you hold the media).
- **Out:** Real/Fake verdict + confidence score; not a personal identifier.
- **Empty/negative result looks like:** a low-confidence score near the decision boundary — treat as inconclusive. Single-model detectors miss synthesis methods outside their training set.

## Gotchas & OpSec
- Single-model and trained on a limited dataset — weaker than multi-model ensembles; don't rely on it alone.
- Compression, filters, and re-encoding degrade accuracy; a verdict is a lead, not proof.
- Run locally to keep sensitive media off third-party servers.

## Overlaps ("do both")
- Cross-check with `[[deepsafe]]` (multi-model ensemble) and `[[faceforensics-plus-plus]]`; agreement across detectors is far stronger than any single verdict.

## Trust & verifiability
`trust: community` — a genuine but small single-model open-source project. Useful as a quick, self-hosted opinion; always corroborate with an independent detector and provenance analysis.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deepfakedetector |
| category | image-video-face |
| selectorsIn → selectorsOut | — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
