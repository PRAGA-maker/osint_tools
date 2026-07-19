---
id: frame-by-frame
name: Frame by Frame
description: Use when you have a video and want to step through it one frame at a time — returns precise still frames for landmark, plate, or face capture.
url: https://chromewebstore.google.com/detail/frame-by-frame/cclnaabdfgnehogonpeddbgejclcjneh
category: image-video-face
path:
- image-video-face
bestFor: Advancing any web video frame-by-frame with the arrow keys to isolate a single revealing still.
selectorsIn:
- image
selectorsOut:
- image
- vehicle-plate
- face
status: live
pricing: free
costNote: Free, open-source Chrome extension (by Code for Charity); no account, no in-app purchases.
opsec: passive
opsecNote: The extension runs locally in your browser on video already loaded on the page; it sends nothing to the video's owner and the developer states it collects no user data. Standard OpSec for how you loaded the video still applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source, Featured on the Chrome Web Store with a public GitHub repo; a simple client-side utility rather than a data source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Frame by Frame for YouTube
tags:
- video-search-and-other-video-tools
- video-analysis
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Frame by Frame

> A tiny, free Chrome extension that lets you step through any web video one frame at a time — the practical way to freeze the single frame that shows a face, a plate, or a landmark.

## When to use
You have a video (a TikTok/YouTube clip, a captured stream, a piece of evidence) and the crucial detail flashes by too fast to pause on: a license plate, a street sign, a reflected face, a house number. Frame by Frame gives you exact single-frame control so you can land on the clearest still, then screenshot it for reverse-image, geolocation, or plate work.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Frame by Frame" from the Chrome Web Store (link above).
2. Open the video in Chrome and play/pause near the moment of interest.
3. Hover the cursor over the video; use the left/right arrow keys to move one frame at a time (hold Shift to jump ~10 frames).
4. The overlay shows current time, duration, and frame count so you can note the exact position.
5. Land on the clearest frame, then screenshot it (OS screenshot or a capture tool) at full resolution.
6. Pivot: the still → reverse-image search / face tools; a `vehicle-plate` → plate lookups; background landmarks → mapping/geolocation.

## Inputs → Outputs
- **In:** a video playing in your browser (source `image`/frames)
- **Out:** precise individual frames you capture as stills — potentially containing a `face`, `vehicle-plate`, or geolocatable detail
- **Empty/negative result looks like:** the detail is simply never sharp in any frame (motion blur, low resolution) — stepping frames can't add detail that isn't there; try a higher-quality copy of the video.

## Gotchas & OpSec
- It exposes existing frames; it does not upscale or de-blur. Quality is capped by the source video.
- Works on standard HTML5 video across sites; some players with custom/DRM video may not respond to the frame controls.
- Chrome-only extension; for other browsers or offline files, a desktop player (VLC) or ffmpeg gives equivalent frame stepping.
- OpSec: fully local and passive — analysis of an already-loaded video leaks nothing to its owner.

## Overlaps ("do both")
- Complements reverse-image, face, and geolocation tools — this isolates the frame; those exploit it. Pair with a downloader so you keep the source clip alongside the extracted stills.

## Trust & verifiability
`trust: community` — an open-source, Featured Chrome utility with a public repo; it only manipulates local playback, so there's no data-quality risk — the evidence is the frame you capture, cited to its source video and timestamp.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | frame-by-frame |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image, vehicle-plate, face |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
