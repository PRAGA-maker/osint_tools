---
id: impulseadventure
name: ImpulseAdventure
description: Use when you have a JPEG and want to inspect its compression signatures and structure for tampering/source clues — returns forensic markers via the JPEGsnoop tool hosted on this site.
url: http://www.impulseadventure.com/photo/jpeg-snoop.html
category: image-video-face
path:
- image-video-face
bestFor: Home/download page for JPEGsnoop, a JPEG forensics tool that reveals compression signatures and edit indicators.
selectorsIn:
- image
- metadata-exif
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free; JPEGsnoop is open-source (GPL).
opsec: passive
opsecNote: This is a documentation/download page plus a downloadable desktop tool; analysis runs locally with no outbound contact to the target.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: trusted
trustNote: ImpulseAdventure is the long-standing personal site of Calvin Hass, original author of JPEGsnoop; widely cited in image-forensics references.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- jpegsnoop
- jpegsnoop-2
aliases:
- JPEGsnoop home
tags:
- image-analysis
- jpeg-forensics
source: awesome-osint
lastVerified: ''
enrichment: full
---

# ImpulseAdventure

> The author's home page for JPEGsnoop — a free Windows tool that decodes a JPEG's internal structure and compression signature to flag editing/re-saving.

## When to use
You have an `image` (JPEG) whose authenticity is in question — e.g., a photo of a missing person that may have been edited, cropped, or re-saved through a phone/editor. JPEGsnoop's database of quantization-table "signatures" can indicate the likely originating software/camera and whether the file was edited rather than straight out of camera.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Open http://www.impulseadventure.com/photo/jpeg-snoop.html and download the JPEGsnoop Windows binary (also mirrored on SourceForge — see `[[jpegsnoop-2]]`).
2. Run the app and open the target `.jpg`.
3. Read the decoded output: EXIF/`metadata-exif`, the compression quality tables, and the "assessment" line indicating whether the image appears edited/processed and the matched software signature.
4. Pivot: EXIF GPS/timestamps feed geolocation and timeline work; a "processed by Photoshop" verdict raises suspicion about a supplied photo.

## Inputs → Outputs
- **In:** `image` (JPEG/JPG; also reads some AVI/PDF/THM)
- **Out:** `metadata-exif`, quantization signatures, edit/processing assessment
- **Empty/negative result looks like:** "Class 1 — Image is processed/edited" vs "Class 3/4 — possibly original"; unknown signatures yield no confident verdict, not proof of authenticity.

## Gotchas & OpSec
- Windows-only desktop tool; signature database skews toward older cameras/software, so modern phone images may be "unknown."
- A processing verdict is a signal, not proof — social platforms re-compress every upload, which itself looks like "editing."
- OpSec: passive; everything runs locally on your machine.

## Overlaps ("do both")
- Pairs with `[[jeffreys-image-metadata-viewer]]` (full EXIF dump) and `[[jimpl]]` for a fast web-based EXIF read before a deep local JPEGsnoop pass.

## Trust & verifiability
`trust: trusted` — original author's site for a well-known open-source forensics tool. The verdicts are heuristic; corroborate edits with a second method.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | impulseadventure |
| category | image-video-face |
| selectorsIn → selectorsOut | image, metadata-exif → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (manual-review) |
