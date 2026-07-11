---
id: slavevoyages-org
name: SlaveVoyages.org
description: Use when you have a historical `name` connected to the Atlantic slave trade (enslaved person or enslaver) and want biographical/voyage records — returns `name`, `geolocation` (embarkation/disembarkation), age (`dob`), and `associate` links.
url: https://slavevoyages.org/resources/names-database
category: people-search
path:
- people-search
bestFor: Genealogical/historical tracing of named individuals — enslaved Africans and enslavers — in the 1514–1866 Atlantic slave trade.
selectorsIn:
- name
selectorsOut:
- name
- geolocation
- dob
- associate
status: live
pricing: free
costNote: Free, open academic resource; datasets are also downloadable. No account required to search.
opsec: passive
opsecNote: Purely a historical academic database — searching it reveals nothing to any living subject and carries no operational risk. It concerns people of the 16th–19th centuries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Scholarly project hosted at Emory University, built from decades of peer-reviewed archival research across Atlantic-world libraries and archives.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SlaveVoyages People Database
- African Names Database
- Trans-Atlantic Slave Trade Database
tags:
- Universal Contact Search and Leaks Search
- genealogy
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# SlaveVoyages.org

> A scholarly database of the Atlantic slave trade — search ~95,000 named Africans plus enslavers across 36,000+ voyages (1514–1866). A genealogical/historical tool, not a modern people-finder.

## When to use
You are doing genealogical or historical research on a named individual tied to the Atlantic slave trade — either an enslaved African (via the African Names / African Origins data, 1808–1862 liberations) or an enslaver/merchant named in voyage records. Reach for it when a family-history or archival trace leads back to the trans-Atlantic or intra-American slave trade and you need names, ages, origins, and voyage context. It has **no** relevance to living persons.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://slavevoyages.org/resources/names-database (the People database).
2. Search a `name` (or browse the African Names/African Origins collection).
3. Read the record: African/given `name`, age (`dob` as recorded), gender, and places of embarkation and disembarkation (`geolocation`), plus the associated voyage.
4. Follow the voyage link to see the ship, dates, and other named people connected to it (`associate`).
5. Pivot: voyage/port data feeds archival and genealogical sources (`[[familysearch]]`, national archives); enslaver names feed historical company/estate records.

## Inputs → Outputs
- **In:** historical `name` (enslaved person or enslaver)
- **Out:** `name`, age (`dob`), `geolocation` (embarkation/disembarkation ports), voyage-linked `associate`s
- **Empty/negative result looks like:** no match — the vast majority of the ~12 million people trafficked were never individually named in surviving records, so absence is expected and not meaningful. Coverage is strongest for the 1808–1862 liberation records.

## Gotchas & OpSec
- Historical only: contains no addresses, phones, or emails despite any stub tag suggesting so — those selectors do not apply to a pre-20th-century dataset.
- Spellings of African and anglicised names vary; try variants and phonetic forms.
- "Age" and origin are as recorded by 19th-century registrars and can be approximate.

## Overlaps ("do both")
- Pairs with `[[familysearch]]` and national archives — SlaveVoyages anchors the voyage/origin, while genealogical services extend the line into later generations and post-emancipation records.

## Trust & verifiability
`trust: trusted` — a rigorously sourced academic project (Emory University); records cite their archival provenance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slavevoyages-org |
| category | people-search |
| selectorsIn → selectorsOut | name → name, geolocation, dob, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
