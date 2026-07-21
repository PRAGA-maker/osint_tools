---
id: scoot
name: Scoot
description: Use when you have a UK business `name`/`employer-org` and a `geolocation` and want its listing — returns `address`, `phone`, and `domain`.
url: http://www.scoot.co.uk
category: public-records
path:
- public-records
bestFor: Looking up a UK business's contact details (address, phone, website) from a national business directory.
selectorsIn:
- name
- employer-org
- geolocation
selectorsOut:
- address
- phone
- domain
status: live
pricing: free
costNote: Free to search and view UK business listings; no account required to browse.
opsec: passive
opsecNote: A public directory lookup that touches only Scoot's servers; the listed business is not notified. Routine sock-puppet browsing is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A UK business directory aggregating listings from multiple feeds; data can be stale or duplicated, so confirm contact details against a second source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- scoot.co.uk
tags:
- company-research
- uk
- business-directory
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Scoot

> A UK business directory — for people work, a way to reach a subject through a business they own or run: its address, phone, and website.

## When to use
You have a UK business `name`/`employer-org` tied to the subject plus a rough `geolocation`, and you want the listed `address`, `phone`, and `domain`. Small and medium UK businesses that don't surface cleanly in Companies House searches often have a Scoot listing with direct contact details — a route to a person via their trade or company.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open scoot.co.uk.
2. Search the business `name`/category and set the UK location to the subject's `geolocation`.
3. Open the matching listing and read the `address`, `phone`, website (`domain`), category, and any additional contact detail.
4. Check listing freshness — directory data is aggregated and can lag behind closures or moves.
5. Pivot: feed the `address` into UK property/records tools, the `phone` into reverse-phone lookup, the `domain` into WHOIS, and the business name into Companies House.

## Inputs → Outputs
- **In:** UK business `name`/`employer-org` + `geolocation`
- **Out:** `address`, `phone`, `domain`/website, category
- **Empty/negative result looks like:** no matching listing — the business isn't in Scoot's index (small/new/closed) or is outside the UK; try Companies House or a maps directory next.

## Gotchas & OpSec
- UK business directory, not a people index — it reaches a person via their business, not directly.
- Aggregated data can be outdated or duplicated; verify contact details against a live source.
- OpSec: passive; nobody is notified.

## Overlaps ("do both")
- Pairs with UK Companies House and reverse-phone/WHOIS tools — Scoot gives quick contact info; those give legal ownership and confirm the details.

## Trust & verifiability
`trust: unverified` — a real UK directory, but listing accuracy depends on its aggregated feeds; treat any address/phone as a lead to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scoot |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, geolocation → address, phone, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
