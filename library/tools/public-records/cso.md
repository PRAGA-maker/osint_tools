---
id: cso
name: CSO
description: Use when you have a `name` and want to check British Columbia (Canada) court records for that party — returns confirmed name, case/file numbers and court-history leads.
url: https://justice.gov.bc.ca/cso/index.do
category: public-records
path:
- public-records
bestFor: Searching British Columbia court records (civil, criminal, appeal, traffic) by party name.
selectorsIn:
- name
selectorsOut:
- name
- document-id
status: live
pricing: freemium
costNote: Party-name record searches are free to view. Viewing/downloading actual court documents incurs per-document fees under the CSO Schedule of Fees; filing requires a registered account.
opsec: passive
opsecNote: Searching the registry is passive — the party is not notified. It is an official government registry that logs access; use a sock-puppet browser as good practice.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Province of British Columbia as the official electronic court registry; authoritative, though data is provided "as is" and may be subject to publication bans.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Court Services Online
- BC CSO
tags:
- court
- inmate
- canada
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# CSO

> British Columbia's official electronic court registry — search civil, criminal, appeal, and traffic records by party name to place a subject in the BC court system.

## When to use
You have a `name` for a subject with a possible British Columbia (Canada) connection and want to check for court involvement — civil suits, criminal matters, appeals, traffic. A hit confirms the person's presence in BC's justice system, yields case/file numbers (`document-id`), and can anchor location and timeline. Strong for locating or corroborating a subject who has litigated or been charged in BC.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://justice.gov.bc.ca/cso/index.do.
2. Use the free party-name search across the court types (civil, criminal, appeal, traffic).
3. Read the record list: matching parties, case/file numbers, court location, and filing history.
4. To see the underlying documents, expect per-document fees (Schedule of Fees); the free layer confirms existence and identifiers.
5. Pivot: a case number + court location anchors geography/time; confirmed BC court involvement feeds broader Canadian records and news-archive work.

## Inputs → Outputs
- **In:** `name` (party)
- **Out:** matching party `name`, case/file number (`document-id`), court location and history; full documents behind a fee
- **Empty/negative result looks like:** no matching party — meaning no BC court record under that name (or a publication ban/sealed matter), not a clean record across Canada; other provinces have separate registries.

## Gotchas & OpSec
- Scope is BC only; each Canadian province runs its own registry.
- Publication bans and sealing can hide or restrict matters; "as is" data may be incomplete.
- Same-name risk: confirm with additional identifiers before attributing a case.

## Overlaps ("do both")
- Complements `[[the-law-pages]]` (UK) and US court/inmate tools: jurisdiction-specific registries each cover their own turf, so pick the one matching your subject's location.

## Trust & verifiability
`trust: trusted` — the official BC government court registry; records are authoritative, with the standard caveats about bans, sealing, and "as is" completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cso |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
