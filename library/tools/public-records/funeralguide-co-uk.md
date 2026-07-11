---
id: funeralguide-co-uk
name: funeralguide.co.uk
description: Use when you have a `name` and want to confirm a UK death and funeral details via obituary/funeral notices — returns death date, funeral location (address), and family associate leads.
url: https://www.funeralguide.co.uk/obituaries
category: public-records
path:
- public-records
bestFor: Searching UK obituaries and funeral notices by name or location to confirm a death and surface funeral details and surviving family.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- associate
status: live
pricing: free
costNote: Free to search and read obituaries and funeral notices; no account required.
opsec: passive
opsecNote: Public obituary/funeral-notice database — searching does not notify the family and reveals only your IP to the site. Fully passive. Handle findings with sensitivity: these are recent bereavements involving grieving families.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established UK funeral-services directory; notices are submitted by funeral directors/families, so details are generally reliable but self-reported.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- deathindexes-com
- archives-library-information-center-alic
aliases:
- Funeral Guide
- funeralguide obituaries
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- obituaries
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# funeralguide.co.uk

> A UK-wide obituary and funeral-notice database — search by name to confirm a death and surface the funeral date, location, and surviving family.

## When to use
You have a `name` (and ideally an area) for someone in the UK who may have died, and you need to confirm the death and gather context. Obituaries and funeral notices are high-value in missing-persons and next-of-kin work: they establish a death date, name the funeral home and service location (an `address` lead), and frequently list surviving relatives (`associate`s) — a fast way to resolve "is this person deceased?" and to reach family.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.funeralguide.co.uk/obituaries.
2. Enter the deceased's name or a location in the search bar.
3. Filter by timeframe (last 7 days up to a year) to narrow recent notices.
4. Open a matching notice and read: birth/death month & year, funeral date and venue, officiating funeral director, and any named family or tribute contributors.
5. Pivot: funeral home/venue is an `address` lead; named relatives are `associate` leads; cross-check the death against official indexes ([[deathindexes-com]]).

## Inputs → Outputs
- **In:** `name` (and/or location)
- **Out:** confirmed `name` + death date, funeral `address`/venue, surviving-family `associate` names
- **Empty/negative result looks like:** no notice — many deaths are never posted here (family choice or a different provider), so absence does NOT confirm the person is alive; check other obituary sources and the official death index.

## Gotchas & OpSec
- Coverage is only deaths whose families/funeral directors chose to post here — a real death may be absent; don't treat a blank as "not deceased."
- Details are self-reported by families/directors and can contain errors or partial dates.
- OpSec: passive, but ethically sensitive — these are active bereavements; handle any family contact with care.

## Overlaps ("do both")
- Pairs with [[deathindexes-com]] (official death indexes) and [[archives-library-information-center-alic]] (vital-records routing) — obituaries give funeral/family context, official indexes give the authoritative death record.

## Trust & verifiability
`trust: community` — an established UK funeral directory. Notices are reliable pointers but self-reported; confirm the death itself against an official index before treating it as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | funeralguide-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address → name, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
