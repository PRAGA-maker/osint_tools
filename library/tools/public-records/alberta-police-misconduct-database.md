---
id: alberta-police-misconduct-database
name: Alberta Police Misconduct Database
description: Use when you have a `name` of an Alberta police officer and want documented misconduct history — returns named incidents, investigation outcomes and source documents.
url: https://www.policemisconductdatabase.ca/database/
category: public-records
path:
- public-records
bestFor: Searching a named Alberta police officer against ~30 years of documented misconduct incidents and their investigation outcomes.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free, publicly accessible database run by an Alberta volunteer group; no account or payment. Compiled from public records (news, disciplinary decisions, CanLII, FOI).
opsec: passive
opsecNote: You search a published public-records database; the officer is not notified and nothing ties the query to you beyond normal web hygiene. Records concern named public officials, so this is low-risk — but treat entries as sourced allegations/outcomes, not blanket guilt.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Compiled by a volunteer group of lawyers, academics and students from publicly available records (news articles, disciplinary decisions, CanLII cases, FOI documents); each entry is source-cited.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- APMD
- Police Misconduct Database Canada
tags:
- police-accountability
- public-records
- canada
- alberta
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Alberta Police Misconduct Database

> Canada's first searchable police-misconduct database — ~400+ documented Alberta incidents naming ~500 officers over three decades, each tied to public source records.

## When to use
You have the `name` of an Alberta (Canada) police officer and want to know whether there's documented misconduct history — assault, excessive force, other disciplinary matters — and how any investigation resolved. Reach for it when vetting an official connected to a case, corroborating a complaint, or researching accountability. It aggregates otherwise-scattered public records (news, disciplinary rulings, court cases, FOI releases) into one searchable place. Scope is Alberta-specific, so relevance is narrow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.policemisconductdatabase.ca/database/.
2. Search by officer `name` (or browse incidents); you can compare outcomes across similar cases.
3. Read each incident: the officer(s) named, the conduct alleged, the investigation/disciplinary outcome, and the cited source documents (`document-id`s: CanLII case, decision, article).
4. Follow the citations to the primary records to confirm details and dates.
5. Pivot: a cited court/disciplinary case feeds broader legal-records searches; the officer's `employer-org` (service/detachment) contextualises jurisdiction.

## Inputs → Outputs
- **In:** officer `name` (Alberta)
- **Out:** named misconduct incident(s), investigation outcomes, and citations (`document-id`) to source records
- **Empty/negative result looks like:** no match — the officer isn't in the database (only publicly documented Alberta cases are logged), which is NOT evidence of a clean record; absence reflects documentation gaps, not innocence.

## Gotchas & OpSec
- Alberta-only and public-record-limited: it captures only incidents that reached public documentation; much misconduct is never public, so coverage is a floor, not a census.
- Entries are sourced allegations and outcomes — read the citations; do not treat a listing as a conviction.
- Names can collide; confirm you have the right officer via the cited case details.
- OpSec: passive lookup of public officials' records.

## Overlaps ("do both")
- Pairs with CanLII/court-record searches — this database surfaces and summarises cases; those provide the full primary legal record behind each citation.

## Trust & verifiability
`trust: community` — a volunteer-compiled database, but rigorously source-cited from public records. Reliability rests on following each entry's citations to the primary document; verify there before relying on any claim.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alberta-police-misconduct-database |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
