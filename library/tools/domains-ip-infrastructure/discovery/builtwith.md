---
id: builtwith
name: BuiltWith
description: Use when you have a `domain` and want to fingerprint the site's technology stack, trackers, and hosting/analytics IDs — returns pivotable `domain` links and infrastructure `ip-address` hints.
url: https://builtwith.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Fingerprinting a website's tech stack and, crucially, pivoting on shared analytics/ad tracking IDs to find other sites the same owner runs.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Core per-domain technology profile is free (no login). Historical data, "Relationships" pivots by shared tracking ID, and bulk lists sit behind paid plans; a limited free account unlocks some extras.
opsec: passive
opsecNote: BuiltWith serves data it already crawled — you never touch the target's server, so nothing is leaked to the site owner. Safe to run without a sock puppet. Do not log in with an attributable account if you want the lookup itself to stay anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established commercial technographics provider (20+ years) with a large, continuously updated crawl; detections are reliable, though absence of a technology is not proof it is unused.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- built-with
- wappalyzer
aliases:
- BuiltWith Technology Lookup
tags:
- toddington
- whois-ip-lookups-website-analysis
- technology-profiling
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# BuiltWith

> Technology-profiling service that reveals what a website is built with — and, more usefully for OSINT, links sites that share the same analytics/ad-tracking IDs.

## When to use
You have a `domain` tied to your subject (a personal blog, a small business, a scam/dating-profile site) and want to (a) understand its stack, or (b) discover **other domains operated by the same person** via shared Google Analytics UA/G-, AdSense, or Facebook Pixel identifiers. The relationship pivot is the investigative payoff: one tracking ID can unmask a whole network of a subject's sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://builtwith.com/ and enter the target `domain` (e.g. `example.com`).
2. Read the profile: CMS, hosting/CDN, analytics, advertising, widgets, email provider, and framework detections, each with a first/last-seen date.
3. Note any **analytics or ad IDs** shown (Google Analytics, AdSense publisher ID, Facebook Pixel). These are the pivot.
4. To find co-owned sites, use the "Relationships" tab / search the tracking ID (some of this is a paid feature; the free profile still surfaces the IDs themselves, which you can then search in `[[spyonweb]]`-style tools or a plain search engine).
5. Pivot: shared UA-/G- IDs → other `domain`s → new WHOIS/registrant leads; hosting/CDN → `ip-address` for infrastructure work.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` (co-owned sites via shared IDs), `ip-address` (hosting/CDN hints), plus a full technology inventory
- **Empty/negative result looks like:** "We haven't found any technologies" or a near-empty profile — common for brand-new domains, sites behind a full CDN/proxy, or ones BuiltWith hasn't crawled. Absence ≠ proof; try a live fetch or `[[wappalyzer]]`.

## Gotchas & OpSec
- Passive: data comes from BuiltWith's own crawl, so the target is not alerted.
- The most valuable feature (reverse-lookup by tracking ID to find co-owned domains) is partly paywalled; the free profile still exposes the raw IDs so you can pivot elsewhere for free.
- Detections lag reality — a "last seen" date can be months old; treat as historical intelligence, not live truth.

## Overlaps ("do both")
- Pairs with `[[wappalyzer]]` — Wappalyzer reads the site live (current stack) while BuiltWith adds history and cross-site relationship data; run both to separate "in use now" from "seen before."

## Trust & verifiability
`trust: trusted` — established commercial technographics vendor with a deep, maintained crawl. Positive detections are dependable; treat missing detections as "unknown," not "absent."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | builtwith |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
