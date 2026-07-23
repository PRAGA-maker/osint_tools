---
id: whoismind
name: WhoisMind
description: Use when you have an `ip-address` and want its location and neighboring sites — returns `geolocation`, ISP/ASN, and reverse-IP `domain`s hosted on it.
url: https://www.whoismind.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reverse-IP lookups (what else is hosted on this IP) plus IP geolocation and ISP context.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
- domain
status: live
pricing: free
costNote: Free web lookups; no account needed.
opsec: passive
opsecNote: "WhoisMind answers from its own IP/hosting database, so you don't touch the target's server — passive. Your queries are logged by whoismind.com; use a sock-puppet session for sensitive lookups. Its self-stated disclaimer that it is not an FCRA consumer-reporting service means results are informational leads, not vetted records."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free IP/reverse-IP utility; reverse-IP and geolocation data are approximate and drawn from third-party feeds, so co-hosted domains and locations are leads to verify, not confirmed facts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whois-service
aliases:
- WhoisMind
- whoismind.com
tags:
- domain-and-ip-research
- reverse-ip
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# WhoisMind

> A free IP-intelligence tool: give it an IP and get its geolocation, ISP/ASN, and the other domains that resolve to the same address (reverse IP).

## When to use
You have an `ip-address` — from an email header, a server log, or a domain lookup — and want to know roughly where it sits (`geolocation`, ISP), and, more usefully, what other `domain`s are hosted on it (reverse IP), which can link a target to their other web properties on shared hosting. Infrastructure-oriented, so direct missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.whoismind.com in a sock-puppet browser.
2. Enter the target `ip-address` (it also offers name/email helper lookups).
3. Read the results: city/region `geolocation`, ISP/ASN, and the reverse-IP list of co-hosted `domain`s.
4. Treat co-hosted domains on shared hosting cautiously — hundreds of unrelated sites can share one IP; a dedicated IP makes the link far stronger.
5. Pivot a promising co-hosted `domain` into WHOIS/passive-DNS tools.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** `geolocation`, ISP/ASN, reverse-IP `domain` list
- **Empty/negative result looks like:** no reverse-IP domains or a generic country-level location — the IP may be dedicated, freshly assigned, or behind a CDN; absence of neighbors isn't proof of isolation.

## Gotchas & OpSec
- Reverse IP on shared hosting is noisy — co-location ≠ common ownership unless the IP is dedicated. Weight the link accordingly.
- Geolocation is ISP/region level, not a physical address.
- Free-feed data can be stale; corroborate with a live WHOIS/DNS query before relying on any link.

## Overlaps ("do both")
- Pairs with [[whois-service]] and [[ipinfo-map]] — WhoisMind gives reverse-IP neighbors, WHOIS gives registration/ownership, and IP mapping visualizes location; run together to separate real links from shared-hosting noise.

## Trust & verifiability
`trust: community` — a free utility over third-party feeds; its own disclaimer flags results as informational, so treat every co-hosted domain and location as a lead to confirm, not a fact.
