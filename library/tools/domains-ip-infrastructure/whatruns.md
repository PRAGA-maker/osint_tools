---
id: whatruns
name: WhatRuns
description: Use when you have a `domain` and want to fingerprint the technologies running a website (CMS, analytics, CDN, plugins, fonts) — returns tech-stack details and pivotable tracker/analytics IDs linking related `domain`s.
url: https://www.whatruns.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-click tech-stack fingerprint of a website, including analytics/tracker IDs that can tie sites to a common owner.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free browser extension; no registration required.
opsec: active
opsecNote: The extension fingerprints the page you are actually viewing, so you load the target site directly from your IP. Use a sock-puppet browser/VPN if the owner might notice a visit; do not log into anything.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular third-party extension (~450k users). Detection is heuristic pattern-matching and can miss or misattribute technologies.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- vstat-info
aliases: []
tags:
- Domain/IP/Links
- Website technology look up
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# WhatRuns

> A one-click technology fingerprinter for websites — see the CMS, analytics, CDN, plugins and fonts behind any page, and harvest the tracker IDs that can link separate sites to one operator.

## When to use
You have a `domain` (a target's blog, shop, forum, scam site) and want to know what it's built on. Two OSINT payoffs: (1) the stack itself (WordPress + specific plugins, a payment provider, a chat widget) narrows who could run it; (2) analytics/ad IDs (Google Analytics/AdSense, Facebook Pixel) are reusable fingerprints — the same ID on another site strongly suggests common ownership, giving you a new `domain` to chase.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install WhatRuns for Chrome/Firefox.
2. Browse to the target site in a clean/sock-puppet profile.
3. Click the WhatRuns toolbar icon — it lists detected apps grouped by category (CMS, analytics, hosting, widgets, fonts…).
4. Note any embedded IDs (UA-/G- analytics, pub- AdSense, pixel IDs) shown or visible in page source.
5. Pivot: paste a shared analytics/AdSense ID into a reverse-analytics service (e.g. a "sites using this ID" lookup) to surface sibling `domain`s.

## Inputs → Outputs
- **In:** `domain` (the site you visit)
- **Out:** technology inventory + tracker/analytics IDs → candidate related `domain`s
- **Empty/negative result looks like:** a short or generic list (e.g. only "Nginx", "Cloudflare") when a site is heavily proxied/obfuscated — the CDN masks the real stack. Absence of a detected ID doesn't mean none exists.

## Gotchas & OpSec
- Human-in-the-loop: none; but you must actually load the page.
- OpSec: **active** — you visit the target from your own browser/IP. Use a burner profile and VPN for sensitive targets; never authenticate.
- Detection is best-effort; confirm any critical finding against page source or a second fingerprinter.

## Overlaps ("do both")
- Pairs with `[[vstat-info]]` — WhatRuns tells you what a site is built with, vstat.info estimates who visits it; together they profile a domain's stack and reach.

## Trust & verifiability
`trust: community` — a widely-used but third-party heuristic tool; good for leads, verify the load-bearing findings (especially shared IDs) manually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatruns |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
