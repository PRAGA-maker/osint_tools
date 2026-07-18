---
id: scene-detection
name: Scene Detection (Scene-Edit-Detection)
description: Use when you have a long video and want its cut points — detects the timecodes where the scene changes, so you can jump between distinct shots instead of watching it all.
url: https://huggingface.co/spaces/fffiloni/scene-edit-detection
category: image-video-face
path:
- image-video-face
bestFor: Finding scene-change timecodes in a video to triage long footage into distinct shots.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public Hugging Face Space; no account needed to run it (heavy use may queue).
opsec: passive
opsecNote: You upload a video you already hold to a third-party Hugging Face Space for processing — do not upload sensitive/evidential footage you can't share; run scene detection locally (PySceneDetect) instead when confidentiality matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built Hugging Face Space (by fffiloni) wrapping standard scene-cut detection (PySceneDetect-style); the technique is reliable, the hosting is a third party.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Scene Edit Detection
- scene-edit-detection
tags:
- Video editing and analyze
- video
- scene-detection
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- efficientnetv2
- get-text-from-video
- hugging-face-ai-detector
- huggingface-co
- huggingface-co-4
- instruct-pix2pix
- kosmos-2
- scene-edit-detection
- youtube-whisperer
---

# Scene Detection (Scene-Edit-Detection)

> A web tool that finds where a video cuts between scenes and lists the timecodes — turning hours of footage into a navigable list of distinct shots to review.

## When to use
You have long video footage tied to a case (surveillance, a livestream capture, a compilation) and don't want to watch all of it. Scene detection identifies the timecodes where the shot/scenery changes, so you can jump straight to each distinct segment — quickly triaging which parts contain new locations, faces, or objects worth a closer look with reverse-image, face, or geolocation tools. It's a video-triage aid, not a person lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Space at https://huggingface.co/spaces/fffiloni/scene-edit-detection.
2. Upload the video you want to analyse (use a copy you're cleared to process off your machine).
3. Run it; it returns the list of scene-change timecodes (cut points) detected in the video.
4. Pivot: jump to each timecode in your own player, grab a representative frame per scene, and feed distinct frames into reverse-image/face/geolocation tools.

## Inputs → Outputs
- **In:** a video file
- **Out:** a list of scene-change timecodes / cut points (segmenting the video into shots)
- **Empty/negative result looks like:** few or no cuts detected — the footage is a single continuous shot, or the change threshold didn't trigger; that's information (it's one scene), not a failure.

## Gotchas & OpSec
- Human-in-the-loop: none, but public Spaces can queue or time out on long/large videos — trim or downscale first if it stalls.
- **Confidentiality:** it's a third-party host — never upload sensitive or evidential footage you can't share; for those, run PySceneDetect locally to get the same cut list offline.
- It detects *cuts*, not content — it tells you where scenes change, not what's in them; pair with analysis tools for the actual review.

## Overlaps ("do both")
- Pairs with reverse-image/face and geolocation tools — scene detection segments the video, then you run those on one frame per scene; also pairs with a local PySceneDetect run when the footage can't leave your machine.

## Trust & verifiability
`trust: community` — a community Hugging Face Space over standard scene-cut detection; the cut list is reproducible, so confirm ambiguous cuts by eye and re-run locally if you need an auditable pipeline.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scene-detection |
| category | image-video-face |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
