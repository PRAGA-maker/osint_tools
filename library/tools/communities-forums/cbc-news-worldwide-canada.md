---
id: cbc-news-worldwide-canada
name: CBC News (Canada)
description: Use when you have a `name` connected to Canada and want news coverage placing them in an event, role, or community — returns `associate`, `employer-org`, `geolocation`.
url: https://www.cbc.ca/news
category: communities-forums
path:
- communities-forums
bestFor: Searching Canada's public broadcaster archive for coverage naming a person, place, or organization.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
- geolocation
status: live
pricing: free
costNote: Free to read and search; no account or paywall for news articles.
opsec: passive
opsecNote: Reading and searching articles is passive and anonymous; the subject is not notified and you disclose nothing about your interest to them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: CBC/Radio-Canada is Canada's national public broadcaster with editorial standards; reliable journalism, though it is reporting, not a records database.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CBC News
- CBC.ca
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# CBC News (Canada)

> Canada's national public broadcaster and its searchable news archive — find coverage that places a Canadian subject in an event, a role, a community, or a location.

## When to use
Your subject has a Canadian connection and you want journalistic context: local news naming them, an incident they were involved in, a business or community event, an obituary, or a court/crime report. CBC's archive is broad and regionally granular (local bureaus across provinces), so a `name` search can surface where a person lived, who they were connected to, and what happened around them. Directly relevant to missing-persons work — local news often carries the earliest and most detailed public account, including family names and locations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cbc.ca/news and use its search, or run a site-scoped query: `site:cbc.ca "Full Name"`.
2. Add a place or context term to disambiguate common names (`site:cbc.ca "Name" Winnipeg`).
3. Read matching articles for named people, quoted family/officials, locations, dates, and organizations.
4. Read the output: `associate` names (family, colleagues, officials), an `employer-org`/community tie, and a `geolocation` (town/region).
5. Pivot: named people feed people-search; a location narrows geographic work; an incident date anchors a timeline; check regional CBC pages for local depth.

## Inputs → Outputs
- **In:** `name` (person) or `employer-org` (organization/place)
- **Out:** `associate` (people named alongside the subject), `employer-org` (org/community links), `geolocation` (town/region)
- **Empty/negative result looks like:** no articles for the name — the subject wasn't covered (most people aren't); try local outlets and other Canadian media before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none for reading.
- OpSec: passive and anonymous.
- It's journalism pinned to a moment — a role/location from an old article may be outdated; date-check and treat as a timeline point.

## Overlaps ("do both")
- Pairs with local/regional Canadian outlets and obituary/records tools — CBC gives authoritative national/regional coverage, while local papers and records add granular detail. Do both to build a full picture of a Canadian subject.

## Trust & verifiability
`trust: trusted` — Canada's national public broadcaster with editorial standards, so its factual reporting is reliable; treat it as sourced journalism to corroborate, not as a primary records database.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cbc-news-worldwide-canada |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
