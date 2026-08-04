---
id: larger-io
name: Larger.io
description: Use when you have a `domain` and want the technologies running on it — returns the site's tech stack (analytics IDs, CMS, hosting, payment, frameworks) for fingerprinting and pivoting.
url: https://www.larger.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fingerprinting a website's technology stack (and analytics/tracking IDs) to characterise and correlate infrastructure.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free tier ~25 anonymous web lookups/day and ~1,000 API calls/month, no card required; paid plans for higher volume.
opsec: passive
opsecNote: Larger.io reports from its own daily-refreshed crawl of ~15M domains, so a lookup does not touch the target's server — you are not fingerprinting the site live. Nothing is disclosed to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial tech-lookup service built on a large crawl; detections are heuristic and can lag site changes, so treat the stack (and any IDs) as leads to confirm.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- larger.io
tags:
- Domain/IP/Links
- Website technology look up
- tech-stack
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Larger.io

> A Wappalyzer-style technology-lookup service over a large daily crawl — give it a `domain` and it returns the analytics, CMS, hosting, payment and framework tech behind the site, including trackable IDs to pivot on.

## When to use
You have a `domain` and want to characterise the operation behind it or link it to others. The tech stack — and especially shared analytics/ad IDs (Google Analytics UA/GA4, AdSense) or a distinctive CMS/host combination — can tie separate sites to the same owner. Larger.io fingerprints a site from its own crawl, useful for scoping infrastructure and finding a starting point for ID-based correlation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.larger.io/ and enter the target `domain` (free tier ~25 lookups/day; API for bulk).
2. Review the detected technologies by category (analytics, CMS, hosting, payment, frameworks).
3. Note any shared/trackable identifiers or unusual stack choices as correlation leads.
4. Pivot: take an analytics/ad ID into an ID-correlation tool (e.g. reverse-analytics search) and the hosting/IP into WHOIS/DNS tools to find sibling sites.

## Inputs → Outputs
- **In:** `domain`
- **Out:** detected technology stack and identifiers; leads toward related `domain`s that share IDs/infrastructure
- **Empty/negative result looks like:** few/no technologies detected — a very small, cloaked, or newly changed site; the crawl may also be stale, so verify against a live fingerprinter.

## Gotchas & OpSec
- Human-in-the-loop: none; free tier is rate-limited (~25/day).
- OpSec: passive — data comes from Larger.io's crawl, not a live hit on the target; nothing reaches the subject.
- Freshness: crawl-based detections can lag recent site changes; confirm a load-bearing detection with a live tool.

## Overlaps ("do both")
- Pairs with live tech-fingerprinters (Wappalyzer/BuiltWith) and reverse-analytics-ID search because this gives the stack/IDs while those confirm them live and expand ID matches into a domain cluster.

## Trust & verifiability
`trust: community` — a commercial crawl-based service; detections are heuristic and possibly dated, so use the stack and IDs as leads and verify before asserting a link.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
