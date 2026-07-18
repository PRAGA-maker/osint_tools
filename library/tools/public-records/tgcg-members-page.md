---
id: tgcg-members-page
name: TGCG Members Page
description: Use when you have a business name or region and want contact details for a listed member org — returns business `name`, `address`, and `phone` from a garden-center trade directory.
url: https://c2ffn114.caspio.com/dp/e6a74000833e44e23c324a10987c
category: public-records
path:
- public-records
bestFor: Looking up an independent garden-center / nursery member business by state to get its address and phone.
selectorsIn:
- employer-org
- address
selectorsOut:
- address
- phone
status: live
pricing: free
costNote: Free public Caspio-hosted directory; no login or payment.
opsec: passive
opsecNote: Passive — reading a published member directory. No subject is notified; the only footprint is your own visit to a third-party Caspio datapage. Standard clean-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A member-maintained trade-group directory embedded via Caspio; contact data is self-reported by member businesses and not independently verified.
missingPersonsRelevance: low
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- TGCG member directory
tags:
- directory
- business
- trade-group
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# TGCG Members Page

> A niche trade-group member directory (independent garden centers / nurseries across the US and Canada), served as a Caspio datapage — a source of business contact details, not personal records.

## When to use
You have a lead pointing to a specific garden-center / nursery business (an employer, a listed associate's workplace, a business named in another record) and want its address and phone, or you want to enumerate member businesses in a given state/province. This is a small, industry-specific directory — reach for it only when a case actually touches this sector; it will not help with a generic person search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Caspio datapage at the URL (enable cookies — the embedded app requires them).
2. Browse the member list, organized by US state / Canadian province, or use the in-page filter to find a business by name.
3. Read the row: business `name`, mailing `address`, and `phone`.
4. Pivot: an address/phone feeds a reverse-phone or property lookup; the business name feeds a corporate-registry or social-profile search to reach the people behind it.

## Inputs → Outputs
- **In:** a member business `name` or a target `address`/region
- **Out:** business `name`, `address`, `phone`
- **Empty/negative result looks like:** a business not affiliated with this group simply won't appear — absence means "not a member," not "doesn't exist."

## Gotchas & OpSec
- **Businesses, not people:** the directory lists organizations and their contact details; there are no personal names beyond what a business chooses to publish.
- Self-reported and un-audited — a listed phone/address may be stale; corroborate before relying on it.
- Very narrow scope (one trade group in horticulture retail); low general applicability.

## Overlaps ("do both")
- Pairs with corporate-registry and reverse-phone tools — this yields the business contact point, and those tie it to the individuals who own or run it.

## Trust & verifiability
`trust: community` — a member-maintained trade directory; the data is self-submitted by the businesses themselves and not independently verified, so treat entries as leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tgcg-members-page |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, address → address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
