---
id: sortedbybirthdate
name: Sortedbybirthdate
description: Use when you have a `dob` (or name) for a deceased US person and want to confirm death details — returns Death Master File entries with name, birth and death dates.
url: https://sortedbybirthdate.com/
category: public-records
path:
- public-records
bestFor: Confirming a deceased US person's birth/death dates via a free Social Security Death Index (Death Master File) listing.
selectorsIn:
- dob
- name
selectorsOut:
- name
- dob
status: live
pricing: freemium
costNote: Free to browse; based on the public Social Security Death Master File (as of ~March 2014), so it is a static historical index, not a live/current record set.
opsec: passive
opsecNote: You browse a public death index — no notification reaches anyone, and the data concerns deceased individuals. Use a sock-puppet browser as routine hygiene. Records are historical (frozen ~2014), so recent deaths won't appear.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free genealogy site republishing the US Social Security Death Master File; the underlying SSDI data is authoritative for deaths it covers, but this copy is dated (~2014) and covers only DMF-reported deaths.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Sorted By Birth Date
- sortedbybirthdate.com
tags:
- ssdi
- death-records
- genealogy
- birthdate
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Sortedbybirthdate

> A free Social Security Death Index browser, organised by birth date — confirm a deceased US person's birth and death dates from public Death Master File data.

## When to use
You have a `dob` (and/or `name`) for a US person you believe is deceased and want to confirm it against the Social Security Death Master File (SSDI/DMF). Confirming a death — with birth and death dates — can resolve a missing-person question or anchor a genealogy chain. The birth-date organisation is handy when you know a DOB but are unsure of the exact name spelling.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sortedbybirthdate.com/ in a sock-puppet browser.
2. Navigate by birth date (year → month → day) to the relevant `dob`, then scan by given name; or search by `name`.
3. Read the matching DMF entry: `name`, birth date, and death date.
4. Treat it as an SSDI record — confirm the person by matching both DOB and name, and note the data is frozen ~2014.
5. Pivot: a confirmed death date + name feeds obituary search (`[[legacy-com]]`, `[[funeral-notices-co-uk]]`) and Find A Grave for family/associate detail; DOB helps disambiguate people-search results.

## Inputs → Outputs
- **In:** `dob` (and/or `name`) of a deceased US person
- **Out:** SSDI/DMF entry with `name`, birth date, death date
- **Empty/negative result looks like:** no entry — the person isn't in the DMF (not all deaths are), died after the ~2014 snapshot, or the DOB/name differs. Absence is NOT proof the person is alive; the index is partial and dated.

## Gotchas & OpSec
- **Static, dated data (~2014)** and DMF-only coverage — recent deaths and non-DMF deaths are absent. Use a current SSDI source (e.g. genealogy services) to cover later years.
- Deceased-only: this won't help with living subjects.
- OpSec: **passive**, public death data; nothing reaches anyone.

## Overlaps ("do both")
- Pairs with `[[legacy-com]]`, `[[funeral-notices-co-uk]]`, Find A Grave, and `[[rootsweb-2]]` — the DMF confirms the dates; obituaries/graves/trees add the family, place, and narrative. Do both to confirm a death and expand the associate graph.

## Trust & verifiability
`trust: community` — a free republication of authoritative SSDI/DMF data, but frozen ~2014 and DMF-limited. The dates are reliable for covered deaths; confirm identity by matching name+DOB and corroborate with an obituary/grave record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sortedbybirthdate |
| category | public-records |
| selectorsIn → selectorsOut | dob, name → name, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
