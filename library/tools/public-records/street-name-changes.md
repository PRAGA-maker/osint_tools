---
id: street-name-changes
name: Street Name Changes (Steve Morse One-Step)
description: Use when you have a historical `address` whose street may have been renamed/renumbered and want the modern (or old) equivalent — returns the mapped current/former street name for the area.
url: https://stevemorse.org/census/changes.html
category: public-records
path:
- public-records
bestFor: Reconciling old and current street names/house numbers when tracing a person through historical census, vital or address records.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free reference tables on Stephen P. Morse's One-Step genealogy site. No account, no payment; part of a donation-supported nonprofit-style resource.
opsec: passive
opsecNote: Fully passive — static reference tables. No query about a person is sent anywhere and nothing is logged against a subject. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Stephen P. Morse's One-Step tools are a widely cited, respected genealogy resource; street-change tables are compiled from municipal records and city sources, though older/city-specific tables can be incomplete.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Steve Morse street name changes
- One-Step street changes
tags:
- public-records
- genealogy
- historical-address
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Street Name Changes (Steve Morse One-Step)

> A genealogy reference on Stephen P. Morse's One-Step site that maps old street names/house numbers to their modern equivalents (and vice versa), so a decades-old address still resolves to a real place.

## When to use
You have a historical `address` — from an old census entry, vital record, immigration file, city directory, or family document — and the street may since have been renamed or renumbered (very common in NYC boroughs, especially Queens and Staten Island in the 1920s, and in many other US cities). Use this to translate the old address to the current street (or the current address back to its historical name) so you can locate it on a modern map, in an ED finder, or in present-day property records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stevemorse.org/census/changes.html and pick the city/area whose tables you need.
2. Open the relevant table (often split old-name→new-name and new-name→old-name, by borough or district).
3. Look up your street; read across to the mapped equivalent name (and any renumbering notes).
4. Read the output: the corresponding modern/historical street name. A hit lets you re-run the address in a map or property search; a miss means that street either wasn't renamed or isn't covered.
5. Pivot: the resolved current address feeds property/records lookups and the One-Step Unified Census ED Finder for the correct enumeration district.

## Inputs → Outputs
- **In:** `address` (a historical street name/number in a covered city)
- **Out:** `address` (the mapped current or former street name/number)
- **Empty/negative result looks like:** the street isn't listed in that city's table — either it was never renamed, or the table doesn't cover it. Not evidence the address never existed.

## Gotchas & OpSec
- US-focused, city-by-city coverage; strongest for NYC and select cities, sparse elsewhere. A missing entry ≠ no change.
- Static reference, not a live geocoder — always confirm the mapped street against a current map/property record.
- OpSec: fully passive; nothing is sent about the subject.

## Overlaps ("do both")
- Pairs with the One-Step census/ED finders and modern property-record tools — this normalizes the street name, those tools then place the person at it in the right era or today.

## Trust & verifiability
`trust: trusted` — a long-standing, well-regarded genealogy resource compiled from municipal records. Treat individual entries as accurate but corroborate the resulting address against a contemporary source, since city-specific tables vary in completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | street-name-changes |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
