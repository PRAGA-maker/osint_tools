---
id: sonicrun
name: SonicRun
description: Use when you have a `name`, `username` or `domain` and want a second, non-Google index — returns web, blog and news results that mainstream engines may bury or omit.
url: https://www.sonicrun.com/
category: search-engines
path:
- search-engines
bestFor: A free alternative/meta search engine to run a name or handle against a different index than Google/Bing.
selectorsIn:
- name
- username
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free to search; ad-supported and offers paid site-submission/SEO listings, but querying costs nothing.
opsec: passive
opsecNote: A third-party search box logs your query and IP like any engine; the target is never contacted. Use a research browser profile. Results quality is uneven, so treat it as a supplementary net, not a primary source.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small independent search/metasearch portal; it surfaces third-party pages it does not control, so verify every hit at its source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Sonic Run
tags:
- toddington
- curated-directory
- search-engines
- alternative-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# SonicRun

> A small free web/blog/news search portal — worth a pass when you want a different index than Google or Bing on a name or handle.

## When to use
You've exhausted the mainstream engines on a `name`, `username`, or `domain` and want a second opinion from a different crawler. Alternative search portals occasionally surface older, niche, or lower-ranked pages that Google demotes. SonicRun offers web, local, blog, and news tabs, so it's a quick supplementary sweep — low yield on average, but cheap to run and sometimes catches the one page the big engines miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sonicrun.com/ and enter your selector in quotes for an exact match (e.g. `"Jane A. Doe"`).
2. Switch between the Web, Blog, and News tabs — each can return different material.
3. Open promising hits and verify the content at the originating site, not on SonicRun's results page.
4. Pivot: a discovered `social-profile` or `domain` feeds the appropriate profile/domain tool next.

## Inputs → Outputs
- **In:** `name`, `username`, or `domain`
- **Out:** web/blog/news result links pointing to `social-profile`s and related `domain`s
- **Empty/negative result looks like:** few or no relevant hits (common) — absence here says nothing; the major engines remain your primary source.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Result quality and freshness are uneven; never treat a SonicRun ranking as authoritative — click through and verify.
- It's ad-supported; ignore sponsored/submission upsell links.

## Overlaps ("do both")
- Pairs with `[[google-and-bing]]` — run the same query on the major engines first; use SonicRun only as a supplementary index for what they miss.

## Trust & verifiability
`trust: unverified` — an independent portal indexing third-party pages; useful as a wider net, but confirm any finding at its original source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sonicrun |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, domain → social-profile, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
