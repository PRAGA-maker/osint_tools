---
id: immo-data-fr
name: immo-data.fr
description: Use when you have a French `address` and want the property's recorded sale prices and transaction history — returns geolocation and price/date records from official DVF data.
url: https://www.immo-data.fr/
category: public-records
path:
- public-records
bestFor: Mapping French property sale transactions (price, date, size) by address or area from open DVF land-value data.
selectorsIn:
- address
selectorsOut:
- address
- geolocation
status: live
pricing: freemium
costNote: Free interactive map of DVF transaction data; some advanced/detailed features may require a paid tier, but the core price/history map is free. No account needed for basic use.
opsec: passive
opsecNote: This visualizes France's open DVF (Demandes de valeurs foncières) dataset — official records of property sales — on a map. It does not name buyers/sellers and does not contact anyone; browsing is fully passive. The subject is never notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built on the French government's official DVF land-transaction dataset; the sale prices/dates are authoritative, though the data omits owner identities.
missingPersonsRelevance: high
coverage:
- fr
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- immo-data.fr
- DVF map
tags:
- propertysites
- Property Related Sites
- france
- property-records
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# immo-data.fr

> An interactive map of France's official property-sale records — enter an address and see what nearby homes sold for and when.

## When to use
You have a French `address` tied to a subject and want context on the property: recorded sale prices, transaction dates, floor area, and type. It won't name the owner (DVF is anonymized), but confirming a property exists, its value bracket, and when it last changed hands corroborates an address, supports timeline work, and frames follow-up requests to the Land Registry (Service de la publicité foncière) for ownership.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `https://www.immo-data.fr/` and enter the `address` or navigate the map to the location.
2. Click the parcel/building: recorded sale price(s), date(s), surface area, and property type appear.
3. Compare against neighbouring transactions to gauge whether a claimed value/timeline is plausible.
4. Note the precise location (`geolocation`) and any recent transaction date for your timeline.
5. Pivot: a confirmed address + transaction date → a formal Land Registry request for owner identity; the location → other French property/records tools.

## Inputs → Outputs
- **In:** `address` (French)
- **Out:** confirmed `address`, `geolocation`, sale price/date/area history for the property
- **Empty/negative result looks like:** no transactions on the parcel — the property may not have sold in the DVF coverage window, or is new/social housing. Absence of a sale isn't absence of a property.

## Gotchas & OpSec
- No owner names: DVF is anonymized — pair with the Land Registry for identity.
- Coverage is transactions within the DVF dataset's period; long-held properties show nothing.
- OpSec: fully **passive** — official open data, no subject contact.

## Overlaps ("do both")
- Pairs with the French Land Registry and address/records tools — immo-data confirms and values the parcel; the registry attaches ownership; `[[planningportal-nsw-gov-au]]` is the equivalent-style tool for NSW, Australia.

## Trust & verifiability
`trust: trusted` — sale prices/dates come from the government's DVF dataset and are authoritative; the limitation is scope (anonymized, transaction-window bound), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | immo-data-fr |
| category | public-records |
| selectorsIn → selectorsOut | address → address, geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
