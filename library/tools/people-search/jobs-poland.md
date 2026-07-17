---
id: jobs-poland
name: JOBS.pl (Poland)
description: Use when you have an employer `name` or a subject's occupation in Poland and want job-market context — returns employer job postings, locations, and hiring/contact leads.
url: http://www.jobs.pl
category: people-search
path:
- people-search
bestFor: Searching Polish job listings for an employer's postings or an occupation, as professional/location context on a subject.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free to search and view job listings; posting jobs or a CV requires a free account.
opsec: passive
opsecNote: Searching public job listings is passive and reveals nothing to any subject. Creating a candidate/employer account is a disclosure — use a puppet identity if needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established Polish job portal (~48k active listings); listings are employer-submitted, so employer/location details are generally reliable while any candidate info is self-supplied.
missingPersonsRelevance: medium
coverage:
- pl
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- JOBS.pl
- jobs.pl Poland
tags:
- job-board
- poland
- employment
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# JOBS.pl (Poland)

> A major Polish job portal — useful less as a direct people-finder than as employer and occupation context: who is hiring, where, and what roles a subject's field looks like in Poland.

## When to use
Your subject has a Polish employment angle and you want context: confirm an employer (`employer-org`) is real and actively hiring, see its office locations, or understand the job market for a stated occupation. Job boards rarely let you look up a *person*, but employer postings corroborate that a company exists and operates in a place, and can surface recruiter contacts and office addresses to pivot on. Treat it as employer/geography context, not a personal record lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.jobs.pl/ (English at jobs.pl/en). Search by employer `name`, keyword, or location.
2. Read matching listings: employer, job location (`address`/city), role, and any recruiter/contact details.
3. Filter by city/region to map an employer's footprint or an occupation's concentration.
4. Pivot: a confirmed employer + location feeds Polish business-registry (KRS) and map checks; a recruiter contact feeds email/phone OSINT.

## Inputs → Outputs
- **In:** employer `name`/`employer-org`, occupation, or location (Poland).
- **Out:** job postings, employer identity, office `address`/city, recruiter/contact leads.
- **Empty/negative result looks like:** no postings — the employer isn't advertising here, or the term is off. Absence says nothing about whether a person works there.

## Gotchas & OpSec
- Not a person search: you find *jobs/employers*, not individuals. Don't expect to look a subject up by name.
- Poland-focused; also lists some Western-European roles for Polish workers.
- Listings expire and rotate; a missing posting doesn't mean the employer is inactive.

## Overlaps ("do both")
- Combine with the Polish company register (KRS/CEIDG) to verify an employer, and with LinkedIn/other job boards (pracuj.pl, praca.pl) for fuller employment coverage.

## Trust & verifiability
`trust: community` — an established job portal. Employer/location data from postings is generally reliable; verify the employer against the official Polish business register before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jobs-poland |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
