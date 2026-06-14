---
id: mediainfo
name: MediaInfo
description: Use when you have a video or audio file and want its technical metadata — returns codec, container, duration, encoder tags and any embedded creation/device fields.
url: https://mediaarea.net/en/MediaInfo
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Reading codec/container/encoder metadata and embedded tags from media files, locally and offline.
input: Video and audio files
output: Codec, bitrate, duration, stream, and tag metadata
selectorsIn:
- metadata-exif
- device-id
selectorsOut:
- metadata-exif
- device-id
status: live
pricing: free
costNote: Free and open source (BSD-style license); GUI, CLI and library all free.
opsec: passive
opsecNote: Runs entirely locally on your machine — nothing is uploaded. Ideal when handling sensitive case media you cannot send to a web service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: MediaInfo is a mature, open-source, widely-used media metadata tool from MediaArea; source is public and it is packaged in major Linux distros. Highly reliable for what it reports.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- mediainfo CLI
tags:
- metadata
- video
- audio
source: arf-seed
lastVerified: ''
enrichment: full
---

# MediaInfo

> Free, open-source local tool that dumps the technical metadata of media files — codec, container, duration, bitrate, encoder strings and embedded tags.

## When to use
You have a video or audio file tied to a case (a clip from a phone, CCTV export, a social download) and want its `metadata-exif`-style technical fields: container/codec, duration, frame rate, encoder string, and any embedded creation date or device/software tags. These can hint at the recording `device-id`/software, confirm whether a file was re-encoded, and time-anchor footage. Run it locally so sensitive media never leaves your machine.

## How to use it (`bestInteractionPattern`: cli)
1. Install MediaInfo from https://mediaarea.net/en/MediaInfo (GUI, CLI, or library; available in most package managers).
2. Run the CLI: `mediainfo path/to/file.mp4` for a full report, or `mediainfo --Output=JSON file.mp4` for parseable output.
3. Read the General/Video/Audio sections (`selectorsOut`: metadata-exif tags, encoder/`device-id` strings, dates).
4. Pivot: an encoder/device string narrows the source device; a creation date supports a timeline; corroborate against the original file's filesystem timestamps.

## Inputs → Outputs
- **In:** a media file; `metadata-exif`/`device-id` you want to read.
- **Out:** `metadata-exif` (codec, container, duration, bitrate, tags, dates), `device-id`/software hints from encoder fields.
- **Empty/negative result looks like:** sparse tags / no creation date — common after re-encoding or platform upload, which strips metadata.

## Gotchas & OpSec
- Social platforms re-encode and strip most metadata; analyse the original file, not a downloaded copy, where possible.
- Reports what is embedded only — absence of a device tag isn't proof of anything.
- OpSec: passive — fully local, nothing uploaded; the right choice for sensitive media.

## Overlaps ("do both")
- Pair with an EXIF-focused image tool (e.g. `[[metadata2go]]`) for stills; MediaInfo is the stronger choice for video/audio containers.

## Trust & verifiability
`trust: trusted` — mature open-source project with public source and wide distribution; reliable for the technical metadata it reports.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mediainfo |
| category | image-video-face |
| selectorsIn → selectorsOut | metadata-exif, device-id → metadata-exif, device-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
