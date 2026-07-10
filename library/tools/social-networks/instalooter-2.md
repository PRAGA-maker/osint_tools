---
id: instalooter-2
name: InstaLooter
url: https://github.com/althonos/instalooter
category: social-networks
path:
- social-networks
description: Use when you have an Instagram `username` and want to bulk-download a profile's media — returns saved `image`s (with any EXIF/`geolocation`); NOTE the project is defunct.
bestFor: Bulk-downloading an Instagram profile's or hashtag's photos/videos from the command line (historically) — now largely non-functional.
selectorsIn:
- username
selectorsOut:
- image
- geolocation
status: down
pricing: free
costNote: Free and open-source (GPL-3.0), but defunct — last release v2.0.0 in April 2018 and marked defunct by its author; Instagram's changes have likely broken it.
opsec: active
opsecNote: Scraping Instagram at volume — especially with login credentials — risks account action and is visible to Instagram. If you ever run it, use a burner account and expect blocks. Because it is defunct, prefer a maintained alternative rather than troubleshooting bans.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: A once-popular (2.1k-star) open-source Instagram scraper, now abandoned; code is auditable but no longer maintained and generally non-working against current Instagram.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- instalooter
- althonos/instalooter
tags:
- instagram
- open-source
- cli
- defunct
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# InstaLooter

> A once-popular Python CLI for bulk-downloading Instagram media without the API — now **defunct** (abandoned since 2018) and generally non-functional; documented here mainly to steer you to a maintained alternative.

## When to use
Historically: you had an Instagram `username` (or hashtag) and wanted to pull all its photos/videos locally — including any that still carried EXIF/`geolocation` — for offline analysis. **In practice, do not reach for this today:** the project is marked defunct, its last release predates years of Instagram anti-scraping changes, and it will usually fail. Use it only if you already have it working against an archived target; otherwise pick a maintained scraper.

## How to use it (`bestInteractionPattern`: cli)
1. (Legacy) Install from source/pip: `pip install instalooter` — expect breakage on current Instagram.
2. Run against a profile: `instalooter user <username> <dest-dir>`, or `instalooter hashtag <tag> <dir>`.
3. Optionally authenticate (`instalooter login`) for private-adjacent access — high ban risk; use a burner.
4. Inspect the downloaded media locally for EXIF/geotags and content.
5. Pivot: if it fails (the common case), switch to a maintained tool; feed any recovered images into reverse-image/EXIF tools.

## Inputs → Outputs
- **In:** Instagram `username` (or hashtag)
- **Out:** downloaded `image`/video files, plus any residual `geolocation`/EXIF
- **Empty/negative result looks like:** errors, empty downloads, or login walls — which today usually means the tool is broken against current Instagram, not that the profile is empty.

## Gotchas & OpSec
- **Defunct:** expect it not to work; don't sink time into fixing a dead scraper.
- Instagram strips most EXIF on upload, so geotags are rarely present anyway.
- OpSec: **active** — scraping (especially logged-in) risks account bans and is visible to Instagram; only ever use a burner account.

## Overlaps ("do both")
- Superseded by maintained scrapers like Instaloader; pair any recovered media with `[[jimpl]]`/`[[verexif]]` (EXIF) and reverse-image search.

## Trust & verifiability
`trust: community` — genuine, auditable open-source, but abandoned and non-working; treat its presence in the library as a historical pointer, not a recommendation to run it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instalooter-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username → image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |
