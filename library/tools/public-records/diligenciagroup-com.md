---
id: diligenciagroup-com
name: ClarifiedBy (Diligencia)
description: Use when you have a `name`, `address`, or `employer-org` linked to the Middle East or Africa and want authoritative corporate-registry data, officers, and beneficial owners — returns `employer-org`, `associate`, and `address` links.
url: https://clarifiedby.diligenciagroup.com/
category: public-records
path:
- public-records
bestFor: Resolving companies, directors, and ultimate beneficial owners across Middle East & Africa jurisdictions from official registry data.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- associate
- address
- name
status: live
pricing: freemium
costNote: ClarifiedBy is a commercial due-diligence platform. Basic entity/person discovery is viewable, but full records, network diagrams, UBO explorer, and bespoke analyst searches are gated behind a paid subscription. Expect a login/paywall for depth.
opsec: passive
opsecNote: Searches run against Diligencia's own aggregated dataset, not the subject's infrastructure, so the target is not alerted. However you must register/authenticate for meaningful use, so your queries are attributable to your account — use an operationally appropriate identity.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established corporate-intelligence provider (Diligencia, founded 2008) curating data exclusively from official registries across 70+ countries; regarded as a reputable MEA-focused source.
missingPersonsRelevance: high
coverage:
- ae
- sa
- global
aliases:
- Diligencia
- ClarifiedBy
- Diligencia Group
tags:
- companysites
- Company Related Sites
- corporate-registry
- ubo
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# ClarifiedBy (Diligencia)

> A Middle East & Africa corporate-intelligence platform built from official registry data — the go-to for company officers, ownership chains, and ultimate beneficial owners in a region where public registries are otherwise thin.

## When to use
You have a `name`, an `employer-org`, or a business `address` connected to the Middle East or Africa and need to map who owns or runs a company, or which entities a person is tied to. Diligencia curates data from 50+ UAE registries/free zones and hundreds of official sources across MEA (25M+ records), filling gaps where standard company-search tools return nothing. Strong for surfacing `associate` links (co-directors, UBOs) around a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL and sign in / start a trial (meaningful results require an account; depth requires a paid plan).
2. Search by company `name`, person `name`, or `address`. Bilingual search (Arabic + English) helps when a subject's name is transliterated.
3. Open an entity record: read officers, registration details, and linked individuals; use the network-diagram / UBO Explorer to map ownership chains and beneficial owners.
4. Read outputs: connected companies (`employer-org`), co-officers and owners (`associate`), and registered `address` values.
5. Pivot: an `associate` or UBO name feeds back into another search here or into global sanctions/PEP and people-search tools; a company `address` feeds geolocation and other registry lookups.

## Inputs → Outputs
- **In:** `name`, `address`, or `employer-org`
- **Out:** `employer-org` (linked companies), `associate` (directors, co-owners, UBOs), registered `address`, confirmed `name` spellings
- **Empty/negative result looks like:** no matching entity/person in the covered jurisdictions — common if the subject's business activity is outside MEA, where this dataset is strongest.

## Gotchas & OpSec
- Human-in-the-loop: expect an account login and a partial paywall — free browsing shows existence and summaries; full officer/UBO detail and analyst-assisted searches are paid.
- Coverage is MEA-centric. Do not treat a null result as global clearance.
- OpSec: passive toward the subject, but authenticated — queries tie to your account.

## Overlaps ("do both")
- Pairs with global corporate-registry and sanctions tools — ClarifiedBy is strongest for MEA official data, while OpenCorporates-style aggregators and PEP/sanctions lists cover other regions and risk flags this may lack.

## Trust & verifiability
`trust: trusted` — Diligencia (est. 2008) sources exclusively from official registries and is a recognized corporate-intelligence provider; still, confirm a critical UBO/officer finding against the underlying registry document where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | diligenciagroup-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, associate, address, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
