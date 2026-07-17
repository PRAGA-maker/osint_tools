---
id: radioreference-communications-wiki
name: RadioReference Communications Wiki
description: Use when you have a `geolocation`/agency and want radio-communications reference data (frequencies, systems, agencies) — returns location/agency comms context, not a person selector.
url: https://wiki.radioreference.com/index.php/Main_Page
category: search-engines
path:
- search-engines
bestFor: Looking up radio systems, frequencies, and agency/trunked-network details for a location to understand and monitor emergency and organisational communications.
selectorsIn:
- geolocation
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: The wiki is free to read; the associated RadioReference database has some premium/subscriber features, but the wiki reference content is open.
opsec: passive
opsecNote: Reading a public reference wiki is passive — no target is contacted. (Actually listening to radio traffic is a separate activity governed by local law; this entry is only about the reference data.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large crowdsourced radio-communications wiki (part of RadioReference); community-maintained, so detail quality varies by region but is broadly reliable for hobbyist/monitoring use.
missingPersonsRelevance: medium
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- radioreference
- radioreference-station-search
aliases:
- RadioReference wiki
- wiki.radioreference.com
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# RadioReference Communications Wiki

> The crowdsourced reference wiki behind RadioReference — documents radio systems, frequencies and agencies by area, useful for understanding the emergency/organisational comms footprint of a location.

## When to use
You have a `geolocation` (a county/region) or an `employer-org`/agency and want to understand its radio communications: which frequencies and trunked systems public-safety, transport, and other bodies use, plus how to identify and monitor them. In a search-and-rescue or missing-persons context, this helps investigators understand the local emergency-comms landscape and cross-reference agency activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the wiki and search by location (state/county), agency, or system name — or browse the "United States" / country portals.
2. Read the area page: agencies, frequencies, trunked-radio system parameters, and monitoring notes.
3. Cross-reference with the RadioReference database for live/updated frequency listings.
4. Pivot: an agency named here feeds public-records/employer research; system/frequency detail informs (lawful) scanner monitoring during an active search.

## Inputs → Outputs
- **In:** `geolocation` (area) or `employer-org`/agency name
- **Out:** `employer-org`/agency comms context — frequencies, radio systems, and monitoring guidance for that area or body.
- **Empty/negative result looks like:** sparse or missing coverage for a region — the wiki is crowdsourced and uneven; check the RadioReference database or local sources.

## Gotchas & OpSec
- Crowdsourced: completeness and freshness vary a lot by area; verify frequencies against the live database.
- US coverage is deepest; other countries are patchier.
- Legal note: reference data is public, but actually intercepting/recording radio traffic is regulated differently by jurisdiction — know the local law.

## Overlaps ("do both")
- Pairs with `[[radioreference]]` and `[[radioreference-station-search]]` — the wiki explains systems and context; those give the searchable live frequency/station database.

## Trust & verifiability
`trust: community` — a well-established but crowd-edited wiki; treat specifics as community-sourced and confirm against the RadioReference database or official agency listings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radioreference-communications-wiki |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation, employer-org → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
