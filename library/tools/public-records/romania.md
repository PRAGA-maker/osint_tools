---
id: romania
name: "Romania Trade Register (ONRC)"
description: Use when you have a Romanian `employer-org`/company name (or CUI) and want the official trade-register record — returns registered `address`, status and associated officers.
url: https://portal.onrc.ro/ONRCPortalWeb/ONRCPortal.portal
category: public-records
path:
- public-records
bestFor: Official Romanian company search — confirm a company exists and pull its registered address and basic record.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- name
status: live
pricing: freemium
costNote: Basic existence/identification search is free; detailed extracts (furnizare informații — officers, financials, history) are paid per-document through the ONRC portal, and full features require an account.
opsec: passive
opsecNote: Passive lookup of the official public registry; the company/officers are not notified. Ordering paid extracts requires an account that logs your requests — use a research account. First-party government source.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Romania's Oficiul Național al Registrului Comerțului (ONRC), the national trade register — authoritative for Romanian company data. Portal is Romanian-language.
missingPersonsRelevance: high
coverage:
- ro
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- gov-cy
aliases:
- ONRC
- Registrul Comertului
- portal.onrc.ro
tags:
- companysites
- Company Related Sites
- corporate-records
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Romania Trade Register (ONRC)

> Romania's official national trade register (ONRC) — the authoritative source for whether a Romanian company exists, its registered address, and (via paid extracts) its officers and filings.

## When to use
You have a Romanian `employer-org` (company name or CUI/registration number) or a person you suspect is tied to a Romanian entity, and you want the official record rather than a third-party aggregator. A registered address and officer list link a subject to a company, a location, and other associated people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the ONRC portal at the URL (Romanian-language; use browser translation if needed).
2. Use the public search ("Verificare disponibilitate firmă" / company search) to find the entity by name or CUI.
3. Read the free identification result: company name, registration number, status, and registered `address`.
4. For officers, history, and financials, order a paid extract ("furnizare informații") — this needs an account and a fee.
5. Pivot: registered address feeds location OSINT; officer names (from a paid extract) feed people-search; a shared address links multiple firms.

## Inputs → Outputs
- **In:** `employer-org` (company name or CUI) or an officer `name`
- **Out:** `employer-org` record, registered `address`, status; officers/`name` via paid extract
- **Empty/negative result looks like:** no matching company — try the exact CUI or name fragments; the free tier confirms existence and address but withholds officer detail until you pay.

## Gotchas & OpSec
- Romanian-language portal; terminology and forms are in Romanian.
- Freemium: existence/address is free, but the investigative gold (officers, filings) is paywalled per-document.
- The public portal occasionally requires an account or is geo/DNS-restricted; retry or use the official ONRC access points.

## Overlaps ("do both")
- Pairs with EU aggregators (OpenCorporates) and other national registries like `[[gov-cy]]` — the aggregator gives a fast multi-country pass; ONRC gives the authoritative Romanian record for anything you'll rely on.

## Trust & verifiability
`trust: trusted` — the official Romanian trade register; records are authoritative, though the free tier is limited and full detail is paid.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | romania |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
