---
id: fish4jobs
name: Fish4Jobs
description: Use when you have a `name` or `employer-org` and want a matching UK job posting or candidate footprint — returns `employer-org`, `geolocation`, and career detail.
url: http://www.fish4.co.uk
category: people-search
path:
- people-search
bestFor: Searching a legacy UK job board for a subject's job applications context or an employer's vacancies by location.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- geolocation
status: degraded
pricing: free
costNote: Free to search and view job listings; posting/recruiter features may need an account. Note the platform is a declining legacy site with reduced coverage.
opsec: passive
opsecNote: Searching public job listings is passive and does not notify anyone. If you register or use recruiter features, that activity is attributable — use a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A once-major UK job board now much diminished (the operating company is in liquidation/dormant); the site still serves listings but coverage is thin, so absence proves little.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- fish4.co.uk
- Fish4
tags:
- job-search-resources
- employment
- uk
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Fish4Jobs

> A legacy UK job board — useful for placing a subject in the UK employment market: an employer's vacancies by location, or the kind of roles/sectors tied to a person or company.

## When to use
You're building a UK subject's employment picture and want to check a job board that historically had strong regional/newspaper-linked coverage. Search an `employer-org` to see whether it's hiring and where (placing the company and its staff geographically), or scan a sector/location to understand a subject's likely job market. Because Fish4 is now a diminished legacy site, treat it as a *supplementary* UK source rather than a primary one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open fish4.co.uk in a sock-puppet browser (the site may bot-block bare fetches; a normal browser session works).
2. Search by role/keyword and location to see live UK vacancies, or by company to find a specific `employer-org`'s postings.
3. Read each posting for the employer, location (`geolocation`), salary band, and contact/recruiter detail.
4. Note that coverage is thin — a missing result is expected and weak evidence.
5. Pivot: feed an `employer-org` into UK corporate-registry (Companies House) tools and professional-network searches; a location into records/maps tools.

## Inputs → Outputs
- **In:** `name`/role or `employer-org` (+ optional location)
- **Out:** matching UK job postings → `employer-org`, `geolocation`, role/sector, recruiter contact
- **Empty/negative result looks like:** few or no matches — expected on a declining board; do not read absence as "the subject/company has no UK footprint."

## Gotchas & OpSec
- **Diminished legacy site:** far smaller than at its peak; use as a secondary UK check, not a comprehensive one.
- Job listings are employer-submitted and time-limited — old roles expire off the board.
- OpSec: passive when browsing; registration/recruiter use is attributable.

## Overlaps ("do both")
- Pairs with Companies House and professional-network tools — Fish4 shows a live vacancy/location; those reach the company's officers and the subject's stated work history.

## Trust & verifiability
`trust: unverified` — a real but declining commercial job board; content is employer-submitted, so any hit is a lead to corroborate and any miss is inconclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fish4jobs |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
