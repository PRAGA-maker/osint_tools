---
id: geotagonline
name: GeoTagOnline
description: Use when you have a JPG `image` and a `geolocation` and want to write (or read/overwrite) the EXIF GPS tag — returns the photo with `metadata-exif` set.
url: https://geotagonline.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Reading or writing the GPS/geolocation EXIF header of JPG photos in bulk from the browser.
selectorsIn:
- image
- geolocation
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free browser-based geotagging for JPGs; marketed for local-SEO. No account needed for basic use.
opsec: passive
opsecNote: Runs in-browser for tagging your own images, so it does not touch any target. The OpSec use here is defensive/sock-puppet — crafting or scrubbing EXIF geolocation on photos you publish so they don't leak your real location. Never upload a subject's sensitive images to a third-party site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small commercial SEO utility; fine for writing EXIF tags on your own images, but it is a third-party site — do not feed it evidence photos.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Geotag Online
tags:
- opsec-investigator-tooling
- metadata
- sock-puppet
- exif
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# GeoTagOnline

> A browser JPG geotagger — read or write the GPS EXIF header of a photo. In an investigator's kit it's mostly a sock-puppet / OpSec tool for controlling the location metadata on images you publish.

## When to use
You have a JPG `image` and want to set, change, or verify its embedded `geolocation` (EXIF GPS). Defensively: strip or fake the geotag on a photo before posting it from a sock-puppet persona so it doesn't reveal where you really are. Analytically: confirm what coordinates a JPG currently carries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://geotagonline.com.
2. Drag-and-drop or upload the JPG(s) — bulk mode is supported. Only `.jpg` is accepted.
3. Click the map to set the coordinates you want written into the EXIF header, add optional description/comment tags.
4. Download the re-tagged photo. Pivot: to *read* a suspect image's existing coordinates for geolocation work, prefer a dedicated EXIF viewer/`[[exiftool]]`-style tool; use this when you need to *write* a tag.

## Inputs → Outputs
- **In:** `image` (JPG) + a chosen `geolocation`
- **Out:** the same image with `metadata-exif` (GPS + description) set
- **Empty/negative result looks like:** a non-JPG is rejected; an image with no GPS tag simply shows blank coordinates until you set them.

## Gotchas & OpSec
- JPG only — PNG/HEIC won't work.
- It is a third-party web app: never upload a victim's or target's sensitive photos to it. Use it on your own persona imagery.
- Writing a fake geotag is for legitimate persona OpSec, not for fabricating evidence.

## Overlaps ("do both")
- Complements EXIF *readers* — those extract location from a subject's photo; this writes/edits location on yours.

## Trust & verifiability
`trust: unverified` — a minor commercial SEO utility with no security assurances; suitable only for tagging your own images, never for handling case evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geotagonline |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | image, geolocation → metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
