---
id: electricalcompetentperson-co-uk
name: electricalcompetentperson.co.uk
description: Use when you have an electrician's or firm `name` (or a UK postcode) and want to confirm government-registered status — returns the registered competent-person listing with company and area.
url: https://electricalcompetentperson.co.uk/
category: public-records
path:
- public-records
bestFor: Verifying that a UK (England & Wales) electrician/firm is on the government-approved Competent Person register.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free public search facility; no account needed.
opsec: passive
opsecNote: Passive — a public register search that only exposes business/trade details and is not attributed to the subject. Low leakage; it returns company-level info, not private home data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Registered Competent Person Electrical single register, backed by UK Government and the scheme operators (NICEIC, NAPIT, Blue Flame); authoritative for registration status in England & Wales.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gas-safe-register
- companies-house
aliases:
- Registered Competent Person Electrical
- Competent Person Electrical Register
tags:
- professionlicensing
- Profession & Licensing Sites
- electricians
- uk
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# electricalcompetentperson.co.uk

> The official UK (England & Wales) register of government-approved electricians — the "Gas Safe Register" equivalent for electrical work, searchable by postcode or company name.

## When to use
You have an electrician's `name`/`employer-org`, or a UK postcode, and want to confirm the person/firm is genuinely on the government-backed Competent Person Electrical register (authorised to self-certify Building Regulations compliance). Use it to vet a trade claim, or to locate/identify a working electrician by area — the listing ties a firm to a locality and registering body.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://electricalcompetentperson.co.uk/ and go to Search.
2. Enter a UK postcode to list registered electricians near it, or search by company name to check a specific firm.
3. Read the result: firm/registrant name, coverage area, and the scheme operator they're registered with (NICEIC, NAPIT, or Blue Flame).
4. A listing confirms current registration; absence suggests the person/firm isn't on this register (they may work in Scotland, be unregistered, or trade under a different name).
5. Pivot: a confirmed firm name feeds `[[companies-house]]` for directors/registered office; the coverage area anchors a geolocation.

## Inputs → Outputs
- **In:** `name`/`employer-org` (electrician or firm) or `address`/postcode
- **Out:** `employer-org` (registered firm), `address`/coverage area, registrant `name`, scheme operator
- **Empty/negative result looks like:** no listing for the searched name/postcode — meaning not on the England & Wales electrical register (not proof of no qualification; Scotland and other routes exist). Verify spelling and try the company name.

## Gotchas & OpSec
- Scope is England & Wales — Scottish electricians register under different schemes and won't appear.
- It confirms registration, not identity of an individual person — cross-check the firm on Companies House to reach named directors.
- Fully passive and low-leakage; only business details are exposed.

## Overlaps ("do both")
- Pairs with `[[gas-safe-register]]` (the analogous register for gas engineers) and `[[companies-house]]` (to turn a registered firm into named directors and a registered office).

## Trust & verifiability
`trust: trusted` — the official government-approved single register operated by the recognised scheme bodies. Registration status is authoritative; use Companies House to attach it to named individuals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | electricalcompetentperson-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
