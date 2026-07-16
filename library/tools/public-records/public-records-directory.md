---
id: public-records-directory
name: Public Records Directory (OnlineSearches)
description: Use when you have a `name`/location and want the right official record source for it — returns a curated directory of free US public-records databases indexed by state, county and record type.
url: http://publicrecords.onlinesearches.com/
category: public-records
path:
- public-records
bestFor: Finding which official county/state database holds the record type you need (property, court, vital, inmate, licenses) for a given US location.
selectorsIn:
- name
- address
selectorsOut:
- address
- document-id
- employer-org
status: live
pricing: free
costNote: Free directory of links to official/free public-records sources; the underlying government databases are also free.
opsec: passive
opsecNote: This is a link directory — you leave it to search the actual government databases, each a passive public-records lookup that does not notify the subject. No account needed. Run downstream searches from a sock-puppet browser to avoid tying your sessions together.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running commercial directory (OnlineSearches) that catalogs links to official government and free public-records sources. It hosts no data itself; verify each linked source and beware sponsored "background check" upsells interspersed with the free links.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- OnlineSearches
- publicrecords.onlinesearches.com
tags:
- toddington
- curated-directory
- specialty-search
- public-records-index
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- court-records-search-directory
- free-public-records-directory-us
- jail-and-inmate-records-search-directory
- laws-and-codes-search-directory-by-state
- marriage-records-search-directory
- os-birth-records
- os-death-records
- os-divorce-records
- permits-and-inspections-search-by-state
- sex-offender-us
- unclaimed-and-abandoned-property-search-directory
---

# Public Records Directory (OnlineSearches)

> A nationwide index of free US public-records sources, organised by state, county and record type — the fastest way to find *which* official database to query for a given place.

## When to use
You know roughly where a subject lived/worked in the US and need the authoritative record source for a specific type — property/assessor, county court, recorder of deeds, vital records, inmate/offender, business/professional licenses. Instead of guessing county URLs, use this directory to jump straight to the correct official database for that jurisdiction, then search it by `name`/`address`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://publicrecords.onlinesearches.com/.
2. Drill down by state → county (or by record category) to the jurisdiction you care about.
3. Click through to the official government database it links (assessor, clerk of court, recorder, DOC, licensing board).
4. Search that source by `name`/`address` for the actual record.
5. Pivot: property records yield an `address`/owner; court records yield a case `document-id`; license lookups yield an `employer-org`/professional status — each feeds the next stage of the workup.

## Inputs → Outputs
- **In:** a US location (state/county) plus `name` or `address` for the downstream search
- **Out:** links to official sources returning `address` (property), case/record `document-id`, `employer-org`/license status
- **Empty/negative result looks like:** the county isn't covered, or the linked source is offline/moved — the directory is only a signpost, so a dead link means check the county's current site directly, not that no record exists.

## Gotchas & OpSec
- OnlineSearches interleaves free official links with paid "background report" ads — click the official/free sources, not the upsells.
- Coverage and freshness vary by county; some links go stale.
- It hosts no records itself — always cite the underlying official source, not this directory.

## Overlaps ("do both")
- Pairs with `[[pibuzz]]`, NETROnline and county-specific tools — this gets you to the right official database; those add specialised angles (government salaries, deeds) the directory may not surface.

## Trust & verifiability
`trust: community` — a reputable, long-standing directory linking to legitimate official sources. Trust the government databases it points to; treat the directory itself as a maintained index that can lag.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | public-records-directory |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, document-id, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
