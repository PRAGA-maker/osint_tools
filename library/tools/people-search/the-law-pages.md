---
id: the-law-pages
name: The Law Pages
description: Use when you have a `name` and want to check whether that person appears in England & Wales Crown Court criminal sentencing records — returns confirmed name, court/case details and a case reference.
url: https://www.thelawpages.com/court-cases/court-case-search.php?mode=1
category: people-search
path:
- people-search
bestFor: Searching UK (England & Wales) criminal court sentencing records by defendant name.
selectorsIn:
- name
selectorsOut:
- name
- document-id
status: live
pricing: free
costNote: The court-case sentencing search is free to use with no account.
opsec: passive
opsecNote: You are searching a public court-records database; the defendant is not notified and nothing touches the subject's own accounts. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running commercial UK legal-directory site compiling Crown Court listings and sentencing results; sourced from public court data but not an official government register, so confirm significant findings against primary court records.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- thelawpages.com
- The Law Pages court case search
tags:
- bellingcat-toolkit
- people
- court-records
source: bellingcat-toolkit
lastVerified: '2026-07-14'
enrichment: full
---

# The Law Pages

> A free, daily-updated database of England & Wales Crown Court sentencing results, searchable by defendant — turning a name into criminal-court case detail.

## When to use
You have a `name` for a UK subject and want to know whether they appear in Crown Court criminal sentencing records — the offence, sentence, court, and hearing detail. Valuable for background, risk, and locating context (a court venue is a geographic/time anchor), and a strong disambiguator when a common name resolves to a specific documented case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the court-case search at https://www.thelawpages.com/court-cases/court-case-search.php.
2. Search by defendant `name`; you can also pivot by offence, court, judge, solicitor firm, or barrister to narrow or corroborate.
3. Read a matched case: defendant name, offence and legislation, sentence/result, court, and hearing date — plus the case's own reference/detail page (`document-id`).
4. Confirm identity carefully — match on more than the name (age, location, co-defendants, dates) before attributing a case to your subject.
5. Pivot: the court/venue and date anchor a timeline; co-defendants are `associate` leads; a confirmed case feeds news-archive searches for fuller reporting.

## Inputs → Outputs
- **In:** `name` (optionally offence / court / legal-team filters)
- **Out:** confirmed defendant `name`, case reference (`document-id`), offence, sentence, court and hearing detail
- **Empty/negative result looks like:** no matching case — which means no *Crown Court sentencing record indexed here*, not a clean record generally (magistrates' matters, other jurisdictions, and unindexed cases won't appear). Coverage is England & Wales.

## Gotchas & OpSec
- Same-name risk: verify with corroborating detail before attributing a criminal case to an individual — misattribution here is defamatory and investigation-ending.
- Not an official register: it compiles public court output; for anything consequential, confirm against the actual court record.
- Scope: England & Wales Crown Court; Scotland/Northern Ireland and lower courts fall outside it.

## Overlaps ("do both")
- Pairs with `[[find-people-search-us]]`-style people-search only loosely (different countries); within the UK, corroborate a hit with news archives and official court listings rather than a single source.

## Trust & verifiability
`trust: community` — a reputable, long-standing commercial compiler of public UK court data (listed in the Bellingcat toolkit), but not the primary source; treat hits as strong leads to confirm against the court record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-law-pages |
| category | people-search |
| selectorsIn → selectorsOut | name → name, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
