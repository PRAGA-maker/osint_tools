---
id: poland
name: Poland (CRBR – Central Register of Beneficial Owners)
description: Use when you have a Polish `employer-org` and want its beneficial owners — returns the natural-person `name`s (with partial `dob`/PESEL) who ultimately own or control the entity.
url: https://crbr.podatki.gov.pl/adcrbr/#/wyszukaj
category: public-records
path:
- public-records
bestFor: Identifying the beneficial owners (natural persons) behind Polish companies via the free, public UBO register.
selectorsIn:
- employer-org
selectorsOut:
- name
- associate
- employer-org
status: live
pricing: free
costNote: Completely free and public — no account, no fee, no e-ID gate. You search by the company's NIP (tax ID).
opsec: passive
opsecNote: You query the official register, not the subject — no notification, and no login is required, so the lookup is effectively anonymous. It is personal data (names, partial PESEL/DOB), so use it for a lawful purpose.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Polish Ministry of Finance beneficial-ownership register (CRBR), maintained under EU AML rules; the data is authoritative statutory filing.
missingPersonsRelevance: medium
coverage:
- pl
auth: none
api: true
localInstall: false
registration: false
aliases:
- CRBR
- Centralny Rejestr Beneficjentów Rzeczywistych
- Poland Register of Beneficial Owners
tags:
- companysites
- Company Related Sites
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Poland (CRBR – Central Register of Beneficial Owners)

> Poland's free, public Register of Beneficial Owners — search a company's tax ID and get the natural persons who ultimately own or control it.

## When to use
You have a Polish company (`employer-org`) and want to pierce to the real people behind it — its beneficial owners. Unlike many countries' UBO registers, Poland's CRBR is fully open and free with no e-ID barrier, making it one of the most accessible ways to link a subject to Polish entities they control (or find the humans behind a company of interest).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://crbr.podatki.gov.pl/adcrbr/#/wyszukaj.
2. Enter the company's **NIP** (Polish tax identification number) — the primary search key.
3. Read the beneficial-owner records: natural-person `name`s, their citizenship, partial PESEL/`dob`, and the nature/extent of their ownership or control.
4. Pivot: owner names → the KRS court register (krs-online / Ministry of Justice) for directorships, and people-search; shared owners across NIPs → `associate`/network mapping.

## Inputs → Outputs
- **In:** `employer-org` identified by NIP (Polish tax ID)
- **Out:** beneficial-owner `name`s (natural persons), citizenship, partial identifiers, ownership/control detail, `associate`/`employer-org` links
- **Empty/negative result looks like:** no beneficial owner for a NIP — the entity may be exempt, newly registered, or non-compliant. You usually need the exact NIP; a name alone won't search here. Cross-check the KRS register.

## Gotchas & OpSec
- **NIP-keyed** — you generally search by the company's tax ID, so get the NIP first (from KRS or invoices/filings).
- Poland-only; other countries' UBO registers differ (some gated, like `[[croatia]]`).
- Personal data — lawful purpose required, though access is anonymous.

## Overlaps ("do both")
- Pairs with the Polish KRS court/company register and `[[b2bhint-com]]` — KRS/B2BHint give the company and directors (and the NIP you need); CRBR gives the ultimate beneficial owners.

## Trust & verifiability
`trust: trusted` — an official statutory UBO register; the data is authoritative. Confirm the NIP maps to the intended entity, and note owners can still be layered through foreign structures.
