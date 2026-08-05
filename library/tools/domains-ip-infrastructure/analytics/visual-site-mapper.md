---
id: visual-site-mapper
name: Visual Site Mapper
description: Use when you have a `domain` and want a fast visual map of its internal link structure and connected pages — returns a `domain` link graph to spot hidden sections.
url: https://github.com/alentum/sitemapper-nodejs
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- analytics
bestFor: Quickly visualising a website's internal page structure and interlinking to find sections that aren't in the main navigation.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free hosted service (visualsitemapper.com); source is open (AGPL-3.0) if you want to self-host with Node.js/MongoDB.
opsec: passive
opsecNote: Using the hosted service is passive for you — visualsitemapper.com's servers crawl the target, so the requests come from the service, not your IP. Note this still hits the target site; if you SELF-HOST the Node crawler, the crawl originates from your machine (active) — run it from an attributable-to-nobody VPS.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project (alentum) with a public hosted instance; it renders a link graph from a live crawl, so results reflect the site at query time rather than any stored dataset.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- visualsitemapper.com
- Site Mapper
tags:
- Domain/IP investigation
- website-structure
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Visual Site Mapper

> Enter a domain and get an interactive graph of its internal pages and how they link together — a quick way to see a site's shape and surface pages the top nav hides.

## When to use
You have a subject's or organisation's `domain` and want to understand the site's structure fast: which pages exist, how they cluster, and whether there are sections (staff pages, archives, member areas, orphaned pages) not linked from the front page. A structural map guides where to look for names, contact details, documents, or a `[[sitemap]]`-style inventory of a small-to-medium site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the hosted service at visualsitemapper.com (source at the GitHub URL if you prefer to self-host).
2. Enter the target `domain` and let it crawl; a node-link map of internal pages renders.
3. Explore the graph — dense clusters are major sections; isolated nodes are often the interesting/forgotten pages.
4. Pivot: open the pages the map reveals to extract `name`/`email`/`address`/document leads, and feed the domain into infrastructure tools (DNS, WHOIS, subdomain enumeration) for the parts a page-crawl can't see.

## Inputs → Outputs
- **In:** `domain` (or a URL seed)
- **Out:** a `domain`-internal page link graph (structure/URLs; not a records dataset)
- **Empty/negative result looks like:** a sparse or single-node map — the site blocks crawling, is a JS-only SPA, or is genuinely tiny; switch to a crawler that renders JS or to sitemap.xml.

## Gotchas & OpSec
- Best for small/medium sites; very large sites get truncated or slow.
- JavaScript-rendered sites and robots.txt/crawl blocks limit what it can see.
- Hosted use is passive for you; self-hosting makes the crawl attributable to your infrastructure — isolate it.

## Overlaps ("do both")
- Pairs with subdomain-enumeration and DNS tools: this maps the pages *within* one host, those find the *other* hosts under the domain — together you get the full footprint.

## Trust & verifiability
`trust: community` — open-source with a public instance; because the map is generated from a live crawl, you can verify any node by simply opening the URL it points to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | visual-site-mapper |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
