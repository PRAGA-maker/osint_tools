---
id: aperislove
name: Aperi'Solve
description: Use when you have an `image` and want to pull hidden data and embedded metadata — returns `metadata-exif` (EXIF/GPS) plus any steganographic payloads for further leads.
url: https://www.aperisolve.com/
category: image-video-face
path:
- image-video-face
bestFor: One-shot layered analysis of an image — EXIF/metadata plus a full steganography sweep (zsteg, steghide, outguess, binwalk, foremost, strings).
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free web service (currently v3.4.2); no account required. Also self-hostable via Docker if you prefer not to upload.
opsec: passive
opsecNote: Passive toward the subject — you analyse a file you already hold, nothing is sent to the image's origin. BUT you are uploading the target's image to a third-party server, which may retain it; for sensitive material use the self-hosted/Docker build or offline exiftool/binwalk instead. Never upload evidence you are not authorised to disclose.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known open-source image-forensics front-end (Aperi'Solve) wrapping standard, trusted CLI tools; results reflect those underlying tools' output.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- exiftool
tags:
- Image Search and Identification
- Image Analyze
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Aperi'Solve

> A browser-based image-forensics workbench: drop in a photo and it runs EXIF/metadata extraction plus a full steganography sweep (zsteg, steghide, outguess, binwalk, foremost, strings) and RGB/alpha layer analysis in one pass.

## When to use
You have an `image` tied to a subject — a profile photo, a photo sent in a chat, a picture from a listing or forum — and want everything it can leak: camera make/model, timestamps, and especially embedded **GPS coordinates** (`geolocation`), plus any hidden files or text a steganography tool can recover. It is the fast first stop before deeper manual forensics.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.aperisolve.com/ (use a sock-puppet/research browser).
2. Drag-and-drop or upload the image (PNG, JPG/JPEG, GIF, BMP, TIFF).
3. Optionally enter a candidate password (for steghide/outguess) and tick **Deep analysis** for a slower, more thorough sweep.
4. Read the panels: EXIF/metadata (look for GPS lat/long, device, timestamps), the per-channel bit-plane images, and the zsteg/steghide/binwalk/foremost/strings output for embedded data.
5. Pivot: GPS → a mapping tool; a camera serial or username string → its own lookup; an extracted file → further analysis.

## Inputs → Outputs
- **In:** `image` file
- **Out:** `metadata-exif` (EXIF, device, timestamps), `geolocation` (GPS tags if present), and any steganographic payload/strings recovered
- **Empty/negative result looks like:** clean metadata and no stego hits — common for images stripped by social platforms (which remove EXIF on upload). Absence of GPS is normal, not a failure; try to obtain the original file rather than a re-saved copy.

## Gotchas & OpSec
- Social networks strip EXIF on upload — a downloaded profile pic usually has none; chase the original send/file.
- **You upload to a third-party server.** For sensitive images, run the Docker/self-hosted version or local `exiftool`/`binwalk` instead.
- Steghide/outguess results depend on guessing the right password; a null result doesn't prove nothing is hidden.

## Overlaps ("do both")
- Pairs with `[[exiftool]]` — Aperi'Solve is the quick all-in-one web pass; ExifTool run locally keeps the file offline and gives finer control over metadata fields.

## Trust & verifiability
`trust: community` — a well-regarded open-source project that simply orchestrates standard, auditable forensics tools; verify any critical finding (e.g. GPS) by re-running the underlying tool locally on the original file.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aperislove |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
