---
id: trellis
name: Trellis
description: Use when you have a `name` and want US state-court litigation — returns cases a person/entity is party to, with docket, court, and analytics.
url: https://trellis.law/
category: public-records
path:
- public-records
bestFor: Searching US state trial-court records by party name to find lawsuits, dockets, and judges.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- address
status: live
pricing: freemium
costNote: Free search surfaces case existence and basic docket info; full documents, alerts, and analytics require a paid subscription.
opsec: passive
opsecNote: You search a court-records aggregator, not the subject — no party is notified. Registering exposes an email to a commercial service; use a sock-puppet account for sensitive research.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial aggregator of state-court records (a layer many state courts don't expose well); case data mirrors official dockets, but coverage varies by state/county and lags the source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- trellis.law
- Trellis Research
tags:
- court-records
- litigation
- public-records
- us
source: inteltechniques-tools
lastVerified: '2026-07-18'
enrichment: full
---

# Trellis

> A search layer over US **state** trial-court records — find the lawsuits a person or business is tied up in, which state courts rarely make searchable across jurisdictions.

## When to use
You have a `name` (person or `employer-org`) and want their state-court litigation history: civil suits, family/probate matters, judgments, and the docket details around them. State courts are notoriously fragmented (per-county systems, no unified search); Trellis aggregates many of them so you can find cases by party name in one place — valuable for background, asset/associate leads, and confirming disputes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://trellis.law/ and search the party `name` (or firm/entity).
2. Review the results: matching cases with court, case number, filing date, case type, and parties.
3. Read the free docket summary; full documents/analytics/alerts prompt a paid subscription.
4. Note counterparties, attorneys, and addresses that appear in the docket.
5. Pivot: opposing parties and attorneys are `associate` leads; a case caption may reveal an `address` or business tie; pull the actual filing from the county court to confirm.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** state-court cases (court, number, type, parties), plus counterparties/attorneys (`associate`) and addresses in dockets
- **Empty/negative result looks like:** no cases — the person may have none, or (importantly) the relevant county/state isn't in Trellis's coverage; absence is not proof of a clean record.

## Gotchas & OpSec
- **Coverage is uneven** — Trellis is strong in some states/counties and thin in others; a null result can be a coverage gap, so also check the specific county court directly.
- It covers **state** courts; for federal cases use PACER/CourtListener.
- Full documents are paywalled; the free tier confirms case existence and basics.
- OpSec: passive; use a sock-puppet account if registering.

## Overlaps ("do both")
- Pairs with PACER/CourtListener (federal) and direct county-court portals — Trellis finds the state cases fast; the primary courts provide the authoritative documents to confirm.

## Trust & verifiability
`trust: community` — a commercial aggregator mirroring official dockets. Case data is generally accurate but can lag or omit jurisdictions, so verify any consequential finding against the originating court record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trellis |
