---
id: land-registry-property-search
name: HM Land Registry — Property Search
description: Use when you have a UK `address` and want the legal owner — returns the registered proprietor's name and title details from the official land register.
url: https://eservices.landregistry.gov.uk/eservices/findaproperty/view/quickenquiryinit.do
category: people-search
path:
- people-search
bestFor: Finding who legally owns a property in England & Wales by address, via the official HM Land Registry title register.
selectorsIn:
- address
selectorsOut:
- name
- associate
- address
status: live
pricing: freemium
costNote: Searching the index is free; obtaining the title register or title plan (which name the owner) costs a small statutory fee (£3–£7 per document).
opsec: passive
opsecNote: You query the official land register by property, not by person, so the owner is not notified. Your purchase ties to your Land Registry order; the data (owner name, price paid) is official public record — use lawfully.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: HM Land Registry is the authoritative UK land-ownership register for England & Wales; the registered proprietor and title details are legally definitive.
missingPersonsRelevance: high
coverage:
- gb-eng
- gb-wls
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- '192'
- scottishepcregister-org-uk
aliases:
- HM Land Registry
- Find a Property
- Land Registry title register
tags:
- address
- property
- land-registry
- uk
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# HM Land Registry — Property Search

> The official England & Wales land register — enter a property `address` and, for a few pounds, obtain the title register naming the legal owner (registered proprietor) and key title details.

## When to use
You have a UK `address` and want to know **who owns it** — a definitive, authoritative answer, unlike aggregator guesses. The title register names the registered proprietor(s), and (via price-paid data) can show when they bought it. This connects a property to a person, reveals co-owners (`associate`s), and can surface a correspondence address if the owner lives elsewhere — powerful for locating someone through property they own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the Land Registry "Find a Property" search and enter the `address` (England & Wales).
2. Identify the correct title from the results.
3. Purchase the **title register** (£3) — this names the registered proprietor(s) and may include a correspondence address and any charges (mortgage lender).
4. Optionally buy the title plan to confirm the exact property boundary.
5. Pivot: the owner `name` and any co-owner `associate` feed `[[192]]`/people-search; a differing correspondence address is a locate lead; property characteristics cross-check with `[[scottishepcregister-org-uk]]` (Scotland) / EPC registers.

## Inputs → Outputs
- **In:** `address` (England & Wales)
- **Out:** registered proprietor `name`(s), co-owner `associate`s, and a correspondence `address` if the owner is elsewhere
- **Empty/negative result looks like:** no title found (unregistered land — older properties never sold since registration became compulsory), or a corporate/overseas owner instead of an individual; absence of an individual owner is itself informative.

## Gotchas & OpSec
- **England & Wales only** — Scotland (Registers of Scotland) and NI (Land Registry NI) are separate.
- Some land is **unregistered**; and ownership may sit behind a company or trust, not a person.
- Human-in-the-loop: the owner name is behind a small **paywall** (the free search only locates the title).
- OpSec: passive; your document order is logged to your account.

## Overlaps ("do both")
- Pairs with `[[192]]` (who lives there vs. who owns it can differ) and property/EPC registers like `[[scottishepcregister-org-uk]]` — combine ownership, occupancy and dwelling detail to fully resolve an address.

## Trust & verifiability
`trust: trusted` — legally definitive ownership data; the only caveats are scope (England & Wales, registered land) and that owners can be companies/trusts rather than named individuals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | land-registry-property-search |
| category | people-search |
| selectorsIn → selectorsOut | address → name, associate, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
</content>
