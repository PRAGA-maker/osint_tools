---
id: deepfakebench
name: DeepfakeBench
description: Use when you have an `image`/`face` and need to build or benchmark deepfake-detection tooling — returns a standardized detector/benchmark framework, not a per-image verdict.
url: https://github.com/SCLBD/DeepfakeBench
category: image-video-face
path:
- image-video-face
- deepfake-detection
bestFor: Benchmarking and running deepfake/face-forgery detectors under a standardized, reproducible framework.
selectorsIn:
- image
- face
selectorsOut:
- image
status: live
pricing: free
costNote: Free and open-source (academic). Running detectors needs your own compute (GPU recommended) and model weights per the repo.
opsec: passive
opsecNote: You run this locally on media you already hold — no network query about a subject, nothing disclosed externally. Keep case media on a controlled machine; don't upload sensitive images to third-party detector services when a local run suffices.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: python-lib
trust: trusted
trustNote: A widely-cited academic benchmark (SCLBD) with open code; results are as trustworthy as the chosen detector and dataset — a research framework, not a courtroom oracle.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- DeepfakeBench
- SCLBD/DeepfakeBench
tags:
- deepfake-detection
- image-forensics
- benchmark
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# DeepfakeBench

> A standardized, open-source framework for training and benchmarking deepfake/face-forgery detectors — infrastructure for verifying imagery, not a one-click "is this fake?" button.

## When to use
You are dealing with suspect `image`/`face` media (a possibly AI-generated profile photo, a manipulated video frame) and want a rigorous, reproducible way to run and compare state-of-the-art deepfake detectors — or to evaluate which detector to trust before applying it to case media. DeepfakeBench unifies datasets, preprocessing, detector implementations and evaluation metrics so results are comparable rather than cherry-picked. Best for the analyst building a verification pipeline, not for a quick field check.

## How to use it (`bestInteractionPattern`: python-lib)
1. Clone `github.com/SCLBD/DeepfakeBench` and follow its setup (Python env, dependencies, model weights, datasets).
2. Choose a detector and the benchmark protocol; run its evaluation to see performance across standard forgery datasets.
3. Apply a chosen, validated detector to your own suspect media, following the repo's inference path.
4. Read the score as a probability/indicator and pivot: corroborate with metadata/EXIF checks, reverse-image search, and manual artefact inspection — never rely on a single detector's number.

## Inputs → Outputs
- **In:** `image`/`face` media (your own suspect files) + a chosen detector/dataset
- **Out:** a real-vs-forged probability/score per detector, plus comparative benchmark metrics
- **Empty/negative result looks like:** a low forgery probability is *not* proof of authenticity — detectors generalise poorly to unseen manipulation methods; treat borderline/negative as inconclusive.

## Gotchas & OpSec
- Requires real setup (GPU, weights, datasets) and ML literacy — not a point-and-click tool.
- Detectors are brittle across novel generators; a confident score can still be wrong — human-in-the-loop review is mandatory.
- Runs locally on your media; keep sensitive case files off third-party upload services.

## Overlaps ("do both")
- Pairs with EXIF/metadata analysis, reverse-image search and error-level/analysis forensics — deepfake detection is one signal; corroborate with provenance and manual inspection.

## Trust & verifiability
`trust: trusted` — an open, widely-cited academic benchmark; the framework is sound, but any verdict depends on the detector and data, so present results as probabilistic, corroborated evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deepfakebench |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | yes (manual-review) |
