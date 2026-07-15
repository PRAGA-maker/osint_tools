---
id: google-com-84
name: google.com (Advanced Image Search)
description: Use when you have a `name` and want to find photos of a person with precise filters — Google Advanced Image Search narrows by size, type, colour, region, site and usage rights to return candidate images.
url: https://www.google.com/advanced_image_search
category: search-engines
path:
- search-engines
bestFor: Finding images of a subject by keyword with advanced filters (site, region, image type, size, usage rights).
selectorsIn:
- name
selectorsOut:
- name
- social-profile
- image
status: live
pricing: free
costNote: Free Google service; no account or payment.
opsec: passive
opsecNote: A keyword image search queries Google, not the subject — passive. Results are anonymous pageviews; only clicking through to a site touches that site. Use a clean/sock-puppet browser to avoid personalized results.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's own advanced image-search interface — authoritative as a search tool; the images it surfaces come from third-party sites and must be judged individually.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google Advanced Image Search
- advanced_image_search
tags:
- searchengines
- Search Engines
- image-search
- google
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# google.com (Advanced Image Search)

> Google's advanced image-search form — the same index as Images, but with precise filters (site, region, image type, size, colour, usage rights) that turn a name into targeted photo leads.

## When to use
You have a `name` (plus context — city, employer, event) and want photos of that person, or want to constrain an image hunt: only a particular site, a specific region/language, faces only, a minimum size, or reusable-licence images. The filters cut the noise that a plain image search buries you in — useful for finding a usable face photo, an event picture, or images hosted on one domain.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.google.com/advanced_image_search.
2. Enter the name/terms; add filters — "site or domain" to pin to one platform, region/language for locale, "type: face" to prioritize portraits, size for resolution, usage rights if you need reusable images.
3. Run it; scan the grid, then open promising images at their source page for context (who posted it, when, caption).
4. Pivot: a strong face photo feeds reverse-image and face-recognition tools; the hosting page feeds profile/identity work.

## Inputs → Outputs
- **In:** `name` (+ optional site, region, event, image-type filters)
- **Out:** candidate `image`s, their source pages (`social-profile`/site), confirming `name`/identity context
- **Empty/negative result looks like:** few or no images, or only generic/stock results — tighten or loosen filters and add discriminators (city, employer). This is a *keyword* image search, not reverse-image: to search *from* a photo, use Google Lens/reverse image instead.

## Gotchas & OpSec
- Not reverse-image search — it finds images matching text+filters, not images matching a photo you have.
- Filters can over-constrain; if empty, drop the tightest filter (usage rights or "type: face") first.
- Verify each image at its source — Google's thumbnail context can be stale or mislabeled.
- OpSec: passive; use a clean browser to avoid personalized/logged results.

## Overlaps ("do both")
- Pairs with reverse-image engines (Google Lens, Yandex, TinEye) and `site:` dorks — this finds photos *by description*, those find where a photo *appears*; run both directions.

## Trust & verifiability
`trust: trusted` — Google's authoritative image index and filters. Reliability of any single image depends on its source, so confirm provenance on the hosting page before using it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-84 |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, social-profile, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
