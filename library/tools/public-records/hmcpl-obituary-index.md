---
id: hmcpl-obituary-index
name: HMCPL Obituary Index
description: Use when you have a `name` of someone likely connected to the Huntsville/Madison County, Alabama area and want to find their obituary — returns `dob`/death date, `associate` (surviving relatives), and `address`/place links.
url: http://obits.hmcpl.org/
category: public-records
path:
- public-records
bestFor: Searching a large local obituary index (Huntsville-Madison County, Alabama) to confirm a death and harvest family/relationship detail.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
status: live
pricing: free
costNote: Free to search the index; photocopies of an individual obituary can be requested for $5 each.
opsec: passive
opsecNote: A public library records index — you search a database, nothing reaches any living relative. No login; a sock puppet is optional.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Huntsville-Madison County Public Library (Special Collections); an authoritative curated index of published obituaries for the area.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Huntsville-Madison County Public Library Obituary Index
tags:
- toddington
- curated-directory
- specialty-search
- obituary
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# HMCPL Obituary Index

> The Huntsville-Madison County Public Library's searchable obituary index — confirm a death and pull family/relationship leads from published Alabama obituaries.

## When to use
You have a `name` with a likely tie to the Huntsville / Madison County, Alabama area and need to confirm whether they are deceased and, if so, mine the obituary for family structure — surviving spouse, children, siblings, employer, and hometown. Obituaries are one of the richest single sources of `associate` links for building or confirming a family tree.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://obits.hmcpl.org/.
2. Search by name of the deceased (also searchable by cemetery or originating newspaper).
3. Read the index entry: date, newspaper, and page reference for the obituary.
4. Request a $5 photocopy of the full obituary from Special Collections if you need the complete text.
5. Pivot: named survivors become `associate` leads for people-search; hometown/church/employer references narrow location and affiliation.

## Inputs → Outputs
- **In:** `name` (of the deceased), or cemetery / newspaper
- **Out:** `name`, death date (and often `dob`/age), `associate` (surviving relatives named in the obituary), place/employer references
- **Empty/negative result looks like:** no index entry — the person likely has no obituary published in the covered Huntsville-area papers (they may be alive, or died elsewhere). Not proof of anything beyond "no local obituary indexed here."

## Gotchas & OpSec
- Geographically scoped to the Huntsville-Madison County, Alabama area — of no use for people with no connection there.
- The index gives a citation; the full obituary text (with the richest family detail) may require the $5 copy request.
- Fully passive and free to search.

## Overlaps ("do both")
- Pairs with `[[legacy-com]]`-style national obituary aggregators and `[[findagrave]]` — HMCPL is deep on one Alabama locality, while national sites give broader (shallower) coverage; do both to confirm and enrich.

## Trust & verifiability
`trust: trusted` — a public-library-curated index, authoritative for its coverage area; the obituary content it points to is primary-source published text.
