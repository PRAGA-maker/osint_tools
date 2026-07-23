---
id: trend-micro-site-safety-center
name: Trend Micro Site Safety Center
description: Use when you have a `domain`/URL and want a vendor safety verdict and content category — returns a reputation rating and classification.
url: https://global.sitesafety.trendmicro.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Getting Trend Micro's safety rating and content category for a domain/URL.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free web lookup, no account. (Trend Micro also offers a reclassification-request flow, but querying a rating is free.)
opsec: passive
opsecNote: You query Trend Micro's pre-scanned reputation database, not the target site, so the subject sees nothing. Only Trend Micro sees the domain you check. Don't then browse a flagged-dangerous URL from a real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party reputation service from Trend Micro, a major security vendor. Categorisation is automated and can be stale or coarse for small/new sites; it's a reputable signal, not a verdict.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Trend Micro Site Safety
- sitesafety.trendmicro.com
tags:
- reputation
- url-reputation
- safe-browsing
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Trend Micro Site Safety Center

> Trend Micro's free URL reputation lookup — check a domain's safety rating (safe / suspicious / dangerous / untested) and its content category from a major vendor's database.

## When to use
You have a `domain` or URL and want a quick, independent reputation read: is it flagged malicious/phishing, and what content category has Trend Micro assigned it? Useful as one vote among several when assessing a suspicious link in a case, or to see how a site is categorised (e.g. "disease vector", "phishing", "shopping").

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://global.sitesafety.trendmicro.com/ .
2. Enter the `domain`/URL and submit.
3. Read the verdict: a safety rating (Safe / Suspicious / Dangerous / Untested) plus an assigned content category.
4. Weigh "Untested" carefully — it means Trend Micro has no rating, not that the site is safe.
5. Pivot: a "dangerous/suspicious" verdict corroborates a phishing/malware assessment; cross-check with other reputation feeds before acting.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** safety rating + content category for that `domain`
- **Empty/negative result looks like:** "Untested" / no category — the site isn't in Trend Micro's database; treat as *unknown*, not *clean*.

## Gotchas & OpSec
- Ratings are automated and can lag reality; a freshly-weaponised domain may still read "Safe/Untested".
- Categorisation is coarse and occasionally wrong for niche sites; use as a signal, not proof.
- OpSec: **passive** — only Trend Micro sees your query; never visit a flagged URL from a real browser to "confirm".

## Overlaps ("do both")
- One vote among reputation sources — combine with `[[https-openphish-com-feed-txt]]`, VirusTotal, and Google Safe Browsing; consensus across vendors is far stronger than any single verdict.

## Trust & verifiability
`trust: trusted` — a first-party service from an established vendor. The rating is a credible signal but automated; corroborate across multiple reputation tools before treating a domain as definitively malicious or clean.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trend-micro-site-safety-center |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
