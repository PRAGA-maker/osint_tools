---
id: exif-viewer-addons-mozilla-org
name: Exif Viewer (Firefox add-on)
description: Use when you have an `image` (local file or a URL) and want its EXIF/IPTC/XMP metadata and any embedded GPS in-browser — returns `metadata-exif` and `geolocation`.
url: https://addons.mozilla.org/en-US/firefox/addon/exif-viewer/
category: documents-metadata
path:
- documents-metadata
bestFor: Viewing EXIF/IPTC/XMP metadata and GPS coordinates of JPEG images directly inside Firefox.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free Firefox add-on (~12.5k users); no account.
opsec: passive
opsecNote: For a LOCAL image the extension parses metadata entirely offline. If you point it at a REMOTE image URL, your browser fetches that image from its host, which logs your IP — do that from a sock-puppet/VPN session, or download the file first and inspect it locally.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Community-published AMO add-on, last updated ~2024 with a middling rating; corroborate any decisive metadata (esp. GPS) with a second EXIF tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- exif viewer firefox
tags:
- exifdata
- EXIF Data Related Sites
- image
- geolocation
- metadata
source: uk-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Exif Viewer (Firefox add-on)

> A one-click Firefox add-on that reads a JPEG's EXIF/IPTC/XMP metadata — including GPS coordinates — without leaving the browser.

## When to use
You have an `image` — a photo saved from a profile, a listing, or a message — and want to know what its embedded metadata reveals: camera make/model, timestamps, software, and crucially any GPS `geolocation` tag that pinpoints where it was taken. Fast triage before deciding whether an image is worth deeper forensic work.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Exif Viewer" from https://addons.mozilla.org/en-US/firefox/addon/exif-viewer/ in Firefox.
2. For a local file: open it, right-click, and choose the Exif Viewer option; for a remote image: right-click the image on the page.
3. Read the panel — EXIF (camera, exposure, timestamps), IPTC/IIM, and XMP fields, plus GPS latitude/longitude if present.
4. If GPS is present, plug the coordinates into a map (e.g. via [[mapswitcher]]) to place the shot.
5. Pivot: a GPS tag gives `geolocation`; camera/software strings and timestamps corroborate device and timeline; absence of metadata is itself informative (see below).

## Inputs → Outputs
- **In:** `image` (local JPEG or an image URL)
- **Out:** `metadata-exif` (camera, timestamps, software, IPTC/XMP) and `geolocation` (GPS tag, when present)
- **Empty/negative result looks like:** no EXIF shown — the image was stripped (most social platforms remove metadata on upload), re-saved, or is a screenshot; absence does NOT mean the original had none.

## Gotchas & OpSec
- Social-media and messaging platforms usually **strip EXIF on upload**, so a clean image often means "went through a platform", not "never geotagged".
- Reading a remote URL fetches the image from its host — do it from a clean session or download first.
- Works on JPEG-family metadata; for other formats/deeper analysis use a dedicated EXIF/forensics tool.

## Overlaps ("do both")
- Pair with a bulk image grabber like [[download-all-images]] (collect a page's images, then inspect each) and with map tools like [[mapswitcher]] to place any GPS hit.

## Trust & verifiability
`trust: community` — a third-party AMO extension; it reports what's in the file accurately but metadata can be edited or forged, so treat a GPS tag as a strong lead to verify, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exif-viewer-addons-mozilla-org |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
