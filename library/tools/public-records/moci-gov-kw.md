---
id: moci-gov-kw
name: moci.gov.kw (Kuwait Commercial Registry)
description: Use when you have a Kuwaiti company or trade `name` and want its official commercial-registration details — returns registry data tying businesses to owners/agents.
url: https://www.moci.gov.kw/en/e-service/electronic-services-managing-commercial-registry/
category: public-records
path:
- public-records
bestFor: Confirming a Kuwaiti company's commercial registration and linking it to owners/agents.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- address
status: live
pricing: free
costNote: Government e-service. Basic access is free, but the commercial-registry inquiry portal (ereg.moci.gov.kw) requires an account login; some filings/extracts may carry a fee.
opsec: active
opsecNote: You query a Kuwaiti government system and must log in to reach the registry inquiry, so activity is authenticated and logged under Kuwaiti jurisdiction. Use a research account, not a personal one, and be aware the interface is primarily Arabic.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Kuwait Ministry of Commerce and Industry portal — authoritative for Kuwaiti commercial registrations; the constraint is access (login, Arabic UI), not data reliability.
missingPersonsRelevance: high
coverage:
- kw
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- opencorporates-com
- blockint-nl
aliases:
- Kuwait MOCI
- Kuwait commercial registry
tags:
- companysites
- Company Related Sites
- corporate-registry
- kuwait
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# moci.gov.kw (Kuwait Commercial Registry)

> Kuwait's Ministry of Commerce and Industry e-services portal — the official commercial registry for confirming a Kuwaiti company and the people (owners, agents) behind it.

## When to use
You have a Kuwaiti company or trade `name` (or a person you believe is a Kuwaiti business owner/commercial agent) and need authoritative corporate data: registration status, trade name, and the owner/agent linkage. This is the primary-source registry for Kuwait — use it to verify a business exists, tie it to individuals, or work backwards from a company to its principals in a Gulf-region investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the MOCI e-services page and go to the commercial-registry management service; you'll be routed to the portal at ereg.moci.gov.kw.
2. Log in with a (research) account — the inquiry services require authentication.
3. Use the "extract / inquiry about an agent or client" service to look up a trade name or commercial registration.
4. Read the registry data: legal entity, trade name, registration number, status, and associated owner/agent (`name`) and address details.
5. Pivot: an owner name feeds people-search and sanctions/PEP checks; a company feeds cross-border corporate mapping via `[[opencorporates-com]]`.

## Inputs → Outputs
- **In:** `employer-org` (trade/company name) or an owner/agent `name`
- **Out:** `employer-org` registration details, associated `name`(s), and business `address`
- **Empty/negative result looks like:** no matching registration in the portal — meaning it isn't in Kuwait's commercial registry (or your spelling/transliteration is off; try the Arabic name). Absence isn't proof the person has no business interests elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: the useful inquiry functions sit behind an account login; expect an Arabic-first interface and possible registration friction.
- Transliteration matters — Arabic company/personal names have many Latin spellings; search the Arabic form when possible.
- Authenticated and jurisdictionally sensitive — use a research account and assume the government logs your queries.

## Overlaps ("do both")
- Pairs with `[[opencorporates-com]]` (cross-border corporate aggregation that may index Kuwaiti entities more searchably) and `[[blockint-nl]]` (for beneficial-ownership routing) — use the official MOCI portal as the authoritative confirm and the others for reach and pivots.

## Trust & verifiability
`trust: trusted` — it is Kuwait's official commercial registry, so the data is authoritative. Reliability isn't the issue; access (login, Arabic UI) is. Verify identities via the registration number and cross-checks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | moci-gov-kw |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
