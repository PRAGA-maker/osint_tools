---
id: pacer-2
name: PACER
description: Use when you have a `name` (party, attorney, or business) and want to find US federal court cases and dockets involving them — returns name, document-id (case numbers) and associate (co-parties).
url: https://search.uscourts.gov/
category: public-records
path:
- public-records
bestFor: Authoritative US federal court case and docket search by party name across district, bankruptcy and appellate courts.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: freemium
costNote: Registration required. Searching and viewing documents costs $0.10/page (capped at $3.00 per document); fees are waived if you accrue less than ~$30 in a quarter, so light searching is effectively free.
opsec: passive
opsecNote: Official government system — searching does not notify the parties. You must register with real/billing details, so your account identity is known to the court system and queries are logged. Nothing is sent to the subject.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official electronic access system for US federal courts (PACER Case Locator); records are authoritative primary-source court data.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- Pacer
- PACER Case Locator
- PCL
tags:
- court
- federal
- records
source: inteltechniques-tools
lastVerified: '2026-07-11'
enrichment: full
---

# PACER

> The US federal judiciary's official electronic records system — search by party name to surface federal court cases, dockets, and filings.

## When to use
You have a `name` — an individual, an attorney, or a business — and want to know whether they appear in US **federal** litigation (district civil/criminal, bankruptcy, or appellate). Court dockets are a rich, authoritative source: they confirm identity, list co-parties and counsel (`associate`s), give case numbers (`document-id`), and the filings themselves can contain addresses, employment, and financial detail. This is the primary source; free aggregators of court data are downstream of it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register for a PACER account at the site (billing details required; light use is fee-free).
2. Open the PACER Case Locator (PCL) at https://search.uscourts.gov/ and search by party `name`, optionally narrowing by court type, region, and date.
3. Review the hit list of cases; open a case to see the docket, parties, counsel, and filing list.
4. Pull specific documents ($0.10/page) only when needed — read the free docket first.
5. Pivot: co-parties/counsel become `associate`s; a case number anchors deeper record pulls; filing content yields addresses/employers to feed people-search.

## Inputs → Outputs
- **In:** `name` (party / attorney / business)
- **Out:** matching case `document-id`s, party/counsel `name`s, `associate` links (co-parties)
- **Empty/negative result looks like:** no cases for the name — the person may simply have no federal litigation history (state cases are elsewhere), or the name is spelled differently; not proof of a clean record.

## Gotchas & OpSec
- **Federal only** — most everyday litigation is in state courts, which PACER does not cover. Absence here says nothing about state cases.
- Human-in-the-loop: account + billing setup, and per-page fees beyond the free threshold.
- Common names produce many hits; disambiguate with location/case type before assuming a match.

## Overlaps ("do both")
- Pairs with free federal-court aggregators (e.g. CourtListener/RECAP) — those give free access to documents others have already purchased, while PACER is the authoritative, complete, up-to-the-minute source; check the free layer first, then PACER for anything missing.

## Trust & verifiability
`trust: trusted` — the official system of record for US federal courts. Data is authoritative primary source; your only judgment calls are name disambiguation and which documents are worth the fee.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pacer-2 |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
