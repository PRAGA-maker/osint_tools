---
id: google-play-scraper
name: Google Play Scraper
description: Use when you have a `username` (developer handle) or an app package name and want to pull an app's full Google Play listing, developer catalog, and reviews programmatically — returns employer-org, associate, and device-id leads.
url: https://github.com/facundoolano/google-play-scraper
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Scripting bulk extraction of Google Play app metadata, developer app catalogs, and user reviews.
selectorsIn:
- username
- employer-org
selectorsOut:
- employer-org
- associate
- social-profile
status: live
pricing: free
costNote: MIT-licensed Node.js library; free to install and run. No API key or Google account required.
opsec: passive
opsecNote: Queries hit Google Play's public web endpoints from your IP. High-volume scraping can trigger rate limiting or a temporary block, so throttle requests and consider a proxy for large runs. No login means no attribution to a named account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Widely-used open-source scraper (facundoolano) with thousands of GitHub stars; author has stated it is no longer actively maintained and may break when Google changes its page layout.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- app-store-scraper
aliases:
- google-play-scraper
- gplay-scraper
tags:
- Apps and programs
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Google Play Scraper

> A Node.js library that turns the Google Play store into a queryable dataset: app details, a developer's full app catalog, reviews, and "similar apps".

## When to use
You have a lead app (its package id, e.g. `com.example.app`) or a developer name/handle tied to a subject, and you want to enumerate everything that developer has published, read the review stream, or pull install counts and contact/developer-website fields — all as structured JSON you can pipe into further analysis. Useful when a person of interest builds or publishes Android apps, or when you need to correlate a developer identity across multiple listings.

## How to use it (`bestInteractionPattern`: python-lib)
This is a JavaScript/Node module, not Python — use it from Node.
1. Install: `npm install google-play-scraper` (or `npm i -g` for a global CLI wrapper).
2. In a script, `const gplay = require('google-play-scraper');`
3. Query by method:
   - `gplay.app({appId: 'com.example.app'})` → full listing (title, description, developer, developer email/website, install count, rating, permissions, data-safety).
   - `gplay.developer({devId: 'Example Studio'})` → every app that developer publishes (pivot for `associate`/`employer-org`).
   - `gplay.reviews({appId, sort: gplay.sort.NEWEST})` → user reviews with author names (paginate with the returned token).
4. Read the output JSON; the developer email/website and cross-app links are the OSINT payload.
5. Pivot: developer website/email feeds domain and email tooling; a developer's other apps feed `[[app-store-scraper]]` for the iOS side of the same publisher.

## Inputs → Outputs
- **In:** app package id, developer handle/`username`, or search term
- **Out:** developer `employer-org`/website/email, other apps by the same publisher (`associate`), reviewer names (`social-profile`), permissions and data-safety declarations (`device-id` hints)
- **Empty/negative result looks like:** a thrown 404 for an unknown appId, or an empty array for a developer with no live apps. A parse error usually means Google changed the page layout, not that the app is gone.

## Gotchas & OpSec
- No human-in-the-loop, but the project is **unmaintained** — expect occasional breakage after Google layout changes; pin a known-good version.
- OpSec: passive but not invisible — bulk requests from one IP get rate-limited. Use `throttle` options and memoization; proxy heavy runs.
- Developer email/website fields are self-reported by the publisher and can be stale or fake.

## Overlaps ("do both")
- Pairs with `[[app-store-scraper]]` (same author) — one covers Google Play, the other the Apple App Store; run both to catch a developer who ships on both platforms.

## Trust & verifiability
`trust: community` — mature, popular open-source library, but author-declared unmaintained; verify any critical field against the live Play listing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-play-scraper |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, employer-org → employer-org, associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
