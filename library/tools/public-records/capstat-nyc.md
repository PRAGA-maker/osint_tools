---
id: capstat-nyc
name: CAPstat.nyc
description: Use when you have a `name` of a New York City police officer (or a lawsuit plaintiff) and want to find their command/precinct history and co-defendants — returns employer-org, associate, and case document-ids.
url: https://www.capstat.nyc/
category: public-records
path:
- public-records
bestFor: Tying an NYPD officer's name to their command/precinct assignments and to the federal civil-rights lawsuits naming them.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
- document-id
status: live
pricing: free
costNote: Free public database published by the Legal Aid Society; no account or payment required.
opsec: passive
opsecNote: Queries hit a third-party public site, not the subject. Nothing is sent to the person being researched. Searches may be logged by the host; use a clean browser/IP if you want to avoid linking the query to your normal browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by the Legal Aid Society's Cop Accountability Project (CAP) from filed federal court records; primary-source, not a scraped aggregator.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CAPstat
- Cop Accountability Project database
- Law Enforcement Lookup
- LELU
tags:
- police-accountability
- court-records
- nypd
- public-records
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# CAPstat.nyc

> The Legal Aid Society's searchable index of federal civil-rights lawsuits against NYPD officers — turns an officer's name into their command history and the cases naming them.

## When to use
You have a `name` you believe belongs to an NYPD officer (or to someone who sued the NYPD) and you want to establish where that officer worked, which precincts/commands they were assigned to, and who else was named alongside them. Useful when a subject in a missing-persons or misconduct context is a New York City police officer, or when corroborating a person's claimed law-enforcement employment in NYC between 2015 and mid-2018 (the core data window).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.capstat.nyc/ and go to the **Search** page (`/search/`).
2. Enter the `name` of the officer-defendant or the plaintiff. You can also browse by **command/precinct** to enumerate officers tied to a station.
3. Read the record: each hit lists the lawsuit(s), the officer-defendants (often several per case), the plaintiff, the command(s) the officer served in, the allegation type, and settlement/disposition details where known.
4. Pivot: a confirmed command feeds NYC-payroll or pension lookups to corroborate employment; co-defendant names are `associate` leads; the case caption/docket is a `document-id` you can pull in PACER or CourtListener.

## Inputs → Outputs
- **In:** `name` (officer or plaintiff), optionally a precinct/command
- **Out:** `employer-org` (NYPD command/precinct assignments), `associate` (co-defendant officers, plaintiffs), `document-id` (case captions/dockets)
- **Empty/negative result looks like:** no matching officer or lawsuit — this only covers officers named in federal civil-rights suits filed roughly 2015–June 2018, so absence means "not in this dataset," not "no such officer."

## Gotchas & OpSec
- Human-in-the-loop: none; no login or captcha for search.
- Coverage is bounded in time (federal filings ~2015 to mid-2018) and jurisdiction (Eastern and Southern Districts of New York). The project has since been expanded/rebranded as **Law Enforcement Lookup (LELU)** with broader misconduct data — check there for newer records.
- OpSec: passive. You are reading court-derived public data; nothing reaches the subject.

## Overlaps ("do both")
- Complements PACER/CourtListener federal-docket search — CAPstat pre-indexes and structures the NYPD suits so you find the officer fast, then the docket tools give you the full filings.

## Trust & verifiability
`trust: trusted` — assembled by the Legal Aid Society from actual federal court filings, so entries trace back to primary documents. Data quality is high within its stated window; its main limitation is scope, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | capstat-nyc |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, associate, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
