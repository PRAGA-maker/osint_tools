---
id: jeffrey-s-exif-viewer
name: Jeffrey's Exif Viewer
description: Use when you have an image (URL or file) and want a thorough EXIF/metadata dump including GPS and camera details — returns full metadata via Jeffrey Friedl's viewer.
url: https://regex.info/blog/
category: image-video-face
path:
- image-video-face
- images
- metadata
bestFor: Comprehensive EXIF/IPTC/XMP metadata readout (including GPS) from an image by URL or upload.
input: Image file or image URL
output: Full EXIF/IPTC/XMP metadata, GPS coordinates, camera/lens, timestamps
selectorsIn:
- image
- metadata-exif
selectorsOut:
- geolocation
- metadata-exif
- device-id
status: live
pricing: free
costNote: Free; donation-supported.
opsec: passive
opsecNote: You submit an image file or URL to a third-party site. Submitting a URL causes that site's server to fetch the image (your IP is not exposed to the host). Uploaded files go to a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Jeffrey Friedl's Image Metadata Viewer is one of the longest-standing, widely cited EXIF tools in OSINT. The blog (regex.info/blog) is its home; the viewer lives at exif.regex.info.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- jeffreys-image-metadata-viewer
- jimpl
aliases:
- Jeffrey Friedl's Image Metadata Viewer
tags:
- metadata
- exif
source: arf-seed
lastVerified: ''
enrichment: full
---

# Jeffrey's Exif Viewer

> Jeffrey Friedl's long-running web EXIF viewer — the canonical "paste a URL or upload a photo, get every metadata field including GPS" tool. (Home/blog URL; the live viewer is at exif.regex.info.)

## When to use
You have an `image` (file or a URL to one) and need its embedded `metadata-exif`: GPS `geolocation`, camera/lens `device-id`, capture timestamps, and software history. Core move when a photo of or from a missing person may still carry geotags or original-device fingerprints before platform stripping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the viewer (linked from https://regex.info/blog/ → "Image Metadata Viewer", i.e. exif.regex.info — see `[[jeffreys-image-metadata-viewer]]`).
2. Paste an image URL or upload a file.
3. Read the full dump: GPS coordinates (with map link), make/model/serial, lens, date/time, and edit/software fields.
4. Pivot: GPS feeds geolocation/mapping; camera serial/model can link multiple photos to one `device-id`; timestamps feed your timeline.

## Inputs → Outputs
- **In:** `image` file or image URL
- **Out:** `geolocation` (GPS), `metadata-exif` (EXIF/IPTC/XMP), camera `device-id`/serial
- **Empty/negative result looks like:** "no EXIF" or only basic dimensions — common for images downloaded from social platforms, which strip metadata on upload.

## Gotchas & OpSec
- Most social-media images are stripped of EXIF; absence of GPS is normal and not evidence the photo lacked it originally. Seek the original file.
- Submitting a URL makes the host's server fetch the image (good for your OpSec); uploading a file sends it to a third party.
- OpSec: passive; the subject is not contacted.

## Overlaps ("do both")
- Same tool as `[[jeffreys-image-metadata-viewer]]` (exif.regex.info). Pair with `[[jimpl]]` for a second opinion and a cleaner GPS map.

## Trust & verifiability
`trust: trusted` — a reference-grade, long-maintained EXIF viewer widely used in OSINT. Metadata can be edited/spoofed, so corroborate GPS/time against image content.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jeffrey-s-exif-viewer |
| category | image-video-face |
| selectorsIn → selectorsOut | image, metadata-exif → geolocation, metadata-exif, device-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
