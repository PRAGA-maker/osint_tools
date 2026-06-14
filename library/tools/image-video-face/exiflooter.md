---
id: exiflooter
name: ExifLooter
description: Use when you have images (or a URL/directory of them) and want to extract GPS metadata and map it — returns geolocation from metadata-exif.
url: https://github.com/aydinnyunus/exiflooter
category: image-video-face
path:
- image-video-face
bestFor: Pull GPS/EXIF from one or many images (including by crawling a URL) and plot the coordinates on a map.
selectorsIn: [image, domain, metadata-exif]
selectorsOut: [geolocation, metadata-exif, device-id]
status: live
pricing: free
opsec: active
opsecNote: When pointed at a remote URL it fetches that target's images directly from your IP and opens map links (OpenStreetMap). Local-file mode is passive. Use a VPN when scanning a live site.
humanInLoop: true
humanInLoopReason: [rate-limit]
bestInteractionPattern: cli
trust: community
trustNote: Open-source project (aydinnyunus/exiflooter) listed in awesome-osint; popular but third-party — review the code before running against sensitive targets.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags: [image-analysis, exif, geolocation, open-source, cli]
source: awesome-osint
lastVerified: ''
enrichment: full
---

# ExifLooter

> A Python CLI that extracts GPS/EXIF from images — single files, whole directories, or every image it can crawl from a URL — and links the coordinates straight to a map.

## When to use
You have one or many `image` files, or a `domain`/URL hosting images, and want to harvest embedded `geolocation`. It shines for bulk work: scanning a directory of recovered photos or a target website's image assets for any pictures that still carry GPS.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install exiflooter` (or clone the repo and `pip install -r requirements.txt`).
2. Single image: `exiflooter -i photo.jpg`. Directory: `exiflooter -p ./images`. URL crawl: `exiflooter -u https://target.tld`.
3. It prints EXIF/GPS and outputs map links (OpenStreetMap) for any coordinates found.
4. Pivot: cluster coordinates to infer a home/work area; correlate timestamps; feed device make/model into corroboration.

## Inputs → Outputs
- **In:** `image`, `domain` (URL to crawl), `metadata-exif`
- **Out:** `geolocation`, `metadata-exif`, `device-id`
- **Empty/negative result looks like:** "no GPS data" for most images — platform-uploaded photos are stripped; original camera/phone files are where you find hits.

## Gotchas & OpSec
- Human-in-the-loop: large URL crawls can hit rate limits / get blocked.
- OpSec: ACTIVE in URL mode — it fetches images from the target site directly, leaving requests in their logs. Run behind a VPN for remote scans; local/directory mode is passive.

## Overlaps ("do both")
- Pairs with `[[exiftool]]` (deeper per-file forensic detail) — use ExifLooter for fast bulk GPS triage, ExifTool to fully dump a flagged file.

## Trust & verifiability
`trust: community` — credible open-source tool with active community use; still third-party code, so inspect it before pointing it at sensitive material.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exiflooter |
| category | image-video-face |
| selectorsIn → selectorsOut | image, domain, metadata-exif → geolocation, metadata-exif, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes |
