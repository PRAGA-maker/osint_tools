---
id: hunter-search-engine
name: Hunter (hunter.how)
description: Use when you have a `domain` or `ip-address` and want to enumerate its internet-exposed hosts, open ports, services, and TLS certificates — returns `ip-address`, `domain`, and infrastructure metadata.
url: https://hunter.how/
category: search-engines
path:
- search-engines
bestFor: Fingerprint-based search of internet-connected hosts/IoT devices — find exposed services, banners, and certificates tied to a domain, IP, or product.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
status: live
pricing: freemium
costNote: Free registered tier gives a monthly quota of web + API queries; higher volume, more filters, and data export require paid plans. An API key (free tier) is needed for programmatic use.
opsec: active
opsecNote: hunter.how serves results from its own internet-wide scans, so browsing results is passive. BUT the moment you connect to a discovered host/port yourself to verify it, that is active and hits the target's infrastructure — do that only from attributable-safe infrastructure and with authorization.
humanInLoop: true
humanInLoopReason:
- api-key
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: A Shodan/Censys-class internet-asset search engine (operated by the Hunter.how team, distinct from the email tool Hunter.io); scan data is generally accurate but reflects last-scan time, not live state.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- shodan
- censys
aliases:
- hunter.how
- Hunter internet asset search
tags:
- speciality-search-engines
- attack-surface
- iot-search
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Hunter (hunter.how)

> An internet-wide asset search engine — query by IP, domain, service, or product and get back the exposed hosts, open ports, banners, and certificates that match.

## When to use
You are mapping the **infrastructure** side of an investigation: you have a `domain` or `ip-address` (a subject's server, a scam site's host, a company's netblock) and want to know what services it exposes, what certificates it presents, and what neighboring hosts share the same fingerprint. Useful for confirming a server's identity, spotting misconfigured exposed panels, and pivoting from one host to a cluster of related ones. (Note: this is *not* Hunter.io, the email-finder — different product.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://hunter.how/ (needed for meaningful quota) and grab your API key from the dashboard if you want programmatic queries.
2. Search by a filter expression: `ip="x.x.x.x"`, `domain="example.com"`, `product="nginx"`, or certificate/port filters.
3. Read the result cards: IP, port, service/product + version, banner, TLS certificate subject/SAN, geolocation, and last-scan time.
4. Pivot on shared attributes — a certificate SAN or favicon hash can reveal other `ip-address`es / `domain`s run by the same operator.
5. For automation, call the search API (`hunter.how/search-api`) with your key, respecting the free-tier rate limit.

## Inputs → Outputs
- **In:** `domain`, `ip-address` (also product/service/certificate filter strings)
- **Out:** `ip-address`, `domain`, plus open ports, service banners, certificate data, and geolocation of hosts
- **Empty/negative result looks like:** zero matching hosts — either the asset is not internet-exposed, sits behind a CDN/proxy, or has not been scanned yet. Absence is not proof the host is offline.

## Gotchas & OpSec
- Human-in-the-loop: an account + API key is required, and the free tier is rate-limited — pace queries.
- Browsing scan data is passive; **verifying** a finding by connecting to the host yourself is active and touches the target — get authorization first.
- Data reflects the last scan, which can be days/weeks old; confirm anything time-sensitive.

## Overlaps ("do both")
- Pairs with `[[shodan]]` and `[[censys]]` — coverage and scan cadence differ between these engines, so a host missing from one often appears in another; run the same query across all three when mapping infrastructure.

## Trust & verifiability
`trust: community` — a legitimate internet-asset scanner in the Shodan/Censys family. Findings are as fresh as the last scan; cross-check with another engine before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hunter-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (api-key, rate-limit) |
