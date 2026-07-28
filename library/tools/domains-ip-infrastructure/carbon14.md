---
id: carbon14
name: Carbon14
description: Use when you have a web page (`domain`/URL) with `image`s and want to estimate when it was published — returns approximate dates from the images' HTTP Last-Modified headers.
url: https://github.com/Lazza/Carbon14
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Estimating when a web page (or its images) was published via HTTP Last-Modified headers — web chronolocation.
selectorsIn:
- domain
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open-source Python CLI.
opsec: active
opsecNote: Carbon14 fetches the target page and its linked images directly from the server to read Last-Modified headers — this touches the target site and appears in its logs. Run it from a sock-puppet/VPN session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by Lazza, referenced in Bellingcat guides; Last-Modified headers can be absent, proxied, or reset by CDNs/regeneration, so treat the dates as estimates, not proof.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Carbon14
tags:
- Domain/IP/Links
- Source Code Analyzes
- chronolocation
- timestamps
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Carbon14

> Named after radiocarbon dating — it dates web content by reading the Last-Modified timestamps of the images a page links to.

## When to use
You have a web page and need to know roughly *when* it (or its images) was published — to date a post with no visible timestamp, sanity-check a claimed date, or order events on a site. Carbon14 downloads the page's linked images and reads each image's HTTP `Last-Modified` header, which often reveals when the file was uploaded.

## How to use it (`bestInteractionPattern`: cli)
1. Install: clone `https://github.com/Lazza/Carbon14` (Python) and install requirements.
2. Run it against the target page URL; it enumerates linked images and queries each one's HTTP headers.
3. Read the reported `Last-Modified` dates per image; clustering of dates suggests when the content was actually put up.
4. Corroborate: compare the header dates against any on-page date, the Wayback Machine, and image EXIF.
5. Pivot: an established publication window supports chronolocation/timeline work built from other evidence.

## Inputs → Outputs
- **In:** a page `domain`/URL (and by extension its `image`s)
- **Out:** approximate publication dates (`metadata-exif`-style temporal metadata) from image Last-Modified headers
- **Empty/negative result looks like:** headers missing or all identical/current — the server strips/regenerates Last-Modified (common behind CDNs), so no reliable date can be inferred; fall back to Wayback/EXIF.

## Gotchas & OpSec
- **Active** — it requests files from the target server; that's logged. Use a clean/VPN session.
- Last-Modified is trivially unreliable: CDNs, re-deploys, and image optimizers reset it, so a date is a hint, not evidence — always corroborate.
- Only as good as the images the page links; text-only or CSS-background images yield nothing.

## Overlaps ("do both")
- Pair with the Wayback Machine (first-capture date) and EXIF tools — Carbon14 reads server upload time, Wayback bounds when a page existed, EXIF gives capture time; together they triangulate.

## Trust & verifiability
`trust: community` — a small, transparent open-source tool; its output is directly checkable (re-request the headers yourself), but the underlying signal is inherently soft.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | carbon14 |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, image → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
