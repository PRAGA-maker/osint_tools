---
id: seek-job-search-engine-new-zealand
name: Seek Job Search Engine (New Zealand)
description: Use when you have a `name` or `employer-org` and want a subject's NZ job/employment footprint — returns employer, role, and location leads from job listings.
url: https://www.seek.co.nz/
category: search-engines
path:
- search-engines
bestFor: Searching New Zealand job listings and company profiles to place a subject at an employer/location.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free to search and browse listings/company pages; posting or full recruiter tools require an account, but searching doesn't.
opsec: passive
opsecNote: Browsing public job listings and company profiles; the subject isn't contacted. Don't apply, message, or create a profile against a target — that would be active and traceable. Read-only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Seek is a major, legitimate Australasian job board; listing content is employer-supplied, so treat role/employer claims as leads, not verified facts.
missingPersonsRelevance: medium
coverage:
- nz
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Seek NZ
- seek.co.nz
tags:
- jobs
- employment
- new-zealand
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Seek Job Search Engine (New Zealand)

> New Zealand's dominant job board — useful for tying a subject to an NZ employer, role, or region via current and recent vacancies and company pages.

## When to use
Your subject has a New Zealand connection and you're trying to establish where they work or worked, or to profile an `employer-org` they're linked to. Job listings and Seek's company profiles surface employer names, locations, and role types — regional employment context that helps place a person geographically and corroborate a claimed job. Also handy for reverse leads: a distinctive vacancy can reveal a small company's location and hiring contacts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.seek.co.nz/.
2. Search by keyword/role and location, or search a `name` / company to find its listings and company profile.
3. Browse the company page for location, size, industry, and current vacancies.
4. Note geographic filters (region/city) to narrow a subject's likely area.
5. Pivot: an `employer-org` found here feeds company-registry lookups; a location feeds people/property search; a niche role hints at the subject's profession.

## Inputs → Outputs
- **In:** `name` (person or company) or `employer-org` + optional NZ location
- **Out:** employer/role listings, company profile with `address`/region, hiring context
- **Empty/negative result looks like:** no listings/company match — the employer may not advertise on Seek, be too small, or not be NZ-based; absence proves nothing about employment.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; creating an applicant profile or applying is out of scope and would be active — don't.
- Listings are employer-written marketing; verify company details against an official NZ registry.
- Coverage is NZ-focused (Seek also runs .com.au for Australia) — pick the right regional site for your subject.
- OpSec: passive, read-only browsing.

## Overlaps ("do both")
- Pairs with company-registry and people-search tools — Seek gives the employment/location lead; the registry confirms the company and the people-search ties it to the individual.

## Trust & verifiability
`trust: community` — Seek is a legitimate, widely-used job board, but its content is employer-supplied advertising; use findings as directional leads and corroborate employment claims elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seek-job-search-engine-new-zealand |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
