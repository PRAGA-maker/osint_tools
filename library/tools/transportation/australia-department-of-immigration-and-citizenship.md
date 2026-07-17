---
id: australia-department-of-immigration-and-citizenship
name: Australia Department of Home Affairs (Immigration & Citizenship)
description: Use when you need official Australian immigration/citizenship/visa reference or the VEVO visa-check entry point — an authoritative reference portal (consent-gated for personal lookups).
url: https://immi.homeaffairs.gov.au
category: transportation
path:
- transportation
bestFor: Official reference on Australian visas, citizenship, and border processes, and the entry point to VEVO visa-status checks (which require the visa holder's details/consent).
selectorsIn:
- name
- document-id
selectorsOut: []
status: live
pricing: free
costNote: Free official government portal; general information is open. VEVO visa checks require the person's passport/visa details.
opsec: passive
opsecNote: Reading the public portal is passive. A VEVO status check requires the visa holder's own identifiers and is intended for the holder or an authorised party (e.g. an employer with consent) — it is not a covert person-search and should only be used lawfully with proper authority.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Australian Government Department of Home Affairs; authoritative for immigration/citizenship/visa information and status.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Australia Home Affairs
- immi.homeaffairs.gov.au
- Department of Immigration
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Australia Department of Home Affairs (Immigration & Citizenship)

> The Australian Government's official immigration and citizenship portal — the authoritative reference for visa/border/citizenship processes and the front door to VEVO visa-status verification.

## When to use
Use it as a reference, not a covert lookup. When an investigation touches Australian immigration — understanding a visa type or its conditions, citizenship/residency processes, border and travel rules, or official forms — this is the primary, authoritative source. It also hosts VEVO (Visa Entitlement Verification Online); a VEVO check confirms a visa's status but requires the holder's own identifiers and is meant for the holder or an authorised party, so it's not a way to search for a person from a bare name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://immi.homeaffairs.gov.au for official information on visas, citizenship, and travel.
2. For a status check, go to VEVO — you must supply the visa holder's passport/visa details (document number, DOB, etc.), which you can only lawfully use with authority/consent.
3. Read official conditions, definitions, and processing information relevant to your case.
4. Pivot: understanding a visa's conditions informs what a subject can/can't lawfully do; formal record requests go through proper channels (FOI / law-enforcement liaison), not this portal.

## Inputs → Outputs
- **In:** `name`/`document-id` only in the sense of official reference; VEVO needs the holder's passport/visa identifiers.
- **Out:** authoritative reference information (and, via VEVO with proper inputs/authority, a visa-status confirmation). No open person-search output.
- **Empty/negative result looks like:** the portal has no public "search a person" function — expecting one is a misuse; without the holder's identifiers and authority, VEVO returns nothing.

## Gotchas & OpSec
- Not a person-search: there is no public lookup of individuals by name here — it's reference + a consent-gated status check.
- Legal-gate: VEVO and any personal record access are governed by Australian law; use only with proper authority.
- OpSec: reading is passive; do not attempt to query personal visa data without lawful basis.

## Overlaps ("do both")
- Complements formal legal channels (FOI, law-enforcement liaison) and Australian public registers — this portal explains the rules and confirms visa status with consent; substantive personal records come through authorised process.

## Trust & verifiability
`trust: trusted` — the official Australian government department; its information and VEVO status checks are authoritative, within the legal limits on personal-data access.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | australia-department-of-immigration-and-citizenship |
| category | transportation |
| selectorsIn → selectorsOut | name, document-id → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
