---
id: exif-remove-chrome-google-com
name: Exif Remove (Chrome extension)
description: Use when you need to strip EXIF/metadata from your OWN images before publishing — an OpSec tool that removes geolocation and camera data — returns cleaned images.
url: https://chromewebstore.google.com/detail/exif-remove/eamoopmkknodiipphhmfckacmigfngda
category: documents-metadata
path:
- documents-metadata
bestFor: Batch-removing EXIF metadata (GPS, camera, timestamps) from images you are about to share, for OpSec.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free Chrome extension; no account or payment. Processing is local in the browser.
opsec: passive
opsecNote: This is a defensive/OpSec tool — it REMOVES metadata rather than reading a target's. Use it on your own images (screenshots, evidence you republish) so you don't leak your GPS/device/timestamp. Processing is client-side, so images aren't uploaded, but verify that on install.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A third-party Chrome extension (not a major vendor); it advertises local, permission-light processing, but audit its permissions before trusting it with sensitive images.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Exif Remove extension
tags:
- exif
- metadata
- opsec
source: uk-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Exif Remove (Chrome extension)

> A one-click/batch EXIF stripper for Chrome — the defensive counterpart to metadata-reading tools: it removes GPS, camera and timestamp data from images before you share them.

## When to use
You are about to publish, send or attach an image and don't want it to leak your own EXIF — GPS coordinates, device model, capture timestamp. This is an OpSec hygiene tool for the investigator, not a way to read a target's metadata (for that, use an EXIF *reader*). Reach for it when you republish evidence, share a screenshot, or upload an image and need it scrubbed of identifying metadata first.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Exif Remove" from the Chrome Web Store and review its requested permissions.
2. Feed it the `image`(s) you want cleaned (it supports JPEG/PNG/TIFF and batch processing).
3. Let it strip the EXIF locally; download the cleaned copies.
4. Verify with an EXIF reader that GPS/camera/timestamp fields are gone before sharing.
5. Pivot: keep the original (with metadata) in your case file; publish only the scrubbed copy.

## Inputs → Outputs
- **In:** `image` (your own, to be cleaned)
- **Out:** the same image with `metadata-exif` removed (GPS/camera/timestamp stripped)
- **Empty/negative result looks like:** an image that still shows EXIF in a reader afterward — some fields (or formats) may survive; confirm, don't assume.

## Gotchas & OpSec
- Direction matters: this **removes** metadata; it does not extract a subject's. Pair with an EXIF reader for the offensive side.
- Trust: it's a third-party extension — audit permissions; the claim of local-only processing should be verified before using it on anything sensitive.
- Always confirm the scrub worked with an independent reader before publishing.

## Overlaps ("do both")
- The mirror image of EXIF *readers* in `documents-metadata` — use a reader to pull a target's metadata, use this to strip your own. Do both sides of the metadata game deliberately.

## Trust & verifiability
`trust: unverified` — a minor third-party extension; verify its permissions and that the output is actually clean with a separate EXIF reader.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exif-remove-chrome-google-com |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
