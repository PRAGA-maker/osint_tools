---
id: infoflow-public-people-search-in-chilean
name: InfoFlow Public People Search In Chilean
description: Use when you have a Chilean `name`, RUN (national ID) or `vehicle-plate` and want identity/vehicle/company data — InfoFlow aggregates Chilean public records into a single lookup.
url: https://infoflow.cloud/
category: people-search
path:
- people-search
- general-people-search
bestFor: Chilean identity resolution — name/RUN/plate to personal data, vehicle registration and company links.
input: Name, RUN (Chilean ID number), or vehicle plate
output: Personal identification data, vehicle registration, company records
selectorsIn:
- name
- document-id
- vehicle-plate
selectorsOut:
- name
- address
- dob
- employer-org
- vehicle-plate
status: live
pricing: freemium
costNote: Freemium — registration (with a Chilean RUT) is required, and fuller results/queries are typically metered or paid beyond a free allowance.
opsec: active
opsecNote: You must register (with a Chilean RUT) and log in, so queries are attributable to your account and may be logged by the operator. This is an aggregator of a third party's compiled data, not an official portal — use a sock-puppet account and assume the searched selectors are recorded.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial aggregator of Chilean public/leaked records; convenient but unofficial, with unverified data currency and provenance.
missingPersonsRelevance: high
coverage:
- cl
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- InfoFlow Chile
- infoflow.cloud
tags:
- people-search
- chile
- vehicle
- identity
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# InfoFlow Public People Search In Chilean

> A Chilean records aggregator — feed it a `name`, RUN (national ID), or `vehicle-plate` and it returns identity data, vehicle registration and company links in one place.

## When to use
You have a Chilean subject and a seed selector — full name, RUN (Rol Único Nacional), or a `vehicle-plate` — and want to resolve identity and pivot: confirm the RUN↔name link, find registered vehicles, and surface companies the person is tied to. Chile's identity system is RUN-centric, so a RUN is the master key that ties records together; this tool exploits that in a single interface instead of querying separate portals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://infoflow.cloud/ and register/log in (a Chilean RUT is required — use a sock-puppet).
2. Search by `name`, RUN, or `vehicle-plate`.
3. Read the aggregated result: personal identification (name, RUN, address, birth data), vehicle registration, and company/role records.
4. Pivot: a RUN feeds official Chilean portals (SII for tax/companies, Registro Civil, court records) to corroborate; a plate ties a person to a vehicle; company links feed corporate OSINT.

## Inputs → Outputs
- **In:** `name` / `document-id` (RUN) / `vehicle-plate`
- **Out:** `name`, `address`, `dob`, `employer-org` (company records), `vehicle-plate`/registration
- **Empty/negative result looks like:** no match, or only partial data behind a paywall/quota. A miss can mean the record isn't in the aggregator's dataset or you've hit the free-tier limit — corroborate a RUN against official Chilean sources before trusting a null.

## Gotchas & OpSec
- **Unofficial aggregator:** data may be stale, incomplete, or sourced from leaks — treat outputs as leads and confirm against official Chilean registries.
- **Registration + login required** (`account-login`): queries are attributable to your account; use a sock puppet and be mindful of Chilean data-protection law.
- RUN formatting/check-digit matters — enter it correctly to avoid false negatives.

## Overlaps ("do both")
- Pairs with official Chilean sources — SII (Servicio de Impuestos Internos) for company/tax, Registro Civil for identity, and the electoral roll — which are authoritative where this aggregator is merely convenient.

## Trust & verifiability
`trust: unverified` — a commercial third-party aggregator, not an official register. Confirm any identity, address, or vehicle link through Chile's official portals before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infoflow-public-people-search-in-chilean |
| category | people-search |
| selectorsIn → selectorsOut | name, document-id, vehicle-plate → name, address, dob, employer-org, vehicle-plate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
