---
id: cnet
name: CNET
description: Use when you have a `name` or `employer-org` in tech/consumer-electronics and want press coverage — returns articles, quotes, and role/company context.
url: https://www.cnet.com
category: communities-forums
path:
- communities-forums
bestFor: Finding technology-industry news coverage, product reviews, and quoted experts to corroborate a subject's role or claims.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free, ad-supported consumer-tech news and reviews; no account needed to read.
opsec: passive
opsecNote: Passive reading and site-scoped searching of a public news site; no subject interaction or notification. Ad/tracker-heavy — use a clean browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established mainstream tech-news publisher (Red Ventures); editorial journalism — reliable reporting but a secondary source for any personal detail.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cnet-technology-products-reviews
aliases:
- CNET.com
- CNET News
tags:
- toddington
- curated-directory
- news
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# CNET

> Mainstream consumer-technology news and reviews — a niche press archive for corroborating a subject tied to the tech industry (founders, executives, engineers, quoted experts).

## When to use
Your subject is connected to consumer tech — a startup founder, a product exec, a security researcher, an engineer — and you want independent coverage: a quote, a launch story, a company profile, a product they built. Use CNET to confirm a `name`↔`employer-org` link, capture a dated professional event, or find named colleagues/partners for `associate` leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cnet.com or run a scoped engine query: `site:cnet.com "<name or company>"`.
2. Read articles for named people, titles, companies, product launches, and dates.
3. Note quotes and bylines — CNET staff writers and the people they interview are both leads.
4. Pivot: a confirmed role feeds LinkedIn/people-search; named partners become `associate`s; dated coverage anchors a career timeline.

## Inputs → Outputs
- **In:** `name` or `employer-org` (tech industry)
- **Out:** press coverage, roles/titles, company `associate` links
- **Empty/negative result looks like:** no articles — your subject isn't tech-press-notable; try trade press, local news, or LinkedIn instead.

## Gotchas & OpSec
- Coverage skews to notable companies/products; ordinary employees rarely appear.
- Secondary-source journalism — good for leads, verify specifics against primary records.
- OpSec: passive news reading.

## Overlaps ("do both")
- Complements general news search and business registries — this is the tech-industry lens; use registries to confirm the corporate facts it reports.

## Trust & verifiability
`trust: community` — established editorial journalism, reliable as reporting but a secondary source for personal identifiers; corroborate before attributing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cnet |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
