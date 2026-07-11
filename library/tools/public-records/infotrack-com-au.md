---
id: infotrack-com-au
name: InfoTrack (Australia)
description: Use when you have a `name`, `address` or `employer-org` in Australia and need professional property, company, court or person-locator searches — returns property ownership, company records, addresses and litigation/associate context. Account-gated professional service.
url: https://www.infotrack.com.au/solutions/searches-certificates/
category: public-records
path:
- public-records
bestFor: Australian professional searches — property ownership, ASIC company data, bankruptcy, person locator, court and PEP/sanctions checks.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
- associate
status: live
pricing: freemium
costNote: A paid B2B professional platform for legal/conveyancing/compliance users — most searches are charged per search/certificate and require an approved account. Some free verification exists (e.g. address/proprietor verification in NSW/VIC/QLD), but there is no meaningful free public tier; treat as effectively paid.
opsec: passive
opsecNote: Searches draw on official registries and are passive toward the subject (no notification). However, access is tied to a verified professional account, so this is not anonymous — your firm/account is attached to each search, and some searches (criminal history, credit) have legal/consent constraints. Only run searches you are authorised and permitted to perform.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major, established Australian searches provider integrating official sources (Land Registries, ASIC, AFSA, PPSR, courts); data is authoritative because it comes from those registries, though access is professional-gated.
missingPersonsRelevance: high
coverage:
- au
auth: account
api: false
localInstall: false
registration: true
aliases:
- InfoTrack Australia
- infotrack.com.au
tags:
- propertysites
- company-records
- property-records
- litigation
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# InfoTrack (Australia)

> Australia's big professional-searches platform — a single account-gated front-end to Land Registry, ASIC, AFSA, PPSR and court data, used by lawyers and conveyancers to pull property, company, bankruptcy and person-locator searches.

## When to use
You have an Australian `name`, `address` or company (`employer-org`) and need authoritative searches: who owns a property, all properties owned by a person (national ownership search), a company's ASIC record and officers, bankruptcy status, civil litigation, or a person locator. Best when you have professional access and need registry-grade results rather than consumer people-search guesses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into an approved InfoTrack account (professional registration required) at https://www.infotrack.com.au/solutions/searches-certificates/.
2. Choose the search type: property (by address/title/owner), company (ASIC), personal (national property ownership, bankruptcy/AFSA, person locator, litigation, criminal history), or risk screening (PEP/sanctions).
3. Enter the identifier and run the (charged) search; results/certificates come from the underlying official registry.
4. Read the result — e.g. registered proprietor and address, company officers, or ownership across the country.
5. Pivot: property ownership ties a person to an `address`; ASIC officer records surface co-directors (`associate`); litigation/bankruptcy adds status context. Confirm anything critical against the source registry.

## Inputs → Outputs
- **In:** `name`, `address`, or company (`employer-org`)
- **Out:** property ownership + `address`, company `employer-org` records and officers, `associate` (co-officers/parties), bankruptcy/litigation status
- **Empty/negative result looks like:** a registry no-hit (no property/company/record found) — authoritative for that registry, but scoped to the specific search you ran and jurisdiction.

## Gotchas & OpSec
- **Access barrier:** professional account required; there is no open public search — individuals without an account can't use it, and per-search fees apply.
- Consent/legal constraints: some searches (criminal history, credit) require lawful basis/consent — don't run them outside your authorisation.
- OpSec: passive toward the subject, but every search is attributable to your account/firm — not anonymous.

## Overlaps ("do both")
- Pairs with the EU/other-jurisdiction registries and, for Australia specifically, with ASIC and state Land Registry direct — InfoTrack aggregates these; going direct is the authoritative confirmation.

## Trust & verifiability
`trust: trusted` — an established provider integrating authoritative Australian registries. The data is registry-grade; the constraints are access (professional-gated) and cost, not reliability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infotrack-com-au |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
