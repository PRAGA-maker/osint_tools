---
id: creepy-2
name: Creepy
description: Use when you have a `username` and want to aggregate geolocated posts into a map — but the tool is deprecated and its social-API sources are largely dead, so expect little to no data.
url: https://github.com/ilektrojohn/creepy
category: social-networks
path:
- social-networks
- twitter
- location-mapping
bestFor: (Historically) mapping a target's geotagged social posts; now largely non-functional.
selectorsIn:
- username
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free and open-source, but effectively abandoned — its value collapsed when Twitter, Flickr, and Instagram closed/changed the geo APIs it relied on.
opsec: active
opsecNote: When it does query platforms, it does so from your machine (attributable traffic). More importantly, it depends on API access that mostly no longer exists, so runs often fail or return nothing.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: A well-known but deprecated geolocation-OSINT tool (ilektrojohn/creepy); no active maintenance and broken data sources, so treat it as historical.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- CreepyAI
- ilektrojohn creepy
tags:
- geolocation
- twitter
- deprecated
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- creepy
---

# Creepy

> A once-popular geolocation aggregator that plotted a target's geotagged posts on a map — now deprecated, with the social APIs it depended on mostly gone.

## When to use
Reach for the *concept*, rarely the tool. Historically: you had a `username` and wanted every geotagged post (Twitter, Flickr, Instagram) plotted on one map to infer a subject's movements and haunts. Today the underlying APIs have closed or changed, so Creepy typically returns little or nothing — it's documented here so you recognize it and know to use current geolocation methods instead.

## How to use it (`bestInteractionPattern`: cli)
1. Understand the status first: modern Twitter/Flickr/Instagram no longer expose the geo data (and free API access) Creepy was built on; installs frequently fail on old dependencies.
2. If experimenting: clone `github.com/ilektrojohn/creepy`, install its (dated) Python/Qt dependencies, and configure API keys where a platform still allows it.
3. Enter a `username` and run collection; expect sparse or empty maps.
4. Pivot to current techniques: pull `geolocation` from image EXIF (`[[picvario-metadata-editor]]`), from Telegram media (`[[telerecon]]`), or from manual review of a subject's posts.

## Inputs → Outputs
- **In:** `username` (+ platform API keys, where still possible)
- **Out:** `geolocation` points/map — in practice mostly empty on today's platforms
- **Empty/negative result looks like:** the normal case now — no geotagged posts retrievable; do not read this as "the subject never posts location," only that the data path is dead.

## Gotchas & OpSec
- Deprecated and dependency-rotten: budget time for install pain and likely failure.
- Broken data sources make it unreliable as evidence; corroborate any point it does return.

## Overlaps ("do both")
- Superseded by EXIF-based geolocation (`[[picvario-metadata-editor]]`) and platform-specific scrapers (`[[telerecon]]`), which reach geo data through paths that still work.

## Trust & verifiability
`trust: unverified` — abandoned tool over dead APIs; treat as historical and verify any output through a working method.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | creepy-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
