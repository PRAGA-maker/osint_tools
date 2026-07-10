---
id: asic-gov-au
name: ASIC Registers (Australia)
description: Use when you have a person `name`, company `name`/ACN or `address` in Australia and want official corporate/registration records — returns companies (`employer-org`), registered `address`es and officeholder `name`s.
url: https://asic.gov.au/online-services/search-asics-registers/
category: public-records
path:
- public-records
bestFor: Searching Australia's official corporate registers to link a person to companies, business names, and registered addresses; some detailed extracts are paid.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: freemium
costNote: Basic register searches (company/business-name existence, status, ABN/ACN) are free; full company extracts, historical/officeholder documents, and current-and-historical searches are paid per document. Note ASIC's business/company registers have been migrating to the ABRS/Business Registry Service.
opsec: passive
opsecNote: Public register search does not notify the subject. Paid extracts require an account/payment that ties the lookup to your billing identity — use an investigative account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Australian Securities and Investments Commission (and the Australian Business Registry Services), the official regulators — authoritative for company and business-name records.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ASIC
- asic.gov.au
- Australia company search
- ABN Lookup
tags:
- companysites
- company-related-sites
- public-records
- corporate-registry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ASIC Registers (Australia)

> Australia's official corporate and business-name registers — the authoritative way to link a person to Australian companies, business names, and registered addresses.

## When to use
You have a `name` with an Australian nexus and want to establish corporate footprint: registered companies, business names, officeholder roles, and the addresses attached to them. Australian company records place a person and reveal co-directors and business addresses — valuable for locating someone or mapping associates. Also use to research a company `name`/ACN or a business name directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://asic.gov.au/online-services/search-asics-registers/ and pick the register: Organisations & Business Names, Professional Registers, Banned/Disqualified, etc. For a company's ABN/basic status, ABN Lookup (abr.business.gov.au) is the free companion.
2. Search a company `name`/ACN or a business name; free results give status, type, and registration dates.
3. For officeholders, registered `address`, and history, request the **company extract** — this is the paid step.
4. Check the **Banned and Disqualified** register by `name` to see if the person is disqualified from managing companies (a strong red flag/lead).
5. Pivot: registered address → property/people-search; co-officers → `associate` graph; ACN/business name → OpenCorporates and news.

## Inputs → Outputs
- **In:** `name` (officer/business owner), company `name`/ACN, business name, or `address`
- **Out:** `employer-org` (companies/business names), `address` (registered/business address, on paid extract), `name` (co-officeholders), plus status, dates, and disqualification records
- **Empty/negative result looks like:** no register match — the person may hold no Australian company/business registrations, or names differ. Free search shows existence/status; officer-level detail usually needs a paid extract, so "no detail" may just mean you haven't purchased it.

## Gotchas & OpSec
- **Migration:** ASIC's registers are moving to the Australian Business Registry Services; some searches/links have shifted — follow the current on-site pointers.
- Free vs paid: existence and status are free; the person-linking detail (officeholders, addresses) is usually a paid extract.
- OpSec: **passive** — public record; paid extracts tie to your billing identity.

## Overlaps ("do both")
- Pairs with free **ABN Lookup** (fast, free company/ABN status) and with `[[company-information-service-gov-uk]]`/OpenCorporates for cross-jurisdiction directorships.

## Trust & verifiability
`trust: trusted` — first-party Australian regulator; corporate records are authoritative. Filed addresses are self-declared, so verify identity where decisive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | asic-gov-au |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
