---
id: gov-uk-13
name: HM Land Registry — Search Property Information (by map)
description: Use when you have a UK `address`/`geolocation` and want to identify a registered property and obtain its ownership — returns the title number via map, with owner details available as a paid title download.
url: https://search-property-information.service.gov.uk/search/search-by-map/
category: public-records
path:
- public-records
bestFor: Identifying a registered England & Wales property from a map and obtaining its title/ownership.
selectorsIn:
- address
- geolocation
selectorsOut:
- address
- name
status: live
pricing: freemium
costNote: Searching the map and identifying a title is free; downloading the title register/plan (which contains the registered owner's name) costs a small statutory fee (a few pounds) per document.
opsec: passive
opsecNote: The search is passive and the property owner is not notified. Buying a title register is logged against the payment/account you use — use a sock-puppet account/payment if the enquiry must stay unattributable.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official HM Land Registry service — the authoritative source of registered land ownership in England & Wales. Owner data comes from the paid title register, which is definitive.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- HM Land Registry search
- Search for property information
- search-property-information.service.gov.uk
tags:
- propertysites
- Property Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# HM Land Registry — Search Property Information (by map)

> The official route from a location to a property owner in England & Wales — pick the property on a map to get its title number, then buy the title register to see the registered owner's name.

## When to use
You have a UK `address` or `geolocation` and want to know who owns the property — a definitive ownership answer that people-search brokers can't give. Central to a missing-person or asset investigation: confirm a subject owns/owned an address, or find the registered owner of a place tied to the subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search-property-information.service.gov.uk/search/search-by-map/ and navigate the map to the `address`/`geolocation`.
2. Click the property to identify its registered title (title number) and confirm it's registered.
3. For ownership, purchase the **title register** (a few pounds) — it names the registered proprietor(s) and shows price-paid and any charges.
4. Optionally buy the title plan for the boundary.
5. Pivot: the registered owner `name` feeds people-search and corroborates a subject's link to the address; price-paid/charges add financial context.

## Inputs → Outputs
- **In:** `address` / `geolocation` (via map)
- **Out:** title number and registration status (free); registered owner `name`, price paid, charges (paid title register)
- **Empty/negative result looks like:** the map shows no registered title for the spot — the land may be unregistered (common for long-held property), or you clicked the wrong parcel. Unregistered ≠ nonexistent.

## Gotchas & OpSec
- Owner name is paywalled: the free step only identifies the title; you must buy the register to see the owner.
- Unregistered land: not everything is registered, especially older holdings — absence of a title isn't absence of ownership.
- Scope: England & Wales (Scotland = Registers of Scotland; NI = Land Registry NI).

## Overlaps ("do both")
- Pairs with `[[onthehouse-com-au]]`-style property data (for other countries) and UK company registries — Land Registry gives the definitive owner, while property portals add market/history context and companies registries resolve corporate owners.

## Trust & verifiability
`trust: trusted` — the official HM Land Registry; the title register is the authoritative record of registered ownership in England & Wales.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-13 |
| category | public-records |
| selectorsIn → selectorsOut | address → address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
