---
id: the-wall-street-journal
name: The Wall Street Journal
description: Use when you have a `name` tied to business/finance and want reported coverage, quotes or bylines — returns employer-org and associate.
url: http://www.wsj.com/news/world
category: communities-forums
path:
- communities-forums
bestFor: Searching a major business/financial news archive for a subject's mentions, quotes, deals and affiliations.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Headlines and search are free; most full articles are behind a paid WSJ subscription. Archived copies and syndication often surface the text without paying.
opsec: passive
opsecNote: Reading/searching published journalism is invisible to any subject. No sock puppet required to read; only a WSJ login would tie a session to you (avoid it).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A leading edited financial newspaper (Dow Jones); bylined, fact-checked reporting that is citable and attributable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- tweet-metadata
- wsj-technology-news
aliases:
- WSJ
- wsj.com
tags:
- news-journalism
- curated-directory
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# The Wall Street Journal

> A major business/financial newspaper of record — the right source when the subject is a corporate, financial, or high-net-worth figure who surfaces in deals, filings, and executive coverage.

## When to use
The subject operates in business, finance, law, or public life and may appear in serious reporting: an executive named in a merger, a defendant in a financial case, a quoted source, or a bylined contributor. Searching their `name` (and any `employer-org`) can yield dated, attributable articles that tie them to companies (`employer-org`), transactions, and named `associate`s. High value for corporate/UHNW subjects; low for private individuals with no business footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use WSJ search, or a scoped engine query: `site:wsj.com "Jane Doe"`.
2. For paywalled hits, read the excerpt/dek, check syndication (Dow Jones wire, Factiva), or an archived copy (`[[wayback]]`-style) to recover the text.
3. Note the company, role, dates, and any people named alongside the subject.
4. Pivot: named company → `employer-org` verification and corporate-registry lookups; co-named people → `associate`; a court/case reference → public-records search.

## Inputs → Outputs
- **In:** `name` (optionally `employer-org`)
- **Out:** `employer-org` (companies/roles from coverage), `associate` (co-named people), plus dated citations
- **Empty/negative result looks like:** no articles reference the subject — expected for most private individuals; means no WSJ footprint, not that the person is unremarkable.

## Gotchas & OpSec
- Paywall: assume full text is gated; recover via archive/syndication rather than subscribing under your real identity.
- Name collisions are common for ordinary names — anchor on company/role/date before attributing.
- OpSec: passive read; safe.

## Overlaps ("do both")
- Run inside a broad news sweep alongside other majors (e.g. `[[the-globe-and-mail]]`) and a general aggregator — WSJ is strongest for finance/corporate angles; pair it so you don't miss regional or non-business coverage.

## Trust & verifiability
`trust: trusted` — edited, bylined, fact-checked reporting; treat named facts as reliable and citable, while still confirming specifics against primary documents (filings, court records).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-wall-street-journal |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
