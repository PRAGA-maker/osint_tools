---
id: companieshouse-gi
name: companieshouse.gi
description: Use when you have a Gibraltar `employer-org` or director `name` and want official company registry data — returns company details, directors/officers (`name`), registered `address`, and filings.
url: https://www.companieshouse.gi/
category: public-records
path:
- public-records
bestFor: Official Gibraltar company registry — company details, directors, and filings for Gibraltar-registered entities.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- address
status: live
pricing: freemium
costNote: The registry is official; basic search may be free, but viewing/downloading company documents via the e-Registry typically requires registration and per-document fees.
opsec: passive
opsecNote: You query the official registry, not the subject — no notification. Buying documents via the e-Registry ties activity to a registered account/payment; use a research account and a lawful basis.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Gibraltar Companies House registry (statutory incorporations/dissolutions and filings); data is authoritative.
missingPersonsRelevance: medium
coverage:
- gi
auth: none
api: false
localInstall: false
registration: true
aliases:
- Companies House Gibraltar
- Gibraltar company registry
tags:
- companysites
- Company Related Sites
- corporate-registry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# companieshouse.gi

> Gibraltar's official company registry — find directors, registered addresses, and filings for Gibraltar-registered entities (a common offshore/holding jurisdiction).

## When to use
You have a Gibraltar `employer-org` or a director `name` and need authoritative corporate data: who the officers/directors are, the registered `address`, incorporation/dissolution status, and filings. Gibraltar is a frequent offshore/holding jurisdiction, so this registry matters when a subject's company trail runs through it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.companieshouse.gi/ and use the e-Registry search.
2. Search by company name (`employer-org`) or, where supported, director `name`/registration number.
3. Read the company record: status, registered `address`, and officers/directors (`name`).
4. Register and pay per-document fees to view/download filed documents (accounts, annual returns) for deeper detail.
5. Pivot: director names → people-search and other registries (UK Companies House, offshore leak databases); shared directors/addresses → `associate`/network mapping.

## Inputs → Outputs
- **In:** `employer-org` (company name/number) or director `name`
- **Out:** `employer-org` details, officers/directors (`name`), registered `address`, filing history
- **Empty/negative result looks like:** no match — the entity isn't Gibraltar-registered, or the name/number is off. Absence here is jurisdiction-specific; check the relevant country's registry.

## Gotchas & OpSec
- Gibraltar-only — for UK companies use Companies House (gov.uk), and other jurisdictions for offshore chains.
- Documents are typically behind registration + per-item fees; basic search may be free.
- Offshore structures can obscure ultimate ownership — corroborate with beneficial-ownership/leak sources.

## Overlaps ("do both")
- Pairs with UK Companies House, `[[croatia]]`-style UBO registers, and offshore leak databases (OpenCorporates, ICIJ Offshore Leaks) — this gives the Gibraltar filing, the others help trace ownership beyond the jurisdiction.

## Trust & verifiability
`trust: trusted` — the official statutory registry; company/officer data is authoritative. Note that registered directors may be nominees — verify ultimate ownership via additional sources.
