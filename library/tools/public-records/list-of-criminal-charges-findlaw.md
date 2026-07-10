---
id: list-of-criminal-charges-findlaw
name: List of Criminal Charges - FindLaw
description: Use when you have a charge or offense name from a court/arrest record and want to understand what it means — returns plain-English legal definitions, felony/misdemeanor class and typical penalties (reference, not a records search).
url: https://www.findlaw.com/criminal/criminal-charges/view-all-criminal-charges.html
category: public-records
path:
- public-records
bestFor: Interpreting the charges and offense terms that appear on court, arrest and inmate records.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free educational legal-reference content published by FindLaw (Thomson Reuters); no account or payment.
opsec: passive
opsecNote: This is a static public reference article — reading it reveals nothing about any subject and touches no target infrastructure. No sock puppet needed beyond normal browsing hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by FindLaw (a Thomson Reuters legal-information brand); authoritative for US legal definitions, though general educational content rather than jurisdiction-specific statute.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- FindLaw criminal charges list
- View All Criminal Charges
tags:
- court
- inmate
- legal-reference
- criminal-charges
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# List of Criminal Charges - FindLaw

> A plain-English glossary of US criminal charges — the decoder ring for the offense terms you pull off court, arrest and inmate records, not a database of people.

## When to use
You have already found a subject on a court docket, arrest log, or inmate roster and are staring at a charge you do not understand ("aggravated assault," "wire fraud," "felony menacing," a statute label). Use this page to learn what the offense actually is, whether it is a felony or misdemeanor, and the typical penalties — context that tells you how serious a record is and what related records (bail, sentencing, appeals, incarceration) might exist to pivot into.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.findlaw.com/criminal/criminal-charges/view-all-criminal-charges.html.
2. Scan the A–Z list (~60+ common offenses) or Ctrl-F for the charge term from your record.
3. Follow the link to that offense's article for the definition, felony/misdemeanor classification, elements, and typical sentencing range.
4. Apply it: use the classification to gauge severity and to predict what downstream records exist (e.g. a felony implies a case file, possible incarceration → inmate locators).
5. Pivot: the interpreted charge sends you back to the actual records source — county court portals, inmate locators — armed with the right terms to search.

## Inputs → Outputs
- **In:** a charge/offense name (from a record you already have) — not a person selector
- **Out:** legal definition, felony vs. misdemeanor class, typical penalties (knowledge, not data about a subject)
- **Empty/negative result looks like:** the specific charge/statute is not in the list — FindLaw covers common offenses generally; obscure or state-specific statute codes may not appear, so consult that state's statutes directly.

## Gotchas & OpSec
- **Not a people-search.** This page contains no searchable records of any individual's arrests or convictions — do not expect to enter a `name` and get a rap sheet. It is purely reference/education.
- Definitions are general US legal information; the exact elements and penalties vary by state statute, so treat it as orientation, not the controlling law.
- OpSec: **passive**, zero-signal — it is a static article.

## Overlaps ("do both")
- Pairs with actual criminal-records sources (county court portals, state inmate locators, `[[polk-court-records]]`) — those find the person and the charge string; this explains what the charge means. Do both: find the record, then decode it here.

## Trust & verifiability
`trust: trusted` — authored by FindLaw/Thomson Reuters, a reputable legal publisher. Reliable as general legal education; for a specific case always confirm the charge against the governing state statute and the court record itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | list-of-criminal-charges-findlaw |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
