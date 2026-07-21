---
id: jobsdb-asia
name: JobsDB (Asia)
description: Use when you have a `name` and an Asian-region employment angle and want to find a subject's job listings, recruiter posts, or (via their CV) an `employer-org` — returns employment/recruitment context across SE Asia.
url: http://www.jobsdb.com
category: search-engines
path:
- search-engines
bestFor: Employment/recruitment OSINT across Hong Kong, Singapore, Malaysia, Thailand, Indonesia, the Philippines and Vietnam via a leading regional job platform.
selectorsIn:
- name
selectorsOut:
- employer-org
- social-profile
status: live
pricing: free
costNote: Free to search and browse job listings; a free jobseeker account unlocks profile/CV features. Employer/recruiter tools are paid but not needed for searching.
opsec: passive
opsecNote: Passive for public job-listing search. If you register a jobseeker account to view more, use a sock-puppet identity; do not contact employers or apply, which would be active and attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major, legitimate SEEK-owned regional job platform (24M+ candidates); listings are real employer/recruiter content, but a person's presence here is inferred from postings, not a verified identity record.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- JobsDB
- SEEK Asia JobsDB
tags:
- toddington
- curated-directory
- specialty-search
- employment
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# JobsDB (Asia)

> The leading job/recruitment platform across Southeast Asia (SEEK-owned) — an employment-OSINT haystack for subjects with a working life in HK, SG, MY, TH, ID, PH or VN.

## When to use
You have a `name` and reason to think the subject works (or job-hunts) in Southeast Asia, and you want employment context: named recruiters, companies hiring for their role, or — if the subject posted a public jobseeker profile/CV — their stated `employer-org`, skills and location. Useful for placing someone in an industry, city, or company.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the relevant country site (www.jobsdb.com redirects to regional domains: hk./sg./my./th./id./ph. jobsdb.com).
2. Search the subject's `name`, employer, or role, and dork externally: `site:*.jobsdb.com "Name"`.
3. Read matching listings (recruiter/company names, locations) and any public jobseeker content.
4. A free jobseeker account (sock-puppet) can surface more profile features — register only if needed.
5. Pivot: a stated employer feeds company OSINT; a recruiter/contact feeds people-search; a city narrows `geolocation`.

## Inputs → Outputs
- **In:** `name` (+ role/employer/city to disambiguate)
- **Out:** `employer-org` and employment/recruitment context, sometimes a jobseeker `social-profile`
- **Empty/negative result looks like:** no listings or profile match — the subject isn't job-seeking here or their content is private; try LinkedIn-style and country-specific job boards.

## Gotchas & OpSec
- Coverage is **Southeast Asia** — not truly global despite the harvested "global" tag; pick the right country site.
- Most content is employer/recruiter listings, not individuals — a person's footprint here is usually indirect.
- OpSec: passive for search; sock-puppet any account and never apply/contact.

## Overlaps ("do both")
- Pairs with professional-network and country-specific employment tools — JobsDB covers SE Asia strongly where global boards are thin; combine to avoid a regional blind spot.

## Trust & verifiability
`trust: community` — a legitimate major platform, but a subject's "presence" is inferred from postings/CVs; confirm employer/role against a second source before treating it as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jobsdb-asia |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
