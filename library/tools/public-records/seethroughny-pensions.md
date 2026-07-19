---
id: seethroughny-pensions
name: SeeThroughNY — Pensions
description: Use when you have a `name` of a New York public-sector retiree and want their pension record — returns employer-org, retirement date and annual pension amount.
url: https://www.seethroughny.net/pensions
category: public-records
path:
- public-records
bestFor: Looking up a named New York State/local government or school retiree's public pension, employer and retirement year.
selectorsIn:
- name
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free public transparency database run by the Empire Center; no account required to search.
opsec: passive
opsecNote: Searching a public transparency database; nothing touches the subject and no login is needed. Passive. The data (pension amounts) is public record but sensitive — handle responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the Empire Center for Public Policy from official NY public-pension-system data obtained via FOIL; a well-known, reliable transparency source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- SeeThroughNY pensions
- Empire Center pensions
tags:
- transparency
- pensions
- public-employees
- new-york
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# SeeThroughNY — Pensions

> The Empire Center's free New York pension-transparency database — search a name to confirm a public-sector retiree's employer, retirement year and annual pension.

## When to use
You have a `name` who may be a retired New York State or local-government/school employee (teacher, police, civil servant) and want to confirm and profile them: which system/employer (`employer-org`) they retired from, their retirement year, and their annual pension amount. Useful in a locate/missing-persons case to confirm a person's career, retirement status, and continued existence in the pension rolls (an active pension implies a living, paid retiree), and to corroborate identity/age indirectly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.seethroughny.net/pensions.
2. Enter the retiree's `name` (last/first); filter by pension system (NYSLRS, NYS Teachers, NYC systems, etc.) if you know it.
3. Read the record: name, retirement system/employer, year of retirement, and annual pension benefit.
4. Cross-check with SeeThroughNY's payroll section for the person's working-era salary/employer if still employed.
5. Pivot: employer/system → workplace and colleague context; retirement year → age/timeline estimate; confirmed record → address/people-search to locate.

## Inputs → Outputs
- **In:** retiree `name`
- **Out:** pension record — retiree `name`, retirement system/`employer-org`, retirement year, annual pension amount
- **Empty/negative result looks like:** no match — the person isn't a NY public-pension recipient (private-sector, another state, federal, or not yet retired); common names return multiple records needing the system/employer to disambiguate.

## Gotchas & OpSec
- New York public-sector only — not private employers, other states, or federal pensions.
- Some systems (notably certain NYC/police-fire) may be partially redacted or absent depending on FOIL outcomes.
- Common names need disambiguation by system/employer/retirement year.
- OpSec: passive; data is public record but personally sensitive — use responsibly.

## Overlaps ("do both")
- Pairs with SeeThroughNY's payroll/salary data and with other states' transparency sites (e.g. Transparent California) — run the appropriate state's database for public-sector subjects.

## Trust & verifiability
`trust: trusted` — sourced from official NY pension systems via FOIL and published by an established policy institute; figures are reliable, with the usual name-disambiguation caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seethroughny-pensions |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
