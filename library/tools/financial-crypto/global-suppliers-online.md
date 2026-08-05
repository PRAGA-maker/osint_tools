---
id: global-suppliers-online
name: Global Suppliers Online
description: Use when you have a company/product (`employer-org`) or country and want to find manufacturers/exporters behind it — a B2B supplier directory returning company listings, `address`, contacts.
url: https://www.globalsuppliersonline.com/
category: financial-crypto
path:
- financial-crypto
bestFor: Tracing a product or trade name to the companies that make/export it, and enumerating suppliers by country or category.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Free to browse and search supplier listings and post buy requirements; contacting suppliers or premium membership features may prompt registration.
opsec: passive
opsecNote: You search a public B2B directory with company/product terms — no target person is queried and nothing is tipped off. Only registration (to message a supplier) exposes an identity; use a sock-puppet account if you go that far.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running B2B marketplace/directory (akin to Alibaba/Global Sources); listings are self-submitted by companies, so treat contact details as claimed-not-verified and corroborate against a corporate registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- globalsuppliersonline.com
tags:
- companies-finance
- b2b-directory
source: bellingcat-toolkit
lastVerified: '2026-08-05'
enrichment: full
---

# Global Suppliers Online

> A global B2B supplier/exporter directory: search a product, company, or country and get the manufacturers and trading companies behind it, with their self-listed contact and location details.

## When to use
You're investigating a company, a trade name, or a physical product and want to connect it to the businesses that manufacture, export, or trade it — for supply-chain, sanctions-evasion, or corporate-network work. You can also enumerate suppliers in a given country or category to map an industry. This is company/trade OSINT, not people search, but supplier records frequently expose an `address`, contact `name`, and linked entities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.globalsuppliersonline.com/.
2. Search by keyword/product, browse by category, or filter by country.
3. Open a supplier listing to read the company profile: products, location/`address`, contact person, and trade leads.
4. Pivot: take the company name into a corporate registry (`[[document-search]]`-style) to verify it exists and find officers; take the contact name/address into people/address search.

## Inputs → Outputs
- **In:** `employer-org` (company/trade name) or product keyword; optionally a country
- **Out:** company listings → `employer-org`, `address`, contact `name`/`associate`, product lines
- **Empty/negative result looks like:** no listings for the term — the company may not advertise on this directory (common for services or Western firms); try another B2B directory or the national registry directly.

## Gotchas & OpSec
- Listings are self-submitted and can be stale, aspirational, or fraudulent — never treat directory contact details as verified; confirm via an official registry.
- Coverage skews toward manufacturing/export sectors and certain regions; absence here means little.
- Messaging a supplier requires an account — use a sock puppet, never your real identity.

## Overlaps ("do both")
- Pairs with a corporate-registry lookup: this surfaces the trade-facing supplier identity, the registry confirms the legal entity, officers and filings behind it.

## Trust & verifiability
`trust: community` — a self-listed marketplace directory. Useful for leads and network mapping, but every contact detail is unverified; corroborate against authoritative company records before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-suppliers-online |
| category | financial-crypto |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
