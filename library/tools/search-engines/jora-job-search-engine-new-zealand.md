---
id: jora-job-search-engine-new-zealand
name: Jora Job Search Engine (New Zealand)
description: Use when you have an `employer-org` or role/location in New Zealand and want current vacancies — returns aggregated job listings by company and place, useful for confirming an employer is hiring.
url: https://nz.jora.com
category: search-engines
path:
- search-engines
bestFor: Aggregated New Zealand job-listing search by company, title and location.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free for job seekers to search and browse; an optional account only adds email alerts.
opsec: passive
opsecNote: Searching listings is passive and notifies no employer or applicant. Browse logged-out; only register (with a sock puppet) if you want saved alerts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established job aggregator (part of SEEK); it republishes third-party listings, so postings are only as accurate as their source.
missingPersonsRelevance: medium
coverage:
- nz
auth: none
api: false
localInstall: false
registration: false
aliases:
- Jora NZ
- nz.jora.com
tags:
- toddington
- curated-directory
- specialty-search
- jobs
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Jora Job Search Engine (New Zealand)

> A New Zealand job-listing aggregator — search by company or location to confirm an organisation is actively hiring, where, and for what roles.

## When to use
You have an `employer-org` (a company a subject claims to work for, or one you're profiling) and want to see whether and where it's hiring in New Zealand, or to test a role/location a subject mentioned. Jora aggregates listings from many boards, so it's useful for corroborating that a company is real and active and for mapping its NZ office locations — indirect, context-building rather than a person lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://nz.jora.com and search by company name (`employer-org`), job title, and/or location.
2. Read the listings: hiring company, office town/region (`address`), role types, and posting dates.
3. Pivot: office locations narrow an employer's NZ footprint; a live listing corroborates the company is active; role patterns hint at the workforce to search on professional networks.

## Inputs → Outputs
- **In:** `employer-org` (or job title + location)
- **Out:** `employer-org` (active listings) and `address`/location of roles
- **Empty/negative result looks like:** no listings for the company/area — the employer may not be hiring or isn't aggregated here; this says nothing about whether the company exists, so verify separately.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing.
- OpSec: passive — searching notifies no one.
- A job/employer source, not a people finder; it returns organisations and locations, not an individual's identity. Coverage here is New Zealand (Jora runs per-country sites).

## Overlaps ("do both")
- Pairs with NZ company registries and professional-network tools — Jora shows where a company hires, a registry confirms its legal identity, and a professional network links named employees.

## Trust & verifiability
`trust: community` — Jora republishes third-party listings, so accuracy depends on the source board; confirm any company detail against the employer's own site or a registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jora-job-search-engine-new-zealand |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
