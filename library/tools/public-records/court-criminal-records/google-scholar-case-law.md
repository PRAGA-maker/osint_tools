---
id: google-scholar-case-law
name: Google Scholar Case Law
description: Use when you have a `name` or case citation and want free full-text US court opinions that may mention a person as a party, witness, or subject — returns case opinions and citing cases.
url: https://scholar.google.com/scholar_courts
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Free full-text search of US federal and state court opinions by party name or citation.
selectorsIn:
- name
selectorsOut:
- document-id
- associate
status: live
pricing: free
costNote: Free Google service; no account needed. Full opinion text is provided at no cost, unlike paid legal databases.
opsec: passive
opsecNote: A Google search; the target is not contacted. Google logs your queries and account activity — search logged out or in a sock-puppet session, and use a VPN, to avoid tying case-law research to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Opinions are indexed from official court sources by Google; the text is authoritative, though coverage varies by jurisdiction and Scholar is not the court of record.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Google Scholar Case Law
- scholar.google.com case law
tags:
- court-records
- case-law
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Google Scholar Case Law

> Free full-text search of US court opinions — where a person's name may surface as a litigant, witness, defendant, or subject of a published decision.

## When to use
You have a subject's `name` (or a specific citation) and want to check whether they appear in published US court opinions — civil suits, criminal appeals, family/probate matters, bankruptcies referenced in opinions. Case text often reveals addresses, employers, relatives, business dealings, and a timeline of events, all corroborated in a court record. It's a free stand-in for Westlaw/LexisNexis for the opinion layer (not dockets), strong for building associate links and confirming legal history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://scholar.google.com/, then select **Case law** (or use https://scholar.google.com/scholar_courts).
2. Search the `name` in quotes; optionally restrict to federal or specific state courts via the jurisdiction selector.
3. Open matching opinions and read for identifying details — parties, counsel, dates, facts naming relatives/employers/addresses.
4. Use **"How cited"** and citing links to find related cases in the same matter or involving the same parties.
5. Pivot: named `associate`s → people-search; an employer/business → company records; a case number → the court's own docket system (PACER/state e-filing) for filings Scholar doesn't carry.

## Inputs → Outputs
- **In:** `name` or case citation
- **Out:** full-text court opinions (`document-id`), parties and related people (`associate`), citing cases
- **Empty/negative result looks like:** no opinions matching the name — the person may have no *published* opinion (most trial-court and settled matters produce none), which is NOT proof of no legal history. Check dockets separately.

## Gotchas & OpSec
- Coverage is **opinions, not dockets**: many cases (especially trial-level, dismissed, or settled) never generate a published opinion, so absence proves little. Google Scholar also lacks sealed records.
- Common names produce many false matches; confirm identity via corroborating detail before attributing a case.
- OpSec: **passive** — a Google search; the subject isn't alerted, but Google logs your activity.

## Overlaps ("do both")
- Pairs with court docket systems (PACER, state e-filing) and paid legal databases — Scholar gives the free opinion text; dockets give the filings and cases that never produced an opinion.

## Trust & verifiability
`trust: trusted` — opinion text is indexed from official court sources and is authoritative; verify coverage gaps against the issuing court, since Scholar is a search layer, not the record of record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-scholar-case-law |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
