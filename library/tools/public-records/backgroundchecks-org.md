---
id: backgroundchecks-org
name: backgroundchecks.org
description: Use when you have a US `name` and need to find which public-records/genealogy database to search — a curated directory of free record sources returning pointers to `address`, `associate`, and vital records.
url: https://backgroundchecks.org/public-records/the-genealogy-resource-guide
category: public-records
path:
- public-records
bestFor: A curated guide/directory of free US public-records and genealogy resources, used to find the right database to search next.
selectorsIn:
- name
selectorsOut:
- address
- associate
- name
status: live
pricing: free
costNote: The resource guide/directory is free to read; the sites it links to vary (some free, some paid). The parent site also markets paid background-check services — stick to the free guide.
opsec: passive
opsecNote: Reading a directory/guide is passive and reaches nothing about the subject. OpSec exposure begins only when you follow a link into an actual records site — apply that site's precautions there.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A useful curated guide, but backgroundchecks.org is a commercial background-check company; the guide is a marketing-adjacent resource list, so evaluate each linked source on its own merits.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cyndi-s-list
- usgenweb-archives-united-states
aliases:
- BackgroundChecks.org genealogy resource guide
- backgroundchecks.org
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- directory
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# backgroundchecks.org

> A curated directory of free US public-records and genealogy resources — a navigation aid for finding which database to search, not a database itself.

## When to use
You have a US `name` and want to broaden your record search but aren't sure which free sources to hit. This guide indexes public-records and genealogy resources (vital records, census, obituaries, court, and more) so you can jump to the right specialist database. Treat it as a starting index like a curated link list, then do the actual lookup on the destination site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://backgroundchecks.org/public-records/the-genealogy-resource-guide.
2. Browse the categorised list of record types/sources and pick those matching your subject's locale and the record you need.
3. Follow the links out to the destination databases and search the `name` there.
4. Ignore the parent site's paid background-check upsells — use the free guide only.
5. Pivot: destination records yield `address`, relatives (`associate`), and vital-record details that feed the rest of your investigation.

## Inputs → Outputs
- **In:** `name` plus a locale/record-type to guide source selection
- **Out:** (via linked sites) `address`, `associate`, and `name`/vital-record confirmations
- **Empty/negative result looks like:** the guide always lists sources; a dead end is a linked site with no record — judge coverage on the destination, not here.

## Gotchas & OpSec
- It holds **no records itself** — do not treat the guide as evidence; it only routes you to sources.
- The parent company sells paid background checks; keep to the free directory and vet each linked source independently.
- Links can go stale; if a destination is dead, note the collection and find its current home.
- OpSec: passive at the directory; adopt the destination site's precautions once you click through.

## Overlaps ("do both")
- Overlaps with `[[cyndi-s-list]]` (a far larger genealogy directory) — use both to discover sources, and drill into holdings like `[[usgenweb-archives-united-states]]`.

## Trust & verifiability
`trust: community` — a helpful curated guide from a commercial background-check firm. Trust it as an index only; the reliability of any record is a property of the destination site, judged separately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | backgroundchecks-org |
| category | public-records |
| selectorsIn → selectorsOut | name → address, associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
