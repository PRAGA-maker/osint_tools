---
id: zoomeye-ai
name: ZoomEye
description: Use when you have an `ip-address`, `domain` or service fingerprint and want internet-wide device/service discovery from pre-scanned data — returns ip-address, domain, geolocation.
url: https://www.zoomeye.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Shodan-style search of internet-facing devices and services by IP, domain, port, banner or fingerprint.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
- geolocation
status: live
pricing: freemium
costNote: Free tier with an account (limited results/queries); paid plans raise limits and unlock API/advanced filters.
opsec: passive
opsecNote: Searches ZoomEye's own pre-scanned internet data, so you do NOT probe the target during a query — the subject's host sees nothing. You must log in, so ZoomEye ties queries to your account; use a sock-puppet account/email for sensitive work.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running internet-scan search engine (operated from China); data is broad but, like all scan engines, can be stale or incomplete, and consider the provider when handling sensitive queries.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools: []
aliases:
- ZoomEye.ai
- zoomeye.org
tags:
- device-search
- attack-surface
- iot
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# ZoomEye

> A Shodan-style search engine over pre-scanned internet data: find exposed devices and services by IP, domain, port, banner or fingerprint — without touching the targets yourself.

## When to use
You have an `ip-address`, `domain`, or a service fingerprint tied to a target and want to know what's exposed on it, or find other hosts that share a fingerprint (same certificate, banner, favicon, title). Because ZoomEye queries its own scan database, you learn about a host's open ports, services, software versions and geolocation passively. Useful for attack-surface mapping, infrastructure attribution, and pivoting from one server to a cluster of related ones.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register/log in at https://www.zoomeye.org/ (use a sock-puppet account for sensitive work).
2. Search by `ip-address`, `domain`, port, service, banner text, or fingerprint (e.g. cert/favicon hashes).
3. Read results: open ports, service banners, software/versions, and `geolocation` per host.
4. Pivot on a distinctive banner/fingerprint to find sibling hosts sharing the same signature.
5. Cross-check with Shodan/Censys (coverage differs) and attribute ownership via `[[hurricane-electric-bgp-toolkit]]`/WHOIS.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, port/service, or a fingerprint/banner
- **Out:** exposed hosts with ports, banners, versions, related `ip-address`/`domain`, and `geolocation`
- **Empty/negative result looks like:** no results — the host may not be in ZoomEye's scan set, may be behind a CDN/firewall, or the fingerprint is too generic; try another scan engine.

## Gotchas & OpSec
- OpSec: passive — searching scan data doesn't probe the target; but you're logged in, so use a sock-puppet account. Consider the provider before submitting sensitive queries.
- Scan data can be stale or partial — a closed-looking port may just be un-scanned; confirm criticality independently (and only actively probe with authorisation).
- Free tier caps results/queries; deep work needs a paid plan.

## Overlaps ("do both")
- Do both with Shodan and Censys — the three scan engines cover different swaths of the internet, so a host missing from one often appears in another; attribute the results with WHOIS/BGP tools.

## Trust & verifiability
`trust: community` — a broad, long-running scan engine; results are verifiable by direct (authorised) checks, but coverage and freshness vary by engine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zoomeye-ai |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
