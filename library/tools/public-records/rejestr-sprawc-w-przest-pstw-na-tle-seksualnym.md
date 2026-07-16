---
id: rejestr-sprawc-w-przest-pstw-na-tle-seksualnym
name: Rejestr Sprawców Przestępstw na Tle Seksualnym
description: Use when you have a `name` of a person possibly convicted of a sexual offence in Poland and want the official public sex-offender register entry — returns `name`, `dob`, last-known locality (`address`), and photo/`physical-description`.
url: https://rps.ms.gov.pl/pl-PL/Public#/home
category: public-records
path:
- public-records
bestFor: Checking Poland's official public register of sexual-offence perpetrators for a named individual.
selectorsIn:
- name
selectorsOut:
- name
- dob
- address
- physical-description
status: live
pricing: free
costNote: The public part of the register is free and open to everyone. A separate "restricted access" register (more detail, incl. exact address) is only available to authorized entities (employers of child-facing roles, institutions) with a justified request.
opsec: passive
opsecNote: You query the official Ministry of Justice register, not the subject — no notification. The public part needs no login; the restricted register requires an authenticated, justified request that is logged. This is sensitive personal data — access and use lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Polish Ministry of Justice (Ministerstwo Sprawiedliwości); entries are authoritative court-derived records.
missingPersonsRelevance: high
coverage:
- pl
auth: none
api: false
localInstall: false
registration: false
aliases:
- Polish Sex Offender Register
- RPS
- Rejestr Sprawców Przestępstw na Tle Seksualnym
tags:
- court
- sex-offender-register
- poland
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- poland
---

# Rejestr Sprawców Przestępstw na Tle Seksualnym

> Poland's official public register of sexual-offence perpetrators — the open portion lets anyone check a named individual, with photo and last-known locality.

## When to use
You have a `name` of someone possibly convicted of a sexual offence in Poland, and you want the authoritative register entry to confirm the conviction, identity (via `dob`/photo), and last-known locality. Useful for risk assessment and identity confirmation of a Polish subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the public register at https://rps.ms.gov.pl/pl-PL/Public#/home.
2. Search the public part by `name` (surname/forename).
3. Read the entry: `name`, `dob`, photo (`physical-description`), and the locality/`address` at the level the public register discloses.
4. For fuller data (e.g. exact address), the **restricted register** requires an authorized, justified request (employers of child-facing roles, institutions) — not open to general researchers.
5. Pivot: confirmed identity/locality feeds people-search and address work in Poland; the photo can seed reverse-image/face search.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name`, `dob`, last-known locality (`address`, coarse in the public part), photo (`physical-description`)
- **Empty/negative result looks like:** no entry — the person isn't in the public register (not convicted of a qualifying offence, or in the restricted-only tier). Absence in the public part is not proof of no record.

## Gotchas & OpSec
- Two tiers: the **public** register (open, coarser data) vs the **restricted** register (detailed, authorized requesters only).
- Poland-only; other countries have their own registers (many, like the UK, are not public).
- Highly sensitive personal data — use strictly for a lawful purpose.

## Overlaps ("do both")
- Pairs with Polish court/company registries and general people-search — the register confirms offender status and identity; the others place the person and their activity.

## Trust & verifiability
`trust: trusted` — an official Ministry of Justice register derived from court records; entries are authoritative. Verify identity via `dob`/photo before acting on a name match.
