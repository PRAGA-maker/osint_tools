---
id: gotanda
name: Gotanda
description: Use when you have a `domain`, `ip-address` or URL on a web page and want to pivot it across many OSINT engines from a right-click menu — returns links into domain/IP lookups.
url: https://chrome.google.com/webstore/detail/gotanda/jbmdcdfnnpenkgliplbglfpninigbiml
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Right-click pivoting of a highlighted domain/IP/URL into dozens of OSINT lookup services at once.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free, open-source browser extension (Chrome/Firefox); no account or payment.
opsec: passive
opsecNote: The extension only builds and opens query URLs — but each service you launch (Censys, AbuseIPDB, SecurityTrails, etc.) then receives the indicator and your request. That is passive toward the target (you never touch their infrastructure), yet it fans your indicator out to many third parties; use a sock-puppet browser profile and be mindful which services log queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source project by HASH1da1 (GitHub HASH1da1/Gotanda); code is inspectable, but it is a community tool, not an official product.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- HASH1da1/Gotanda
tags:
- Domain/IP/Links
- Domain/IP investigation
- browser-extension
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Gotanda

> A browser extension that turns any highlighted indicator on a page — IP, domain, URL — into a right-click launcher across dozens of OSINT engines.

## When to use
You're reading a page (a report, a paste, a WHOIS record, a forum post) and it contains an IOC — a `domain`, `ip-address`, or URL — that you want to investigate across many services without copy-pasting into each one. Gotanda adds a context-menu that fires the selected indicator into search/lookup engines like Censys, SecurityTrails, AbuseIPDB, HackerTarget, ThreatCrowd, whoisds and more, plus quick social-timeline searches. It's a pivot accelerator layered on top of tools you already use.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Gotanda from the Chrome Web Store (or build the Firefox/Chrome extension from github.com/HASH1da1/Gotanda) in a dedicated investigation browser profile.
2. On any web page, highlight the indicator you care about — an IP, domain, or URL.
3. Right-click and open the Gotanda context menu; pick the target lookup service (or category of services).
4. The extension opens the corresponding lookup in a new tab with your indicator pre-filled; read each service's result as you would natively.
5. Pivot: use the aggregated views (WHOIS, passive DNS, IP reputation, certs) to decide which single service to go deep on next.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or URL highlighted on a page
- **Out:** pre-filled lookups on many third-party engines returning WHOIS, passive DNS, reputation, certificate and related `domain`/`ip-address` data
- **Empty/negative result looks like:** the extension always opens the query; "empty" is per-service (a given engine has no record for the indicator). Gotanda itself doesn't hold data — it routes you to sources.

## Gotchas & OpSec
- Human-in-the-loop: none beyond installing the extension and choosing services.
- OpSec: **passive** toward the subject, but it broadcasts your indicator to many external services at once — each may log it. Use a sock-puppet profile; disable it when not investigating.
- It's a launcher, not a data source: results quality depends entirely on the downstream engines, some of which now gate results behind logins or rate limits.

## Overlaps ("do both")
- Complements the individual lookup services it links to (Censys, SecurityTrails, AbuseIPDB, etc.) — Gotanda is the fast pivot layer, while those tools are where the actual analysis happens.

## Trust & verifiability
`trust: community` — an open-source extension (source on GitHub) with no official backing. The extension only constructs query URLs, which you can audit in the code; trust in any given result rests on the underlying third-party service, not on Gotanda.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gotanda |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
