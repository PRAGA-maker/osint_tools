---
id: citizen-evidence-lab
name: Citizen Evidence Lab
description: Use when you have a video or `image` (often eyewitness/social footage) and want to verify its origin, upload time, and authenticity — returns metadata-exif and geolocation verification leads.
url: https://citizenevidence.org/category/method/digital-verification/
category: image-video-face
path:
- image-video-face
bestFor: Verifying eyewitness videos/images — provenance, upload time, and location corroboration.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free resource hub run by Amnesty International; the linked YouTube DataViewer and guides are free.
opsec: passive
opsecNote: Reading guides and running the DataViewer on a public video URL is passive and does not alert an uploader. Standard reverse-image/geolocation OpSec applies when you pivot to those steps.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Amnesty International's crisis/verification team; a respected, methodical authority on open-source video/image verification.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- youtube-dataviewer
- invid
- tineye
- citizen-evidence-lab-toolbox
aliases:
- citizenevidence.org
- Amnesty Citizen Evidence Lab
tags:
- toddington
- curated-directory
- video-verification
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Citizen Evidence Lab

> Amnesty International's digital-verification hub — the methodology and tooling (notably the YouTube DataViewer) for establishing whether a video/image is authentic, when it was uploaded, and where it was shot.

## When to use
You have an eyewitness or social-media video/`image` — for example footage that purportedly shows a missing person, a location, or an event — and need to verify it rather than take it at face value. Citizen Evidence Lab gives you a structured verification workflow (source, date, location, manipulation checks) and the YouTube DataViewer to pull a video's true upload timestamp and thumbnails for reverse-image search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the digital-verification section at https://citizenevidence.org/category/method/digital-verification/.
2. Follow the verification checklist: confirm the original source, extract the real upload time, and cross-check claimed location.
3. Use the YouTube DataViewer (linked from the site) on a video URL to get its upload date/time and thumbnail images.
4. Reverse-image the thumbnails and geolocate visual cues to confirm or debunk the claimed place/date.
5. Pivot: an extracted `geolocation` feeds map analysis; the earliest source often leads to the uploader's account and other footage.

## Inputs → Outputs
- **In:** `image` / video URL
- **Out:** `metadata-exif` (upload time, thumbnails), `geolocation` (verified/derived location)
- **Empty/negative result looks like:** a video that can't be traced to an original or whose claimed time/location fails the checks — that is itself a finding (likely miscaptioned or recycled footage), not a dead end.

## Gotchas & OpSec
- Human-in-the-loop: none, though verification is analyst-driven work, not a one-click answer.
- OpSec: **passive** for reading/analysis; apply normal caution when you pivot to reverse-image and account lookups.
- It is a methodology hub plus the DataViewer — not a face-recognition engine; use it to verify footage, then hand faces to dedicated tools.

## Overlaps ("do both")
- Pairs with `[[youtube-dataviewer]]` — the core Amnesty tool for upload time + thumbnails, applied within this method.
- Pairs with `[[invid]]` and `[[tineye]]` — frame extraction and reverse image search to complete the verification.

## Trust & verifiability
`trust: trusted` — authored by Amnesty International's verification specialists; the guidance is authoritative and the DataViewer's timestamps come straight from platform metadata.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | citizen-evidence-lab |
| category | image-video-face |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
