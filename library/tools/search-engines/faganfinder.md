---
id: faganfinder
name: FaganFinder
description: Use when you need the right search engine/tool for a task and don't know it exists — a curated portal of specialist search tools by category.
url: http://www.faganfinder.com/engines
category: search-engines
path:
- search-engines
bestFor: Discovering the best specialist search engine or database for a specific need (images, academic, news, government, social, dark web) rather than defaulting to Google.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free directory; some tools it links to may themselves be paid, but FaganFinder access is free.
opsec: passive
opsecNote: A static link directory — you browse categories and click out to other tools. No target is queried; fully passive. OpSec depends on the downstream tool you choose.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running (since 2001), individually maintained by Michael Fagan; a respected, curated meta-directory rather than an automated scraper.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Fagan Finder
- faganfinder.com
tags:
- search-portal
- directory
- meta-search
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# FaganFinder

> A veteran, human-curated portal of "the largest, broadest, most significant tools for finding information" — go here when Google isn't the right engine and you need to find the one that is.

## When to use
You have a research need (find a scholarly paper, a specific image type, a government dataset, a news archive, a social-media search) and want a shortlist of the best specialist engines for it, with notes on when to use each. FaganFinder is orientation/discovery tooling — it finds tools, not people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.faganfinder.com/engines.
2. Browse the category matching your need — web, images, video/audio, academic, news, government/data, books/libraries, social, or dark web.
3. Read the short notes on each listed tool to pick the right one for your task.
4. Click through to the chosen engine and run your actual search there.
5. Bookmark categories you return to; it's a launchpad, not a destination.

## Inputs → Outputs
- **In:** none (you browse by category)
- **Out:** curated links to specialist search engines/tools with usage notes
- **Empty/negative result looks like:** not applicable — it always returns its directory; the "miss" is if no listed tool fits, in which case broaden the category.

## Gotchas & OpSec
- It's a directory, not a search engine — it points you elsewhere and finds nothing itself.
- Some listed resources are paid or region-restricted; check before relying on them.
- The design is dated but the curation is current and well-regarded.

## Overlaps ("do both")
- Overlaps with OSINT Framework and similar directory tools — FaganFinder is broader/less OSINT-specific, so use both when scoping which tool to reach for.

## Trust & verifiability
`trust: trusted` — a long-standing, personally-curated directory; the links are vetted, though the ultimate data quality comes from whichever tool you follow to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | faganfinder |
