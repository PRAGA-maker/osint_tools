---
id: osint-combine-tools
name: OSINT Combine Tools
description: Use when you have a `username`, `geolocation`, or social handle and want a vetted free toolset to expand it — returns social-profiles, geo leads, and username hits.
url: https://www.osintcombine.com/tools
category: search-engines
path:
- search-engines
bestFor: A curated hub of free, single-purpose browser tools (username enumeration, social geo, TikTok/Instagram search) from a reputable OSINT vendor.
selectorsIn:
- username
- geolocation
- name
selectorsOut:
- social-profile
- username
- geolocation
- image
status: live
pricing: freemium
costNote: The listed tools are free to use in-browser; OSINT Combine's flagship NexusXplore platform and training are paid, but nothing on this tools page requires payment.
opsec: passive
opsecNote: Most tools are client-side query builders or link launchers that hand you off to the target platform (TikTok, Instagram, etc.) — so the platform, not OSINT Combine, sees the eventual request. Run the actual lookups from a sock-puppet browser/session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: OSINT Combine is a well-known commercial OSINT training/tooling company; these are its own maintained free utilities.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINT Combine free tools
- osintcombine.com/tools
tags:
- tool-collection
- social-networks
- language
source: ultimate-osint
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- facebook-geo
- instagram-explorer
- osint-combine-blog
- osint-combine-reddit-post-analyzer
- osint-combine-tiktok-quick-search
- osintcombine-com
- osintcombine-com-2
- snapchat-multi-viewer-osint-combine
---

# OSINT Combine Tools

> A vendor-maintained landing page of free, focused OSINT utilities — the fastest single stop for username enumeration, social-geo search, and platform-specific quick searches.

## When to use
You have a `username`, a rough `geolocation`, or a target on a specific platform and want a trusted, ready-made tool instead of hand-rolling a query. This page bundles several high-value free tools — WhatsMyName username enumeration, Instagram Explorer (images by date + location), Social Geo Lens, TikTok Quick Search, Alt-Tech Social Search — each of which turns one selector into `social-profile` / `username` / `geolocation` leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.osintcombine.com/tools and scan the tile list; pick the tool matching your selector.
2. For a `username`: launch **WhatsMyName Username Tool**, enter the handle, and read the list of sites where it exists.
3. For a place/event: use **Social Geo Lens** or **Instagram Explorer** to build a location/date-bounded search.
4. For a platform target: use **TikTok Quick Search** or **Alt-Tech Social Search** to jump straight into filtered results.
5. Pivot: enumerated accounts feed profile-by-profile review; geo hits feed map/imagery corroboration.

## Inputs → Outputs
- **In:** `username`, `geolocation`, `name`, or a platform handle
- **Out:** cross-site `social-profile`/`username` hits, geo-bounded post/image leads, `image` results
- **Empty/negative result looks like:** WhatsMyName returning no site matches for a handle (the username is unused or unique to one platform), or a geo search with no posts in the window — a coverage gap, not proof of absence.

## Gotchas & OpSec
- These are launchers/query-builders, not databases: the real request is made against the destination platform, so apply that platform's OpSec (sock-puppet, no personal login).
- Tool availability shifts as OSINT Combine updates the page; a tile may be retired or moved — verify the specific utility still loads.
- OpSec: the tools page itself is passive; watch the handoff step where you actually hit a live platform.

## Overlaps ("do both")
- Pairs with [[instagram-explorer]] and [[osint-combine-tiktok-quick-search]] (surfaced here) and with standalone username tools — running the same handle through WhatsMyName plus a second enumerator catches sites each misses.

## Trust & verifiability
`trust: trusted` — maintained by an established commercial OSINT firm; the tools are legitimate and widely used, though results still depend on the third-party platforms they query.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-combine-tools |
| category | search-engines |
| selectorsIn → selectorsOut | username, geolocation, name → social-profile, username, geolocation, image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
