---
id: eurojobs
name: Eurojobs
description: Use when you have a person's `name` or an `employer-org` and want to check for a matching CV/candidate profile or job posting across Europe — returns `employer-org`, `geolocation`, and career detail.
url: https://www.eurojobs.com
category: people-search
path:
- people-search
bestFor: Searching a pan-European jobs/CV board for a subject's posted resume or an employer's live vacancies.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- geolocation
- social-profile
status: live
pricing: freemium
costNote: Free to search job listings and register; browsing the CV/resume database and contacting candidates is a recruiter feature that may require an employer account.
opsec: passive
opsecNote: Searching public listings is passive. If you register or view CVs while logged in, the platform can log your activity; use a sock-puppet recruiter account and never contact the subject from an attributable identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running commercial European job aggregator; postings and CVs are user/employer-submitted, so treat any match as a lead to corroborate.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- eurojobs.com
tags:
- job-search-resources
- employment
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Eurojobs

> A pan-European jobs and CV board — in OSINT terms, a place to check whether a subject posted a resume (revealing employer history, skills, and location) or to map an employer's current hiring.

## When to use
You have a subject's `name` (or a known `employer-org`) and want to see whether they are job-seeking or have a public CV on a European board. A candidate profile can expose a work-history timeline, current city (`geolocation`), languages, and contact handles — strong corroboration for identity and whereabouts. Alternatively, searching an employer's postings tells you the org is active and hiring in a given location, which can place associates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.eurojobs.com in a sock-puppet browser.
2. Use the "Find Jobs" search with the target `employer-org` and a location to enumerate that company's live vacancies, or search the "Companies" directory.
3. To look for a subject's own CV, register a (sock-puppet) account and use the "Post Resumes"/candidate-search side — resume access is generally gated behind a recruiter login.
4. Read the profile/posting: employer names, dates, city, languages, and any contact details are the OSINT payload.
5. Pivot: feed an `employer-org` into corporate-registry and LinkedIn-style tools, and a city `geolocation` into records/maps tools.

## Inputs → Outputs
- **In:** `name` (candidate) or `employer-org`
- **Out:** matching CV/candidate `social-profile`, work history, current-city `geolocation`, and employer vacancy data
- **Empty/negative result looks like:** no candidate or posting match — the subject simply may not use this board (it's one of many regional job sites); weak negative evidence.

## Gotchas & OpSec
- Human-in-the-loop: full CV/candidate search typically needs a (free) employer/recruiter account; job-listing search is open.
- Data is self-submitted and can be stale — a CV may be years old; verify employer/dates elsewhere.
- OpSec: passive when browsing listings; logged-in CV access is attributable — use a sock puppet and never reach out to the subject.

## Overlaps ("do both")
- Pairs with professional-network and corporate-registry tools — Eurojobs may hold a CV or vacancy the subject never mirrored to LinkedIn, and vice versa.

## Trust & verifiability
`trust: unverified` — a real commercial job board, but all content is user/employer-submitted with no identity verification, so any hit is a lead to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eurojobs |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org, geolocation, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
