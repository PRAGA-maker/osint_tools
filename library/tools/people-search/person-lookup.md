---
id: person-lookup
name: Person Lookup (South Africa)
description: Use when you have a `name` or `phone` in South Africa and want the matching landline and address — returns telephone/address records and property data for ~5.5M South Africans.
url: https://personlookup.co.za/
category: people-search
path:
- people-search
bestFor: South African name-to-phone/address and reverse-phone lookups.
selectorsIn:
- name
- phone
selectorsOut:
- address
- phone
- name
status: live
pricing: freemium
costNote: Basic search/preview appears free; fuller contact and property details are typically gated behind payment, as with most people-search databases.
opsec: passive
opsecNote: Searching is passive and not shown to the subject, but you are querying a commercial data broker that logs lookups. Use a sock-puppet. Data is regional (South Africa) and drawn from telephone/address and property records.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Listed in the Bellingcat toolkit (South Africa). A commercial landline/address database compiled from public and directory sources; can be stale or incomplete (landline-centric), so corroborate.
missingPersonsRelevance: high
coverage:
- za
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- truecaller
- whitepages
aliases:
- personlookup.co.za
- Person Lookup ZA
tags:
- bellingcat-toolkit
- people
- south-africa
source: bellingcat-toolkit
lastVerified: '2026-07-14'
enrichment: full
---

# Person Lookup (South Africa)

> A South African telephone-and-address database (~5.5M landline records) with reverse-phone and property lookups — a regional people-search anchor for ZA subjects.

## When to use
You have a `name` or a South African `phone` number and want to tie it to a landline and physical address, or run it in reverse (number → name/address). Because it's regionally focused and includes property valuation/sale history, it can pin down a South African subject where global people-search engines are thin. Best treated as leads to confirm.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://personlookup.co.za/ in a sock-puppet browser.
2. Search by `name` (add a province to disambiguate) or enter a `phone` number for reverse lookup.
3. Read the preview: matched name, landline, and address; property records may accompany an address.
4. For fuller detail, the site may prompt payment — decide whether the free preview already gives you a pivot.
5. Pivot: an address feeds property/deeds and neighbour checks; a phone feeds `[[truecaller]]`-style caller-ID; a confirmed name feeds broader people-search.

## Inputs → Outputs
- **In:** `name` or `phone` (South Africa)
- **Out:** `address`, `phone` (landline), `name`, and associated property data
- **Empty/negative result looks like:** no match — common for mobile-only individuals (the database is landline-centric) or people with no directory footprint. Absence isn't proof of non-existence.

## Gotchas & OpSec
- Landline-centric: South Africa is heavily mobile, so many people won't appear; a null result is weak.
- Data-broker caveats: stale addresses and same-name merges — verify before acting.
- Passive to the subject, but the operator logs your queries; sock-puppet it.

## Overlaps ("do both")
- Pairs with `[[truecaller]]` (crowd-sourced caller ID, strong on mobiles where this is weak) and `[[whitepages]]`-style directories — run both so mobile and landline footprints are covered.

## Trust & verifiability
`trust: community` — a Bellingcat-listed regional data broker, useful but not authoritative. Corroborate contact and property data against a second source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | person-lookup |
| category | people-search |
| selectorsIn → selectorsOut | name, phone → address, phone, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
