---
id: genealogy-links
name: Genealogy Links
description: Use when you have a `name` and want the right regional genealogy/vital-records source — returns a directory of 50k+ curated links to birth/marriage/death, census and cemetery records across the English-speaking world.
url: http://www.genealogylinks.net
category: people-search
path:
- people-search
bestFor: Finding the correct regional birth/marriage/death, census and cemetery record source for a subject or their ancestors across the US, UK/Ireland, Canada, Australia and NZ.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
status: live
pricing: free
costNote: The directory is free (online since 1997); some destination archives it links to may charge for record copies.
opsec: passive
opsecNote: A link directory — searches happen on the destination archive sites, which see your IP/query. Genealogy work often touches living relatives' data; be mindful and use a sock-puppet browser for sensitive traces.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running curated directory (50k+ links) maintained since 1997; result quality is that of each linked archive, and some links inevitably rot over the decades.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nettrace
- court-records-directory
- genealogy-links-us-and-other-countries
aliases:
- genealogylinks.net
tags:
- people-investigations
- genealogy
- vital-records
- directory
source: awesome-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Genealogy Links

> A 50,000-link directory of genealogy and vital-records sources, sorted by region and record type — the map to the right birth/death/marriage archive when a person's trail runs into the past.

## When to use
You have a `name` and need historical/vital records — births, marriages, deaths, census, cemetery/burial listings — for the subject or their family, across the US, UK/Ireland, Canada, Australia or New Zealand. Rather than guessing which archive holds a given county/parish's records, Genealogy Links routes you to the correct source, where you then search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.genealogylinks.net.
2. Drill down by region (country → state/county/parish) and record type.
3. Follow the curated link to the destination archive and search the `name`.
4. Read the destination's output: births/marriages/deaths with dates, places, and relatives.
5. Pivot: a `dob`/date-of-death anchors identity; named parents/spouses/children feed `associate` and family-tree mapping.

## Inputs → Outputs
- **In:** `name` + region (you pick the right link)
- **Out:** links to archives returning `name`, `dob`/dates, family `associate` links, places
- **Empty/negative result looks like:** no listed source for that locale/record type, or a dead link (inevitable in a decades-old directory) — Genealogy Links only points; it holds no records itself.

## Gotchas & OpSec
- Human-in-the-loop: you choose the region and interpret each archive; expect some rotted links after 25+ years.
- Strongest for the English-speaking world and historical records; less useful for living, non-Anglophone subjects.
- OpSec: passive; the directory collects nothing, but be careful with living relatives' data downstream.

## Overlaps ("do both")
- Pairs with `[[nettrace]]` (AU-focused) and `[[court-records-directory]]` (US court/criminal) — each is a curated directory for a different record class/region; combine them to cover a subject's full paper trail.

## Trust & verifiability
`trust: community` — a respected long-standing curator; verifiability comes from each destination archive, so confirm findings on the source record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | genealogy-links |
