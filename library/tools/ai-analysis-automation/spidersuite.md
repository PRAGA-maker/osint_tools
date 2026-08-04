---
id: spidersuite
name: SpiderSuite
description: Use when you have a `domain`/URL and want to crawl and map a site's full structure, links, and assets — returns discovered URLs, endpoints, and a link graph for reconnaissance.
url: https://github.com/3nock/SpiderSuite
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Cross-platform GUI web crawling to enumerate a target site's pages, subdomains, and linked assets during recon.
selectorsIn:
- domain
selectorsOut:
- domain
- document-id
status: live
pricing: free
costNote: Free and open-source; download a release build and install per the wiki.
opsec: active
opsecNote: Crawling actively fetches every page of the target site from YOUR machine/IP, generating traffic in the target's server logs — this is NOT passive. Use a VPN/proxy, throttle the crawl, and only crawl sites you're authorised to (or that are clearly public) to avoid legal/abuse issues.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Open-source project (~1k stars) with active community (Discord); a community tool you run yourself, so audit the build and verify findings.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- ote-osint-template-engine
- sub3-suite
aliases:
- Spider Suite
- 3nock SpiderSuite
tags:
- web-crawler
- reconnaissance
- spider
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# SpiderSuite

> A cross-platform GUI web crawler for reconnaissance — point it at a site and get back the full map of its pages, links, and assets.

## When to use
You have a `domain`/URL and need to understand a website's whole structure: every reachable page, linked subdomain, form, and asset. In OSINT this surfaces content that isn't obvious from the front page — old pages, staff/contact pages, uploaded documents, dev artifacts — and builds a link graph you can mine for `email`s, `document-id`s, and further `domain`s. Reach for it when a target site is worth mapping exhaustively rather than browsing by hand.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download a release build from the GitHub releases page and install following the wiki (cross-platform: Windows/Linux).
2. Launch the GUI, enter the target `domain`/seed URL, and configure crawl depth/scope.
3. Run the crawl; watch it enumerate URLs, links, and assets into a browsable tree/graph.
4. Export/review the discovered endpoints and documents.
5. Pivot: harvested `document-id`s go to metadata analysis; discovered subdomains/`domain`s feed infrastructure OSINT; contact pages yield `email`s.

## Inputs → Outputs
- **In:** `domain`/seed URL
- **Out:** discovered `domain`s/subdomains, URLs and `document-id`s (site map + link graph)
- **Empty/negative result looks like:** a shallow crawl with few URLs — the site may be a JS-heavy SPA (limited link discovery), block crawlers, or genuinely be small; adjust scope/depth and consider a JS-aware crawler.

## Gotchas & OpSec
- Crawling is **active** and traffic-heavy from your IP — throttle it, use a proxy/VPN, and stay within authorised/public scope.
- SPA/JS-rendered sites limit link discovery for traditional crawlers.
- It's a tool you run yourself — audit the release build.

## Overlaps ("do both")
- Complements passive site-mapping (sitemaps, web-archive crawls) and content-search dorks: SpiderSuite actively enumerates the *live* site, while archives show historical pages and dorks find indexed content — do all three for full coverage of a domain.

## Trust & verifiability
`trust: community` — an open-source community crawler; the code is auditable but you're responsible for running it lawfully and for verifying that discovered URLs/assets are what they appear to be.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spidersuite |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
