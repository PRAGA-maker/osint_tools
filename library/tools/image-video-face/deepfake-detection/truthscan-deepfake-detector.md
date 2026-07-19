---
id: truthscan-deepfake-detector
name: TruthScan Deepfake Detector
description: Use when you have an `image`, video or audio clip of uncertain origin and want an AI-manipulation verdict — returns a synthetic-probability score and forensic indicators.
url: https://truthscan.com/
category: image-video-face
path:
- image-video-face
- deepfake-detection
bestFor: Triaging whether a photo, video or voice clip of a subject is AI-generated/deepfaked before you rely on it as evidence.
selectorsIn:
- image
- face
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free trial with ~20,000 credits and no credit card required; paid plans start around $49/month for higher volume and API access.
opsec: active
opsecNote: You must upload the media to TruthScan's cloud to analyse it, so the file (and any faces/metadata in it) leaves your control and may be retained. Never upload case media you are not authorised to share; strip identifying metadata first if only the pixels matter, and use a sock-puppet account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial AI-detection vendor claiming 99%+ accuracy; such claims are self-reported and detectors produce false positives/negatives, so treat the score as one signal, not proof.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- TruthScan
- truthscan.com
tags:
- deepfake
- image-forensics
- ai-detection
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# TruthScan Deepfake Detector

> A commercial AI-content detector that scores images, video and audio for signs of synthesis or deepfaking — a triage step for verifying media authenticity before it drives an investigative conclusion.

## When to use
You have an `image`, video or voice clip tied to a subject (a purported sighting photo, a "proof of life" video, a scam caller's voice) and need a fast read on whether it is AI-generated or manipulated. In missing-persons and fraud work, a confirmed deepfake changes everything — you want to know before treating media as genuine. Use it to flag suspicious media, then corroborate with metadata analysis and provenance checks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a sock-puppet account at https://truthscan.com/ (free credits cover ad-hoc checks).
2. Choose the detector matching the media type (image, video, audio/voice, or text).
3. Upload the file and run the analysis.
4. Read the synthetic-probability score, forensic heatmap and indicators; note the model's stated confidence.
5. Treat the verdict as one input — corroborate with EXIF/metadata tools, reverse-image search, and reverse chronology before concluding.

## Inputs → Outputs
- **In:** `image` / `face` (also video and audio clips)
- **Out:** AI-generation probability score, forensic indicators/heatmap, an analysis report (`metadata-exif`-adjacent forensic signals)
- **Empty/negative result looks like:** a low synthetic-probability ("likely authentic") — which is not a guarantee of authenticity, only that this detector found no strong manipulation markers.

## Gotchas & OpSec
- Human-in-the-loop: account registration required; the free tier is metered by credits.
- OpSec: **active** — analysis requires uploading the media to a third party who may store it. Do not upload sensitive/unauthorised case files; use a burner account.
- Detector accuracy is imperfect and adversarially fragile; both false positives (real media flagged fake) and false negatives (good fakes passing) occur. Never treat the score as dispositive.

## Overlaps ("do both")
- Pairs with EXIF/metadata and reverse-image tools, which establish provenance independently of the AI-detection score.

## Trust & verifiability
`trust: unverified` — a commercial vendor with self-reported accuracy claims; useful as a triage signal but its verdicts must be cross-checked, not taken as forensic proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | truthscan-deepfake-detector |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
