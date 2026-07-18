---
id: recruit-net
name: Recruit.net
description: Use when you have an `employer-org` or role and want job-posting context — aggregates listings from company sites and boards across many countries into one search.
url: https://www.recruit.net/
category: search-engines
path:
- search-engines
bestFor: Aggregated job-listing search across employers and boards to corroborate that a company is hiring for specific roles/locations.
selectorsIn:
- employer-org
- geolocation
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free to search and browse aggregated job listings; monetized via employer/advertiser referrals, not user fees. No account needed to search.
opsec: passive
opsecNote: Passive — browsing aggregated public job listings leaks nothing about a subject. Applying to a listing is a separate, identity-linked action done off-site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A job-aggregator that indexes listings from many third-party sources; postings are as accurate as the originating employer/board and can be stale or duplicated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- recruit.net
- usa.recruit.net
tags:
- toddington
- curated-directory
- employment
- job-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Recruit.net

> A multi-country job-listing aggregator — search hiring activity by company, role, or location as background context, not as a way to look up individuals.

## When to use
You want employment/company context: is an `employer-org` hiring, for which roles, in which locations? Aggregated job listings can corroborate that a company is real and active, hint at its size/growth and where it operates, and place a subject's stated role in context. It aggregates postings across countries, so it's useful for a broad first pass. It does **not** profile individuals — the OSINT value is the employer/role signal, not people lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.recruit.net/ (country subsites like usa.recruit.net exist) and search by keyword, company, or location.
2. Review aggregated listings: employer, role, location, and a link to the original posting/source.
3. Use the results to corroborate an employer's activity, hiring locations, or a role's existence.
4. Follow a listing to its source (company careers page or board) for authoritative detail.
5. Pivot: a confirmed `employer-org` and location feed corporate-registry and LinkedIn research; role/location patterns add company context.

## Inputs → Outputs
- **In:** an `employer-org`, role keyword, or `geolocation`
- **Out:** aggregated job listings — employer, role, and location context
- **Empty/negative result looks like:** no listings for a company just means nothing is currently aggregated (it may hire via other channels) — and no individual will ever appear, since it indexes postings, not people.

## Gotchas & OpSec
- **Aggregator caveats:** listings can be stale, duplicated, or reposted; confirm against the original source before relying on a detail.
- It profiles *jobs*, not people — don't expect to find a named individual here.
- Coverage and freshness vary by country and employer.

## Overlaps ("do both")
- Complements LinkedIn, corporate registries, and other job boards (`[[careerbuilder]]`, `[[eluta-canada]]`) — Recruit.net gives broad multi-source hiring context, while those provide person-level or authoritative company detail.

## Trust & verifiability
`trust: community` — a legitimate aggregator whose data is only as good as the sources it indexes; treat postings as leads and verify specifics at the originating employer/board.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | recruit-net |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, geolocation → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
