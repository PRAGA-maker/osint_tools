---
id: land-registry-map-enquiry
name: HM Land Registry – Map Enquiry
description: Use when you have a property `address` in England & Wales and want to identify its registered owner — returns the title number free, then the owner's name/address on the title register for a small fee.
url: https://eservices.landregistry.gov.uk/eservices/findaproperty/view/mapenquiryinit.do
category: people-search
path:
- people-search
bestFor: Turning a property address into the registered legal owner via HM Land Registry's official title records.
selectorsIn:
- address
selectorsOut:
- name
- document-id
status: live
pricing: freemium
costNote: Finding a property and its title number via the map is free; the title register / title plan that reveals the owner's name costs a small statutory fee (a few pounds) paid by card.
opsec: passive
opsecNote: An official records query — the registered owner is not notified. Ordering documents requires payment details tied to you; use a research payment method if you need separation.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: HM Land Registry is the official government register of property ownership in England & Wales; the title register is authoritative.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- HM Land Registry Find a Property
- Land Registry map search
tags:
- address
- property
- uk
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# HM Land Registry – Map Enquiry

> The official England & Wales route from an address to the person who legally owns it — free to find the title, small fee to see the name.

## When to use
You have a property `address` and want to know who owns it — a core people-search pivot for locating a subject, confirming a residence, or finding a landlord/associate. HM Land Registry's map enquiry lets you click the property on a map to get its title number, then order the title register (for a small fee) which names the registered proprietor(s) and their address for service.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the map enquiry service and search/zoom to the target `address`.
2. Select the property polygon; the service returns the registered title number(s) — this step is free.
3. Order the **title register** for that title (small card payment); it names the registered owner(s), the price paid history, and any address for service.
4. Optionally order the **title plan** to confirm boundaries.
5. Pivot: the owner `name` feeds people/company search; an off-address for service (owner living elsewhere) is itself a lead; a company owner feeds `[[companies-house]]`.

## Inputs → Outputs
- **In:** property `address` (or map location)
- **Out:** `document-id` (title number) free; on paid title register — registered owner `name`, their service address, price-paid history
- **Empty/negative result looks like:** the map returns no registered title — some land remains unregistered (older/never-sold parcels), so an absence means "not registered," not "no owner." Leasehold vs freehold may also split into multiple titles.

## Gotchas & OpSec
- The owner's name is **not** free — the map/title-number lookup is free, but you pay a small fee per title register to see the proprietor.
- England & Wales only — Scotland uses Registers of Scotland (ScotLIS); Northern Ireland has its own registry.
- OpSec: **passive**; the owner is not notified, but the payment ties the order to you.

## Overlaps ("do both")
- Pairs with `[[companies-house]]` (when the owner is a company) and electoral-roll / people-search tools — the register gives the legal owner, those flesh out who actually lives there.

## Trust & verifiability
`trust: trusted` — a first-party government register; the title register is the definitive legal record of ownership in England & Wales.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | land-registry-map-enquiry |
| category | people-search |
| selectorsIn → selectorsOut | address → name, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
