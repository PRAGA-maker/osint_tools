---
id: find-a-prisoner
name: Find a prisoner (gov.uk)
description: Use when you have a `name` and believe someone is in prison in England or Wales but don't know which one — a request service (not a public database) — returns which prison holds them, by post, with the prisoner's consent.
url: https://www.gov.uk/find-prisoner
category: public-records
path:
- public-records
bestFor: Locating which English/Welsh prison holds a named person via the official HMPPS request service.
selectorsIn:
- name
selectorsOut:
- address
status: live
pricing: free
costNote: Free government service. Not instant and not public — you submit a request and HMPPS replies by post within ~4 weeks, and only shares the prison if the prisoner consents.
opsec: active
opsecNote: This is a request to a government body, not an anonymous database query. You must give your own details, and the prisoner is asked for permission before information is shared — so both you and your interest become known. Use only with a genuine, lawful reason.
humanInLoop: true
humanInLoopReason:
- manual-review
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official gov.uk / HMPPS service; authoritative, but access is gated (manual review + prisoner consent), so it is not an open OSINT lookup.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Find a prisoner
- HMPPS prisoner location service
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Find a prisoner (gov.uk)

> The official England & Wales service to find out which prison holds someone — a consent-gated request handled by post, not a public inmate database.

## When to use
You have a `name` and believe the person is imprisoned in England or Wales but don't know where — for example, to explain a missing adult's whereabouts or to contact them. Unlike US inmate locators, the UK has no public search; this is the sanctioned route, but it depends on the prisoner's consent and a manual reply.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.uk/find-prisoner and read who may use it (the public route; solicitors must email directly and confirm the prisoner is their client).
2. Submit the prisoner's `name` (and aliases), `dob`/age if known, and prisoner number if you have it — plus your own details and reason.
3. HMPPS reviews the request and asks the prisoner for permission.
4. If consented, you receive — by post, within ~4 weeks — the prison holding them.
5. Pivot: with the prison known, you can arrange correspondence/visits per prison rules.

## Inputs → Outputs
- **In:** `name` (+ aliases, `dob`/age, prisoner number if known)
- **Out:** which English/Welsh prison holds the person (an `address`), by post — only with the prisoner's consent
- **Empty/negative result looks like:** no location shared — the person may not be in an English/Welsh prison, or (crucially) declined to consent. A non-answer is not proof they aren't imprisoned.

## Gotchas & OpSec
- **Not a database, not instant** — manual review, ~4-week postal reply, and the prisoner can refuse.
- England & Wales only — Scotland (SPS) and Northern Ireland differ.
- You must identify yourself and give a reason; use lawfully.

## Overlaps ("do both")
- Pairs with US/other DOC locators (`[[idaho]]`, `[[florida-probation-search]]`, federal BOP) for non-UK jurisdictions — those are instant/public, this is consent-gated. For UK court context, cross-check court listings/news.

## Trust & verifiability
`trust: trusted` — an official HMPPS service; authoritative but access-gated. Treat a non-response as inconclusive rather than negative.
