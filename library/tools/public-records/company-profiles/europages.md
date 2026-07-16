---
id: europages
name: Europages
description: Use when you have a company `name`, product, or `employer-org` and want European B2B company listings — returns employer-org contact details, address and domain leads.
url: https://www.europages.co.uk/
category: public-records
path:
- public-records
- company-profiles
bestFor: Finding European suppliers, manufacturers, and B2B companies by name, product, or sector, with contact details.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- domain
status: live
pricing: free
costNote: Free B2B directory search; no account needed to browse company listings. Companies pay for enhanced listings, but searching is free.
opsec: passive
opsecNote: Browsing directory listings is passive and does not contact the companies. Avoid the "contact supplier"/quote-request forms for a target company — those send your enquiry to the business and expose your interest.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running pan-European B2B directory; listings are largely self-submitted by companies, so details are useful leads but not authoritative registry data.
missingPersonsRelevance: low
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
aliases:
- europages.com
- europages.co.uk
tags:
- company-search
- b2b
- directory
- europe
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Europages

> A pan-European B2B directory: search a company name, product, or industry and get supplier/manufacturer listings with contact details, products, and locations across Europe.

## When to use
A business-context tool. When your investigation touches a European company — a supplier, manufacturer, or trading business tied to your subject — Europages helps locate the `employer-org` and its listed `address`, phone, website (`domain`), and product lines. Useful for characterising a business, finding its contact points, or confirming it operates in a claimed sector/country before pivoting to an authoritative company registry.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.europages.co.uk/ (or the localized domain).
2. Search by company name, product, or industry sector; filter by country/region.
3. Open a listing for the company's address, contact details, website, certifications, and product catalogue.
4. Pivot: the `domain` → WHOIS/site analysis; the `address` and legal name → the national company registry (Companies House, France's Infogreffe, etc.) for authoritative ownership; product/sector → context on what the business does.

## Inputs → Outputs
- **In:** company `name`, product, or sector (`employer-org`)
- **Out:** European B2B listings → `employer-org` contact details, `address`, and website `domain`.
- **Empty/negative result looks like:** no listing for the company — it isn't registered in Europages (small, non-B2B, or non-European); use a national registry instead.

## Gotchas & OpSec
- Listings are largely self-submitted marketing profiles — treat details as leads, verify legal/ownership facts in an official registry.
- Coverage is B2B and Europe-focused; consumer businesses and non-EU firms may be absent.
- Enhanced/paid listings rank higher, which is promotion, not authority.

## Overlaps ("do both")
- Pairs with OpenCorporates and national registries — Europages gives contact/product context, those give authoritative incorporation and officer data.

## Trust & verifiability
`trust: community` — a directory of self-submitted business profiles; good for contact leads and sector context, but confirm identity and ownership against an official corporate registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | europages |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
