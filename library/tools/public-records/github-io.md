---
id: github-io
name: cipher387 Graves Search (github.io)
description: Use when you have the `name` of a deceased person and want to find their burial record and, via neighbouring graves, family surnames — returns cemetery/burial location, relatives and dates.
url: https://cipher387.github.io/osint_stuff_tool_collection/graves_search.html
category: public-records
path:
- public-records
bestFor: A single jump-off page linking ~25 grave/cemetery databases (Find a Grave, BillionGraves, CWGC, JewishGen, regional registers) for genealogical death research.
selectorsIn:
- name
selectorsOut:
- address
- associate
- name
- dob
status: live
pricing: free
costNote: The directory page itself is a free static list; each linked database is free to search, though a few (e.g. Ancestry) gate full records behind their own subscriptions.
opsec: passive
opsecNote: Searching public grave/genealogy databases is passive and does not alert anyone. The subject here is typically deceased; the OpSec concern is the living relatives you surface, so handle their names with care and use a clean browser for the third-party sites.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A curated static link page by well-known OSINT collector cipher387; the page is a reliable index but the author notes it is somewhat dated, and the linked databases vary in quality.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- graves search
- cipher387 osint tool collection
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- cemetery
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# cipher387 Graves Search (github.io)

> A single curated launchpad to ~25 burial and cemetery databases — turn a deceased person's name into a burial record and, through neighbouring graves, a family tree.

## When to use
You are researching a deceased or long-missing person, or building a family network around a subject, and you have a `name`. Grave databases confirm death dates and burial locations, and — as the page itself highlights — the graves *around* a person often carry relatives' surnames (including a mother's maiden name) and point to a family's home town. Reach for this to (a) confirm a death, (b) resolve a family tree, or (c) generate ancestor/relative leads for genealogical pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the page at the URL — it is a static list of grave/cemetery search links grouped by region.
2. Pick a database by geography: broad ones (Find a Grave, BillionGraves, Commonwealth War Graves, JewishGen) or a country register (US, France, Germany, Russia, Poland, Australia, Eastern Europe).
3. On the chosen site, search the subject `name` (add approximate dates/location to disambiguate).
4. Read the record: burial `address`/cemetery, birth–death `dob`/dates, and nearby interments.
5. Pivot: neighbouring surnames become candidate `associate`s/relatives; the home town seeds local records, obituaries and voter/property searches.

## Inputs → Outputs
- **In:** `name` (of the deceased)
- **Out:** burial `address`/cemetery, death & birth `dob` dates, `name` variants, relative `associate` leads from adjacent graves
- **Empty/negative result looks like:** no matching interment across the linked databases — the person may be alive, cremated with no memorial, buried without a digitised record, or in a region these sites don't cover; absence is not proof of anything.

## Gotchas & OpSec
- Dated index: cipher387 flags the list as somewhat old and points to a broader "Worldwide OSINT Tools Map"; some links may have moved.
- Data quality varies wildly between the linked crowd-sourced (Find a Grave) and official (CWGC) databases — corroborate dates before relying on them.
- OpSec: passive, but you are surfacing living relatives — treat their details responsibly.

## Overlaps ("do both")
- Pairs with obituary/newspaper-archive tools — the grave gives the death date, the obituary names the survivors explicitly.
- Pairs with `[[ufind-name]]`-style people search to pursue the living relatives the graves reveal.

## Trust & verifiability
`trust: community` — a reputable collector's curated link page (transparent, no data of its own); reliability rests on the third-party databases it points to, so verify each record at its source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-io |
