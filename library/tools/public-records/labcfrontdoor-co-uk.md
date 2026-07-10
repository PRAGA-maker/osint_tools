---
id: labcfrontdoor-co-uk
name: labcfrontdoor.co.uk
description: Use when you have a UK `address`/postcode or trade `employer-org` and want to find the registered "competent person" building tradespeople there — returns `employer-org` (business), `address`, and trade/registration status.
url: https://labcfrontdoor.co.uk/find-a-competent-person
category: public-records
path:
- public-records
bestFor: Looking up UK building tradespeople registered under a Competent Person Scheme by postcode, business name, or trade.
selectorsIn:
- address
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free public register lookup; no account or payment.
opsec: passive
opsecNote: A public professional-register search — you query LABC's directory, nothing reaches the tradesperson/subject. No login; standard browser hygiene only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by LABC (Local Authority Building Control), the body coordinating council building-control services in England & Wales; the register reflects official Competent Person Scheme membership.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- LABC FrontDoor
- Find a Competent Person
tags:
- professionlicensing
- Profession & Licensing Sites
- uk-trades-register
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# labcfrontdoor.co.uk

> LABC's public "Find a Competent Person" register — locate UK building tradespeople (electricians, gas, glazing, roofing, etc.) registered to self-certify work, by postcode or business name.

## When to use
You have a UK `address`/postcode or a trade `employer-org` and want to confirm whether a business/tradesperson is a registered "competent person" for a given trade in that area — useful for verifying a claimed trade credential, tying a business to a locality, or building the professional picture around a subject who works in the building trades.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://labcfrontdoor.co.uk/find-a-competent-person.
2. Enter a full postcode and/or a business name, and optionally filter by trade (glazing, insulation, electrics, heating, plumbing, ventilation/aircon, gas, renewables, roofing).
3. Submit and read the list of registered businesses matching the area/trade.
4. Note the business name (`employer-org`) and location (`address`).
5. Pivot: take the business name into Companies House / `[[windeed-co-za]]`-style company lookups (for UK, use Companies House) and into general web search to find the individual behind it.

## Inputs → Outputs
- **In:** `address` (postcode) and/or `employer-org` (business name), optional trade filter
- **Out:** `employer-org` (registered businesses), `address`/service area, trade + registration status
- **Empty/negative result looks like:** no registered businesses for that postcode/trade — meaning none in the Competent Person register there (they may work unregistered, or under a scheme LABC doesn't index). Absence isn't proof someone isn't a tradesperson.

## Gotchas & OpSec
- Search is by postcode/business/trade, **not** by individual person's name — pivot to company registries to get to a named individual.
- Scope is England & Wales building trades under Competent Person Schemes; other UK trades/registers are elsewhere.
- Fully passive and free.

## Overlaps ("do both")
- Pairs with UK Companies House and trade-body registers (Gas Safe, NICEIC) — LABC confirms competent-person status, the others give directors/individuals and deeper credential detail.

## Trust & verifiability
`trust: trusted` — an official LABC register, authoritative for Competent Person Scheme membership; corroborate the person-behind-the-business via company records.
