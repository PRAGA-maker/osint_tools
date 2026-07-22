---
id: wikimatrix
name: WikiMatrix
description: Use when you have a `username` or topic and want to discover which wiki platforms/communities exist to search it against — returns a directory of comparable wiki sites (`domain` leads).
url: http://www.wikimatrix.org
category: search-engines
path:
- search-engines
bestFor: Comparing wiki software and discovering the range of wiki platforms/communities a subject might contribute to.
selectorsIn:
- username
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free to browse and use the comparison/choice-wizard; a service by CosmoCode.
opsec: passive
opsecNote: Purely a reference directory of wiki software; browsing leaks nothing about a subject. No account, no queries about individuals.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-running wiki-software comparison site (CosmoCode); accurate for what it is, but only tangentially an OSINT resource.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- wikimatrix.org
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# WikiMatrix

> A comparison directory of 80+ wiki platforms — a niche aid for identifying which wiki engine a site runs, or enumerating wiki communities where a subject might have an account.

## When to use
This is a low-relevance specialty resource. Reach for it when (a) you want to identify or compare the wiki software behind a target's site (MediaWiki, DokuWiki, Confluence, XWiki, etc.) as an infrastructure clue, or (b) you are enumerating the landscape of wiki platforms so you can then search a subject's `username` across the ones they might edit. It does not itself search people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.wikimatrix.org.
2. Browse the catalogue of listed wikis, or use the Choice Wizard / feature filters to narrow by capability.
3. Compare candidate platforms side-by-side (hosting model, features, licensing) to identify or characterise a wiki engine.
4. Take the resulting list of wiki platforms and pivot: search the subject's `username` on each platform's user-contribution pages, or fingerprint a target site's engine against the comparison.

## Inputs → Outputs
- **In:** `username` (to fan out across platforms) or a `domain`/topic
- **Out:** `domain` leads — names and links of comparable wiki platforms/communities
- **Empty/negative result looks like:** the directory always returns platform listings; a "negative" here just means none of the compared wikis fit your fingerprint or search need. It never confirms anything about a person.

## Gotchas & OpSec
- This is a software-comparison catalogue, not a people or content search — its OSINT value is indirect and modest.
- Listings can lag current software versions; treat feature data as approximate.
- OpSec: passive, anonymous browsing; nothing about a subject is transmitted.

## Overlaps ("do both")
- Pairs with username-search tools: use WikiMatrix to enumerate candidate wiki communities, then run the actual `username` search on each.

## Trust & verifiability
`trust: unverified` — an accurate long-standing comparison site, but a third-party directory with minimal direct investigative value; use it only as a pivot aid.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikimatrix |
| category | search-engines |
