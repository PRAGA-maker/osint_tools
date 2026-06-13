---
id: ffmpeg
name: FFmpeg
description: Multimedia framework for extracting, converting and processing video and audio.
url: https://ffmpeg.org/
category: documents-metadata
path:
- documents-metadata
bestFor: Pulling frames/thumbnails and metadata from video evidence for analysis.
selectorsIn:
- metadata-exif
selectorsOut:
- image
- metadata-exif
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Listed in Trace Labs awesome-osint (Images & Video Analysis).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- video
- audio
- frame-extraction
source: tracelabs-repos
lastVerified: ''
enrichment: full
---

# FFmpeg

> Multimedia framework for extracting, converting and processing video and audio.

- **URL:** https://ffmpeg.org/
- **Best for:** Pulling frames/thumbnails and metadata from video evidence for analysis.
- **Source:** harvested from `tracelabs-repos`

Use to extract key frames from a video for reverse image/face search, or to read embedded video metadata.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
