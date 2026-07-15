---
id: gla-gov-uk
name: GLAA Public Register (gla.gov.uk)
description: Use when you have a UK labour provider/gangmaster `name`, business or `address` and want to confirm their licence — returns the licensed business, its address, authorised sectors and licence status.
url: https://glass.gla.gov.uk/public/s/
category: public-records
path:
- public-records
bestFor: Confirming whether a UK labour provider (gangmaster) is licensed and pulling the licensed business's details and authorised sectors.
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
costNote: Free official public register run by the GLAA; no account or payment needed for basic register checks.
opsec: passive
opsecNote: Official government register lookup; you query the register, not any individual, and no notification is sent. No login required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Gangmasters and Labour Abuse Authority (GLAA), a UK government body; the register is the authoritative record of who holds a gangmaster's licence.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- GLAA Public Register
- Gangmasters and Labour Abuse Authority
- glass.gla.gov.uk
tags:
- professionlicensing
- Profession & Licensing Sites
- licensing-register
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# GLAA Public Register (gla.gov.uk)

> The UK Gangmasters and Labour Abuse Authority's official register: confirm whether a labour provider is licensed and see the business behind it, its address and authorised sectors.

## When to use
You have a UK labour-provider/gangmaster business `name`, a unique reference number (URN), or a business `address`/location and want to confirm the licence and pull the registered business detail. This matters when a subject is tied to labour supply (agriculture, food processing, shellfish, care) — the register links a person/business to a licensed entity, a business `address`, and authorised sectors, and confirms whether the licence is current, applied-for, or revoked.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Public Register at https://glass.gla.gov.uk/public/s/.
2. Search by business `name`, URN, or business location. Use the "Advanced Public Register Search" to filter by country of location and countries supplied to.
3. Select the licence to view details: registered business/`employer-org`, contact `address`, authorised sectors, and licence date/status.
4. Read status carefully: "licensed", "application in progress", "revoked", or absent all mean different things for a due-diligence conclusion.
5. Pivot: the business name feeds Companies House for directors/officers; the address feeds mapping; a revoked/absent licence is itself a red-flag lead.

## Inputs → Outputs
- **In:** business `name` / URN / `address`-location (`employer-org`)
- **Out:** licensed `employer-org`, business `address`, authorised sectors, licence status/date
- **Empty/negative result looks like:** no matching record — meaning the provider isn't licensed (an offence to use, and a red flag), not merely "not found"; the GLAA helpline can confirm a negative.

## Gotchas & OpSec
- Human-in-the-loop: none — open official register.
- Scope: covers GLAA-regulated labour sectors only; a business outside those sectors legitimately won't appear, so absence isn't automatically suspicious outside regulated sectors.
- OpSec: fully passive; a government register lookup that never touches the subject.

## Overlaps ("do both")
- Pairs with UK Companies House and company-registry tools — the GLAA confirms the labour licence and sectors; Companies House ties the business to its directors and current status.

## Trust & verifiability
`trust: trusted` — the GLAA is a UK government authority and this is its statutory public register, so licence status is authoritative; corroborate the business's people/ownership via Companies House.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gla-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
