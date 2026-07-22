---
id: abc-television-australia
name: ABC (Australian Broadcasting Corporation)
description: Use when you have a `name` and want Australian national/local news coverage of a subject — returns `social-profile`/mention, event dates and named `associate` context.
url: http://www.abc.net.au
category: communities-forums
path:
- communities-forums
bestFor: Searching Australia's national public broadcaster archive for a person named, quoted, or reported on.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free public-broadcaster content; no paywall, no account needed.
opsec: passive
opsecNote: Reading and dorking a public news site is passive and invisible to any subject; only the ABC's servers log the visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Australia's national public broadcaster with strong editorial standards and deep local/regional coverage; credible journalism, still secondary to primary records.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- ABC News Australia
- abc.net.au
- Australian Broadcasting Corporation
tags:
- news-media
- archive
- australia
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# ABC (Australian Broadcasting Corporation)

> Australia's national public broadcaster — deep national *and* local/regional coverage that can place an Australian subject in a reported event with a firm date and location.

## When to use
You have a `name` with an Australian connection and want news coverage: subject of reporting (crime, accident, missing-person appeal, court case, coronial inquest), a quoted source, a bylined journalist, or a community/regional story. The ABC's local and regional bureaus mean it often covers ordinary Australians and small-town events that national commercial outlets skip — valuable for a date-stamped event, a location, named associates and quoted context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use the ABC's on-site search, or Google-dork it: `site:abc.net.au "<full name>"` (add a town/state or event term to cut noise).
2. Open matching articles and read for the connection — subject, source or byline — plus date, location and named associates.
3. Check ABC regional/local sections for community-level coverage of the subject.
4. Pivot: named `associate`/relatives feed relationship mapping; an event date/location anchors a timeline; local coverage feeds regional-record checks.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile`/mention, named `associate`/relatives, event date, location and quoted context
- **Empty/negative result looks like:** no articles for the name — no ABC footprint (try commercial AU outlets and local papers); disambiguate same-name matches by context.

## Gotchas & OpSec
- Australia-focused; irrelevant for non-AU subjects.
- Same-name collisions; confirm identity from article detail.
- Journalism is interpretation — corroborate with primary records (courts, coronial, registries).

## Overlaps ("do both")
- Pairs with commercial Australian news, local newspapers and AU court/registry tools — the ABC surfaces the story (including local ones); primary records confirm the facts.

## Trust & verifiability
`trust: trusted` — a national public broadcaster with strong standards and local reach; credible reporting, still secondary journalism to anchor against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | abc-television-australia |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
