---
id: facebook-geo
name: Facebook Geo (OSINT Combine)
description: Use when you have a `geolocation` or place and want to surface Facebook posts/pages tied to that location — returns `social-profile` and post links with `geolocation` context.
url: https://www.osintcombine.com/facebook-geo-pages
category: social-networks
path:
- social-networks
bestFor: Finding Facebook content and pages associated with a specific geographic location for place-based investigation.
selectorsIn:
- geolocation
- address
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free tool provided by OSINT Combine; no account required for the basic geo-page search.
opsec: passive
opsecNote: The tool builds Facebook geo/search queries; the searches hit Facebook, not the people posting, so subjects aren't directly alerted. Run from a sock-puppet browser. Facebook increasingly gates location content behind login — do not use a real account to view more.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by OSINT Combine, a well-known professional OSINT training/tooling company; the tool is a query-builder over Facebook's own surfaces.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINT Combine Facebook Geo
- Facebook geo pages
tags:
- facebook
- geolocation
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- instagram-explorer
- osint-combine-blog
- osint-combine-reddit-post-analyzer
- osint-combine-tiktok-quick-search
- osint-combine-tools
- osintcombine-com
- osintcombine-com-2
- snapchat-multi-viewer-osint-combine
---

# Facebook Geo (OSINT Combine)

> An OSINT Combine query-builder that points Facebook's own search at a location — surfacing place-tagged posts and pages when you're working from a where, not a who.

## When to use
You have a `geolocation` or a place (a town, venue, area) and want to see Facebook activity tied to it — posts tagged there, local pages, and people associated with the location. Useful in a missing-person or event investigation where you know *where* but not *who*: last-seen location, a venue a subject frequents, or a place named in a lead. It flips the usual name-first search into a place-first one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.osintcombine.com/facebook-geo-pages.
2. Enter the location / place of interest as prompted; the tool constructs the appropriate Facebook geo/search query.
3. Follow the generated query into Facebook (logged-out or sock puppet) and read results: location-tagged posts, local pages, and associated profiles.
4. Scan for `social-profile` links and posts carrying `geolocation` context relevant to your subject/timeframe.
5. Pivot: a profile that posts from the location feeds name/photo confirmation; a page or venue feeds further place-based searches and event reconstruction.

## Inputs → Outputs
- **In:** `geolocation` / place (or `address`)
- **Out:** location-associated Facebook `social-profile`s and posts, `geolocation`-tagged content, local pages
- **Empty/negative result looks like:** few or no results — Facebook has increasingly restricted graph/location search, so a thin result is common and doesn't prove no activity exists there. Combine with other geo tools.

## Gotchas & OpSec
- Facebook has steadily dismantled its graph/location search; some geo queries return little or require login. Expect degraded coverage versus a few years ago.
- Location tags are user-supplied and can be spoofed — corroborate before treating a tag as ground truth.
- OpSec: passive against individuals; run from a sock puppet and don't escalate to a real account.

## Overlaps ("do both")
- Pairs with other geolocation tools and Facebook name/dork searches — Facebook Geo is place-first, while name dorks (e.g. `[[school-or-university]]`) are person-first. Use both to connect a where to a who, and cross-check tags against imagery/EXIF.

## Trust & verifiability
`trust: trusted` — from OSINT Combine, a reputable professional OSINT provider; it merely builds queries over Facebook's own surfaces. Reliability of *results* is bounded by Facebook's ever-tightening search, so verify any location claim with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-geo |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation, address → social-profile, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
