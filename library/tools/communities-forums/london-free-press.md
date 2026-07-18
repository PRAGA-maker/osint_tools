---
id: london-free-press
name: London Free Press
description: Use when you have a `name` and want news coverage from London, Ontario — returns articles, obituaries and local reporting that can place or corroborate a subject.
url: http://www.lfpress.com
category: communities-forums
path:
- communities-forums
bestFor: Searching the London Free Press (London/southwestern Ontario) archive for a person, event, obituary or local incident.
selectorsIn:
- name
selectorsOut:
- associate
- employer-org
- geolocation
status: live
pricing: freemium
costNote: Free to search and read headlines/many articles; some content sits behind a Postmedia metered paywall. Search itself is free.
opsec: passive
opsecNote: Reading a public news site is passive; the subject is not notified. Standard clean-session hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established Postmedia daily newspaper (London Free Press); reporting is professionally edited and citable, though article availability varies by paywall and archive depth.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- LFP
- lfpress.com
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# London Free Press

> The London Free Press's searchable archive — a way to find London/southwestern-Ontario news coverage, obituaries and local reporting tied to a subject.

## When to use
Your subject has a connection to London, Ontario or the surrounding region and you have a `name`. Local newspaper coverage can pin down a last-known event, confirm a death via an obituary, name relatives and associates, or corroborate an employer, area, or incident that national searches miss. Use it as a regional news layer when a person's trail runs through southwestern Ontario.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://lfpress.com/ and use the site search (or a `site:lfpress.com` dork in Google for deeper reach).
2. Search the subject's `name` (quoted), adding a town, middle name, or event term to cut noise.
3. Read matching articles/obituaries for dates, locations, named relatives/associates (`associate`), and roles (`employer-org`).
4. Pivot: a named relative or employer feeds people/company search; a place or date feeds public-records and further local-news follow-up.

## Inputs → Outputs
- **In:** `name` (+ location/event qualifier)
- **Out:** articles yielding `associate`, `employer-org`, `geolocation`, dates
- **Empty/negative result looks like:** no articles for the name — the subject may have no regional news footprint, or coverage is paywalled/aged out of the index; try a broader news search and the paper's obituary section.

## Gotchas & OpSec
- A metered paywall hides some article bodies; a `site:` search plus cached/archived copies often recovers the text.
- Common names produce noise — always disambiguate with a locality or event.
- OpSec: passive public-news reading.

## Overlaps ("do both")
- Pairs with broader news-search tools and other regional Postmedia titles — local papers catch detail national aggregators drop; run both for coverage.

## Trust & verifiability
`trust: trusted` — a professional, edited daily of record for the region; treat reporting as reliable and citable, while noting paywall/archive gaps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | london-free-press |
| category | communities-forums |
| selectorsIn → selectorsOut | name → associate, employer-org, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
