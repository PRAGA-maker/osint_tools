---
id: eircode-ie
name: Eircode Finder
description: Use when you have an Irish `address` and want its unique Eircode (postcode), or an Eircode and want the matching address — returns a precise address for a single property.
url: https://finder.eircode.ie/#/
category: public-records
path:
- public-records
bestFor: Resolving an Irish address to its unique property-level Eircode, or reverse.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free public lookup operated by the official Eircode service. No account.
opsec: passive
opsecNote: Official address-lookup utility; searching is anonymous and does not identify or notify anyone. No people data is returned — only address/postcode.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Eircode (An Post / Capita) — the authoritative Irish postcode system; address↔Eircode mapping is official.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-maps
- eircode-ie-2
aliases:
- Eircode finder
- finder.eircode.ie
tags:
- propertysites
- Property Related Sites
- ireland
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Eircode Finder

> Ireland's official postcode finder — maps a specific Irish address to its unique, property-level Eircode and back.

## When to use
You have an Irish `address` (even a partial one) for a subject and want to normalize it to a precise, unambiguous property identifier — the Eircode. Unlike UK/US postcodes, every individual Irish address has its OWN Eircode, so it pins a single door, not a street. Use it to disambiguate a vague address, confirm a property exists, or produce a clean address for downstream property/records searches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://finder.eircode.ie/#/.
2. Type the address (street, town, or building) and select the matching property from the suggestions to get its Eircode; or enter an Eircode to get the exact address.
3. Read the result: the specific address and its Eircode, plus a map pin.
4. Pivot: the confirmed address feeds Irish property/land-registry and people-search tools; the map pin feeds `[[google-maps]]` for street-level context.

## Inputs → Outputs
- **In:** `address` (or an Eircode)
- **Out:** `address` (precise, property-level) + Eircode
- **Empty/negative result looks like:** no matching property — the address may be mistyped, newly built, or a non-postal location. It returns no occupant names; this is address data only.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; anonymous official lookup, no people data.
- Scope: gives you the property, not who lives there — pair with occupancy/electoral sources to link an address to a person.

## Overlaps ("do both")
- Pairs with `[[google-maps]]` — turn the confirmed Eircode/address into satellite and street-view imagery of the property.
- Pairs with `[[eircode-ie-2]]` — alternate Eircode lookup path for cross-checking or bulk work.

## Trust & verifiability
`trust: trusted` — first-party official Irish postcode authority; the address↔Eircode mapping is authoritative. Its limit is that it holds no occupant/identity data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eircode-ie |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
