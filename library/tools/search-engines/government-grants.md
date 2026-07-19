---
id: government-grants
name: Government Grants (Grants.gov)
description: Use when you have an `employer-org` or keyword and want US federal grant activity — returns funding opportunities and (via awards) organisation/`associate` leads.
url: https://www.grants.gov/search-grants
category: search-engines
path:
- search-engines
bestFor: Searching US federal grant opportunities by keyword/agency/eligibility to link an organisation or individual to federal funding activity.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free official US government portal (run under HHS); search and opportunity details are open with no account. Applying requires registration, but searching does not.
opsec: passive
opsecNote: A public government search; anonymous and non-alerting. Safe to use directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official US federal grants portal; opportunity data is authoritative. Note it lists opportunities — for who actually received awards, pair with USAspending/agency award data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Grants.gov
- grants.gov
tags:
- toddington
- curated-directory
- specialty-search
- government-data
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Government Grants (Grants.gov)

> The US government's official portal of federal grant opportunities — searchable by keyword, agency and eligibility, and a jumping-off point into who gets federal funding.

## When to use
You're profiling an organisation, nonprofit, researcher or program tied to your subject and want its US federal funding footprint. Grants.gov lists the opportunities (and their eligibility, agency and categories); combined with award data it helps connect an `employer-org` or `name` to federal money, board members, and partner institutions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.grants.gov/search-grants.
2. Search by keyword (org name, program, topic) and filter by agency, eligibility, category, and status (posted/closed/archived).
3. Open an opportunity for the funding agency, eligibility, amounts and program contacts.
4. Pivot: Grants.gov shows *opportunities*, not recipients — take the agency/program into **USAspending.gov** or the agency's award database to find who actually received the money, then take those orgs/people into corporate and people search.

## Inputs → Outputs
- **In:** `employer-org` or keyword (program/topic/`name`)
- **Out:** matching funding opportunities, agencies, eligibility, program contacts → `employer-org` leads
- **Empty/negative result looks like:** no opportunities — the topic/org has no matching current or archived federal opportunity here. For actual awards received, this is the wrong tool; use award-level data.

## Gotchas & OpSec
- **Opportunities, not awards.** This lists what's available to apply for, not who won — always pair with USAspending for recipients.
- US federal only; state/local and non-US grants are elsewhere.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with USAspending.gov and agency award databases (recipients, amounts, sub-awards) and with nonprofit filings (IRS 990) — Grants.gov is the front door, those show where the money landed.

## Trust & verifiability
`trust: trusted` — the official federal portal; opportunity data is authoritative. Because it doesn't show recipients, corroborate any funding-to-entity claim with award-level sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | government-grants |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, name → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
