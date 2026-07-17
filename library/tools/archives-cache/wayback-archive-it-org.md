---
id: wayback-archive-it-org
name: Wayback.archive-it.org
description: Use when you have a `domain` or URL and want to find it inside a curated institutional web-archive collection (governments, universities, NGOs, libraries) — returns archived captures (document-id) not always present in the main Wayback index.
url: http://wayback.archive-it.org/
category: archives-cache
path:
- archives-cache
bestFor: Finding archived captures of a page inside themed collections curated by libraries, universities, and government bodies.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to search and browse public collections. Archive-It is a subscription service for the institutions that build collections, but reading the resulting public archives costs nothing.
opsec: passive
opsecNote: You query the Internet Archive's Archive-It infrastructure, not the target site, so the subject sees nothing. Only the Archive logs your request. Safe without a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Internet Archive on behalf of named partner institutions; captures are timestamped and attributable to the curating organization, so provenance is strong.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- archive-org
- archive-vn
- archive-it
- archive-it-org
aliases:
- Archive-It
- Archive-It Wayback
tags:
- Archives
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Wayback.archive-it.org

> The public Wayback front-end for Archive-It — the Internet Archive's curated-collections program, where libraries, universities, and governments crawl specific sites into themed archives.

## When to use
You have a `domain` or URL and the main Wayback Machine has no (or a poor) capture, but the site is the kind an institution would deliberately preserve — a government agency page, an election campaign site, a university department, an NGO, a news outlet covering a specific event. Because partner institutions crawl targeted sites deeply and on their own schedules, Archive-It sometimes holds captures that web.archive.org missed, plus richer coverage of niche or short-lived pages tied to a curated topic.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://wayback.archive-it.org/ and enter the target URL, or browse https://archive-it.org/explore to search across collections and organizations.
2. Use the collection browser to narrow by curating institution or theme (e.g. a state library's "local government" collection) when you know who would have archived the target.
3. Open a capture to read the page as preserved by that institution; note the collection name for provenance in your report.
4. Pivot: recovered emails/handles/names feed the matching selector tools; the collection metadata itself can corroborate an organizational affiliation.

## Inputs → Outputs
- **In:** `domain` or full page URL
- **Out:** archived captures (`document-id`) within one or more curated collections
- **Empty/negative result looks like:** no matching captures found — the URL isn't part of any partner institution's crawl. Fall back to [[archive-org]] (the broad Wayback index) or [[archive-vn]] (on-demand capture).

## Gotchas & OpSec
- Coverage is uneven and topic-driven: it is deep where an institution chose to crawl and empty everywhere else. This is a supplement to, not a replacement for, the main Wayback Machine.
- The interface is dated and collection search can be clunky; browsing by organization is often faster than free-text search.
- OpSec: **passive** — only the Internet Archive sees your query.

## Overlaps ("do both")
- Pairs with [[archive-org]] because the two indexes overlap only partially; a page absent from one may be present in the other.
- Pairs with [[archive-vn]] for on-demand capture of anything neither Wayback index holds.

## Trust & verifiability
`trust: trusted` — operated by the Internet Archive and populated by named partner institutions, so each capture is timestamped and attributable to a real curating organization.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayback-archive-it-org |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
