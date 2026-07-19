---
id: boston-police-internal-affairs-cases-2010-2020
name: Boston Police Internal Affairs Cases (2010–2020)
description: Use when you have a `name` of a Boston Police officer and want their internal-affairs/disciplinary history — returns documented IA cases (2010–Aug 2020) with allegation type, outcome, and officer attributes.
url: https://apps.bostonglobe.com/graphics/2020/law-enforcement/index.html
category: public-records
path:
- public-records
bestFor: Searching Boston Police Department internal-affairs cases and disciplinary outcomes 2010–2020 by officer name or attribute.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- physical-description
status: live
pricing: free
costNote: Free public interactive database published by The Boston Globe; no account needed.
opsec: passive
opsecNote: You browse a published news database of already-public records; the officer is not notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Compiled by The Boston Globe from records obtained from the Boston Police Department; a vetted journalistic dataset covering Jan 2010–Aug 2020, not a live official registry.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Boston Globe police IA database
tags:
- police-misconduct
- public-records
- boston
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Boston Police Internal Affairs Cases (2010–2020)

> A Boston Globe interactive database of 3,100+ Boston Police internal-affairs cases (7,700+ allegations), January 2010–August 2020 — search a BPD officer by name to see their documented complaints, allegation types, and disciplinary outcomes.

## When to use
You have a `name` you believe is a Boston Police Department officer (or you're profiling BPD as an `employer-org`) and want their internal-affairs record: how many complaints, what kinds of allegations (use of force, conduct, etc.), and how each was resolved. Useful for vetting an officer named in a case, corroborating a misconduct allegation, or building context on a BPD officer connected to your subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://apps.bostonglobe.com/graphics/2020/law-enforcement/index.html.
2. Search by officer `name`, or filter by attributes — gender, race/ethnicity, rank, number of cases, awards, year, and incident type.
3. Open an officer's record to read their internal-affairs cases: allegation category, year, and disposition/outcome.
4. Corroborate against the Globe's reporting and any official BPD/oversight records, since this is a fixed 2010–2020 snapshot.
5. Pivot: an officer's rank/attributes and case detail feed people-search and news-archive lookups; the agency context feeds broader police-misconduct databases.

## Inputs → Outputs
- **In:** `name` (BPD officer) or `employer-org` (BPD)
- **Out:** `document-id` (internal-affairs cases: allegation, year, outcome) plus officer `physical-description` attributes (rank, gender, race/ethnicity)
- **Empty/negative result looks like:** no record for a name — the officer may have no IA case in the window, may not be BPD, or a name variant differs; absence isn't proof of a spotless record, only of nothing in this dataset/timeframe.

## Gotchas & OpSec
- Human-in-the-loop: none; interactive search.
- OpSec: fully **passive** — a published database of public records.
- Fixed scope: Boston PD only, Jan 2010–Aug 2020; nothing after Aug 2020 and nothing from other departments. Dispositions reflect what was recorded at publication and may have changed since.

## Overlaps ("do both")
- Pairs with the [[policecrime-bgsu-edu]] national arrest database and with local court records — this gives BPD *internal* discipline (complaints/outcomes), while those give criminal arrests and court status; together they cover both the administrative and criminal sides of an officer's record.

## Trust & verifiability
`trust: trusted` — a vetted Boston Globe dataset built from records obtained from the BPD; the figures are journalistically verified for the covered window, though it is a static snapshot, so confirm current status against official sources for anything consequential.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | boston-police-internal-affairs-cases-2010-2020 |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → document-id, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
