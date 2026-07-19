---
id: better-business-bureau
name: Better Business Bureau
description: Use when you have a business `name` or `employer-org` and want its contact details, principals and complaint history — returns `address`, `phone` and `associate` leads.
url: https://www.bbb.org
category: public-records
path:
- public-records
bestFor: Profiling a US/Canada business — address, phone, listed principals, accreditation and complaint history — and checking a name against the BBB Scam Tracker.
selectorsIn:
- name
- employer-org
selectorsOut:
- address
- phone
- associate
status: live
pricing: free
costNote: Free to search and read business profiles, reviews, complaints and the Scam Tracker; no account required.
opsec: passive
opsecNote: Reading BBB profiles is anonymous and does not notify the business. Filing a complaint or review would be active and identifying — stay on the read side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established nonprofit. Business contact/principal data is generally reliable; ratings and complaint outcomes are BBB's own methodology and reflect its process, not a court finding.
missingPersonsRelevance: medium
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BBB
- bbb.org
- BBB Scam Tracker
tags:
- company-research
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Better Business Bureau

> A searchable directory of US/Canada businesses with contact details, listed principals, complaint histories and a public scam-report tracker.

## When to use
You have a business `name` or `employer-org` tied to your subject — an employer, a shell company, a shop from a listing — and you want its address, phone, the people running it, and whether it has a trail of complaints or scam reports. Also useful to check a business/person name against the **Scam Tracker** for consumer-filed fraud reports.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bbb.org and search the business `name` and location.
2. Open the profile: read the `address`, `phone`, website, "Business Management" / principals (`associate` names), accreditation status and years in business.
3. Review the complaints and customer-review sections for patterns and named parties.
4. Separately, check the **BBB Scam Tracker** (bbb.org/scamtracker) for the name/phone/URL.
5. Pivot: take principal names into people-search, and the address/phone into reverse lookups; feed the company into a state corporate registry for officers and filings.

## Inputs → Outputs
- **In:** business `name` / `employer-org` (optionally + location)
- **Out:** `address`, `phone`, listed principals (`associate`), plus complaint/scam history
- **Empty/negative result looks like:** no profile — many small/informal businesses aren't listed; absence isn't proof the business doesn't exist. Common names return several profiles, so disambiguate by location.

## Gotchas & OpSec
- Ratings and "accreditation" reflect BBB's own process (and accreditation is paid), so a grade is not an independent verdict — use the factual fields (address, principals, complaints), not the letter grade.
- Coverage is US/Canada only.
- OpSec: passive read; filing anything is identifying.

## Overlaps ("do both")
- Pairs with state/provincial corporate registries (officers, registered agent) and reverse phone/address tools — BBB gives the human-readable profile and complaint trail, the registry gives the legal filing detail.

## Trust & verifiability
`trust: community` — an established nonprofit with generally reliable contact data, but ratings are its own methodology. Treat complaints as allegations and confirm principals/addresses against an official registry before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | better-business-bureau |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → address, phone, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
