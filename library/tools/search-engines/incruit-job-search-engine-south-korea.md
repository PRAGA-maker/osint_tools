---
id: incruit-job-search-engine-south-korea
name: Incruit Job Search Engine (South Korea)
description: Use when you have a `name` or `employer-org` and want Korean employment/recruitment traces — returns company profiles, job postings and `employer-org` links.
url: http://www.incruit.com
category: search-engines
path:
- search-engines
bestFor: Searching South Korean job listings and company profiles to tie a person or employer to the Korean job market.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free to browse job postings and company pages; a Korean account (and often KR phone verification) is needed to apply or see some employer detail.
opsec: passive
opsecNote: Browsing listings and company pages is passive and reaches no individual. Creating an account/applying is active and typically requires Korean identity verification — avoid unless you have a legitimate, lawful basis.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Major established Korean recruitment portal; company/job data is employer-supplied, so treat postings as claims.
missingPersonsRelevance: medium
coverage:
- kr
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Incruit
- incruit.com
tags:
- toddington
- curated-directory
- job-search
- korea
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Incruit Job Search Engine (South Korea)

> One of South Korea's long-running recruitment portals — search job postings and company profiles to connect a person or an `employer-org` to the Korean employment market.

## When to use
Your subject may work (or have worked) in South Korea, or you're profiling a Korean company. Incruit lists job postings and employer profiles that can corroborate where a company operates, what roles it hires, and its scale/location — indirect employment context around a `name` or `employer-org`. It's a market/company-research tool rather than a personal-records database: you confirm and characterise an employer more than you look up an individual directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.incruit.com (Korean-language site — use browser translation if needed).
2. Search by company name (`employer-org`) to find its profile and current/past postings, or by keyword/role/region.
3. Read the company page: industry, size, location, and the roles it advertises — context that corroborates an employment claim.
4. Note that applying or viewing some detail needs a Korean account with identity verification; browsing does not.
5. Pivot: cross-check the company in Korean corporate registries and on other Korean job sites (Saramin, JobKorea); feed the employer into `name`-based searches on Korean engines like `[[daum-search-engine-south-korea]]`.

## Inputs → Outputs
- **In:** `name` (limited) or `employer-org`
- **Out:** `employer-org` profiles, job postings, company location/industry context
- **Empty/negative result looks like:** no company/postings — the employer doesn't recruit via Incruit (try Saramin/JobKorea), or the query wasn't in Korean. Individuals generally won't appear as records here.

## Gotchas & OpSec
- OpSec: **passive** for browsing; account creation/applying is active and gated by Korean identity verification.
- Korean-language site; postings are employer-supplied marketing — verify claims independently.
- Best as a company/market lens, not a people-locator; use it to characterise an employer.

## Overlaps ("do both")
- Pairs with other Korean job portals (Saramin, JobKorea) and `[[daum-search-engine-south-korea]]` — job sites cover different employers, and Daum finds the wider Korean-web footprint.

## Trust & verifiability
`trust: community` — an established portal, but its content is employer-provided; corroborate company facts against Korean corporate registries before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | incruit-job-search-engine-south-korea |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
