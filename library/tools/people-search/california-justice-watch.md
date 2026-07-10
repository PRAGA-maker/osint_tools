---
id: california-justice-watch
name: California Justice Watch
description: Use when you have a `name` for a California DA, judge, or police officer and want documented misconduct/accountability records — returns case histories, disciplinary/decertification data and associated parties.
url: https://cajusticewatch.com
category: people-search
path:
- people-search
bestFor: Vetting a named California prosecutor, judge, or law-enforcement officer for documented misconduct, or pulling accountability data on a case.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
- document-id
status: live
pricing: free
costNote: Free public-interest project; nothing to sign up for, no payment.
opsec: passive
opsecNote: Read-only browsing of an aggregated public-records accountability database. You are not contacting anyone; nothing about your subject is transmitted. Use a clean session for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A nonpartisan accountability project aggregating public records (POST decertification, Brady lists, court filings); source data is public but the grading/commentary is the project's editorial judgment.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- california
aliases:
- CA Justice Watch
- cajusticewatch
tags:
- people-investigations
- accountability
- police-misconduct
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# California Justice Watch

> A nonpartisan California criminal-justice accountability database — case-level records on prosecutors, judges, and officers built from public records.

## When to use
You have a `name` tied to California's justice system — a district attorney, judge, or police officer — and you want documented context: misconduct findings, use-of-force incidents, POST decertification, Brady-list status, or the parties and settlements in a specific case. Useful for vetting an official who appears in a case, corroborating claims about a wrongful conviction, or mapping the people connected to an incident. Less about locating a private individual than characterizing officials and cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cajusticewatch.com.
2. Browse by the relevant entity type — cases, district attorneys (all 58 counties graded), judges, officers, counties, or witnesses — and search the `name`.
3. Read the record: case breakdowns with timelines, evidence summaries, settlement amounts, disciplinary/decertification data (`document-id`), and the key players involved (`associate`, `employer-org`).
4. Pivot: an officer's agency (`employer-org`) or a linked case feeds court-record and news searches; a confirmed name feeds people-search.

## Inputs → Outputs
- **In:** `name` (DA, judge, officer) or a case identifier
- **Out:** `employer-org` (agency/office), `associate` (co-parties), `document-id` (decertification/Brady references), case timelines and settlement data
- **Empty/negative result looks like:** no tracked record for that name — the project covers a curated set (100+ cases, 174+ officers, top-100 judges), so absence means "not in this dataset," not "no misconduct."

## Gotchas & OpSec
- Coverage is curated/California-only, not exhaustive; absence is not exculpatory and presence reflects the project's editorial grading.
- Best for officials and cases, not for locating a missing private person directly.
- OpSec: **passive** — a public-records read.

## Overlaps ("do both")
- Pairs with `[[california]]` (CDCR inmate locator) and county court-record tools — this characterizes the officials/cases while custody and court dockets give the primary records.

## Trust & verifiability
`trust: community` — aggregates authoritative public records, but the scoring and framing are the project's; always trace a finding back to the underlying court/POST record before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | california-justice-watch |
| category | people-search |
| selectorsIn → selectorsOut | name → employer-org, associate, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
