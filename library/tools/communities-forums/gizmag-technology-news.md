---
id: gizmag-technology-news
name: GizMag Technology News (New Atlas)
description: Use when you have a `name` in tech/science/startups and want product or coverage mentions — returns social-profile and employer-org.
url: http://www.gizmag.com
category: communities-forums
path:
- communities-forums
bestFor: Searching a science/technology/gadget news archive (now branded New Atlas) for a subject's inventions, products or coverage.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free, ad-supported; no account required. gizmag.com redirects to its current brand, newatlas.com.
opsec: passive
opsecNote: Reading and searching published articles reveals nothing to any subject. Standard browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established science/tech news publication rebranded from Gizmag to New Atlas in 2016; edited, bylined content.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Gizmag
- New Atlas
- newatlas.com
tags:
- news-journalism
- curated-directory
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# GizMag Technology News (New Atlas)

> A science/technology/gadget news outlet — worth a keyword pass when the subject is an inventor, startup founder, or maker likely to appear in emerging-tech coverage.

## When to use
The subject is tied to invention, engineering, startups, gadgets, or science, and you want published mentions: a product they launched, a Kickstarter/company covered, a quote, or a byline. A hit connects a `name` to a company/product (`employer-org`) and an author or profile link (`social-profile`). Note the site rebranded from **Gizmag to New Atlas** in 2016 — old `gizmag.com` links redirect there and the full pre-2016 archive is searchable under the new domain.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to www.gizmag.com (redirects to newatlas.com) and use site search, or run `site:newatlas.com "Jane Doe"` / `site:gizmag.com "Jane Doe"`.
2. Read matching articles for the subject as inventor, founder, quoted source, or author.
3. Note the product/company, dates, and any collaborators named.
4. Pivot: company/product → `employer-org` and crowdfunding-platform lookups; co-named makers → `associate`; author page → `social-profile`.

## Inputs → Outputs
- **In:** `name` (or a product/company term)
- **Out:** `social-profile` (author/mention page), `employer-org` (company/product from context)
- **Empty/negative result looks like:** no articles match — expected for most subjects; means no coverage here, nothing more.

## Gotchas & OpSec
- Remember the rebrand: search **both** `gizmag.com` and `newatlas.com` to catch old and new URLs.
- Single-vertical outlet — a null result is meaningless; a hit is one corroborating data point.
- OpSec: passive read; safe.

## Overlaps ("do both")
- Use within a broader news/tech sweep (alongside `[[extremetech]]` and a general aggregator) so single-outlet gaps don't hide coverage that ran elsewhere.

## Trust & verifiability
`trust: trusted` — edited, bylined tech journalism; mentions are attributable to dated articles, though product claims should be checked against primary/company sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gizmag-technology-news |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
