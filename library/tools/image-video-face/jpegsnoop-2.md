---
id: jpegsnoop-2
name: JPEGsnoop
description: Use when you have an `image` (JPEG/AVI/PSD) and want to read its embedded metadata and detect editing/forgery from its compression signature — returns metadata-exif, geolocation, device-id.
url: https://sourceforge.net/projects/jpegsnoop
category: image-video-face
path:
- image-video-face
bestFor: Deep JPEG metadata extraction and tamper/edit detection via compression-signature analysis.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
- device-id
status: live
pricing: free
costNote: Free and open source (GPLv2); a standalone Windows executable, no account or purchase.
opsec: passive
opsecNote: Fully offline analysis on a file you already hold — nothing is sent to the target or any server, so it is completely passive and safe for sensitive evidence. Work on a copy to preserve the original's hash.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-standing, widely cited forensic utility (Calvin Hass) with 100k+ downloads; its EXIF read-out is authoritative, but its tamper "assessment" is a heuristic on quantization tables, not proof of manipulation.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- JPEGsnoop
tags:
- image-analysis
- exif
- forensics
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- falcon-arch-linux
- sourceforge-net
---

# JPEGsnoop

> A free Windows JPEG forensic decoder: read every scrap of embedded metadata and flag likely edits from the image's compression fingerprint.

## When to use
You have an `image` (a photo of/from the subject, a suspect profile picture, a location shot) and want two things offline: (1) all embedded `metadata-exif` — camera make/model (`device-id`), timestamps, and GPS `geolocation` if present; and (2) a signal on whether the file was re-saved/edited (e.g. run through Photoshop) rather than being a camera original. Ideal when you need to do this without uploading the image anywhere.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download JPEGsnoop from https://sourceforge.net/projects/jpegsnoop (or its GitHub mirror) — Windows, no install needed.
2. Open a **copy** of the target `image` (File → Open Image). Batch mode handles many files at once.
3. Read the decoded report: full EXIF (camera, lens, timestamps, GPS coords → `geolocation`; make/model → `device-id`), embedded thumbnails, and any software tags.
4. Check the "compression signature" verdict — JPEGsnoop compares the file's quantization tables against a database of known cameras/editors to guess "processed/edited" vs "original camera". Treat this as a lead, not a verdict.
5. Pivot: GPS coords feed mapping; an editor/software tag suggests the image is not an original; extracted thumbnails may differ from the visible image (revealing prior crops/edits).

## Inputs → Outputs
- **In:** `image` (JPEG, AVI/MJPG, or PSD file)
- **Out:** `metadata-exif`, `geolocation` (GPS), `device-id` (camera make/model), edit/forgery heuristic, embedded thumbnails
- **Empty/negative result looks like:** metadata stripped (common for social-media downloads) — no EXIF/GPS. The compression analysis still runs, but absence of metadata is expected for re-hosted images, not proof of nothing.

## Gotchas & OpSec
- Human-in-the-loop: interpreting the tamper heuristic needs judgement — it detects re-compression, which happens innocently (every social upload re-saves).
- Social platforms strip EXIF on upload; a metadata-free image usually means it was re-hosted, not that it was scrubbed maliciously.
- OpSec: fully offline/passive — the reason to prefer it over an online EXIF viewer for sensitive files.

## Overlaps ("do both")
- Pairs with online EXIF viewers and reverse-image tools ([[pimeyes-com]]) — JPEGsnoop gives forensic depth offline; reverse-image tells you where else the picture appears.

## Trust & verifiability
`trust: community` — a mature, heavily-used open-source forensic tool; its raw metadata output is reliable, while the edit-detection is a well-regarded heuristic that should corroborate, not conclude.
