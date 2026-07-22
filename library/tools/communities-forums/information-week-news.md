---
id: information-week-news
name: InformationWeek
description: Use when you have a `name` or `employer-org` and want enterprise-IT/tech news mentioning them — returns `social-profile`/byline, `employer-org` context and named `associate` links.
url: http://www.informationweek.com
category: communities-forums
path:
- communities-forums
bestFor: Finding enterprise-IT and business-technology coverage naming a person, executive, or company.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to read most articles; some gated/registration-walled analyst content.
opsec: passive
opsecNote: Reading and dorking a public trade-news site is passive and invisible to any subject; only the publisher/ad partners log the visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running enterprise-IT trade publication; credible for tech-industry context, mixing reporting with vendor-adjacent and contributed content — corroborate specifics.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Information Week
- informationweek.com
tags:
- news-media
- tech
- enterprise-it
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# InformationWeek

> A veteran enterprise-IT news outlet — the place a tech executive, CIO, vendor or IT professional may surface in coverage, quotes or contributed articles.

## When to use
You have a `name` or `employer-org` with a business-technology angle and want context: coverage naming an IT executive/CIO, a vendor or company, a quoted expert, or a bylined contributor. Useful for verifying a claimed tech-industry role or seniority, identifying decision-makers/associates at a tech company, and dating a person's professional activity via article timestamps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use the site's search, or Google-dork it: `site:informationweek.com "<name or company>"`.
2. Open matching articles and read for the connection — subject, quoted source, or byline — with date, role and named associates.
3. Follow bylined-author pages for a contributor's profile and other pieces.
4. Pivot: a named executive/`associate` feeds LinkedIn and company-registry checks; an `employer-org` feeds `[[company-research-resources-by-country-comparably]]`; a byline feeds journalist enumeration.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `social-profile`/byline, named `associate`s (executives/experts), `employer-org` context and article dates
- **Empty/negative result looks like:** no hits — the subject/company has no enterprise-IT press footprint (common outside tech); disambiguate same-name matches by context.

## Gotchas & OpSec
- Tech/enterprise-IT niche; irrelevant for unrelated subjects.
- Mixes reporting with contributed/vendor-adjacent content — weight sources and corroborate.
- Passive; no subject notification.

## Overlaps ("do both")
- Pairs with LinkedIn, Crunchbase, other tech press (`[[mashable]]`) and corporate registries — the article surfaces the person/role; those confirm the employer and current position.

## Trust & verifiability
`trust: community` — an established trade publication; credible for industry context, but corroborate specific factual/role claims against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | information-week-news |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
