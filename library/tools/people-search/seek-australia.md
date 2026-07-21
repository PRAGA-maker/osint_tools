---
id: seek-australia
name: SEEK (Australia)
description: Use when you have a `name` or `employer-org` in Australia/NZ and want employment context — returns recruiter/company postings and profile leads from the region's dominant job marketplace.
url: http://www.seek.com.au
category: people-search
path:
- people-search
bestFor: Employment and employer research in Australia/New Zealand via the region's largest job board.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- social-profile
status: live
pricing: freemium
costNote: Free to browse and search job listings and company pages; posting jobs and full candidate-profile features require an employer/recruiter account.
opsec: passive
opsecNote: Browsing public listings and company pages is passive. A candidate profile requires login and would expose you — stay a passive reader for OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major commercial job marketplace; listings and company pages are self-published by employers/recruiters, useful as leads rather than verified records.
missingPersonsRelevance: low
coverage:
- au
- nz
auth: none
api: false
localInstall: false
registration: false
aliases:
- SEEK
- seek.com.au
tags:
- job-search-resources
- employment
- australia
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# SEEK (Australia)

> Australia and New Zealand's dominant job marketplace — an employment-context source for tying people to employers and reading a company's hiring footprint, not a direct person index.

## When to use
An indirect, contextual resource. When a subject is in Australia/NZ and you're building their employment picture, SEEK helps two ways: its company/employer pages profile an `employer-org` (locations, reviews, active roles), and job listings can reveal recruiters, team structures, and where an organization is hiring — useful for inferring where someone works or might apply. It rarely names your subject directly; it characterizes the employers around them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.seek.com.au and search by company name to reach its employer/company page, or by role/location for the hiring picture.
2. Read the company profile: offices, size, reviews, and current openings.
3. Note recruiter names/agencies and role details that indicate team composition or locations.
4. Use a `site:seek.com.au` Google search to catch cached/older listings.
5. Pivot: an `employer-org` feeds ASIC/company registries and LinkedIn; a recruiter or agency feeds people-search.

## Inputs → Outputs
- **In:** `name` (rarely) or `employer-org` / role / location
- **Out:** `employer-org` company pages, hiring/location signals, recruiter and agency `social-profile` leads
- **Empty/negative result looks like:** no company page or listings — the employer may not recruit via SEEK; absence is not informative about a person.

## Gotchas & OpSec
- Not a people directory: expect employer/role data, not individual records.
- Listings expire; use web archives / Google cache for historical hiring signals.
- OpSec: passive as a browser; do not create a candidate profile for OSINT.

## Overlaps ("do both")
- Pairs with LinkedIn and the Australian company registers — SEEK shows the hiring/employer surface; those name the actual people and directors.

## Trust & verifiability
`trust: community` — a commercial marketplace of self-published listings; treat everything as an employer-supplied lead to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seek-australia |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
