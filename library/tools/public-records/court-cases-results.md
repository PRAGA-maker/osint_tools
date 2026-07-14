---
id: court-cases-results
name: Court Cases Results
description: Use when you have a `name` (or offence/court) and want UK Crown Court criminal sentencing records — returns matching convictions with offence, sentence, court, and case details as document-id references.
url: https://www.thelawpages.com/court-cases/court-case-search.php
category: public-records
path:
- public-records
bestFor: Searching UK Crown Court criminal sentencing/conviction records by defendant name, offence, court, or judge.
selectorsIn:
- name
selectorsOut:
- name
- document-id
status: live
pricing: free
costNote: Free to search the criminal sentencing database on The Law Pages; no account required.
opsec: passive
opsecNote: A published legal-record database — searching it does not notify anyone and reveals only already-public court outcomes. Passive; use a sock-puppet browser if you want to avoid tying the query to yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The Law Pages is an established UK legal resource publishing Crown Court hearing lists and a daily-updated criminal sentencing database. Reliable as a secondary index; the primary record remains the court itself.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- gov-uk-court-lists
aliases:
- The Law Pages court search
- UK criminal sentencing search
tags:
- court
- inmate
- uk
- criminal-records
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Court Cases Results

> The Law Pages' UK Crown Court criminal-sentencing search: find convictions and sentences by defendant name, offence, court, or judge.

## When to use
You have a subject's `name` and want to check for UK Crown Court criminal convictions — offence, sentence/jail term, court, date, and the legal teams involved. Useful for background/risk context on a person, corroborating an identity via a documented case, or working from an offence/court angle when you don't yet have a name. The database updates daily and covers serious offences (fraud, theft, robbery, murder, sexual offences, motoring, etc.).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.thelawpages.com/court-cases/court-case-search.php.
2. Search by defendant name (or switch to offence / court / judge / legal-firm criteria).
3. Read matches: defendant, offence + legislation, sentence, court, date, and linked case detail (`document-id`).
4. Pivot: a confirmed case ties the person to a court/date and often an address area; cross-check current/upcoming matters against official Crown Court daily listings (`[[gov-uk-court-lists]]`).

## Inputs → Outputs
- **In:** `name` (or offence/court/judge)
- **Out:** confirmed `name`, case/sentence detail with a `document-id` reference (offence, sentence, court, date)
- **Empty/negative result looks like:** no match — no Crown Court sentencing record indexed for that name (many cases, especially Magistrates' Court or older/unreported ones, won't appear); absence is not proof of no record.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — public court outcomes; no subject notification.
- Name-collision risk: common names return multiple defendants — confirm via offence/date/court before attributing a conviction to your subject. This is a secondary index; treat the court record as authoritative.

## Overlaps ("do both")
- Pairs with `[[gov-uk-court-lists]]` — The Law Pages indexes past sentencing results; official court lists cover current/scheduled hearings.

## Trust & verifiability
`trust: community` — a reputable independent UK legal publisher, but a secondary aggregator. Verify any conviction against the originating court record, and disambiguate common-name matches carefully.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | court-cases-results |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
