---
id: state-local-tribal-gov-page-search
name: State, Local, Tribal Gov Page Search
description: Use when you need the official website for a specific US state, county, city or tribal government to reach its records — USA.gov's authoritative directory routes you to the right jurisdiction's portal.
url: https://www.usa.gov/state-tribal-governments
category: public-records
path:
- public-records
bestFor: Finding the official government website for a US state/county/city/tribe as the gateway to that jurisdiction's own records searches.
selectorsIn:
- name
- address
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free official US government directory; no account.
opsec: passive
opsecNote: Browsing a government directory is passive and anonymous. Records searches on the destination sites you reach are separate actions governed by each site's own rules.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: USA.gov is the US federal government's official web portal; its directory of state, local and tribal government sites is authoritative for routing, though it holds no personal records itself.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- USA.gov state and tribal governments
- state local tribal government directory
tags:
- court
- inmate
- directory
- us
- gateway
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# State, Local, Tribal Gov Page Search

> USA.gov's official directory of state, county, city and tribal government sites — the reliable first step for finding *which* jurisdiction's portal holds the records you need.

## When to use
US records are radically decentralized — courts, inmate lookups, recorders, assessors and vital records live on thousands of separate state/county/city/tribal sites. When you know the jurisdiction tied to a subject (from an `address`, a court, a tribe) but not the official URL, this directory routes you to the authentic government site, avoiding the copycat/data-broker sites that clutter search results. It's the map, not the records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.usa.gov/state-tribal-governments.
2. Drill down to the relevant state, and from there to county/city or the specific tribal government.
3. Follow the official link to that jurisdiction's site, then use *its* search (court records, inmate locator, recorder, assessor, vital records).
4. Pivot: the destination site returns the actual `document-id`/record; combine county records with state and federal searches for full coverage.

## Inputs → Outputs
- **In:** `name` / `address` (used to identify the jurisdiction)
- **Out:** the correct official government portal → downstream records (`document-id`, court/inmate data) on that site
- **Empty/negative result looks like:** the directory always resolves to a government site; a dead end means that jurisdiction publishes little online, not that no records exist — you may need an in-person/clerk request.

## Gotchas & OpSec
- **Router, not a database:** it never returns a person's record directly — its value is landing you on the authentic jurisdiction site (and away from broker impostors).
- Coverage/quality of online records varies wildly by county and tribe; many require offline requests.
- OpSec: passive; downstream searches follow each site's own rules.

## Overlaps ("do both")
- Pairs with [[the-tribal-court-clearinghouse]] (for tribal jurisdictions) and national court/inmate aggregators — this pinpoints the official venue; those cover the search once you're there.

## Trust & verifiability
`trust: trusted` — the authoritative US government directory. It reliably routes you to genuine official sites; verification of any actual record happens on the destination portal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | state-local-tribal-gov-page-search |
| category | public-records |
| selectorsIn → selectorsOut | name, address → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
