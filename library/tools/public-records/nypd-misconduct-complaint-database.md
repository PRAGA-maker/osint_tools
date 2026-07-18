---
id: nypd-misconduct-complaint-database
name: NYPD Misconduct Complaint Database (NYCLU)
description: Use when you have an NYPD officer `name` and want their civilian-complaint history — returns per-officer CCRB complaints, allegations, and substantiation outcomes.
url: https://www.nyclu.org/data/nypd-misconduct-database
category: public-records
path:
- public-records
bestFor: Looking up a named current/former NYPD officer's civilian misconduct-complaint record (CCRB) — incidents, allegations, and outcomes.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free public database; no account. Built from public CCRB records; underlying data also downloadable as open data.
opsec: passive
opsecNote: You search NYCLU's hosted database, not any police system — the lookup is invisible to the officer and to the NYPD. Nothing you enter is sent to a target. Standard research-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the New York Civil Liberties Union from official Civilian Complaint Review Board records obtained after the 2020 repeal of NY Civil Rights Law §50-a; methodology and raw data are published openly.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- NYCLU CCRB database
- NYPD misconduct database
tags:
- police-accountability
- public-records
- ccrb
- new-york
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# NYPD Misconduct Complaint Database (NYCLU)

> The NYCLU's searchable record of civilian misconduct complaints against NYPD officers — one row per officer, drawn from official CCRB investigation data.

## When to use
Your subject is (or is claimed to be) a current or former NYPD officer, and you want their documented civilian-complaint history. Search a `name` to see the officer's rank/status, demographic fields, and their tally of incidents, allegations, substantiated allegations, and force complaints. Useful to verify an officer's identity/service, assess a pattern of complaints, or corroborate an account involving NYPD personnel. Scope is NYPD only.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nyclu.org/data/nypd-misconduct-database and enter the officer's `name` (or browse/filter).
2. Read the officer's row: name, gender, race/ethnicity, current employment status (`employer-org` = NYPD and precinct/command where shown), and complaint counts.
3. Open the record for the breakdown — incidents, individual allegations, which the CCRB substantiated, and force allegations.
4. For the fullest/most current detail, follow through to the original CCRB source or cross-reference a companion database.
5. Pivot: a confirmed officer identity/command → other NYPD records and news; complaint patterns → context for an incident; name disambiguation via rank/command.

## Inputs → Outputs
- **In:** NYPD officer `name` (optionally narrowed by command/status)
- **Out:** officer identity fields, `employer-org` (NYPD/command), complaint/allegation counts and outcomes
- **Empty/negative result looks like:** no matching officer — the person was never named in a CCRB complaint since 2000, isn't NYPD, or the name differs from official spelling; absence is not proof of a clean record beyond CCRB's scope.

## Gotchas & OpSec
- NYPD-only and CCRB-only: it does not cover other departments or non-CCRB discipline.
- A complaint is an allegation, not a finding — distinguish filed allegations from CCRB-substantiated ones before drawing conclusions.
- Data is current only to the last update the NYCLU published; for the latest, go to the primary CCRB source.
- Fully passive and anonymous.

## Overlaps ("do both")
- Complements ProPublica's "The NYPD Files" and 50-a.org (both cover the same CCRB data with different interfaces/coverage) — cross-check an officer across them, since counts and freshness differ.

## Trust & verifiability
`trust: trusted` — an authoritative civil-liberties organization publishing official CCRB records with open methodology and downloadable source data, so any figure can be traced back to the primary complaint data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nypd-misconduct-complaint-database |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
