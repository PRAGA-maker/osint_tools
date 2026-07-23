---
id: thexifer
name: TheXifer
description: Use when you have an `image` and want to read, strip or forge its EXIF/IPTC/XMP metadata — returns viewed or rewritten metadata-exif.
url: https://www.thexifer.net
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Viewing, editing, stripping, or planting fake EXIF/IPTC/XMP metadata in a photo online.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free tier — up to 5 files / 60 MB with limited features. Premium adds batch processing (100 files / 300 MB), geolocation editing, and optimisation.
opsec: active
opsecNote: You upload the image to thexifer.net's servers, so a third party receives your file and its original metadata — never upload a sensitive/evidential original; work on a copy. For OpSec use (stripping/forging metadata on your own sock-puppet images) that's fine; for analysing a subject's photo prefer a local tool (ExifTool) so the file never leaves your machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A convenient online metadata editor of unknown operator; because it requires uploading your file, trust is limited. Fine for throwaway sock-puppet images, not for handling evidence.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- thexifer-net
aliases:
- theXifer
- thexifer.net
tags:
- Sock Puppets
- metadata
- exif
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# TheXifer

> An online EXIF/IPTC/XMP metadata viewer *and editor* — read a photo's embedded metadata, strip it clean, or plant fabricated tags (dates, camera, location) for OpSec purposes.

## When to use
Two OSINT uses. Offensive OpSec: you're building a sock puppet and want to **strip** identifying metadata from images you post (or **plant** plausible fake EXIF so a puppet's photos look organically captured). Analytical: quickly **read** the EXIF/IPTC/XMP of an image (camera, timestamps, GPS) — though for a subject's real image you should prefer a local tool so you don't upload evidence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.thexifer.net and upload a **copy** of the image (free tier: up to 5 files / 60 MB).
2. To read: inspect the parsed EXIF/IPTC/XMP panel — camera make/model, timestamps, software, and any GPS `geolocation`.
3. To sanitise: clear the metadata fields and export a stripped copy for safe posting.
4. To forge (OpSec): set fabricated values across the 175 editable tags (date taken, device, location) so a sock-puppet photo carries a consistent, innocuous backstory. Download the rewritten file.
5. Pivot: extracted GPS/timestamps from a *read* corroborate location/time claims; a *stripped* image is now safe to attach to a puppet account.

## Inputs → Outputs
- **In:** an `image` (JPG/PNG/TIFF/GIF/WEBP, some video/PDF)
- **Out:** viewed `metadata-exif`, or a re-exported image with metadata stripped or replaced
- **Empty/negative result looks like:** the metadata panel is largely blank — the image was already stripped (e.g. downloaded from a social platform that scrubs EXIF), so there's nothing to read.

## Gotchas & OpSec
- **Uploading is the risk**: your file (and its original metadata) goes to a third-party server. Never upload an evidential original or a sensitive personal photo — use ExifTool locally for those.
- Planted metadata is trivially detectable as edited by anyone with forensic tooling; it defeats casual inspection, not scrutiny.
- Social platforms strip EXIF on upload anyway, so stripping is often belt-and-braces; the forging use is the more distinctive one.

## Overlaps ("do both")
- For *reading/analysing* a subject's image, prefer a local `exiftool`-based workflow (no upload). Use TheXifer's browser convenience mainly for your own sock-puppet images.

## Trust & verifiability
`trust: unverified` — an anonymous-operator online editor that needs your upload. Acceptable for throwaway OpSec images; keep evidence and sensitive files off it and process those locally.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thexifer |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
