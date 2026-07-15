---
id: greece
name: Greece
description: Use when you have a Greek company `name`/`employer-org` and want its beneficial owners (UBO) — returns the natural persons behind the entity, though public access is now gated.
url: https://www.gsis.gr/en/citizens-businesses/businesses/real-beneficiaries-register
category: public-records
path:
- public-records
bestFor: Identifying the natural-person beneficial owners behind a Greek legal entity via the government UBO register.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- employer-org
- address
status: degraded
pricing: free
costNote: Official Greek government register, free where accessible. Since a Nov 2022 notice (following the EU CJEU ruling on UBO registers) full public access was suspended — access is now restricted to authorised users / those with a demonstrable legitimate interest, typically via TaxisNet credentials.
opsec: passive
opsecNote: Passive against the target — you query a government register, not the person or their company's own systems, and no notification is sent to the subject. However, access itself is authenticated/gated, so using it ties the lookup to whatever official credentials you authenticate with — do not use personal credentials for covert work.
humanInLoop: true
humanInLoopReason:
- legal-gate
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Greek government beneficial-ownership register (GSIS/AADE), the authoritative source for Greek UBO data; limitation is access restriction, not data quality.
missingPersonsRelevance: high
coverage:
- gr
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- bloomberg-com
aliases:
- Greek Central Register of Real Beneficiaries
- Κεντρικό Μητρώο Πραγματικών Δικαιούχων
- UBO register Greece
tags:
- companysites
- Company Related Sites
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Greece

> Greece's Central Register of Real Beneficiaries (UBO) — the authoritative link from a Greek company to the natural persons who actually own/control it, now behind an access gate.

## When to use
Your subject is connected to a Greek `employer-org`, or you're trying to find which companies a person beneficially owns/controls in Greece. The UBO register maps legal entities to their real (natural-person) beneficial owners — a direct way to tie a name to corporate control, and to surface co-owners as `associate` leads. Reach for it when Greek corporate ownership is central to the trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start at https://www.gsis.gr/en/citizens-businesses/businesses/real-beneficiaries-register (the register app lives at webapps.gsis.gr/dsae/boregistry).
2. Authenticate — since Nov 2022, public browsing is suspended; you'll need authorised access (TaxisNet credentials / demonstrated legitimate interest).
3. Search by company/entity to retrieve its registered beneficial owners.
4. Read the natural-person owners tied to the entity.
5. Pivot: named owners feed people-search and international corporate registries; cross-reference the company via `[[bloomberg-com]]` or OpenCorporates for a fuller picture.

## Inputs → Outputs
- **In:** Greek company/`employer-org` (or a person, to test ownership)
- **Out:** beneficial-owner `name`(s), the `employer-org` link, sometimes address details
- **Empty/negative result looks like:** access denied at the auth gate (you lack authorised access — not a data absence), or no registered UBO for exempt entity types.

## Gotchas & OpSec
- Access is the main obstacle: public access is suspended; without authorised credentials/legitimate interest you can't query it. Treat a login wall as an access issue, not "no record."
- Data is only as current as the entity's filing obligations.
- OpSec: **passive** toward the target, but the register itself is authenticated — never use personal/official credentials for covert work.

## Overlaps ("do both")
- Pair with `[[bloomberg-com]]` and international registries (OpenCorporates) — the Greek register gives the legally-filed beneficial owners; the others add executives, financials and cross-border links the UBO filing omits.

## Trust & verifiability
`trust: trusted` — a first-party government register, authoritative for Greek beneficial ownership. The only caveat is availability: access restrictions (not accuracy) are what limit its use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | greece |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
