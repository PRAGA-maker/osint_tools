---
id: app-store-scraper
name: App Store Scraper
description: Use when you have an app name, developer, or app ID and want structured Apple App Store data — returns app metadata, developer catalogs, and user reviews (with reviewer handles).
url: https://github.com/facundoolano/app-store-scraper
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Programmatically pulling Apple App Store app details, a developer's full app catalog, and reviews.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- username
- social-profile
status: live
pricing: free
costNote: Free, open-source Node.js library; no account or API key. Uses undocumented iTunes endpoints, so heavy use can be rate-limited.
opsec: passive
opsecNote: It queries Apple's public iTunes/App Store endpoints, not the developer directly — the target is not notified. It runs from your IP, so throttle and use a VPN for large pulls. Reviews are public, but scraping them en masse can draw rate-limits/blocks.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely-used open-source library (sibling of google-play-scraper) by facundoolano; data is Apple's own, so accuracy is high, though endpoint drift can break fields.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- google-play-scraper
aliases:
- app-store-scraper
- iTunes app scraper
tags:
- app-store
- scraper
- developer-osint
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# App Store Scraper

> A Node.js library that pulls structured Apple App Store data — app details, a developer's entire catalog, and user reviews — mirroring the popular google-play-scraper.

## When to use
You are profiling a person or entity that publishes iOS/Mac apps, or you found one app and want everything connected to it. Given an app `name`/ID or a developer (`employer-org`), it returns the developer's full catalog, per-app metadata, and reviews. In an investigation this links a developer identity across apps, exposes support/contact details and `social-profile` links in listings, and surfaces reviewer `username`s — a pivot from "they made this app" to the wider footprint.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `npm install app-store-scraper` (Node.js).
2. App details: `store.app({id: 123456})` or by bundle ID — returns title, description, developer, URLs, pricing, ratings, privacy info.
3. Developer catalog: `store.developer({devId: ...})` — every app under that developer account.
4. Reviews: `store.reviews({id: ..., sort: store.sort.RECENT})` — reviewer handles and text.
5. Search: `store.search({term: ...})`. Cache/throttle to avoid rate-limits; export JSON for analysis.

## Inputs → Outputs
- **In:** app `name` / app ID / bundle ID / developer (`employer-org`) ID
- **Out:** app metadata, developer catalog (`employer-org` link), listing `social-profile`/contact links, reviewer `username`s
- **Empty/negative result looks like:** empty arrays or a thrown error — often rate-limiting or a wrong country code, not "no such app." Retry with backoff and a valid `country`.

## Gotchas & OpSec
- Uses **undocumented iTunes endpoints** — Apple can change them; expect occasional breakage and keep the library updated.
- Bulk review scraping triggers rate-limits/blocks — throttle, cache, and VPN for volume.
- OpSec: **passive** — you hit Apple, not the developer; still, control your request footprint.

## Overlaps ("do both")
- Pairs with `[[google-play-scraper]]` — same author, same API shape for Android. Run both to cover a developer who ships on both stores; cross-reference names/contact links to unify the identity.

## Trust & verifiability
`trust: community` — mature open-source project pulling Apple's own listing data, so values are authoritative; verify against the live App Store page when a field looks stale.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | app-store-scraper |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, employer-org → employer-org, username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
