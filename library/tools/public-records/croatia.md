---
id: croatia
name: Croatia (FINA Register of Beneficial Owners)
description: Use when you have a Croatian `employer-org` (company) and want its beneficial owners — returns the natural-person `name`s who ultimately own/control the entity, plus `associate` links.
url: https://rsv.fina.hr/RSV-javnost/login
category: public-records
path:
- public-records
bestFor: Identifying the beneficial owners (natural persons) behind Croatian legal entities via the official UBO register.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- associate
- employer-org
status: live
pricing: free
costNote: The data is provided free of charge, but access to the public register requires authentication through Croatia's NIAS national e-identity system — a hard gate for anyone without Croatian e-ID credentials.
opsec: passive
opsecNote: You query the official register, not the target — the subject isn't notified. However, access is via NIAS login, which ties every lookup to an authenticated (Croatian) identity; there is no anonymous access, so plan for attribution and a lawful basis (it is personal data under AML law).
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by FINA for Croatia's Ministry of Finance under the Money Laundering and Terrorist Financing Prevention Act; the beneficial-owner data is authoritative statutory filing.
missingPersonsRelevance: medium
coverage:
- hr
auth: account
api: false
localInstall: false
registration: true
aliases:
- Registar stvarnih vlasnika
- Croatia Register of Beneficial Owners
- FINA RSV
tags:
- companysites
- Company Related Sites
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Croatia (FINA Register of Beneficial Owners)

> Croatia's official Register of Beneficial Owners (Registar stvarnih vlasnika) — the natural persons who ultimately own or control Croatian legal entities.

## When to use
You have a Croatian company or legal entity (`employer-org`) and need to pierce the corporate veil to the real people behind it — the beneficial owners. Essential for association/asset mapping in Croatia: linking a subject to companies they ultimately control, or finding the humans behind an entity of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://rsv.fina.hr/RSV-javnost/login.
2. Authenticate via NIAS (Croatia's national identification/authentication system) — this requires Croatian e-ID credentials.
3. Search for the entity by name/OIB (company identifier).
4. Read the beneficial-owner records: the natural-person `name`s, their nature/percentage of ownership or control, and dates.
5. Pivot: owner names → Croatian court/company registry (sudreg) and people-search; shared owners across entities → `associate`/network mapping.

## Inputs → Outputs
- **In:** `employer-org` (Croatian entity, by name/OIB), or a `name` to check UBO links
- **Out:** beneficial-owner `name`s (natural persons), ownership/control detail, `associate`/`employer-org` links
- **Empty/negative result looks like:** no beneficial owner listed for an entity — some entity types are exempt, or the filing is incomplete/overdue. Absence isn't proof of no owner; cross-check the company registry.

## Gotchas & OpSec
- **NIAS gate:** public access needs Croatian e-ID — a real barrier for foreign investigators; you may need a Croatian collaborator or an alternative (EU BO-register interconnection, where available).
- Croatia-only; other countries have their own (often more open) UBO registers.
- Personal data under AML law — access lawfully; every lookup is authenticated/attributable.

## Overlaps ("do both")
- Pairs with the Croatian court/company registry (sudreg.pravosudje.hr) and EU beneficial-ownership resources — the company registry gives directors/filings, this gives the ultimate owners.

## Trust & verifiability
`trust: trusted` — an official statutory register; the beneficial-owner data is authoritative, with the main caveat being restricted (NIAS-gated) access.
