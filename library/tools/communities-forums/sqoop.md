---
id: sqoop
name: Sqoop
description: Use when you have a `name` or `employer-org` and want US federal court, SEC, patent, and DOJ filings that mention it — returns document hits yielding `associate`, `employer-org`, and case `document-id`.
url: https://sqoop.com/
category: communities-forums
path:
- communities-forums
bestFor: One-stop searching (and alerting) across SEC filings, PACER federal court dockets, patents, and DOJ records for a person or company.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- employer-org
- associate
status: live
pricing: free
costNote: Free for journalists/researchers; requires a free account to search and set alerts.
opsec: passive
opsecNote: Searching aggregated public filings is passive and never touches the subject. You do create an account (with your email) on Sqoop itself — use a research/sock-puppet email, since your saved searches and alerts live under that account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Sqoop is an established newsroom research tool aggregating authoritative US government sources (SEC/EDGAR, PACER, USPTO, DOJ); the underlying records are official.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- sqoop.com
tags:
- toddington
- curated-directory
- news-journalism
- court-records
- sec-filings
source: toddington-resources
lastVerified: '2026-07-20'
---

# Sqoop

> A newsroom research tool that unifies SEC, PACER court, patent, and DOJ filings into one search with alerting — a fast way to find where a person or company appears in US federal records.

## When to use
You have a `name` or `employer-org` and want to know where they surface in US federal public documents — SEC/EDGAR filings, PACER federal court dockets, USPTO patents, and DOJ records — without hopping between four clunky government sites. Sqoop searches all of them at once and can email you when a new matching record appears ("Docket Watch" tracks a specific case). For missing persons, PACER/court hits and SEC filings can reveal litigation, business ties, and named `associate`s.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free Sqoop account at https://sqoop.com/ (use a research email; the site may block automated fetchers — use a browser).
2. Search the subject `name` or company across the aggregated sources.
3. Read results by source: SEC filings (officers, ownership), PACER dockets (parties, case `document-id`), patents (inventors/assignees), DOJ items.
4. Optionally save the search or set a "Docket Watch" alert to catch future filings.
5. Pivot: PACER case numbers feed court-record retrieval; SEC/patent parties feed corporate and people searches; named co-parties are `associate` leads.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** federal filings → case `document-id` (PACER), `employer-org` (SEC/patent parties), named `associate`s, filing dates
- **Empty/negative result looks like:** no filings — expected for people with no federal-court, SEC, or patent footprint; absence is weak evidence, not proof.

## Gotchas & OpSec
- Account-gated (free) — you must register; your saved searches/alerts tie to that email, so use a research account.
- Federal/US scope — it does not cover state courts or non-US records; combine with state tools.
- PACER documents themselves may cost to download at the source even though Sqoop's search/alert is free.

## Overlaps ("do both")
- Pairs with state court portals (`[[national-center-for-state-courts-united-states]]`) and corporate-registry tools — Sqoop covers the federal/SEC/patent layer; those cover state courts and company registration.

## Trust & verifiability
`trust: trusted` — aggregates authoritative US government sources; results point to official filings, so verify by opening the primary document (EDGAR/PACER/USPTO) it references.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sqoop |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → document-id, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
