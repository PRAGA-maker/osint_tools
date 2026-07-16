---
id: ffmpeg
name: FFmpeg
description: Use when you have a video/audio file (a `metadata-exif` carrier) and want to pull frames and embedded metadata — returns `image` stills and `metadata-exif` for downstream search.
url: https://ffmpeg.org/
category: documents-metadata
path:
- documents-metadata
bestFor: Extracting frames/thumbnails and reading embedded metadata from video/audio evidence.
selectorsIn:
- metadata-exif
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Free and open-source; runs locally on any OS. No account, no data leaves your machine.
opsec: passive
opsecNote: FFmpeg runs entirely offline on your own machine — nothing is uploaded, so processing a target's video leaks nothing. This is the safe way to handle sensitive footage before touching any online tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: The de-facto standard open-source multimedia framework, widely audited and used across the industry (listed in Trace Labs' awesome-osint, Images & Video Analysis).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- ffmpeg
- ffprobe
tags:
- video
- audio
- frame-extraction
- metadata
source: tracelabs-repos
lastVerified: '2026-07-16'
enrichment: full
---

# FFmpeg

> The universal, offline video/audio toolkit — turn a clip into searchable stills and read its hidden metadata, all on your own machine.

## When to use
You have a video (a ransom clip, a social post, CCTV, a phone video) and need to (a) pull clean frames to run through reverse-image/face search, or (b) read embedded metadata (creation time, device, GPS, codec) that can date or place the recording. Because it runs locally, it's the correct first step for any footage you don't want to expose to a cloud service.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://ffmpeg.org/ (ships with `ffprobe`).
2. Read metadata: `ffprobe -v quiet -print_format json -show_format -show_streams input.mp4` — look for `creation_time`, `com.apple.quicktime.location.*` (GPS), make/model, encoder.
3. Extract key frames for face/reverse-image search: `ffmpeg -i input.mp4 -vf "fps=1" frame_%04d.jpg` (or `-vf select='eq(pict_type,I)'` for scene keyframes).
4. Sharpen a still or grab one exact timestamp: `ffmpeg -ss 00:01:23 -i input.mp4 -frames:v 1 still.png`.
5. Pivot: feed extracted `image` frames to `[[tineye-reverse-image-search]]`/face-search; feed GPS/`metadata-exif` to mapping and timeline tools.

## Inputs → Outputs
- **In:** a video/audio file (the `metadata-exif` carrier)
- **Out:** extracted `image` frames/thumbnails and dumped `metadata-exif` (timestamps, GPS, device, codec)
- **Empty/negative result looks like:** `ffprobe` shows only technical stream data with no creation time/GPS/device — the file was re-encoded or stripped (most platform uploads strip metadata); frames still extract fine.

## Gotchas & OpSec
- Social platforms re-encode uploads and strip most metadata — don't expect GPS on a downloaded Instagram/WhatsApp video; a original-off-the-phone file is far richer.
- Frame extraction quality depends on source resolution/compression; grab I-frames for the cleanest stills.
- It's a CLI with a steep flag set — keep a cheat-sheet; wrong flags silently produce empty or huge output.

## Overlaps ("do both")
- Pairs with `[[tineye-reverse-image-search]]` and face-search (FFmpeg makes the stills they search) and with EXIF tools like ExifTool — ExifTool is deeper on metadata, FFmpeg is the frame/transcode workhorse.

## Trust & verifiability
`trust: trusted` — an industry-standard, open-source, locally-run tool; output is exactly what's in the file, so the only trust question is the source file's own authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ffmpeg |
| category | documents-metadata |
| selectorsIn → selectorsOut | metadata-exif → image, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
