---
id: adzuna-job-search-engine-united-kingdom
name: Adzuna Job Search Engine (UK)
description: Use when you have an `employer-org` or role/location and want current UK vacancies and salary data — returns aggregated job listings by company and place, useful for confirming an employer is hiring.
url: https://www.adzuna.co.uk
category: search-engines
path:
- search-engines
bestFor: Aggregated UK job-listing search by company, title and location, with salary statistics.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free for job seekers to search and browse; Adzuna also offers a free developer API (key required) for programmatic access.
opsec: passive
opsecNote: Searching listings is passive and notifies no employer or applicant. Browse logged-out; only register (with a sock puppet) if you want saved alerts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established job-search aggregator; it republishes third-party listings and models salary statistics, so postings are only as accurate as their source.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
aliases:
- Adzuna
- adzuna.co.uk
tags:
- toddington
- curated-directory
- specialty-search
- jobs
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Adzuna Job Search Engine (UK)

> A UK job-listing aggregator with salary analytics — search by company or location to confirm an organisation is actively hiring, where, and for what.

## When to use
You have an `employer-org` (a company a subject claims to work for, or one you're profiling) and want to see whether and where it's hiring in the UK, or to test a role/location a subject mentioned. Adzuna aggregates listings from many boards and adds salary statistics, making it useful for corroborating that a company is real and active and for mapping its UK office locations — indirect, context-building rather than a person lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.adzuna.co.uk and search by company name (`employer-org`), job title, and/or location.
2. Read the listings: hiring company, office town/region (`address`), role types, posting dates, and the salary band/statistics Adzuna models.
3. For scale, use Adzuna's free developer API (register for a key) to query listings programmatically.
4. Pivot: office locations narrow an employer's footprint; a live listing corroborates the company is active; role patterns hint at the workforce to search on professional networks.

## Inputs → Outputs
- **In:** `employer-org` (or job title + location)
- **Out:** `employer-org` (active listings), `address`/location of roles, plus salary statistics
- **Empty/negative result looks like:** no listings for the company/area — the employer may not be hiring or isn't aggregated here; this says nothing about whether the company exists, so verify separately.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; API access needs a free key.
- OpSec: passive — searching notifies no one.
- This is a job/employer source, not a people finder; it returns organisations and locations, not an individual's identity. Coverage here is UK (Adzuna runs per-country sites).

## Overlaps ("do both")
- Pairs with company registries and professional-network tools — Adzuna shows where a company hires, a registry confirms its legal identity, and a professional network links named employees; use together to build the org picture.

## Trust & verifiability
`trust: community` — Adzuna republishes third-party listings and estimates salaries, so accuracy depends on the source board; confirm any company detail against the employer's own site or a registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | adzuna-job-search-engine-united-kingdom |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
