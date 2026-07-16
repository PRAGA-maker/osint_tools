---
id: marriage-records-search-directory
name: Marriage Records Search Directory
description: Use when you have a `name` and want to find US marriage records — returns links to state/county marriage-record search resources that confirm spouses and dates.
url: http://publicrecords.onlinesearches.com/marriage-records.htm
category: public-records
path:
- public-records
bestFor: Routing to the correct US state/county marriage-record search to confirm a spouse and marriage date.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- name
status: live
pricing: free
costNote: The directory of links is free; most linked state/county vital-records searches are free indexes, though ordering a certified certificate usually costs a fee.
opsec: passive
opsecNote: Browsing the directory and the linked public indexes is passive and not attributed to the subject. Watch for Intelius-style paid-report upsells woven into onlinesearches pages — those route to a commercial data broker.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A curated link directory (onlinesearches.com, Intelius-powered) pointing to authoritative state/county vital-records sources; trust the destination registries, not the aggregator's upsells.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- jail-and-inmate-records-search-directory
- familysearch
- court-records-search-directory
- free-public-records-directory-us
- laws-and-codes-search-directory-by-state
- os-birth-records
- os-death-records
- os-divorce-records
- permits-and-inspections-search-by-state
- public-records-directory
- sex-offender-us
- unclaimed-and-abandoned-property-search-directory
aliases:
- OnlineSearches marriage records
- marriage records directory
tags:
- genealogy
- family
- vital-records
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Marriage Records Search Directory

> A state/county routing index for US marriage records — it points you to the official vital-records and county-clerk searches that confirm a marriage, a date, and a spouse's name.

## When to use
You have a `name` and want to establish a marriage: who someone married, when, and where — which surfaces a spouse (`associate`), a maiden/married name change (critical for re-finding women who changed surnames), and a date/place that anchors location history. Marriage records are held at state vital-records offices and county clerks; this directory maps you to the right one instead of guessing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the directory (http://publicrecords.onlinesearches.com/marriage-records.htm).
2. Select the state, then the county or statewide vital-records link.
3. Search the destination index by `name` (try maiden and married surnames).
4. Read the record: both spouses' names, marriage date, and county/place; note that online indexes often show the index entry, with the certified certificate available by paid order.
5. Ignore the paid "background report" upsells; use the free official indexes as your pivot.

## Inputs → Outputs
- **In:** `name` (maiden or married; add state/county to narrow)
- **Out:** spouse `name`/`associate`, marriage date, place; a maiden↔married name link, and sometimes age/`dob`
- **Empty/negative result looks like:** no index hit on the destination site — meaning *that* jurisdiction has no matching online record; the marriage may be in another state/county, pre-digitization, or restricted. Absence isn't proof.

## Gotchas & OpSec
- It's a directory, not a search engine — run the actual query on the linked state/county site.
- Online coverage and searchable date ranges vary hugely by jurisdiction; many older records aren't digitized.
- The name-change link (maiden→married) is often the real prize; search both surnames.

## Overlaps ("do both")
- Pairs with `[[familysearch]]` (huge free genealogical marriage index, cross-jurisdiction) and `[[jail-and-inmate-records-search-directory]]` (same onlinesearches directory family for a different record type) — use FamilySearch to catch records this directory's destinations miss.

## Trust & verifiability
`trust: community` — the aggregator is a convenience layer; verify any hit against the official state/county vital-records source it links to, which is the authoritative record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | marriage-records-search-directory |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
