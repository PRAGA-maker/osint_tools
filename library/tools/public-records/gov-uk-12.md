---
id: gov-uk-12
name: gov.uk (HM Land Registry Property Search)
description: Use when you have an `address` in England or Wales and want the registered owner and title details — returns the proprietor's `name`, the property `address`/description, and price-paid history.
url: https://www.gov.uk/search-property-information-land-registry
category: public-records
path:
- public-records
bestFor: Finding the registered legal owner of a property in England & Wales from its address (official HM Land Registry title data).
selectorsIn:
- address
selectorsOut:
- name
- address
status: live
pricing: freemium
costNote: The service is official and cheap, not free — the title register (which names the owner) and title plan cost £3 each, paid by card. Basic property/price-paid info is viewable free.
opsec: passive
opsecNote: You query HM Land Registry's records, not the owner — the subject is not notified. Purchasing a title register is logged against your payment/account; use a research payment method and stay within a lawful purpose (this is personal data).
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: HM Land Registry is the official government register of property ownership in England & Wales; the title register is authoritative primary-source data.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- HM Land Registry property search
- Search for property information
tags:
- propertysites
- Property Related Sites
- land-registry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# gov.uk (HM Land Registry Property Search)

> The official route to England & Wales property ownership — turn an address into the registered proprietor's name and the title history for £3.

## When to use
You have an `address` in England or Wales and need to know who legally owns it — to confirm a subject lives at / owns a property, identify a landlord, or find a name behind an address. HM Land Registry's title register is the authoritative source for registered ownership, and this gov.uk service is the sanctioned way to buy it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.uk/search-property-information-land-registry.
2. Enter the property `address` and select the matching title.
3. View the free summary (property description, tenure, and often price-paid history).
4. To get the owner's `name`, purchase the **title register** (£3); the title plan (£3) shows boundaries.
5. Pivot: the proprietor `name` feeds people-search and company registries; price-paid dates give an occupancy/purchase timeline; a corporate owner feeds Companies House.

## Inputs → Outputs
- **In:** `address` (England or Wales)
- **Out:** registered proprietor `name` (in the paid title register), property `address`/description, tenure, price-paid history
- **Empty/negative result looks like:** the address isn't found or the title is unregistered (some long-held properties are still unregistered) — meaning no digital title to buy, not that no one owns it. Scotland/NI use different registers.

## Gotchas & OpSec
- **England & Wales only** — Scotland is Registers of Scotland, NI is Land & Property Services.
- The owner's name is behind the £3 title register; the free view alone won't name them.
- Some older properties are unregistered; absence of a title ≠ no owner.
- Personal data — use lawfully.

## Overlaps ("do both")
- Pairs with `[[planning-org-uk]]` (works/applicants at the address) and Companies House (for corporate owners) — Land Registry gives *who owns it now*, planning gives *activity and applicants*.

## Trust & verifiability
`trust: trusted` — the official government property register; the purchased title register is authoritative primary evidence of registered ownership.
