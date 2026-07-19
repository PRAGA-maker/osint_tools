---
id: property-search-public-records-by-state
name: Property Search — Public Records by State (BlackBookOnline)
description: Use when you have a US `name` or `address` and want the right county/state property-records portal — returns links to official assessor/recorder searches that yield owner name and address.
url: https://www.blackbookonline.info/usa-property.aspx
category: public-records
path:
- public-records
bestFor: A state-by-state directory routing you to the correct free official property-records search for a US address or owner.
selectorsIn:
- name
- address
selectorsOut:
- address
- name
status: live
pricing: free
costNote: BlackBookOnline's directory is free; it links to official county/state assessor and recorder sites, which are themselves free to search.
opsec: passive
opsecNote: A directory of official record portals; you query government sites, not the subject — passive, no notification. No account required for the directory.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: BlackBookOnline is a well-known free public-records link directory; the linked assessor/recorder sites are authoritative, the directory itself is a curated index.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- black-book-online-criminal-search
- nationwide-county-court-records-by-state-and
- arrest-warrants
- criminal-search-criminal-records-by-state-and
- free-aviation-records-black-book-online
- jail-records
- sex-offender-search
aliases:
- BlackBookOnline property search
- USA property public records
tags:
- property
- public-records-directory
- real-estate
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# Property Search — Public Records by State (BlackBookOnline)

> A free state-by-state directory that routes you to the correct official county/state property-records search — the fast way to find the authoritative assessor/recorder site for a given US address or owner.

## When to use
You have a US `address` or an owner `name` and need the *official* property record — owner of record, parcel details, assessed value, sale history — but property records live in thousands of separate county assessor/recorder databases. This BlackBookOnline page indexes them by state (and often county), so you jump straight to the right free government portal instead of hunting for it. Owner-of-record data is one of the most reliable ways to tie a person to an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blackbookonline.info/usa-property.aspx.
2. Pick the state, then the county/jurisdiction covering your target `address`.
3. Follow the link to the official assessor/recorder search and enter the `address` (or owner `name` where the county allows name search).
4. Read the parcel record: owner of record, mailing address, assessed value, and (via the recorder) deed/sale history.
5. Pivot: owner name → people-search and corporate registries; mailing address (if different from the property) → a second location; deed history → prior owners/associates.

## Inputs → Outputs
- **In:** US `address` (or owner `name`, where the county supports it)
- **Out:** links to official portals returning owner `name`, property `address`/parcel, assessed value, sale/deed history
- **Empty/negative result looks like:** a county with no online records (some are offline/paper-only), or a portal that only allows parcel/address (not name) search — the directory can't add coverage a county doesn't publish online.

## Gotchas & OpSec
- Coverage is uneven — many counties are online and free, some are paywalled or offline; the directory reflects, not fixes, that.
- Name-based search availability varies by county; address search is more universal.
- Owner "mailing address" can differ from the property address — a useful second lead.
- OpSec: passive; you touch government sites, not the subject.

## Overlaps ("do both")
- Pairs with commercial property aggregators (Zillow/Realtor/Trulia for listing history) — this directory gets you the *official owner-of-record*, those add market/photo context; use both to confirm.

## Trust & verifiability
`trust: community` — the directory is a curated index, but it points to authoritative county/state records, so the underlying data (once you reach the official portal) is highly reliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | property-search-public-records-by-state |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
