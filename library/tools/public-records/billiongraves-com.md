---
id: billiongraves-com
name: BillionGraves
description: Use when you have a `name` and want burial/headstone records — returns death/birth dates, GPS-tagged cemetery location and family members buried nearby.
url: https://billiongraves.com/search
category: public-records
path:
- public-records
bestFor: Finding a person's grave record — dates of birth/death, cemetery with GPS location, headstone photo, and linked family members.
selectorsIn:
- name
selectorsOut:
- dob
- geolocation
- associate
- name
status: live
pricing: freemium
costNote: Search and basic records are free; some features and deeper genealogy tools sit behind a paid plan, and it partners with genealogy services.
opsec: passive
opsecNote: You search a public genealogy/burial database; no living person is contacted. Records concern the deceased, so privacy risk is low, but linked family trees can expose living relatives — handle those responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large volunteer-photographed headstone database with GPS coordinates; individual transcriptions are volunteer-made and can contain errors, so verify dates against a certificate where it matters.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gro-gov-uk
aliases:
- billiongraves.com
tags:
- genealogybdmANDwills
- genealogy
- burial-records
- graves
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# BillionGraves

> A GPS-tagged headstone/burial database — search a `name` to find a grave record with dates of birth/death, the cemetery's exact coordinates, a headstone photo, and family members buried nearby.

## When to use
You have a `name` and want to establish whether a person is deceased and, if so, confirm their vital dates and place — or you're building a family tree and need to link relatives. Because records include GPS coordinates and headstone photos, and often cluster family plots, BillionGraves is strong for confirming a death, pinning a hometown/region, and discovering `associate`/family links (spouses, parents, children buried together).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://billiongraves.com/search and search by `name`, optionally with birth/death years or location.
2. Open a matching record: dates of birth/death, cemetery name and **GPS coordinates**, headstone photo, and linked family members.
3. Use the family links to map relatives; use the cemetery location as a geographic anchor to the person's community.
4. Cross-check volunteer-transcribed dates against a primary record where accuracy matters.
5. Pivot: family `associate` names feed people-search; confirmed vital dates corroborate identity; for England & Wales, verify with `[[gro-gov-uk]]`.

## Inputs → Outputs
- **In:** `name` (optionally + years/place)
- **Out:** `dob`/death dates, cemetery `geolocation` (GPS), headstone photo, and family `associate` links (plus confirmed `name`)
- **Empty/negative result looks like:** no matching grave — the person may be living, buried elsewhere/uncatalogued, or recorded under a variant name; absence isn't proof of anything.

## Gotchas & OpSec
- Transcriptions are **volunteer-made** — dates/spellings can be wrong; verify against a certificate for critical facts.
- Coverage varies hugely by country/region; strong where volunteers are active, thin elsewhere.
- Linked trees can expose **living** relatives — handle that data responsibly.
- OpSec: passive; concerns the deceased.

## Overlaps ("do both")
- Complements civil registers like `[[gro-gov-uk]]` and other genealogy sources — BillionGraves adds GPS location and headstone evidence; registers give authoritative dates/parentage. Do both to confirm death and map family.

## Trust & verifiability
`trust: community` — a large, useful crowd-sourced database with real GPS/photo evidence, but volunteer transcription means errors exist; corroborate dates before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | billiongraves-com |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, geolocation, associate, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
