---
id: thepaperboy
name: ThePaperboy
description: Use when you have a `geolocation` (country/region) and want the local/national newspapers covering it — returns newspaper `domain`s to search for coverage of a person or event.
url: https://www.thepaperboy.com/newspapers-by-country.cfm
category: communities-forums
path:
- communities-forums
bestFor: Finding the right local/national newspaper websites for a country, US state, or city to hunt for press coverage of a subject.
selectorsIn:
- geolocation
- address
selectorsOut:
- domain
status: live
pricing: free
costNote: Free directory; no account or payment. Online since 1997, rebuilt 2025.
opsec: passive
opsecNote: Browsing the directory itself is passive — you are only reading a public list of publication links. OpSec exposure begins only once you follow through to a specific newspaper's site and run searches there; the target is never touched by using Paperboy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent directory (since 1997) cataloguing 11,000+ papers across 230+ countries; it curates links, it does not hold personal data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- paperboy
aliases:
- Paperboy
- World Newspaper Directory
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# ThePaperboy

> A 25-year-old directory that maps any country, US state, or city to the newspapers that cover it — your index into local press for a missing-person case.

## When to use
You know roughly *where* a subject lived, went missing, or made news (`geolocation` / `address`) and want the specific newspapers whose archives and websites you should search — a local paper often carries names, photos, obituaries, court notes, and community appeals that never reach the national web.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.thepaperboy.com/newspapers-by-country.cfm (or the interactive map on the homepage).
2. Drill to the relevant country → region → city, or use the publication-name search to jump to a known title.
3. Read the output: each entry links out to the newspaper's own website. Note the small-town/regional papers, not just the nationals — those hold the granular local coverage.
4. Pivot: open each paper's site and run its on-site search for the subject's `name`, or feed the paper's `domain` into a `site:` Google/Yandex query and into archive tools for deleted articles.

## Inputs → Outputs
- **In:** `geolocation` / `address` (country, state, city)
- **Out:** `domain`s of matching newspapers (a shortlist to search individually)
- **Empty/negative result looks like:** a sparse or empty list for very small localities — fall back to a broader region, or to a national paper's regional section.

## Gotchas & OpSec
- This is a *directory*, not a search engine over article text — it points you at papers; you still do the reading on each site.
- Human-in-the-loop: none for browsing; individual newspaper sites may carry their own paywalls or logins.
- OpSec: passive. The subject is never queried; only your later searches on the linked papers carry any footprint.

## Overlaps ("do both")
- Pairs with `[[paperboy]]` (the same project's front-pages/archive view) — use this to pick the right titles, that to read front pages.

## Trust & verifiability
`trust: community` — an independent, long-lived curated directory; treat it as a reliable pointer to publications, and verify any personal detail on the newspaper's own page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thepaperboy |
| category | communities-forums |
| selectorsIn → selectorsOut | geolocation, address → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
