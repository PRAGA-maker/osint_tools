---
id: cloudflare-radar
name: Cloudflare Radar
description: Use when you have a `domain` or `ip-address` and want internet-intelligence on it — returns domain rankings, traffic/AS data, URL-scan results and outage/trend context.
url: https://radar.cloudflare.com
category: search-engines
path:
- search-engines
bestFor: Checking a domain/IP against Cloudflare's global network data — popularity rank, hosting/AS info, a safe URL scan, and connectivity/traffic trends.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free public dashboards and a free URL scanner; no account for browsing. Some deep API/data features may need a free Cloudflare account or API token.
opsec: passive
opsecNote: Domain/AS/trend lookups query Cloudflare's own aggregated data — passive, the target's server isn't touched. The URL Scanner, however, actively visits the target URL from Cloudflare's infrastructure (not your IP); prefer a private scan so results aren't publicly listed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Cloudflare from its own global network telemetry; authoritative for traffic/routing trends and a reputable URL-scanning source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Cloudflare Radar
- radar.cloudflare.com
tags:
- speciality-search-engines
- domain
- infrastructure
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Cloudflare Radar

> Cloudflare's public window onto the internet — domain popularity rankings, routing/AS data, a safe URL scanner, and traffic/outage trends drawn from its global network.

## When to use
You have a `domain` or `ip-address` and want infrastructure intelligence without touching the target: how popular/ranked a domain is, what network (AS) and hosting sit behind it, whether it's seen unusual traffic, and — via the built-in URL Scanner — what a page actually loads (redirects, resources, screenshot) from Cloudflare's servers rather than your own. Useful for vetting a domain tied to a subject, profiling a site's hosting, and safely inspecting a suspicious link.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://radar.cloudflare.com and enter a `domain` or `ip-address` in the search/lookup, or open the URL Scanner.
2. For a domain: read its ranking/popularity trend, associated AS/network, and traffic context.
3. For a link: run a URL scan to see redirects, loaded resources, a screenshot, and any flagged behaviour — set the scan to private so it isn't published in the public scan feed.
4. Browse Radar's trend dashboards (outages, protocol/traffic trends) for country/network context.
5. Pivot: the AS/hosting and resolved IPs feed WHOIS/reverse-IP and passive-DNS tools; the URL scan corroborates what a page does before you visit it directly.

## Inputs → Outputs
- **In:** `domain` / `ip-address` / URL
- **Out:** popularity rank, AS/network + `ip-address` info, URL-scan behaviour/screenshot, traffic/outage trends
- **Empty/negative result looks like:** a domain not ranked or with sparse data — small/new/low-traffic sites won't appear in rankings; that's not evidence the domain is fake, just below Cloudflare's visibility threshold.

## Gotchas & OpSec
- Rankings/trends cover popular and Cloudflare-visible traffic — long-tail and non-Cloudflare-routed sites have thin data.
- The URL Scanner actively fetches the target (from Cloudflare, not you); use private scans for sensitive casework so results aren't public.
- It's infrastructure intel, not people data — relevance to locating a person is indirect (via a domain they run).
- OpSec: passive for lookups; the scanner is active but originates from Cloudflare.

## Overlaps ("do both")
- Pairs with WHOIS/passive-DNS and reverse-IP tools — Radar gives ranking, AS, and safe page behaviour; those resolve ownership and co-hosted domains for the same infrastructure.

## Trust & verifiability
`trust: trusted` — first-party Cloudflare network telemetry and a reputable scanner. Data is authoritative for what Cloudflare observes; corroborate ownership/hosting conclusions with dedicated DNS/WHOIS tools.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloudflare-radar |
| category | search-engines |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
