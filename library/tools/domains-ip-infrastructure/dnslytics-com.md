---
id: dnslytics-com
name: dnslytics.com
description: Use when you have a `domain` or `ip-address` and want to find other domains sharing its Analytics/AdSense ID, IP, or nameservers — returns linked `domain`s revealing common ownership.
url: https://dnslytics.com/reverse-analytics
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Pivoting from a domain/IP/Analytics-ID to the network of other domains owned or operated by the same party.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free tier returns limited results per lookup (reverse IP/NS/Analytics, WHOIS, basics). Full historical data and the complete 20M+ Analytics-ID database require a paid plan.
opsec: passive
opsecNote: Queries hit DNSlytics' own dataset, not the target's infrastructure, so the subject is not alerted. DNSlytics logs your searches; use a clean session for sensitive pivots. Do not run the live "ping/traceroute" style tools against a target if you want to stay passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial DNS/domain intelligence aggregator with an 8+ year history index. Reverse data is a strong lead but connection inferences (shared Analytics ID) should be corroborated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- search-dnslytics-com
- tcp-ip-utils-domain-neighbors
aliases:
- DNSlytics
- dnslytics reverse analytics
tags:
- domainsandips
- dns
- reverse-analytics
- infrastructure
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# dnslytics.com

> Domain-connection engine: given a domain, IP, or Google Analytics/AdSense ID, find every other site that shares it — the classic way to unmask a person's or company's wider web footprint.

## When to use
You have a `domain` (or an `ip-address`, or a tracking ID pulled from a page's source) and want to discover what *else* the same operator runs. Shared Google Analytics (`UA-/G-/GTM-`) or AdSense (`pub-`) IDs, a common IP, or shared nameservers frequently tie a scam network, a person's cluster of side projects, or a company's brands together. This is a core infrastructure-pivot tool for expanding from one asset to a whole footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dnslytics.com/ and pick the relevant reverse tool (Reverse Analytics, Reverse IP, Reverse NS, Reverse MX/PTR).
2. Enter your selector: a domain, an IP, or an Analytics/AdSense ID (view the target page's HTML source to extract its tracking IDs first).
3. Read the list of connected domains. For Reverse Analytics, matches sharing the exact ID are strong common-ownership signals.
4. Note the free-tier truncation — if only a few of many results show, that's the paywall, not the full picture.
5. Pivot: each returned `domain` goes back through WHOIS/history and social-footprint tools; a confirmed shared Analytics ID is often decisive attribution evidence.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or a tracking/Analytics ID
- **Out:** connected `domain`s (and `ip-address` relationships) sharing the queried asset
- **Empty/negative result looks like:** "no domains found" for a reverse lookup means no *indexed* shared asset — small or private sites may simply not be in the dataset, so absence isn't proof of isolation.

## Gotchas & OpSec
- Free results are capped; a short list may hide a much larger cluster behind the paywall.
- Shared Analytics IDs are strong but not infallible (agencies reuse IDs across clients) — corroborate before asserting single ownership.
- OpSec: passive — you query DNSlytics, not the target. Avoid the live network-probe utilities if staying non-attributable matters.

## Overlaps ("do both")
- Pairs with `[[search-dnslytics-com]]` (same provider, keyword/domain search) and `[[tcp-ip-utils-domain-neighbors]]` — cross-check reverse-IP neighbors on a second source, since shared-hosting IPs produce false links that Analytics-ID matches don't.

## Trust & verifiability
`trust: community` — a commercial aggregator with deep historical DNS data. Reverse-lookup output is reliable as leads; treat inferred ownership connections as hypotheses to confirm against WHOIS, content, and a second reverse-lookup provider.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnslytics-com |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
