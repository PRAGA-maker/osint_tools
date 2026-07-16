---
id: legacy
name: Legacy.com
description: Use when you have a `name` and want to find a published obituary/memorial to confirm a death and harvest family detail — returns death date, `dob`/age, `associate` (named survivors), and hometown/location.
url: https://www.legacy.com
category: public-records
path:
- public-records
bestFor: The largest aggregator of US/international newspaper obituaries — confirming deaths and extracting family relationships.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
status: live
pricing: free
costNote: Free to search and read obituaries and guest-book condolences; optional paid extras (flowers, permanent memorials) exist but are not needed for research.
opsec: passive
opsecNote: Reading obituaries is passive and touches only Legacy.com — nothing reaches any living relative. Avoid signing a guest book or leaving condolences from an attributable identity, as those are public and traceable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates obituaries hosted with thousands of real newspapers and funeral homes; the underlying notices are primary published sources, though family-submitted detail can contain errors.
missingPersonsRelevance: high
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Legacy.com
- Legacy obituaries
tags:
- genealogy
- family
- obituary
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- legacy-com
- obituaries-from-newspapers-north-america
---

# Legacy.com

> The web's largest obituary aggregator — partnered with thousands of newspapers and funeral homes — to confirm a death and mine an obituary for family links.

## When to use
You have a `name` and need to know whether the person (or a relative) has died, and if so, to pull the obituary's rich relationship data: surviving spouse, children, siblings, parents, hometown, employer, and church/affiliations. Obituaries are among the single densest sources of `associate` links for family-tree confirmation, and Legacy aggregates them nationally so you don't have to search each paper.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.legacy.com and use the obituary search.
2. Enter the `name`, optionally narrowing by location/date or newspaper.
3. Open matching notices — read the death/birth dates, and note every named survivor and place.
4. Cross-check the funeral home/newspaper listed to gauge geography and confirm it's the right person.
5. Pivot: named survivors (`associate`) feed people-search; hometown/employer narrow location; a confirmed death date can close out a "missing" hypothesis or open a next-of-kin lead.

## Inputs → Outputs
- **In:** `name` (optionally + location/date)
- **Out:** death date, `dob`/age, `associate` (named survivors and predeceased relatives), hometown, employer, funeral details
- **Empty/negative result looks like:** no matching obituary — the person may be alive, died without a published notice, or the notice is only in a paper not partnered with Legacy. Absence is not proof of anything; also try `[[hmcpl-obituary-index]]`-style local indexes and `[[findagrave]]`.

## Gotchas & OpSec
- Not every death has a published obituary, and coverage skews US/newspaper-partnered — absence ≠ alive.
- Family-submitted detail can contain errors or omissions; corroborate names/dates.
- Passive; just don't sign guest books from a real identity.

## Overlaps ("do both")
- Pairs with `[[findagrave]]` (cemetery/grave records) and local obituary indexes like `[[hmcpl-obituary-index]]` — Legacy is broad, the others catch locality-specific notices it misses; do both to confirm and enrich.

## Trust & verifiability
`trust: trusted` — aggregates genuine newspaper/funeral-home notices, making it reliable for confirming a death; treat the family-authored relationship detail as strong leads to verify.
