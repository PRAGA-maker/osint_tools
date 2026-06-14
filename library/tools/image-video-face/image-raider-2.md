---
id: image-raider-2
name: Image Raider
description: Use when you have a photo and want Infringement Report's multi-engine reverse-image search (the current home of ImageRaider) to find every page reusing it — returns matching URLs.
url: https://infringement.report/api/raider-reverse-image-search/
category: image-video-face
path:
- image-video-face
bestFor: The current ImageRaider reverse-image search, hosted by Infringement Report — multi-engine image match aggregation for finding reused photos.
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- name
- domain
status: live
pricing: freemium
costNote: Free tier with limits; bulk/API and higher volumes are paid via Infringement Report. The path suggests an API endpoint, but it is used through the web tool.
opsec: active
opsecNote: Images are uploaded to Infringement Report and queried against third-party search engines, so the photo leaves your machine.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Infringement Report is the current operator of the ImageRaider reverse-image search; it is a legitimate brand-protection/reverse-image service. Confirm matches by hand.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ImageRaider
tags:
- reverse-image
- image-search
source: osint4all
lastVerified: ''
enrichment: full
---

# Image Raider

> ImageRaider's reverse-image search as it lives today, under Infringement Report: submit a photo, get aggregated matches across multiple engines.

## When to use
You have an `image` or `face` crop and want broad, multi-engine reverse-image coverage to find reused profile pictures, scraped photos, and the original source. This is the live successor to the older `[[image-raider]]` standalone site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://infringement.report/api/raider-reverse-image-search/ (or the Infringement Report reverse-image search page).
2. Upload the image or paste an image URL (batch of URLs supported in the paid tier).
3. Review aggregated matches grouped by source page/engine.
4. Pivot: open matching pages for `name`/`social-profile`; note repeated hosting `domain`s.

## Inputs → Outputs
- **In:** `image` / `face`.
- **Out:** matching page URLs → `social-profile`, `name`, `domain`s.
- **Empty/negative result looks like:** no aggregated matches — novel/edited image, or you hit the free-tier limit. Re-crop and also run engines directly.

## Gotchas & OpSec
- Free tier is rate/volume limited; bulk needs a paid Infringement Report plan or API key.
- Aggregators can trail native engines — also run Google/Yandex/TinEye directly.
- OpSec: **active** — your image is uploaded and distributed to multiple engines.

## Overlaps ("do both")
- Same lineage as `[[image-raider]]` (legacy URL → this). Complement with `[[image-google-com]]` and Yandex/TinEye to cover matches the aggregator misses.

## Trust & verifiability
`trust: community` — a legitimate commercial reverse-image/brand-protection service. Treat every hit as a lead and confirm by opening the source page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | image-raider-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, name, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
