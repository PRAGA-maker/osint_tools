---
id: deepsafe
name: DeepSafe
description: Use when you have an `image`, video, or audio clip and want to test whether it is AI-generated/manipulated — returns per-model real/fake verdicts with confidence scores.
url: https://github.com/siddharthksah/DeepSafe
category: image-video-face
path:
- image-video-face
- deepfake-detection
bestFor: Running several deepfake detectors at once over one media file and comparing their verdicts.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: MIT-licensed and fully self-hosted; no fees, no account. You supply the compute (Docker) and pull model weights from Hugging Face.
opsec: passive
opsecNote: When you run it locally with Docker the media never leaves your machine, so analysis is passive. Only the hosted/demo deployments upload the file externally — prefer the local `make start` path for a sensitive image of a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Open-source project (MIT) by an independent developer; ~100+ stars, active commits. It orchestrates third-party detection models, so verdict quality depends on those models, not on DeepSafe itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- deepfake-detect
- deepfakebench
- faceforensics-plus-plus
- truthscan-deepfake-detector
aliases:
- DeepSafe deepfake detection
- siddharthksah/DeepSafe
tags:
- deepfake
- media-verification
- Image Search and Identification
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# DeepSafe

> A self-hosted "detector of detectors": one Docker stack that runs several deepfake models over an image, video, or audio clip and shows you where they agree.

## When to use
You have a photograph, video, or voice clip tied to a subject (a "proof of life" image, a purported CCTV still, a voicemail) and need to gauge whether it is synthetic or manipulated before you build an investigation on it. DeepSafe is most useful when you don't want to trust a single detector — it fans the file out to multiple models and reports each one's probability, so you can weigh consensus rather than one black-box score.

## How to use it (`bestInteractionPattern`: docker)
1. Clone the repo: `git clone https://github.com/siddharthksah/DeepSafe`.
2. Ensure Docker + docker-compose are installed; the model weights are pulled from Hugging Face on first run.
3. From the repo root run `make start`. Each detector runs as its own container behind a FastAPI gateway.
4. Open the dashboard at `http://localhost:8888` and upload the media file (or POST base64-encoded media to the API gateway).
5. Read the output: a real/fake verdict plus a 0–1 confidence, broken down per model. Look for agreement across models — a single outlier is weaker evidence than a cluster.

## Inputs → Outputs
- **In:** an image, video, or audio file (no personal selector — you already hold the media).
- **Out:** authenticity verdict (real/fake) + per-model confidence scores; not a personal identifier.
- **Empty/negative result looks like:** models split or all hover near 0.5 — treat as inconclusive, not as "confirmed real." Detectors trained on older generators miss newer synthesis methods.

## Gotchas & OpSec
- Detection is probabilistic: a "fake" verdict is a lead, never proof. Compression, re-encoding, and screenshots degrade the signal.
- Run locally so the subject's media stays on your machine; avoid third-party hosted demos for sensitive files.
- First run is heavy (container builds + weight downloads); budget disk and time.

## Overlaps ("do both")
- Pairs with `[[faceforensics-plus-plus]]` and `[[deepfakebench]]` — those are benchmark/model suites; DeepSafe is the convenient orchestrator that runs several at once.
- Cross-check a suspicious frame with `[[truthscan-deepfake-detector]]` for an independent second opinion.

## Trust & verifiability
`trust: community` — a well-starred MIT open-source project, but it is a wrapper: the actual verdicts come from the bundled models, whose accuracy varies by generator and modality. Corroborate with a second detector and with provenance/metadata checks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deepsafe |
| category | image-video-face |
| selectorsIn → selectorsOut | — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | docker |
| opsec | passive |
| human-in-loop | no |
