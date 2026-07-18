---
id: eluta-canada
name: Eluta (Canada)
description: Use when you have a `name` or `employer-org` in Canada and want employment signal — a job engine that indexes employer career pages directly, corroborating who works where.
url: https://www.eluta.ca
category: people-search
path:
- people-search
bestFor: Searching Canadian jobs indexed straight from employer websites to corroborate a company's hiring and, occasionally, named hiring contacts.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free to search job listings; monetized via employer/advertising, not user fees. No account needed to search.
opsec: passive
opsecNote: Passive — browsing indexed public job postings leaks nothing about a subject. Applying to a job is a separate, identity-linked action done on the employer's site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established Canadian job-search engine (Mediacorp) that crawls employer career pages directly; postings reflect the employers' own sites, but Eluta itself is a third-party index.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- eluta.ca
tags:
- job-search-resources
- employment
- canada
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Eluta (Canada)

> A Canadian job engine that indexes employer career pages *directly* rather than reposting boards — useful for confirming a company's real hiring activity, and sometimes surfacing named contacts, in an employment-OSINT check.

## When to use
You have a `name` or `employer-org` in Canada and want employment context: is a company actively hiring, for what roles, in which cities, and does a posting name a hiring manager or contact. Because Eluta crawls employers' own sites, its listings are close to the source and can corroborate that a company is real and active or place a subject's stated role in context. Its people value is indirect — the occasional named contact in a posting — so treat it as employer/role signal rather than a person directory.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.eluta.ca and search by keyword, employer, or location.
2. Review listings sourced directly from employer career pages; open a posting for role, location, and the originating company site.
3. Scan postings for named hiring contacts or team details that occasionally appear.
4. Follow through to the employer's own careers page for authoritative detail.
5. Pivot: a confirmed `employer-org` and location feed corporate-registry and LinkedIn research; a named contact feeds people-search; role/location patterns add company context.

## Inputs → Outputs
- **In:** an `employer-org`, role keyword, or a `name` (as a long shot in posting text)
- **Out:** Canadian job postings tied to an `employer-org` — role, location, and occasionally a named contact
- **Empty/negative result looks like:** no postings for a company means nothing is currently indexed from its site (it may not be hiring) — and individuals generally won't appear, since it indexes jobs, not people.

## Gotchas & OpSec
- **Jobs, not people:** its OSINT value is employer/role corroboration; named individuals are incidental, not searchable as a directory.
- Canada-focused; limited value elsewhere.
- Index freshness depends on Eluta's crawl of each employer site — confirm a decisive detail on the company's own careers page.

## Overlaps ("do both")
- Complements LinkedIn, Canadian corporate registries, and other job tools (`[[careerbuilder]]`, `[[recruit-net]]`) — Eluta's edge is employer-sourced listings, while those provide person-level or broader aggregated coverage.

## Trust & verifiability
`trust: community` — a reputable Canadian job engine indexing employer sites; postings trace back to the employers themselves, but as a third-party index, verify specifics at the source career page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eluta-canada |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
