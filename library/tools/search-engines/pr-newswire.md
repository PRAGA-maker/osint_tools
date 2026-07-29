---
id: pr-newswire
name: PR Newswire
description: Use when you have a `name` or `employer-org` and want official press releases mentioning them — returns timestamped corporate/personnel announcements and associates.
url: http://www.prnewswire.com
category: search-engines
path:
- search-engines
bestFor: Searching official press releases for executive/personnel moves and company announcements.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- name
status: live
pricing: free
costNote: Free to search and read published releases (distribution/publishing is the paid side, for issuers).
opsec: passive
opsecNote: Passive — you read publicly-distributed press releases; no subject is contacted. Ordinary browsing footprint applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established press-release distributor (owned by Cision); releases are official statements from the issuing organisations, though inherently promotional.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- prnewswire
aliases:
- prnewswire.com
tags:
- news
- press-releases
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# PR Newswire

> A major press-release distribution archive — searchable, timestamped official announcements useful for tracing people's professional roles and company events.

## When to use
You have a `name` (often an executive/spokesperson) or an `employer-org` and want dated, official statements: appointments, departures, promotions, board changes, partnerships, product launches, financials. Press releases pin a person to a role, organisation and date, and often name colleagues, making them good corroboration and pivot material for professional/associate mapping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to prnewswire.com and use its search, or run a site-scoped web search: `site:prnewswire.com "Full Name"` or `"Company Name"`.
2. Browse by industry/topic or filter to narrow results.
3. Read matching releases for role/title, organisation, date, quotes and named colleagues.
4. Note the timestamp and issuer — these are official-but-promotional statements.
5. Pivot: a named executive → LinkedIn/company site; an `employer-org` → corporate-registry research; quoted colleagues → `associate` mapping.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` (role/affiliation), `associate`s (named colleagues), `name`s, with dates
- **Empty/negative result looks like:** no releases (most private individuals never appear) — absence says nothing about the person.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; standard browsing footprint.
- Releases are self-serving corporate messaging — accurate on names/dates/titles, but framing is promotional; corroborate substantive claims.

## Overlaps ("do both")
- Pair with other newswires and general news search — coverage differs by distributor, so a person announced on one wire may not be on another; the `[[prnewswire]]` entry covers the same source.

## Trust & verifiability
`trust: trusted` — official issuer statements via a reputable distributor; treat factual details (name, title, date, org) as reliable and the surrounding spin as marketing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pr-newswire |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
