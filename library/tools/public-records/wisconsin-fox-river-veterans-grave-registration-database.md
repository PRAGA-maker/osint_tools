---
id: wisconsin-fox-river-veterans-grave-registration-database
name: Wisconsin Fox River Veterans' Grave Registration Database
description: Use when you have a veteran's `name` connected to the Fox River region of Wisconsin and want burial details — returns cemetery/grave location and service information from a grave-registration database.
url: https://c3cqk813.caspio.com/dp/b201500011643c5f4c7f4bfba7d1
category: public-records
path:
- public-records
bestFor: Locating the burial/grave of a veteran in the Fox River area of Wisconsin and confirming a death.
selectorsIn:
- name
selectorsOut:
- name
- address
- dob
status: live
pricing: free
costNote: Free community/genealogy database (hosted on Caspio); no account to search.
opsec: passive
opsecNote: Read-only search of a public grave-registration database; no living person is queried or notified. Use a clean session for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A niche, locally-compiled veterans' grave-registration dataset (VetGraveEntries) hosted on Caspio; genealogically useful but community-maintained and geographically narrow.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- sortedbyname-com
aliases:
- Fox River Veterans Grave Registration
- VetGraveEntries
tags:
- veterans
- grave-registration
- cemetery
- wisconsin
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Wisconsin Fox River Veterans' Grave Registration Database

> A locally-compiled, searchable record of veterans' grave registrations for the Fox River region of Wisconsin — a niche way to confirm a death and locate a burial.

## When to use
You have a veteran's `name` with a plausible connection to the Fox River area of Wisconsin and you need to confirm they are deceased and where they are buried. Grave-registration databases like this record the cemetery and plot, and often service details and dates — decisive for closing a missing-persons line (confirmed death + burial site) or for corroborating a family history. Its scope is narrow (a specific Wisconsin region), so it's a supplement to national death/cemetery indexes, not a substitute.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the database at https://c3cqk813.caspio.com/dp/b201500011643c5f4c7f4bfba7d1 (the "VetGraveEntries Search and Report" datapage).
2. Search by veteran `name`.
3. Read the record: cemetery/grave location (`address`), service dates and any birth/death dates (`dob`).
4. Corroborate the death/burial against a broader index before relying on it.
5. Pivot: a confirmed burial + dates feed obituary and cemetery cross-checks; the name feeds `[[sortedbyname-com]]` and national grave indexes.

## Inputs → Outputs
- **In:** veteran `name`
- **Out:** `name`, cemetery/grave location (`address`), service and birth/death dates (`dob`)
- **Empty/negative result looks like:** no matching entry — the veteran isn't in this regional dataset (they may be buried elsewhere, or not covered). Absence says nothing beyond "not in this local database."

## Gotchas & OpSec
- **Geographically narrow**: Fox River / Wisconsin region only — always cross-check national indexes (Find A Grave, VA Nationwide Gravesite Locator) for broader coverage.
- Community-compiled; completeness and accuracy vary — corroborate.
- OpSec: **passive** — a public grave-registry read.

## Overlaps ("do both")
- Pairs with `[[sortedbyname-com]]` and national grave locators — this gives the local grave-registration detail; national indexes confirm and broaden the death/burial record.

## Trust & verifiability
`trust: community` — a genuine but niche, locally-maintained dataset; useful for its region, but corroborate any death/burial against a wider authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wisconsin-fox-river-veterans-grave-registration-database |
| category | public-records |
| selectorsIn → selectorsOut | name → name, address, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
