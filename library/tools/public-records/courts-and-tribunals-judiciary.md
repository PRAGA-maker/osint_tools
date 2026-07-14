---
id: courts-and-tribunals-judiciary
name: Courts and Tribunals Judiciary
description: Use when you have a `name` and want to find UK court/tribunal judgments naming them — returns published judgments, sentencing remarks and orders (party names, facts, dates).
url: https://www.judiciary.uk/judgments
category: public-records
path:
- public-records
bestFor: Finding published England & Wales court and tribunal judgments that name a person as a party, defendant or subject.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: free
costNote: Free official archive; no account. Links onward to the National Archives Find Case Law database (also free).
opsec: passive
opsecNote: Fully passive — searching a public judgments archive is anonymous and not attributed to the subject. It surfaces only what a court published (which can itself be sensitive), so handle the retrieved detail carefully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official judiciary of England & Wales archive — authoritative primary-source judgments; note anonymised judgments deliberately withhold names, and not every case is published.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- find-case-law-nationalarchives
- bailii
aliases:
- judiciary.uk judgments
- Courts and Tribunals Judiciary
tags:
- court
- judgments
- legal
- uk
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Courts and Tribunals Judiciary

> The official England & Wales judgments archive — search published court and tribunal decisions, sentencing remarks and orders by name or keyword.

## When to use
You have a `name` and want to know whether the person appears in UK court proceedings — as a party, defendant, claimant, or subject of sentencing remarks. Published judgments can reveal a person's legal disputes, criminal sentencing, financial/family matters, business conduct, and named associates (co-parties, family members in family cases). A strong, authoritative check when building a picture of someone's legal history in England & Wales.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.judiciary.uk/judgments.
2. Enter the person's `name` as a keyword; refine with judgment type (judgment, sentencing remarks, order), subject area/court, and date range.
3. Sort by relevance or date and open matching judgments — read the full text for the named parties, facts, dates and outcome.
4. For deeper/older case law, follow the link to the National Archives "Find Case Law" database.
5. Pivot: named co-parties/family feed `associate` mapping; a case citation (`document-id`) feeds fuller retrieval; facts (addresses, employers, dates) feed further OSINT.

## Inputs → Outputs
- **In:** `name` (or case keyword)
- **Out:** published judgment(s) → party `name`s, case citation/`document-id`, `associate`s, dates, facts and outcome
- **Empty/negative result looks like:** no matching judgment — meaning nothing *published under a searchable name*. Many cases are unpublished, settled, in lower courts, or **anonymised** (names replaced by initials, common in family/vulnerable-party cases), so absence is not proof of no litigation.

## Gotchas & OpSec
- Anonymisation: family and some sensitive judgments deliberately hide names — a null result there is expected.
- Coverage is selective: not every hearing produces a published judgment; lower-court/magistrates' matters are largely absent.
- Passive and free, but the content itself can be sensitive personal data — handle accordingly.

## Overlaps ("do both")
- Pairs with `[[find-case-law-nationalarchives]]` (the National Archives Find Case Law service, broader/structured) and `[[bailii]]` (long-running free case-law database) — run all three, as each indexes and retains different judgments.

## Trust & verifiability
`trust: trusted` — the official judiciary archive, i.e. primary-source judgments. Reliable for what it contains; just remember it is selective and sometimes anonymised, so it under-reports rather than over-reports.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | courts-and-tribunals-judiciary |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
