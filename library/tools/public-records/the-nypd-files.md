---
id: the-nypd-files
name: The NYPD Files
description: Use when you have a New York City police officer `name` (or badge number) and want their civilian-complaint history — returns misconduct records tied to that `employer-org` role.
url: https://projects.propublica.org/nypd-ccrb/
category: public-records
path:
- public-records
bestFor: Looking up an NYPD officer's substantiated civilian-complaint record from the CCRB (1985–2020).
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- document-id
status: degraded
pricing: free
costNote: Free and open; no account required. The dataset is frozen — it stopped being updated in July 2020.
opsec: passive
opsecNote: A read-only ProPublica web app. No login, no query attribution to your subject. Records name real officers; handle as sensitive personal data and corroborate before drawing conclusions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published by ProPublica from official CCRB data obtained after the repeal of NY Civil Rights Law 50-a. Sourcing is documented; ProPublica is a reputable investigative newsroom.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- 527-explorer
- coronavirus-bailouts-search-every-company-approved-for-federal-loans-over-150k
- credibly-accused
- nonprofit-explorer
- nursing-home-inspect
- parler-capitol-videos
- police-protest-videos
aliases:
- NYPD CCRB database
- ProPublica NYPD Files
tags:
- public-records
- police
- us
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# The NYPD Files

> ProPublica's searchable database of civilian complaints against ~4,000 NYPD officers with at least one substantiated allegation, drawn from CCRB records (Sept 1985 – Jan 2020).

## When to use
You have the `name` (or badge/tax ID) of a current or former New York City police officer and want to check their civilian-complaint history within the `employer-org` (NYPD). Useful for vetting an officer named in a background check, corroborating a subject's law-enforcement employment, or building context on a named individual. Not a person-finder for the general public — it only covers NYPD officers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://projects.propublica.org/nypd-ccrb/ .
2. Search by officer name, precinct/command, or complaint category.
3. Open an officer record to see allegation categories, complainant/officer demographics, and whether the CCRB substantiated each allegation.
4. Note that coverage ends January 2020 and only officers with ≥1 substantiated allegation are included; for newer or unsubstantiated records use the NYC CCRB's own database.
5. Pivot: a confirmed officer name/command feeds broader people-search and news searches.

## Inputs → Outputs
- **In:** `name` (officer) / `employer-org` (NYPD command)
- **Out:** officer `name`, `employer-org` (precinct/unit), complaint categories, disposition, `document-id` (complaint identifiers)
- **Empty/negative result looks like:** no matching officer — either the name is not NYPD, has no substantiated complaints in-window, or is spelled differently. Absence here is not a clean record.

## Gotchas & OpSec
- Human-in-the-loop: none — fully public, no login.
- OpSec: **passive**; the target is never notified.
- The set is deliberately narrow (substantiated-only, frozen at 2020). Do not treat "not found" as exoneration, and do not confuse two officers with the same common name — confirm by command/tax ID.

## Overlaps ("do both")
- Pairs with [[credibly-accused]] and [[police-protest-videos]] — same investigative-newsroom family, each covering a different accountability dataset.

## Trust & verifiability
`trust: community` — an authoritative newsroom (ProPublica) republishing official CCRB data with documented methodology; reliable but static and scope-limited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-nypd-files |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
