---
id: college-recruiter
name: College Recruiter
description: Use when you have a `name` or `employer-org` and want to check entry-level/student job listings and employer pages — returns job postings and hiring-employer context, occasionally corroborating a person's early-career or student status.
url: https://www.collegerecruiter.com
category: people-search
path:
- people-search
bestFor: Searching entry-level, internship, and student job listings and the employers posting them.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free for job seekers to search and view listings; monetised via employer job-posting/advertising services. No account needed to browse.
opsec: passive
opsecNote: You search a public job board; nothing reaches the subject. Applying to or registering with a listing is active and identifiable — stay on the search/browse side for OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established US entry-level job board; it lists employer postings, not a searchable people/resume database, so its direct person-lookup value is limited.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- collegerecruiter.com
tags:
- job-search-resources
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# College Recruiter

> A US job board for entry-level, internship, and student roles — an employer/listing search rather than a people finder, with only indirect OSINT value for placing someone in an early-career or student context.

## When to use
Reach for this when your subject is a student or recent graduate and you want context around their employment search or an employer they mention: what entry-level/internship roles a company posts, which industries/regions a role sits in, or whether an "employer" in a subject's story is a real hiring organisation. It does **not** let you search for a person by name — it is job-listing-oriented — so treat it as weak corroboration, not a primary lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.collegerecruiter.com.
2. Search by job title/keyword and location to see current entry-level/internship/seasonal postings.
3. Filter by employer to view a specific `employer-org`'s open entry-level roles and how it presents itself to students.
4. Read listings for context — role types, locations, and the hiring company — but expect no candidate/resume search.
5. Pivot: a confirmed employer or role feeds LinkedIn/people-search and company-lookup tools where the actual person-level data lives.

## Inputs → Outputs
- **In:** `name` (weak — only if it appears in a posting/blog), or `employer-org`
- **Out:** `employer-org` and job-posting context (role, location, seniority)
- **Empty/negative result looks like:** no matching listings, which says nothing about the person — this board only reflects currently advertised jobs, not who was hired.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; applying/registering is a separate, identifiable action to avoid.
- OpSec: **passive** while searching. Do not create a job-seeker account or apply — that exposes you and touches employers.
- Scope limit: it is a listings board, not a people database. Don't expect to find an individual here; use it to enrich employer/role context only.

## Overlaps ("do both")
- Pairs with LinkedIn, Indeed, and dedicated people-search tools — those hold the person-level and resume data this board lacks; use College Recruiter only to sanity-check an employer or entry-level role that came up elsewhere.

## Trust & verifiability
`trust: community` — a legitimate, long-standing job board, but as a listings aggregator its person-level relevance is indirect; anything you infer about an individual from it must be confirmed against a real people/employment source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | college-recruiter |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
