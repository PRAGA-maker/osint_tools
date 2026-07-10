---
id: info-clipper-com
name: info-clipper.com
description: Use when you have a company `name` (or an `employer-org`/`phone`) and want its registry profile, directors and address across 200 countries — returns `employer-org`, `address`, `associate` (directors).
url: https://www.info-clipper.com/en/
category: public-records
path:
- public-records
bestFor: Worldwide company KYC lookups — profiles, directors, shareholders and addresses across 200 countries.
selectorsIn:
- name
- employer-org
- phone
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Company search and directory browsing are free; full reports (registration detail, financials, official documents) are pay-as-you-go with no subscription (a prepaid pass lowers per-report cost). Budget for a paid report to get the meaty data.
opsec: passive
opsecNote: Passive — you query info-clipper's aggregated registry data; the company/directors are not notified. Info-clipper logs your searches and requires payment (hence identity/payment trail) for full reports; use appropriate billing hygiene if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial reseller aggregating official company registers from many jurisdictions; data ultimately derives from registries but is repackaged, so verify against the primary register for critical facts.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- info-clipper
tags:
- companysites
- Company Related Sites
- corporate-records
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# info-clipper.com

> A global company-registry aggregator: search a firm in 200 countries and pull its directors, shareholders, address and corporate structure.

## When to use
You have a company `name`, an `employer-org` tied to your subject, or a business `phone`/registration number, and you need the corporate picture: who the directors and shareholders are (`associate` leads), the registered `address`, and parent/subsidiary links. Strong when a missing-persons or fraud trail runs through a business, especially outside the US/UK where a single worldwide search saves hunting each national register.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.info-clipper.com/en/ and search by company `name`, telephone number, or registration number; pick the country.
2. Browse the free company profile: jurisdiction, registration detail, HQ `address`, and listed directors.
3. For directors/shareholders, financials, or official documents, order the pay-as-you-go report (prepaid pass reduces cost).
4. Note each director/shareholder `name` as an `associate` pivot.
5. Pivot: run directors through `[[companycheck-co-uk]]` (UK) or `[[familytree]]` (US), and the company address through mapping/records tools.

## Inputs → Outputs
- **In:** company `name`, `employer-org`, `phone`, or registration number
- **Out:** `employer-org` profile, registered `address`, `associate` (directors/shareholders), corporate structure
- **Empty/negative result looks like:** no company matched, or only a bare stub with paid detail locked — the firm isn't in that jurisdiction's covered register, or you need to buy the report to see more. Absence isn't proof the company doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: **payment-wall-partial** — the useful director/financial detail sits behind a per-report charge.
- OpSec: **passive** to the target; paying leaves a billing trail on your side — use appropriate hygiene.
- It's a reseller: for anything legally critical, confirm against the country's official register directly.

## Overlaps ("do both")
- Pairs with `[[companycheck-co-uk]]` (UK depth) and `[[familytree]]` (US individuals) — info-clipper gives the global corporate map; the others enrich the people behind it.

## Trust & verifiability
`trust: community` — commercial aggregator of official registers. Good for coverage and triage; verify director/ownership facts against the primary registry before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | info-clipper-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, phone → employer-org, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
