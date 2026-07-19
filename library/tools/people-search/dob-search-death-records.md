---
id: dob-search-death-records
name: DOBSearch — Death Records
description: Use when you have a `name` and want to determine whether the person is deceased — returns death date/location, obituary, and burial leads.
url: http://www.dobsearch.com/death-records
category: people-search
path:
- people-search
bestFor: Checking whether a subject is deceased and pulling death date, place, obituary, and burial pointers before spending effort on a live-person search.
selectorsIn:
- name
- dob
selectorsOut:
- dob
- address
status: live
pricing: freemium
costNote: Free curated links (SSDI/National Death Index, state vital records, obituary and news archives) plus free preliminary people-finder results; full death certificates and detailed reports are paid.
opsec: passive
opsecNote: A passive records lookup; the (deceased) subject is not notified and no living contact is alerted. The paid people-finder tier may prompt for your details — decline and stay on the free death-record resources for pure OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: DOBSearch is a commercial people-search aggregator; its death-records page curates authoritative sources (CDC/NDI, state vital records) but its own aggregated matches should be confirmed against a primary source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- dobsearch
aliases:
- DOB Search death records
- dobsearch.com death records
tags:
- people-search
- death-records
- vital-records
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# DOBSearch — Death Records

> A death-records gateway: a `name` in, and a fast read on whether the person is deceased, plus death date/place, obituary, and burial leads — the check that reshapes an entire search.

## When to use
You have a `name` (ideally with a `dob` or location) and need to establish whether the subject is alive before committing to a live-person trace. A confirmed death redirects the whole investigation toward estate, obituary, next-of-kin, and cemetery leads; ruling death out saves wasted effort. Use it early when a trail goes cold.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.dobsearch.com/death-records.
2. Use the free curated resources first — SSDI/National Death Index (CDC), state vital-records offices, obituary and local-news archives — and DOBSearch's preliminary people-finder.
3. Read for death date, place of death, obituary text, and burial/cemetery information.
4. Pivot: an obituary names next-of-kin and hometown (`associate`/`address` leads); a confirmed death date feeds estate/probate and Find-a-Grave searches. Avoid the paid report unless free sources are inconclusive.

## Inputs → Outputs
- **In:** `name` (+ `dob`/location if known)
- **Out:** death `dob` (date/place), obituary, burial/`address` leads
- **Empty/negative result looks like:** no death record found — suggests the person is alive OR the death isn't yet indexed (recent deaths lag; SSDI has gaps). Absence is not proof of life; corroborate.

## Gotchas & OpSec
- US-focused; SSDI/NDI have known coverage gaps and reporting lag, so a "no record" can be a false negative.
- The site upsells paid reports — the OSINT value is in the free authoritative links it curates; don't pay for what a state vital-records office provides free.
- OpSec: passive records search.

## Overlaps ("do both")
- Pairs with obituary/Find-a-Grave and SSDI tools — this curates the entry points; use those primary sources to confirm and enrich next-of-kin.

## Trust & verifiability
`trust: community` — a commercial aggregator pointing at authoritative sources; treat its own matches as leads and confirm a death against the primary record (state vital records / official obituary).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dob-search-death-records |
| category | people-search |
| selectorsIn → selectorsOut | name, dob → dob, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
