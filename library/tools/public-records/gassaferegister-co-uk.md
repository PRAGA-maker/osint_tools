---
id: gassaferegister-co-uk
name: gassaferegister.co.uk
description: Use when you have a UK gas engineer/business `name`, `employer-org`, or `address`/postcode and want to verify Gas Safe registration — returns registered business/engineer `name`, `employer-org`, licence number, and service `address`/area.
url: https://www.gassaferegister.co.uk/
category: public-records
path:
- public-records
bestFor: Verifying whether a UK gas engineer or business is Gas Safe registered, and finding registered businesses by area.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free public "check the register" / "find an engineer" lookup; no account or payment.
opsec: passive
opsecNote: A public professional-register search — you query the official register, nothing reaches the subject. No login; standard browser hygiene only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Gas Safe Register is the official statutory register of legally registered gas engineers/businesses in the UK; membership data is authoritative.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Gas Safe Register
- gassaferegister
tags:
- professionlicensing
- Profession & Licensing Sites
- uk-trades-register
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# gassaferegister.co.uk

> The UK's official Gas Safe Register — verify that a gas engineer or business is legally registered, or find registered businesses by area.

## When to use
You have a UK gas engineer's `name`, a business (`employer-org`), a licence number, or an `address`/postcode, and you want to confirm Gas Safe registration status — verifying a claimed trade credential, tying a person to a registered business, or finding registered engineers serving a location. It's the authoritative check for legal gas work in the UK.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gassaferegister.co.uk/.
2. Use "Check the Register" (verify a specific engineer/business by licence number, name, or business) or "Find an Engineer" (by postcode).
3. Read the result: registered business/engineer `name`, `employer-org`, licence number, the gas work types they're qualified for, and service area/`address`.
4. Pivot: the business name → UK Companies House for directors/individuals; the individual → general web/people-search; the licence status → credential verification.

## Inputs → Outputs
- **In:** `name`, `employer-org`, licence number, or `address`/postcode
- **Out:** registered `name`/`employer-org`, licence number, qualified work types, service `address`/area, registration status
- **Empty/negative result looks like:** no match — the person/business isn't Gas Safe registered (they may be working illegally, use a different name, or not be a gas engineer). Absence is meaningful here: legal gas work *requires* registration.

## Gotchas & OpSec
- UK-only, gas trade only — other trades use other registers (`[[labcfrontdoor-co-uk]]`, NICEIC for electrics).
- Search is by business/engineer/area, not primarily by an individual's personal name — pivot via the business.
- Fully passive and free; data is authoritative.

## Overlaps ("do both")
- Pairs with `[[labcfrontdoor-co-uk]]` (building competent-person register) and Companies House — Gas Safe confirms gas-trade legitimacy, the others give building credentials and the directors/individuals behind a business.

## Trust & verifiability
`trust: trusted` — the official statutory register; registration status is authoritative. A "not registered" result is itself a strong (and legally meaningful) finding.
