---
id: rjsc-connect
name: RJSC Connect (Nova Scotia Registry of Joint Stock Companies)
description: Use when you have an `employer-org` or business name in Nova Scotia and want its registration record — returns entity status, registered address, and associated officers/agents.
url: https://rjsc.novascotia.ca/
category: public-records
path:
- public-records
bestFor: Confirming and looking up Nova Scotia (Canada) registered companies, societies, and business names.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Name/existence search is free; obtaining full certificates or detailed filing documents typically incurs a Service Nova Scotia fee and may require a Connect account.
opsec: passive
opsecNote: An official provincial government registry; you query the government's system, not any target, and the business owner is not notified. Some detailed lookups require signing in with a Nova Scotia account — use appropriate hygiene if you create one.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Service Nova Scotia / Access Nova Scotia — the authoritative provincial corporate and business-name registry (Registry of Joint Stock Companies).
missingPersonsRelevance: low
coverage:
- ca
auth: account
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- employee-contact-directory-search-novascotia-ca
- opencorporates
aliases:
- Registry of Joint Stock Companies
- Nova Scotia RJSC
- Access Nova Scotia business registry
tags:
- business-registry
- canada
- corporate-records
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# RJSC Connect (Nova Scotia Registry of Joint Stock Companies)

> Nova Scotia's official corporate registry — search whether a company, society, or business name is registered in the province and pull its status, address, and associated people.

## When to use
You have an `employer-org` or business name tied to a subject in Nova Scotia, Canada, and want to confirm it exists, check whether it is active or struck off, and identify its registered address and associated officers/agents. Use it to verify a business claim, tie a person to a company, or find the registered address behind a Nova Scotia entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://rjsc.novascotia.ca/ and open the registry / business-name search.
2. Enter the `employer-org` / business name (or a partial name) and search.
3. Read the result: entity name, registry ID, status (active / inactive / revoked), type (company, society, sole proprietorship), and registered office `address`.
4. For officers/agents, ownership, or an official certificate, open the entity and request the detailed record — this may prompt a Nova Scotia account sign-in and a fee.
5. Pivot: a registered `address` and `associate` names feed people-search and further registry checks; cross-province ownership feeds `[[opencorporates]]`.

## Inputs → Outputs
- **In:** `employer-org` / business `name`
- **Out:** entity status, registry ID, registered `address`, associated officers/agents (`associate`)
- **Empty/negative result looks like:** "no matching registration" — the name is not registered in Nova Scotia (it may be registered in another province, federally, or under a variant spelling); try partial-name search and other Canadian registries.

## Gotchas & OpSec
- Provincial scope only — a Nova Scotia entity may operate under a different name federally or in another province. Absence here ≠ no company anywhere.
- Free tier shows existence, status, and basic details; full documents and some officer data sit behind a login and a Service Nova Scotia fee.
- Business names (sole proprietorships) and incorporated companies are both indexed — check the entity type before assuming corporate structure.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` — RJSC is the authoritative provincial source; OpenCorporates aggregates across jurisdictions and may surface the same entity plus related filings elsewhere. Confirm here, broaden there.
- Combine with `[[employee-contact-directory-search-novascotia-ca]]` for Nova Scotia public-sector staff lookups.

## Trust & verifiability
`trust: trusted` — a first-party government registry, authoritative for Nova Scotia corporate/business-name status. Certified copies for legal use require the paid official document.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rjsc-connect |
