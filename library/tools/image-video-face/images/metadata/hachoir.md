---
id: hachoir
name: Hachoir
description: Use when you have a media or binary file and want to extract embedded metadata and inspect its internal structure — a Python library/CLI returning EXIF, timestamps, device info, and field-level binary layout.
url: https://hachoir.readthedocs.io/
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Extracting embedded metadata and parsing the internal structure of media/binary files.
input: A local file (image, video, audio, archive, or other binary)
output: Embedded metadata (EXIF, timestamps, device/software, duration) and a parsed field tree
selectorsIn:
- image
- metadata-exif
selectorsOut:
- metadata-exif
- device-id
- geolocation
- name
status: live
pricing: free
costNote: Free and open source (pip install hachoir).
opsec: passive
opsecNote: Runs entirely locally on a file you already hold; nothing is sent to any server, so it leaks nothing about your investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Mature, widely used open-source Python project for binary/metadata parsing; deterministic and offline.
missingPersonsRelevance: high
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
- hachoir-metadata
tags:
- metadata
- exif
- python-lib
source: arf-seed
lastVerified: ''
enrichment: full
---

# Hachoir

> An open-source Python library and CLI that parses binary files field-by-field and extracts embedded metadata from images, video, audio, and many other formats.

## When to use
You have a media file (an `image`, video, or audio clip from a tip, social download, or device) and want its embedded `metadata-exif` — capture timestamps, camera/software (`device-id`), and any embedded GPS for a `geolocation` lead, or author/`name` fields. Works offline, so it is ideal for evidence files you must not upload to a web service.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install hachoir`.
2. Extract metadata: `hachoir-metadata suspect_photo.jpg` — prints creation date, camera model, software, GPS (if present), dimensions, duration, etc.
3. Inspect raw structure: `hachoir-urwid file.ext` (interactive tree) or use the Python API (`from hachoir.metadata import extractMetadata`) for scripted bulk processing.
4. Pivot GPS coordinates into mapping tools; cross-check camera/software fields across multiple files to link them to the same device; reverse-search the image itself in `[[google-images]]`.

## Inputs → Outputs
- **In:** `image` (or other binary), `metadata-exif`
- **Out:** `metadata-exif`, `device-id` (camera/software), `geolocation` (if GPS embedded), `name` (author/artist fields)
- **Empty/negative result looks like:** few or no metadata fields — the file was stripped (most images re-uploaded to social platforms lose EXIF) or never had it; absence of GPS is common and not suspicious.

## Gotchas & OpSec
- Social platforms (Facebook, Instagram, Twitter/X) strip EXIF on upload, so files saved from them usually carry no useful metadata — get the original where possible.
- Metadata is trivially editable; treat timestamps and GPS as leads, not proof.
- OpSec: fully passive and offline — strongest privacy posture of any tool here; nothing about the file or your search leaves your machine.

## Overlaps ("do both")
- Complements web EXIF viewers (which require upload) — prefer Hachoir for sensitive evidence. Pair with reverse-image tools (`[[google-images]]`) to combine metadata with where-it-appears analysis.

## Trust & verifiability
`trust: trusted` — mature, well-maintained open-source project; output is deterministic and locally verifiable, with full documentation at hachoir.readthedocs.io.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hachoir |
| category | image-video-face |
| selectorsIn → selectorsOut | image, metadata-exif → metadata-exif, device-id, geolocation, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
