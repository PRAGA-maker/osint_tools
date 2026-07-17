---
id: httparchive-org
name: HTTP Archive
description: Use when you have a `domain` and want its historical tech stack and third-party dependencies — returns detected technologies, request `domain`s and infra fingerprint.
url: https://httparchive.org
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Profiling what technologies, trackers and third-party hosts a website loads, over time, from a public crawl dataset.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open public dataset (reports on the site; full data via the Google BigQuery public dataset). No account for the reports; BigQuery needs a free Google Cloud account.
opsec: passive
opsecNote: You query a pre-collected crawl archive, never the target site, so the subject's server sees nothing from you. Ideal for recon on a site you don't want to touch directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-running, transparent open-source project (now under the HTTP Archive/Google umbrella) crawling the top sites; data is reproducible and openly published.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- httparchive.org
- HTTP Archive dataset
tags:
- web-technology
- tech-stack
- passive-recon
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# HTTP Archive

> A public archive that periodically crawls the top sites and records exactly what each page loads — the technologies, scripts, trackers and third-party hosts — letting you fingerprint a `domain`'s infrastructure without touching it.

## When to use
You have a `domain` and want to know how it's built and who it talks to: CMS/framework, analytics and ad trackers, tag IDs, CDN, and every third-party `domain` it pulls resources from. Because HTTP Archive stores historical crawls, you can also see how a site's stack changed over time. Shared analytics/AdSense IDs or a distinctive third-party set can link seemingly separate sites to the same operator — a passive-recon pivot that never alerts the target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://httparchive.org and browse the reports (tech adoption, Core Web Vitals) or the Web Almanac.
2. For a specific `domain`, use the Google BigQuery public dataset (`httparchive`) — query the crawl tables for that site's detected technologies, requests and response metadata.
3. Read the results: detected tech (Wappalyzer-style), the list of third-party request `domain`s, and embedded IDs.
4. Compare across dates to see stack changes, or across sites to find shared infrastructure/trackers.
5. Pivot: take shared analytics/tag IDs and third-party `domain`s into infrastructure-correlation tooling to connect related sites.

## Inputs → Outputs
- **In:** `domain`
- **Out:** detected technologies, third-party request `domain`s, embedded tracker/tag IDs, historical stack
- **Empty/negative result looks like:** the domain isn't in the crawl — HTTP Archive samples top/popular sites, so small or obscure domains may be absent. Absence is a coverage gap, not a finding; fall back to a live tech-fingerprint tool.

## Gotchas & OpSec
- OpSec: **passive** — an archived dataset; the target site is never contacted by you.
- Coverage is the crawled top-sites sample; niche sites often aren't included.
- Detailed per-domain analysis lives in BigQuery (needs a free Google Cloud account); the website itself mostly shows aggregate reports.

## Overlaps ("do both")
- Pairs with live tech-fingerprint tools (Wappalyzer, BuiltWith) and `[[fullhunt]]` — HTTP Archive gives historical/passive stack data; the live tools cover any domain right now.

## Trust & verifiability
`trust: trusted` — an open, reproducible dataset; anyone can re-run the same BigQuery and get the same crawl facts, so findings are verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | httparchive-org |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
