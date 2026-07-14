---
id: pacer-case-locator
name: PACER Case Locator
description: Use when you have a `name` and want to find any US federal court cases (civil, criminal, bankruptcy, appellate) a person is party to — returns case numbers (`document-id`), the court, and party details.
url: https://pcl.uscourts.gov/pcl/index.jsf
category: public-records
path:
- public-records
bestFor: A single nationwide index search across all US federal district, appellate, and bankruptcy courts for a named party.
selectorsIn:
- name
selectorsOut:
- document-id
- name
status: live
pricing: freemium
costNote: A PACER account is required. Searching the Case Locator and viewing dockets costs $0.10/page (capped at $3.00 per document); fees are waived if you accrue under $30 in a quarter, so light lookups are effectively free.
opsec: passive
opsecNote: You query the courts' system, not the subject; parties are not notified of a search. However every action is logged to your billable PACER account — use an account not tied to your true identity if attribution matters, and never file or docket anything.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US Administrative Office of the Courts; this is the authoritative federal-court index, not a third-party aggregator.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: true
localInstall: false
registration: true
aliases:
- PCL
- PACER
- Public Access to Court Electronic Records
tags:
- court
- inmate
- federal
- legal
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# PACER Case Locator

> The official nationwide index of US federal court cases — one search tells you every district, appellate, and bankruptcy court where a person appears as a party.

## When to use
You have a subject's `name` and want to know whether they are (or were) involved in US federal litigation — as a defendant, plaintiff, debtor, or in a criminal matter. A hit yields the court, case number, filing date, and party role, which then unlocks the full docket (and, for a fee, the filings themselves — often rich with addresses, employers, associates, and financial detail).

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a PACER account (free to create) and sign in at https://pcl.uscourts.gov/pcl/index.jsf.
2. Choose the case type tab (Civil, Criminal, Appellate, Bankruptcy, or All) and enter the party `name` (last, first). Narrow by court, date range, or nature-of-suit to cut noise.
3. Read the results: matched party name, case number (`document-id`), court, and dates.
4. Open a promising case to view the docket; pull individual filings only when needed (they are billed per page).
5. Pivot: docket filings expose addresses, employers, co-parties (`associate`s), and counsel; feed those into people-search and the specific court's CM/ECF.

## Inputs → Outputs
- **In:** `name` (party name; optionally SSN/last-four for bankruptcy)
- **Out:** `document-id` (case numbers), confirmed party `name`, court, role, dates; downstream: addresses/employers/associates inside filings
- **Empty/negative result looks like:** "no matching cases" — means no *federal* case indexed for that name; it says nothing about state-court matters (search those separately).

## Gotchas & OpSec
- Federal only: state and local cases are NOT here — this is a common blind spot.
- Common names produce many hits; disambiguate with court/date/nature-of-suit before attributing.
- Sealed cases and some criminal records may not appear. Charges/filings are allegations unless adjudicated.
- Everything is billed and logged to your PACER account.

## Overlaps ("do both")
- Pairs with `[[courtlistener-com]]`/RECAP (free mirror of many PACER dockets) — check RECAP first to avoid fees, then use PCL for authoritative, complete coverage. Complement with state-court portals for non-federal matters.

## Trust & verifiability
`trust: trusted` — the US courts' own system; the index is authoritative. Interpretation caveats (allegations vs. convictions, name collisions) apply, not data authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pacer-case-locator |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
