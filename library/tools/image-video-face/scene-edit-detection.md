---
id: scene-edit-detection
name: Scene Edit Detection
description: Use when you have a video (`image`/frames) and want its cut points found automatically — returns the frames/timestamps where a new scene begins, so you can triage long footage fast.
url: https://huggingface.co/spaces/fffiloni/scene-edit-detection
category: image-video-face
path:
- image-video-face
bestFor: Automatically detecting scene/shot boundaries in a video to jump to key segments instead of watching it all.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: free
costNote: Free public Hugging Face Space; heavy use may queue. No account needed to try.
opsec: passive
opsecNote: You upload the video to a third-party Hugging Face Space, so the footage leaves your machine and is processed on someone else's infrastructure. Do NOT upload sensitive/evidential video here; run the underlying PySceneDetect locally instead for anything confidential.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community Hugging Face Space by fffiloni wrapping standard scene-detection (PySceneDetect-style); fine for triage, but a third-party host, not an evidence tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- efficientnetv2
- get-text-from-video
- hugging-face-ai-detector
- huggingface-co
- huggingface-co-4
- instruct-pix2pix
- kosmos-2
- pix2pix-video
- youtube-whisperer
- scene-detection
aliases:
- fffiloni scene-edit-detection
tags:
- Video editing and analyze
- scene-detection
- video-triage
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Scene Edit Detection

> Upload a video and get its scene-change frames — a fast way to skim long footage for the moments that matter.

## When to use
You have long video (surveillance, a livestream capture, a dumped clip) and need to find where scenes/shots change so you can jump straight to key segments — faces, locations, handoffs — instead of scrubbing frame by frame. It marks the cut points; you still do the interpreting.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://huggingface.co/spaces/fffiloni/scene-edit-detection.
2. Upload the video file (short clips process fastest; the Space may queue under load).
3. Run it; read the output: the frames/timestamps where new scenes begin.
4. Pivot: open your video at those timestamps, extract key frames, and feed them into face-recognition, reverse-image, and geolocation tools.

## Inputs → Outputs
- **In:** a video (a sequence of `image` frames)
- **Out:** the scene-boundary frames/timestamps (key `image` frames to analyse)
- **Empty/negative result looks like:** a static/single-shot video yields few or no boundaries — expected; it means no hard cuts, not a failure.

## Gotchas & OpSec
- **Privacy:** the upload goes to a public third-party Space — never send confidential or evidential footage; use local PySceneDetect for those.
- Hosted Spaces can be down, rate-limited, or removed without notice.
- Human-in-the-loop: none. OpSec: passive toward any subject, but exposes your file to the host.

## Overlaps ("do both")
- Pairs with `[[get-text-from-video]]` / `[[youtube-whisperer]]` (transcript) — scene cuts + transcript together let you index a video by both visuals and speech.

## Trust & verifiability
`trust: community` — a community demo of a standard technique; treat detected boundaries as a triage aid and verify by viewing the actual frames.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scene-edit-detection |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
