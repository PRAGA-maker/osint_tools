---
id: indeed
name: Indeed
description: Use when you have a `name` or `employer-org` and want employment context — company profiles, reviews, and (via public resumes/job posts) work-history leads — returns employer and career-footprint signals.
url: https://www.indeed.com
category: people-search
path:
- people-search
bestFor: Researching an employer (reviews, locations, staff signals) and picking up work-history leads around a person.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free to search jobs and read company pages/reviews. The searchable resume database is an employer-paid feature; general users get job listings and company research only.
opsec: passive
opsecNote: Searching listings and company pages is passive. If you view/contact via an Indeed employer account, that account is attributable — use a sock-puppet and stay in read-only public browsing for OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Indeed is a major mainstream job platform; company data and reviews are user/employer-contributed (so reviews are opinion), while job postings come from employers.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- indeed.com
- Indeed Jobs
tags:
- job-search-resources
- employment
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- indeed-job-search-engine-canada
- indeed-job-search-engine-worldwide
---

# Indeed

> A major job platform — use it for employer research and work-history leads, not as a direct people-finder (resume search is employer-paid).

## When to use
You have an `employer-org` you want to understand (locations, size signals, what roles they hire, how staff review it) or a `name` whose employment you're tracing. Indeed's public side gives company profiles and reviews, and its job listings reveal where a company operates and hires. It's context and lead-generation around employment — the searchable *resume* database that would directly surface a person is gated behind paid employer accounts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.indeed.com. For a company, open its **Company Page** (reviews, locations, salaries, Q&A).
2. Read reviews and Q&A for insider signals — office locations, team names, working patterns — that corroborate or expand what you know.
3. Scan the company's active job listings for locations, departments, and hiring managers named in posts.
4. For a person, treat Indeed as corroboration: their stated employer can be sanity-checked against the company's real footprint here, but you won't reliably find the individual without the paid resume DB.
5. Pivot: confirmed employer + location → `[[company-search-tool]]` / corporate registries and LinkedIn; named managers → `associate` leads.

## Inputs → Outputs
- **In:** `name` (weak, indirect) or `employer-org`
- **Out:** company profile, reviews, locations (`address`), job listings, salary/role signals
- **Empty/negative result looks like:** a thin or missing company page means the employer is small/absent from Indeed — try LinkedIn or a registry; and remember you generally *cannot* look a specific person up here without the employer-side resume product.

## Gotchas & OpSec
- Human-in-the-loop: none for public browsing; the resume database requires a paid employer account (out of scope for passive OSINT).
- Reviews are anonymous user opinion — useful as signal, not fact; watch for planted positive/negative reviews.
- It's employer-centric: strong for company research, weak as a direct person locator.

## Overlaps ("do both")
- Pairs with LinkedIn and `[[company-search-tool]]` — Indeed gives employer reviews/footprint and job signals; LinkedIn ties individuals to the employer, and registries confirm the corporate entity.

## Trust & verifiability
`trust: trusted` — a mainstream platform; job postings come from employers (reliable for roles/locations) while reviews are anonymous opinion (treat as signal). Verify any employment inference against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | indeed |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
