---
id: open-intelligence
name: open-intelligence
description: Use when you have security-camera/CCTV `image` or video and want automated face, object, and license-plate detection over it — returns detected `face`s, `vehicle-plate`s, and object/`physical-description` tags.
url: https://github.com/norkator/open-intelligence
category: image-video-face
path:
- image-video-face
bestFor: Self-hosted pipeline to run face/object/license-plate detection across CCTV or security-camera footage.
selectorsIn:
- image
- face
- vehicle-plate
selectorsOut:
- face
- vehicle-plate
- physical-description
status: live
pricing: free
costNote: Free and open-source (GitHub). Cost is compute — it wants local GPU/CPU resources and setup time, not money.
opsec: passive
opsecNote: All processing is local on your own machine/footage, so nothing is sent to a third party and nothing reaches the subject — this is the private, self-hosted alternative to cloud face/plate services. OpSec risk is on your side: handle the footage and any extracted biometric/plate data lawfully and securely.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: docker
trust: community
trustNote: Community GitHub project (~187 stars) bundling TypeScript + Python ML models; capable but self-hosted and dependency-heavy — validate detections manually.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- open-intelligence
- norkator open-intelligence
tags:
- face-detection
- cctv
- license-plate
- object-detection
- video-analysis
source: gh-topic-intelligence-gathering
lastVerified: '2026-07-10'
enrichment: full
---

# open-intelligence

> A self-hosted CCTV analysis stack — run face, object, and license-plate detection over your own security-camera footage without sending anything to the cloud.

## When to use
You have CCTV/security-camera `image`s or video (e.g. footage from around a missing person's last-known location, or clips showing a vehicle of interest) and want machines to surface the faces, objects, and license plates in it so you don't have to scrub hours of frames by hand. Best when the footage is sensitive and must stay local.

## How to use it (`bestInteractionPattern`: docker)
1. Clone https://github.com/norkator/open-intelligence and follow its setup (Docker / TypeScript backend + Python ML services); provision a machine with adequate CPU/GPU.
2. Point it at your camera image/video sources.
3. Let the pipeline run detection: it flags and crops `face`s, classifies objects, and reads `vehicle-plate`s (ALPR).
4. Review the dashboard of detections — manually confirm each (false positives are expected).
5. Pivot: take a clean cropped `face` into a face-search engine; take a `vehicle-plate` into a plate/DVLA lookup; use object/`physical-description` tags to build a scene timeline.

## Inputs → Outputs
- **In:** `image`/video from CCTV or security cameras (optionally seed `face`/`vehicle-plate` to look for)
- **Out:** detected `face`s (cropped), `vehicle-plate`s (ALPR text), object detections / `physical-description` tags, timestamped
- **Empty/negative result looks like:** no detections in a clip — could mean genuinely nothing of interest, or poor footage quality/angle/lighting defeating the models. Absence is not proof; sample frames manually.

## Gotchas & OpSec
- Self-hosted and dependency-heavy — expect real setup effort and compute cost.
- ML detections carry false positives/negatives; every hit needs human confirmation before it's evidence.
- Handling faces/plates from footage is biometric data — process lawfully and store securely.

## Overlaps ("do both")
- Pairs with a face-search engine (e.g. `[[pimeyes]]`-class) and plate lookups — open-intelligence *finds and crops* the faces/plates in raw footage; those tools then *identify* them.

## Trust & verifiability
`trust: community` — a capable open-source project, but community-maintained and model-dependent. Treat its detections as leads to verify frame-by-frame, not conclusions.
