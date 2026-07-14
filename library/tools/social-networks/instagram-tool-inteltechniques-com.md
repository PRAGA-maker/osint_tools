---
id: instagram-tool-inteltechniques-com
name: Instagram Tool - IntelTechniques.com
description: Use when you have an Instagram `username` and want a one-stop panel of query shortcuts (profile, media, followers, location) — returns pre-built links into Instagram's search surfaces.
url: https://inteltechniques.com/osint/instagram.html
category: social-networks
path:
- social-networks
bestFor: Firing a battery of pre-built Instagram investigative queries from one page instead of hand-crafting each URL.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
- geolocation
status: degraded
pricing: freemium
costNote: Bazzell removed the public online tools in June 2019 after cease-and-desist/DMCA pressure; the working search panels now live behind a paid login (bundled with his OSINT training/books). The public instagram.html may render but its query boxes are often gated or non-functional without the member login.
opsec: passive
opsecNote: The tool only builds and opens query URLs from your browser — it doesn't proxy anything — so requests go directly from your IP to Instagram/Google. That is passive but attributable to you; run it in a sock-puppet browser logged into a research Instagram account, never your real one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Michael Bazzell (IntelTechniques), a widely respected OSINT author; the methodology is authoritative, but the free/public version has been curtailed and query boxes break as Instagram changes its URL structure.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- inteltechniques-search-tool
- osintgram
aliases:
- IntelTechniques Instagram tool
- Bazzell Instagram OSINT
tags:
- instagram
- bazzell
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Instagram Tool - IntelTechniques.com

> Michael Bazzell's consolidated Instagram query panel: enter a username once and fire off dozens of pre-built lookups into Instagram, Google and third-party viewers — now largely behind a members' login.

## When to use
You have an Instagram `username` and want to run the full battery of investigative queries — profile JSON, media, tagged content, followers/following, location and hashtag pivots, reverse-image on the avatar — without hand-building each URL. This page is the classic "one input, many queries" panel. Reach for it when you want breadth of angles fast; but expect that, since 2019, the public version is degraded and the fully working boxes require Bazzell's paid login.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inteltechniques.com/osint/instagram.html in a sock-puppet browser (be logged into a research Instagram account, since many queries require an authenticated IG session to return data).
2. Enter the target `username` (and/or user ID) in the panel.
3. Trigger the individual query buttons — each opens a pre-built URL against Instagram, Google, or a third-party viewer in a new tab.
4. If a box is greyed out or does nothing, that feature is gated behind the paid member login or has broken against Instagram's current URL scheme — fall back to building the query manually.
5. Pivot: profile/media hits feed reverse-image and face tools; location/tag hits feed `[[geolocation]]` work; the numeric user ID is your durable pivot.

## Inputs → Outputs
- **In:** `username` (or Instagram numeric user ID)
- **Out:** links resolving to `social-profile`, `image` (media/avatar), and `geolocation`/tag data
- **Empty/negative result looks like:** buttons that open Instagram's login wall, error pages, or empty JSON — usually the query needs an authenticated IG session, is member-gated, or Instagram changed the endpoint. Not proof the profile lacks data.

## Gotchas & OpSec
- Human-in-the-loop: the reliable version sits behind a paid IntelTechniques login; many public boxes are curtailed or stale.
- Instagram frequently changes its private/undocumented endpoints, so individual queries rot over time — verify each still returns real data.
- It runs queries from *your* browser/IP against Instagram; use a sock-puppet research account, never your personal one, and expect Instagram to rate-limit.

## Overlaps ("do both")
- Pairs with `[[inteltechniques-search-tool]]` (the broader multi-platform IntelTechniques panel) and `[[osintgram]]` (a CLI that pulls IG data programmatically) — use the CLI when the browser panels are gated or broken.

## Trust & verifiability
`trust: trusted` — authored by Michael Bazzell, a reputable OSINT practitioner, so the methodology is sound. But rate the *availability* as degraded: the free public tool was pulled in 2019 and now needs a paid login, and query boxes break with Instagram's changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instagram-tool-inteltechniques-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
