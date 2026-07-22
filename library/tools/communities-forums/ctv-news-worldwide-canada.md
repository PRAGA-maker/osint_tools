---
id: ctv-news-worldwide-canada
name: CTV News (Canada)
description: Use when you have a `name` and want Canadian national/local news coverage of a subject — returns `social-profile`/mention, event dates and named `associate` context.
url: http://www.ctvnews.ca
category: communities-forums
path:
- communities-forums
bestFor: Searching a major Canadian news archive for a person named, quoted, or reported on.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to read and search; ad-supported, no hard paywall.
opsec: passive
opsecNote: Reading and dorking a public news site is passive and invisible to any subject; only CTV/its ad partners log the visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major Canadian broadcast news organisation with editorial standards and regional stations; credible reporting, still secondary to primary records.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- CTV News
- ctvnews.ca
tags:
- news-media
- archive
- canada
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# CTV News (Canada)

> A major Canadian news network with national and regional coverage — searchable reporting that can place a Canadian subject in an event with a firm date and location.

## When to use
You have a `name` with a Canadian connection and want news coverage: subject of reporting (crime, accident, missing-person appeal, court case), a quoted source, a bylined journalist, or a tribute/obituary. CTV's regional stations (across Canadian provinces) mean it often covers local events and ordinary people, not just national stories — valuable for a date-stamped event, a location, named associates and quoted context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use CTV's on-site search, or Google-dork it: `site:ctvnews.ca "<full name>"` (add a city/province or event term to cut noise).
2. Open matching articles and read for the connection — subject, source or byline — plus date, location and named associates.
3. Check regional CTV station coverage for local-level detail on the subject.
4. Pivot: named `associate`/relatives feed relationship mapping; an event date/location anchors a timeline; local coverage feeds provincial-record checks.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile`/mention, named `associate`/relatives, event date, location and quoted context
- **Empty/negative result looks like:** no articles — no CTV footprint (try CBC, local papers and other outlets); disambiguate same-name matches by context.

## Gotchas & OpSec
- Canada-focused; irrelevant for non-Canadian subjects.
- Same-name collisions; confirm identity from article detail.
- Journalism is interpretation — corroborate with primary records.

## Overlaps ("do both")
- Pairs with CBC, local Canadian newspapers and court/registry tools — CTV surfaces the story (including regional ones); primary records confirm the facts.

## Trust & verifiability
`trust: trusted` — a major Canadian news organisation with regional reach; credible reporting, still secondary journalism to anchor against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ctv-news-worldwide-canada |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
