---
id: case-tracker-justice-uk
name: Case Tracker for Civil Appeals – Justice UK
description: Use when you have a UK civil-appeal case number or party `name` and want its status — the official tracker returns the case title (parties), reference, and current progress/hearing dates.
url: https://casetracker.justice.gov.uk/search.jsp
category: public-records
path:
- public-records
bestFor: Checking the status and party details of a case in the Court of Appeal (Civil Division) by case number, title, or date.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- document-id
status: live
pricing: free
costNote: Free official UK court service; no account required.
opsec: passive
opsecNote: Read-only lookup of an official court tracker; parties are not notified. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by HM Courts & Tribunals Service (justice.gov.uk); authoritative for the civil-appeals cases it covers.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Civil Appeals Case Tracker
- casetracker.justice.gov.uk
tags:
- court
- inmate
- uk
- litigation
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Case Tracker for Civil Appeals – Justice UK

> The official England & Wales tracker for Court of Appeal (Civil Division) cases: confirm a case exists, who the parties are, and where it stands.

## When to use
You have a UK civil-appeal reference — a case number, a case title, or a hearing date — or a party `name` you think is involved in a Court of Appeal (Civil Division) matter, and you want to confirm and follow it. This is narrow and specific: it tracks *civil appeals*, not general county-court claims, criminal cases, or custody. Use it to verify litigation a subject is party to and monitor its progress.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://casetracker.justice.gov.uk/search.jsp.
2. Search by case number, case title (which contains the parties' `name`s), or date.
3. Read the result: the case title (parties), the reference `document-id`, and current status/hearing information.
4. Pivot: confirmed parties (`name`s) tie your subject to specific litigation and to opposing/associated parties; the case reference feeds requests for judgments/documents and press coverage.

## Inputs → Outputs
- **In:** case number (`document-id`), case title, or date — or a party `name` to match a title
- **Out:** case title (`name`s of parties), case `document-id`/reference, status and hearing dates
- **Empty/negative result looks like:** no match — the case isn't a Court of Appeal (Civil Division) matter in the tracker (wrong court/level), or the reference/spelling is off. Absence here does not mean the person has no litigation history; other courts have separate systems.

## Gotchas & OpSec
- Scope is **civil appeals only** — not county court claims, not criminal, not the general "court records" the harvested tags suggest; don't over-read a miss.
- Best when you already hold a reference or exact title; free-text name matching is limited to what appears in case titles.
- OpSec: **passive**, official, read-only.

## Overlaps ("do both")
- Pairs with `[[courtserve]]`/court-listing services and the National Archives' judgments (caselaw.nationalarchives.gov.uk) — the tracker gives live status, those give listings and full judgment text.

## Trust & verifiability
`trust: trusted` — a first-party HMCTS service; authoritative for the civil-appeals cases it tracks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | case-tracker-justice-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
