---
id: siteliner
name: Siteliner
description: Use when you have a `domain` and want a content/link audit — returns duplicate-content matches, broken links and page inventory for the site.
url: https://www.siteliner.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- analytics
bestFor: Auditing a website for duplicate content, broken links, and its page structure.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free scan covers up to ~250 pages per domain; Siteliner Premium (from the makers of Copyscape) removes limits and adds history.
opsec: active
opsecNote: Siteliner CRAWLS the target site to build its report, so requests hit the site and appear in its logs (from Siteliner's crawler, not you directly). Fine for public sites; avoid if you don't want a crawl footprint on a sensitive target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established SEO-audit tool by Indigo Stream Technologies (Copyscape); reliable for content/link structure, though a third-party crawl-based estimate.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Siteliner audit
tags:
- domains-ip-infrastructure
- analytics
- seo
- duplicate-content
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Siteliner

> A site-audit tool that crawls a website and reports duplicate content, broken links, and its page inventory — handy for understanding and fingerprinting a target site's structure.

## When to use
You have a `domain` and want a quick structural picture: which pages exist, which contain duplicate/templated content, and where the broken links are. Beyond SEO, the duplicate-content view can reveal that a site is templated/cloned, and the page inventory surfaces URLs you might otherwise miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.siteliner.com/ and enter the `domain`.
2. Let it crawl (free scan covers up to ~250 pages).
3. Read the report: duplicate-content percentage and matching pages, broken links, page count, and average page size/load.
4. Pivot: the page inventory feeds content review and archiving; heavy duplicate content across "different" sites hints they share a template/operator — cross-check with reverse-analytics tools.

## Inputs → Outputs
- **In:** `domain`
- **Out:** duplicate-content matches, broken links, and a page inventory for the `domain`
- **Empty/negative result looks like:** a tiny report for a small/single-page site, or a crawl blocked by robots.txt — Siteliner then sees little.

## Gotchas & OpSec
- It actively crawls the target — a footprint appears in the site's logs (as Siteliner's crawler).
- Free scan is capped (~250 pages); large sites need Premium for full coverage.
- Duplicate-content detection is within/near the site — for cross-web plagiarism use Copyscape.

## Overlaps ("do both")
- Pairs with `[[similarweb]]` and reverse-analytics tools — Siteliner maps the site's internal structure/duplication; those add audience size and cross-site operator links.

## Trust & verifiability
`trust: community` — a solid, established audit tool; results are its crawler's view of the site, accurate for structure but a third-party estimate, so confirm anything pivotal directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | siteliner |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
