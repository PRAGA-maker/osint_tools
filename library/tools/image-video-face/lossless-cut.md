---
id: lossless-cut
name: LosslessCut
description: Use when you have an `image`/video file and want to trim, split or inspect it without re-encoding — returns clipped segments and preserved `metadata-exif`.
url: https://github.com/mifi/lossless-cut
category: image-video-face
path:
- image-video-face
bestFor: Fast lossless trimming, splitting and frame extraction from video/audio while keeping original quality and metadata.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open source (MIT); cross-platform desktop app for Windows/macOS/Linux. No account, no cloud upload.
opsec: passive
opsecNote: Runs entirely offline on your own machine; nothing is uploaded and the subject cannot see that you handled the file. Because it is lossless, embedded metadata (timestamps, GPS, device) is preserved — mind that when you export clips you may intend to share.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Popular, actively maintained open-source project (mifi/LosslessCut) built on ffmpeg; widely used and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- LosslessCut
- lossless-cut
tags:
- Video editing and analyze
- video
- ffmpeg
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# LosslessCut

> An ffmpeg-based desktop app for quickly trimming, splitting and extracting frames from video/audio *without re-encoding* — so evidence clips keep their original quality and embedded metadata intact.

## When to use
You have a video (or audio) file relevant to a case and need to isolate a moment — a face, a plate, a timestamp overlay, a spoken segment — into a clean clip for closer analysis or sharing, without the quality loss and metadata scrubbing that normal editors cause. Because cuts are lossless and near-instant, it is ideal for chopping long CCTV/dashcam/livestream recordings into the exact seconds that matter and for extracting still frames to feed into image and face tools.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download the app for your OS from https://github.com/mifi/lossless-cut/releases and open the target file locally.
2. Set in/out points on the timeline for the segment(s) you care about; add multiple segments for batch export.
3. Export lossless clips (stream copy — no re-encode), or use "Extract frame" / "Export all frames" to pull stills.
4. Inspect the file's format/streams in the app; then run exported frames through image analysis and the clips through detail review.
5. Pivot: feed extracted frames to reverse-image, face-search and EXIF/metadata tools; the clip's preserved `metadata-exif` may carry device/time/location.

## Inputs → Outputs
- **In:** `image`/video/audio file (local)
- **Out:** trimmed segments and extracted frames with original `metadata-exif` preserved
- **Empty/negative result looks like:** a corrupt or DRM-protected file that won't open, or a container ffmpeg can't stream-copy cleanly (rare; the app will warn and offer a re-encode fallback that breaks the lossless guarantee).

## Gotchas & OpSec
- OpSec: **passive** — fully local; no upload, nothing reaches the subject.
- It is a *cutter*, not an analyser: it isolates footage; the actual identification happens in the tools you feed the clips/frames into.
- Lossless keying is on keyframes, so exact cut points can shift by a fraction of a second unless you enable smart-cut (which re-encodes the boundary).

## Overlaps ("do both")
- Pairs with reverse-image/face-search and metadata tools — LosslessCut produces the precise frame or clip that those tools then analyse.

## Trust & verifiability
`trust: trusted` — open source and built on ffmpeg; operations are local and reproducible, so an exported clip is a faithful, verifiable subset of the original.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lossless-cut |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
