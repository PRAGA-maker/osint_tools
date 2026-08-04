---
id: fortune-500-list-of-companies-2020-fortune
name: Fortune 500 List
description: Use when you have a large US company (`employer-org`) or executive `name` and want corporate facts — the ranked list returns revenue, sector, HQ and leadership for the biggest firms.
url: https://fortune.com/fortune500
category: public-records
path:
- public-records
bestFor: Quick authoritative reference on the largest US companies — rank, revenue, industry, headquarters and CEO.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: The ranked list and core company facts are free to browse; some deeper Fortune articles/analysis sit behind a subscription.
opsec: passive
opsecNote: Read-only browsing of a public business publication — no target interaction and nothing about a subject transmitted. Only your own visit is logged by Fortune.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Fortune's flagship ranking, compiled from company financial filings; authoritative for the headline corporate facts it lists, though scoped to the largest US firms and updated annually.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fortune-magazine
aliases:
- Fortune 500
- Fortune500 list
tags:
- corporate
source: metaosint
lastVerified: '2026-08-04'
enrichment: full
---

# Fortune 500 List

> The annual ranked list of the largest US companies by revenue — a fast, authoritative reference for a big firm's basic corporate facts and who leads it.

## When to use
An investigation touches a major US company as an `employer-org`, or you have an executive `name` and want to confirm/contextualise their company. The Fortune 500 gives each firm's rank, revenue, industry, headquarters location, and CEO — quick corroboration of scale and leadership, and a jumping-off point to registry and filings research.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://fortune.com/fortune500.
2. Search or sort the list by company name, industry, or rank.
3. Open a company's entry: rank, revenue, sector, HQ, and CEO/leadership.
4. Pivot: the CEO/executive (`associate`) feeds people-search; the HQ and legal name feed corporate-registry and SEC-filings lookups.

## Inputs → Outputs
- **In:** `employer-org` (a large US company) or an executive `name`
- **Out:** corporate facts — revenue, industry, HQ, and leadership (`associate` executives) for that `employer-org`
- **Empty/negative result looks like:** the company isn't listed — it's below the top-500 US-revenue threshold, private/foreign, or a subsidiary; absence just means "not a Fortune 500 firm."

## Gotchas & OpSec
- **Scope-limited:** only the largest US companies; most firms you'll investigate won't appear — use company registries for the long tail.
- Annual snapshot — leadership and figures may be out of date between editions; confirm current officers via filings.
- Headline facts only; it is not a corporate-records database (no ownership structure, filings, or officers beyond the top).

## Overlaps ("do both")
- A starting reference that pairs with authoritative company sources — corporate registries, SEC EDGAR, and [[fortune-magazine]] — which give the filings, officers and ownership this list only summarises.

## Trust & verifiability
`trust: trusted` — a reputable ranking built from company financials; the listed facts are citable, with the caveat that they're an annual snapshot of only the largest firms.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fortune-500-list-of-companies-2020-fortune |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
