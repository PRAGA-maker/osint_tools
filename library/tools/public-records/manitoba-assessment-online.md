---
id: manitoba-assessment-online
name: Manitoba Assessment Online
description: Use when you have a Manitoba property `address` (or roll/title number) and want its official assessment record — returns property details, roll number, and assessed value tied to that location.
url: https://www.gov.mb.ca/mao/public/search_select.aspx
category: public-records
path:
- public-records
bestFor: Looking up official property assessment records for a Manitoba address (property details and value; not owner names).
selectorsIn:
- address
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free public government service; no account required.
opsec: passive
opsecNote: A first-party government records search — you submit only a property address/identifier, and results are already public assessment data. Route through a VPN as routine hygiene; nothing about your subject is disclosed to the site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Province of Manitoba (Municipal and Northern Relations); authoritative government assessment data. Note: personal identifiers (owner names) are deliberately not searchable per provincial privacy law.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- manitoba-court-records
- manitoba-sex-offender
aliases:
- MAO
- Manitoba property assessment
tags:
- property-records
- public-records
- canada
- manitoba
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Manitoba Assessment Online

> The Province of Manitoba's official property-assessment lookup — resolve an address (or roll/title number) to its assessment record and value.

## When to use
Your case is anchored to a property in Manitoba (excluding the City of Winnipeg, which runs its own system) and you want the authoritative assessment record: property details, roll number, legal description, and assessed value. It confirms a property exists, characterises it, and links an `address` to official identifiers you can carry into court/land-title research. Note it is **address-in, property-out** — you cannot search by owner name (privacy law blocks personal identifiers as search keys).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.mb.ca/mao/public/search_select.aspx.
2. Choose a search method: civic **address**, certificate-of-title number, legal description, **roll number**, lot/block/plan, or Section-Township-Range (rural); a map search is also available.
3. Enter the identifier and submit.
4. Read the assessment record: roll number, property/legal details, and assessed value for that parcel.
5. Pivot: the roll number and legal description feed land-title and `[[manitoba-court-records]]` searches; the confirmed property `address`/`geolocation` anchors further canvassing.

## Inputs → Outputs
- **In:** Manitoba property `address` (or roll/title/legal identifier)
- **Out:** assessment record — roll number, property details, assessed value, confirmed `address`/`geolocation`
- **Empty/negative result looks like:** "no records" for a Winnipeg address (handled by the City of Winnipeg's separate system) or a mistyped identifier; a blank ≠ the property doesn't exist, it may just be outside MAO's scope.

## Gotchas & OpSec
- Human-in-the-loop: none, but the service is unavailable every Monday 3:30–4:30 p.m. for maintenance.
- OpSec: **passive** — first-party public records; you disclose nothing about your subject.
- You cannot search by owner name (privacy law) — this yields property/value data, not a person directly; pair it with land-title records to reach ownership.

## Overlaps ("do both")
- Pairs with `[[manitoba-court-records]]` and land-title searches — MAO gives the property and its identifiers, those add legal proceedings and registered ownership for the same parcel.

## Trust & verifiability
`trust: trusted` — an official Province of Manitoba system, so assessment data is authoritative; just remember its deliberate limitation (no owner-name search) and the Winnipeg carve-out.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | manitoba-assessment-online |
| category | public-records |
| selectorsIn → selectorsOut | address → address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
