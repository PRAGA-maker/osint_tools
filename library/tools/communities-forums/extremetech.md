---
id: extremetech
name: ExtremeTech
description: Use when you have a `name` tied to the tech/hardware industry and want news mentions, bylines or product coverage — returns social-profile and employer-org.
url: http://www.extremetech.com
category: communities-forums
path:
- communities-forums
bestFor: Searching a long-running consumer-tech/hardware news publication for a subject's bylines, quotes or coverage.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free to read; ad-supported. No account required.
opsec: passive
opsecNote: Reading and searching published articles is invisible to any subject. No sock puppet needed beyond normal browsing hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established consumer-technology publication (Ziff Davis); an edited news outlet, so bylined content is attributable and citable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- extremetech-virutal-box
aliases:
- extremetech.com
tags:
- news-journalism
- curated-directory
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# ExtremeTech

> A consumer-tech and computing-hardware news site — a narrow source worth a keyword pass only when the subject works in or is quoted about the tech industry.

## When to use
The subject is a technology journalist, hardware engineer, startup figure, or otherwise likely to appear in tech-industry coverage, and you want published mentions: an authored byline, a quote, a product they built, a company they were named in. A hit ties a `name` to an `employer-org` and to an author profile (`social-profile`) you can pivot from. For anyone outside tech this source is low-yield — skip it in favour of general news search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.extremetech.com and use the site search, or run a scoped engine query: `site:extremetech.com "Jane Doe"`.
2. Read matching articles for the subject as author, subject, or quoted source.
3. Note the byline/author page, any stated affiliation, and companies/products mentioned alongside them.
4. Pivot: author page → `social-profile`/contact; named company → `employer-org`; co-mentioned people → `associate`.

## Inputs → Outputs
- **In:** `name` (or a company/product term)
- **Out:** `social-profile` (author page / mention), `employer-org` (affiliation from context)
- **Empty/negative result looks like:** no articles mention the term — expected for the vast majority of subjects; means only that they have no ExtremeTech footprint.

## Gotchas & OpSec
- Single-outlet, single-vertical coverage — treat a null result as meaningless and a hit as one data point to corroborate elsewhere.
- Use a general news aggregator for breadth; this only makes sense for tech-industry subjects.
- OpSec: passive read; safe.

## Overlaps ("do both")
- Best used through a broad news search (Google News, or a media-aggregator tool) rather than alone; this entry just documents one tech-specific outlet worth including in a `site:` sweep.

## Trust & verifiability
`trust: trusted` — an edited, bylined publication, so any mention is attributable to a dated article you can cite; still cross-check factual claims against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | extremetech |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
