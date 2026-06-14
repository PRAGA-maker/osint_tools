---
id: image-raider
name: Image Raider
description: Use when you have a photo and want to run it across multiple reverse-image engines at once to find every page reusing it — returns matching URLs.
url: https://www.imageraider.com
category: image-video-face
path:
- image-video-face
bestFor: Multi-engine reverse-image search that fans one image out to Google/Bing/Yandex and aggregates the matching pages.
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- name
- domain
status: degraded
pricing: freemium
costNote: Originally free with limits; the standalone imageraider.com domain now redirects to / was absorbed by Infringement Report. Verify before relying on it.
opsec: active
opsecNote: The image is uploaded and queried against third-party search engines, so it leaves your machine and is associated with the service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known older multi-engine reverse-image tool cited in awesome-osint; the original domain has since moved to Infringement Report, so the legacy URL may redirect or be dead.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- image-search
- reverse-image
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Image Raider

> A multi-engine reverse-image search: submit one photo and it queries several engines, aggregating every page that reuses the image. Now operated under Infringement Report.

## When to use
You have an `image` or `face` crop and want broad coverage in one shot — finding reused profile pictures, scraped photos, and the source of an image across Google, Bing, and Yandex without running each manually. Useful for locating other `social-profile`s using the same photo and the `domain`s hosting it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.imageraider.com — if it redirects, follow it to the Infringement Report reverse-image tool (`[[image-raider-2]]`).
2. Upload the image (or submit an image URL / a list of URLs for batch).
3. Let it query the underlying engines; review the aggregated list of matching pages.
4. Pivot: open matching pages to harvest `name`/`social-profile`; note recurring `domain`s.

## Inputs → Outputs
- **In:** `image` / `face`.
- **Out:** matching page URLs → `social-profile`, `name`, hosting `domain`s.
- **Empty/negative result looks like:** no matches across engines — the image is novel or heavily edited; not proof of uniqueness. Re-crop and also run engines directly.

## Gotchas & OpSec
- **Status caution:** the legacy imageraider.com brand merged into Infringement Report; the standalone domain may redirect or be down. Use `[[image-raider-2]]` as the current entry point.
- Aggregators lag the native engines and can miss recent matches — also run Google/Yandex directly.
- OpSec: **active** — your image is uploaded and farmed out to multiple engines.

## Overlaps ("do both")
- Current home: `[[image-raider-2]]` (Infringement Report). Also run the source engines directly via `[[image-google-com]]` plus Yandex/TinEye, which catch matches the aggregator misses.

## Trust & verifiability
`trust: community` — a long-cited OSINT tool whose hosting has changed; verify which URL is live and confirm each match by opening the source page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | image-raider |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, name, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
