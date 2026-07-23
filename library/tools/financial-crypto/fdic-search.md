---
id: fdic-search
name: FDIC BankFind Suite
description: Use when you have a bank name (`employer-org`) and want authoritative US regulatory details — charter, headquarters `address`, branches, history and status — returns official institution records.
url: https://banks.data.fdic.gov/bankfind-suite/bankfind
category: financial-crypto
path:
- financial-crypto
bestFor: Authoritative lookup of any FDIC-insured US bank's official name, address, branches, charter and history.
selectorsIn:
- employer-org
- name
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free official US government service (FDIC); an open API is also provided at no cost.
opsec: passive
opsecNote: Fully passive — querying a public federal database of institutions. No target is contacted and nothing is logged against your subject. This covers institutions, not individual account holders.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party US Federal Deposit Insurance Corporation data — the authoritative record for FDIC-insured banks.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- FDIC BankFind
- BankFind Suite
tags:
- banking
- public-records
- financial
- us-government
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# FDIC BankFind Suite

> The FDIC's official directory of insured US banks — authoritative name, headquarters, branches, charter and history for any institution.

## When to use
You have the name of a US bank (`employer-org`) — perhaps a subject's stated employer, or an institution named in documents — and need to confirm it's a real, FDIC-insured bank and pull its official details: legal name, headquarters `address`, branch locations, regulator, charter/establishment date, and whether it's active, merged, or failed. Institution-level intelligence, not account-holder data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://banks.data.fdic.gov/bankfind-suite/bankfind.
2. Search by bank `name`, city, or FDIC certificate number.
3. Open the matching institution to see official name, HQ `address`, class/regulator, establishment date, and status (active/merged/failed).
4. Use the Locations/Branches view to map its physical footprint.
5. For bulk/automated work, hit the free FDIC API (banks.data.fdic.gov) instead of the UI.

## Inputs → Outputs
- **In:** bank `name`/`employer-org` (or city, or FDIC cert #)
- **Out:** official institution name, headquarters `address`, branch addresses, regulator/charter, establishment date, status
- **Empty/negative result looks like:** no match — the entity may not be an FDIC-insured bank (e.g. a credit union, fintech, or non-US institution), which is itself a useful finding.

## Gotchas & OpSec
- Covers FDIC-insured banks only — credit unions (see NCUA) and non-US banks won't appear.
- Historical entities show as merged/inactive with successor info; read status carefully.
- Institution data only — it does not expose individual customers or accounts.

## Overlaps ("do both")
- Pairs with NCUA (credit unions) and SEC/EDGAR (public-company filings) — use FDIC to authoritatively confirm a bank, then those for related financial entities.

## Trust & verifiability
`trust: trusted` — first-party FDIC data, the authoritative US source for insured-bank records; safe to cite directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fdic-search |
