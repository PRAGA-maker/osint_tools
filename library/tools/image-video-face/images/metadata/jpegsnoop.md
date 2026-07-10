---
id: jpegsnoop
name: JPEGsnoop
description: Use when you have a JPEG `image` and want deep forensic analysis — returns EXIF `metadata-exif`, camera signature (`device-id`), and tamper/edit indicators to judge authenticity.
url: https://www.impulseadventure.com/photo/jpeg-snoop.html
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Local JPEG forensics — extracting hidden metadata and detecting whether an image was edited/re-saved (e.g. in Photoshop).
selectorsIn:
- image
selectorsOut:
- metadata-exif
- device-id
status: live
pricing: free
costNote: Free Windows desktop tool (also runnable via Wine); open-source. No account.
opsec: passive
opsecNote: Analysis is entirely local — the image never leaves your machine, so nothing is disclosed to any third party or the subject. This makes it safer for sensitive imagery than online metadata viewers. Still handle the file within your legal/ethical rules.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: A long-standing, respected JPEG-forensics utility; its compression-signature database and structural analysis are well-regarded, though "edited" signals are indicators requiring interpretation, not proof.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- online-exif-viewer
- ghiro
aliases:
- JPEGsnoop
- JPEG Snoop
tags:
- metadata
- forensics
- exif
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# JPEGsnoop

> A local JPEG-forensics tool — pull the full hidden metadata, identify the camera/software that produced a file, and read tamper signals to judge whether an image is original or edited.

## When to use
You have a JPEG (a suspected-manipulated photo, an image whose provenance matters, or one you want camera detail from) and need more than a surface EXIF read. JPEGsnoop dumps the full structure and metadata, matches the file's compression signature against known cameras/software (`device-id`), and flags edit indicators — helping you decide if a photo was Photoshopped or re-saved, and what device likely made the original. Doing it locally keeps sensitive imagery off third-party servers.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download JPEGsnoop from impulseadventure.com and run it (Windows; via Wine on Linux/Mac).
2. Open the target `image`.
3. Read the output: full EXIF/`metadata-exif` (camera, timestamps, GPS if present), the compression signature match (which camera/software produced/last-saved it), and the "class" assessment (e.g. likely edited).
4. Interpret edit indicators as signals, not verdicts — a re-save or benign export can trip them.
5. Pivot: GPS EXIF feeds geolocation; camera signature can link multiple images to one device; compare with a plain viewer like `[[online-exif-viewer]]` and batch forensics in `[[ghiro]]`.

## Inputs → Outputs
- **In:** a JPEG `image` (and some other supported files)
- **Out:** `metadata-exif` (camera, timestamps, GPS), camera/software signature (`device-id`), edit/tamper indicators
- **Empty/negative result looks like:** metadata stripped (common for social-media downloads) and an "unknown" signature — absence of EXIF is itself a signal (the image was processed/scrubbed), not a tool failure.

## Gotchas & OpSec
- "Edited/processed" is an **indicator** requiring judgment — re-saving, resizing, or platform re-encoding can trigger it without malicious intent.
- Social-media platforms strip EXIF, so downloaded images often carry no camera/GPS data.
- Windows-native (use Wine elsewhere).
- OpSec: fully local and passive — the file never leaves your machine, ideal for sensitive imagery.

## Overlaps ("do both")
- Complements `[[online-exif-viewer]]` (quick metadata) and `[[ghiro]]` (automated batch forensics) — use JPEGsnoop for deep, offline single-file analysis and authenticity judgment.

## Trust & verifiability
`trust: community` — a respected forensic utility; its metadata/signature output is reliable, but tamper signals need expert interpretation. Corroborate an "edited" conclusion with error-level analysis and provenance before asserting manipulation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jpegsnoop |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
