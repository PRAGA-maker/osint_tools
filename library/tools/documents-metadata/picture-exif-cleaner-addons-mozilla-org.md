---
id: picture-exif-cleaner-addons-mozilla-org
name: picture exif cleaner (addons.mozilla.org)
description: Use when you (the investigator) are about to share an image and want to strip its EXIF metadata first — a Firefox add-on that removes embedded GPS/camera data so you don't leak your own info.
url: https://addons.mozilla.org/en-US/firefox/addon/picture-exif-cleaner/
category: documents-metadata
path:
- documents-metadata
bestFor: Stripping EXIF/metadata from images before you upload or share them (OpSec hygiene).
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free Firefox add-on (Mozilla Public License 2.0); no account or payment.
opsec: passive
opsecNote: This is a defensive OpSec tool for YOUR OWN images — it removes EXIF (including GPS coordinates and device info) before you share, so you don't inadvertently leak your location or hardware. It does not read a target's metadata; for that use an EXIF viewer instead. Processing happens locally in the browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A small third-party add-on (~50 users, last updated 2024, modest rating) on Mozilla's official store; low install base means limited community vetting — inspect before trusting with sensitive images.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- picture exif cleaner
tags:
- exifdata
- EXIF Data Related Sites
- opsec
- metadata-removal
source: uk-osint
lastVerified: '2026-07-23'
enrichment: full
---

# picture exif cleaner (addons.mozilla.org)

> A Firefox add-on that scrubs EXIF metadata (GPS, camera model, timestamps) out of images before you share them — an OpSec hygiene tool for the investigator, not a metadata *viewer*.

## When to use
You are about to upload or send an image — a screenshot, a photo, a document scan — as part of an operation and you don't want its embedded EXIF (which can carry GPS coordinates, camera serial, and timestamps) to leak your identity or location. Reach for this to clean your own images. Note the direction: it *removes* metadata for privacy; if your goal is to *read* a target's EXIF to geolocate them, you want an EXIF viewer/extractor instead.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the add-on from https://addons.mozilla.org/en-US/firefox/addon/picture-exif-cleaner/ in Firefox.
2. Load or select the image you intend to share.
3. Use the extension to strip the embedded EXIF/metadata; processing runs locally in your browser.
4. Verify the cleaned copy has no residual GPS/device fields (cross-check with an EXIF viewer) before sharing.
5. Pivot: this is a terminal OpSec step — the cleaned image is what you release; keep the original if you need the metadata for your own records.

## Inputs → Outputs
- **In:** an `image` you own and are about to share
- **Out:** a metadata-stripped copy of the image (no selector output — it removes data, it doesn't yield it)
- **Empty/negative result looks like:** an image that already had no EXIF (e.g. many screenshots) — nothing to strip; that's fine, verify and proceed.

## Gotchas & OpSec
- Direction matters: this cleans metadata; it does not extract a target's. Don't confuse it with an EXIF reader.
- Small, lightly-reviewed add-on — verify it fully removes GPS before relying on it for sensitive material, and consider a maintained alternative for high-stakes work.
- OpSec: the whole point is defensive — always scrub images before sharing to avoid self-doxxing.

## Overlaps ("do both")
- The inverse of EXIF *viewers*/extractors: use a viewer to read a subject's image metadata, and this cleaner to remove your own before you publish. Pair both sides in any workflow where you both analyse and share images.

## Trust & verifiability
`trust: unverified` — a low-install third-party add-on on Mozilla's official store; the code is inspectable but community vetting is thin, so confirm the strip worked before trusting it with anything sensitive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | picture-exif-cleaner-addons-mozilla-org |
| category | documents-metadata |
| selectorsIn → selectorsOut | image →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
