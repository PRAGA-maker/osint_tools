---
id: zoopla-co-uk
name: zoopla.co.uk
description: Use when you have a UK `address` and want property intelligence — returns sold-price history, current/past listings, property details and photos of interiors.
url: https://www.zoopla.co.uk/house-prices/
category: public-records
path:
- public-records
bestFor: UK property research — sold-price history, listing history and interior photos for an address.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free to browse house prices, sold history and listings; no account needed (an account only adds saved searches/alerts).
opsec: passive
opsecNote: You research a property, not a person — no notification reaches anyone. Zoopla shows publicly listed property data (Land Registry sold prices, past listings). Use a sock-puppet browser. Note: it reveals property/occupancy context, not directly who currently lives there.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major UK property portal drawing on Land Registry sold-price data and estate-agent listings; reliable for property facts, though "estimated value" figures are modelled.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Zoopla
- zoopla.co.uk
tags:
- propertysites
- Property Related Sites
- uk
- property
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# zoopla.co.uk

> A UK property intelligence source — sold-price history, listing history, and often interior photos for any address.

## When to use
You have a UK `address` linked to a subject and want context about the property: when it last sold and for how much, whether it's currently or was recently listed for sale/rent, its size/type, and — valuably — interior/exterior photos from past listings. Property research places a subject geographically, hints at circumstances (recent move, sale), and the listing photos can corroborate or reveal detail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.zoopla.co.uk/house-prices/ in a sock-puppet browser.
2. Enter the `address` or postcode.
3. Read the property page: Land Registry sold-price history (dates + amounts), current/past sale & rental listings, property type/size, and photo galleries from any listings.
4. Cross-reference with Rightmove (which may hold different listing history/photos) for the same address.
5. Pivot: sold dates hint at when a subject moved in/out; listing photos give interior/context detail; the postcode feeds electoral-roll and neighbour research.

## Inputs → Outputs
- **In:** `address` / postcode (UK)
- **Out:** sold-price history, listing history, property details, and listing photos for the `address`
- **Empty/negative result looks like:** sparse data — a property never listed on Zoopla or with no recorded sale (e.g. long-held or council property). Absence of listings doesn't mean the address is invalid; check Rightmove and Land Registry directly.

## Gotchas & OpSec
- **Property, not people:** Zoopla tells you about the dwelling, not who currently lives there — pair with the electoral roll/people-search to link property to person.
- "Estimated value" is a model, not a fact; sold prices (Land Registry) are the reliable figures.
- OpSec: **passive**; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with Rightmove, the Land Registry, and UK electoral-roll/people tools — Zoopla and Rightmove hold overlapping-but-different listing photos/history, and the electoral roll links the address to occupants. Do all for full property+occupant context.

## Trust & verifiability
`trust: trusted` — a major portal built on Land Registry and agent data; sold-price and listing facts are reliable, while estimated valuations are modelled. Confirm sold prices against the Land Registry when precision matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zoopla-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
