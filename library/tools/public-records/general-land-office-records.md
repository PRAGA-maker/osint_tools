---
id: general-land-office-records
name: General Land Office Records (BLM GLO)
description: Use when you have a `name` and want historical US federal land grants to that person — returns land-patent records with `geolocation` (state/county/legal description).
url: https://glorecords.blm.gov/search/default.aspx
category: public-records
path:
- public-records
bestFor: Finding historical federal land patents by patentee name to tie an ancestor/person to a specific place, date and parcel in US land-grant history.
selectorsIn:
- name
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free official US Bureau of Land Management site; records and scanned patent images are viewable/downloadable at no cost.
opsec: passive
opsecNote: A public federal records search; nothing is sent to any living person. Entirely safe and non-alerting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official BLM General Land Office records site; land patents are authoritative federal documents, mostly 1800s–early 1900s.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- GLO Records
- BLM GLO
- glorecords.blm.gov
- Federal Land Records
tags:
- toddington
- curated-directory
- specialty-search
- land-records
- genealogy
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# General Land Office Records (BLM GLO)

> The US government's official archive of federal land patents — search by patentee name to place a person on a specific parcel, in a specific county, on a specific date in land-grant history.

## When to use
You're doing genealogical or historical person-work in the US and have a `name`. GLO records reveal whether that person received a federal land patent — with the state, county, legal land description, acreage and issue date — anchoring an ancestor to a place and time. Most useful for 19th- and early-20th-century subjects and family-history threads in a long-cold case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://glorecords.blm.gov/search/default.aspx and choose "Land Patents."
2. Enter the patentee's last (and first) `name`; optionally narrow by state.
3. Review results: patentee, document type, state/county, land description (aliquot/section-township-range), acreage and date; open the scanned patent image.
4. Pivot: take the county + date into local historical records (deeds, census, cemeteries) and map the legal land description to modern coordinates to locate the parcel.

## Inputs → Outputs
- **In:** `name` (patentee)
- **Out:** `geolocation` — state/county and legal land description of granted parcels, plus dates and scanned documents
- **Empty/negative result looks like:** no patents — the person never received a federal land grant (most people didn't), or the name is spelled differently in the record. Absence says nothing about non-landholding individuals.

## Gotchas & OpSec
- **Historical scope.** This is federal land-grant history (largely pre-1930s), not modern property ownership — for current owners use county assessor/deed records.
- Legal land descriptions (township/range/section) need converting to lat/long to map — use a PLSS-to-coordinates tool.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with county deed/assessor records (modern ownership) and genealogy/census tools — GLO gives the original federal grant, those trace what happened to the land and the family afterward.

## Trust & verifiability
`trust: trusted` — authoritative federal records with scanned original documents. Verify name matches against the patent image, since transcription/spelling variants are common in historical records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | general-land-office-records |
| category | public-records |
| selectorsIn → selectorsOut | name → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
