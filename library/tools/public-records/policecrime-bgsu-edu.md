---
id: policecrime-bgsu-edu
name: Henry A. Wallace Police Crime Database
description: Use when you have a `name`, agency, or location and want to check whether a U.S. law-enforcement officer was arrested/charged with a crime — returns documented officer arrest cases (2005–2021) with agency, charge, and outcome.
url: https://policecrime.bgsu.edu/
category: public-records
path:
- public-records
bestFor: Checking whether a named U.S. police officer (or an officer at a given agency/location) has a documented criminal arrest 2005–2021.
selectorsIn:
- name
- employer-org
- geolocation
selectorsOut:
- document-id
- employer-org
status: live
pricing: free
costNote: Free academic research database (Bowling Green State University); no account required.
opsec: passive
opsecNote: You search an academic database compiled from public news and court records; nothing reaches the officer or their agency. Fully safe to use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by criminologist Philip M. Stinson at BGSU from public arrest/court records and news reports; peer-referenced and widely cited, though it covers only arrests that became public (2005–2021) and is not a complete misconduct registry.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Police Crime Database
- Stinson police crime database
- policecrime.bgsu.edu
tags:
- police-misconduct
- public-records
- criminal-records
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Henry A. Wallace Police Crime Database

> A research database of 20,000+ documented criminal-arrest cases involving U.S. non-federal sworn law-enforcement officers (2005–2021) — the go-to source for checking whether a named officer, or an officer at a given agency, has a public criminal case.

## When to use
You have a `name` you believe is (or was) a U.S. police officer, or you want to profile an `employer-org` (a police department) or a `geolocation` (county/state), and you need to know whether officers there have documented criminal arrests. Useful when vetting an officer named in a case, checking an agency's integrity record, or corroborating an allegation of police misconduct with a documented arrest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://policecrime.bgsu.edu/.
2. Use the search options — by location (state/county/agency), by crime type, and by victim category — to filter cases.
3. Review returned cases: each documents the officer, agency, the criminal charge(s), the year, and (where known) the case outcome/conviction.
4. Cross-check a specific officer against the local court record or news report cited, since the database aggregates from those public sources.
5. Pivot: an agency and charge feed local court-record and news searches; a confirmed officer identity feeds people-search tools.

## Inputs → Outputs
- **In:** `name` (officer), `employer-org` (agency), or `geolocation` (state/county)
- **Out:** `document-id` (documented arrest cases: charge, year, outcome) and the associated `employer-org` (agency)
- **Empty/negative result looks like:** no cases for that officer/agency/area — this means no *publicly documented arrest 2005–2021 in the dataset*, not that no misconduct occurred; the database captures arrests that became public within its window.

## Gotchas & OpSec
- Human-in-the-loop: none; direct search.
- OpSec: fully **passive** — an academic archive of already-public records; the officer/agency is not notified.
- Scope limits: coverage is 2005–2021 and only *arrests* that became public (not internal discipline or unreported conduct); a clean result is not proof of a clean record. Verify each case against its underlying court/news source.

## Overlaps ("do both")
- Pairs with local U.S. court-record portals, news archives, and police-misconduct/decertification databases — this gives the aggregated arrest record; those give the current case status, the full court file, and non-arrest disciplinary actions the database omits.

## Trust & verifiability
`trust: trusted` — a well-established academic project (BGSU / Prof. Philip Stinson) compiled from public court and news records and widely cited in research and journalism; each case traces to a verifiable public source, though the dataset's date/scope limits must be respected.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | policecrime-bgsu-edu |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, geolocation → document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
