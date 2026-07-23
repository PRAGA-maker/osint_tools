---
id: web-check
name: Web-Check
description: Use when you have a `domain` and want a one-page infrastructure profile — returns DNS, SSL/TLS, headers, server tech, hosting `ip-address`, and historical/archive context.
url: https://web-check.as93.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A fast, all-in-one dashboard of everything publicly knowable about a website's infrastructure.
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free and open-source (MIT); use the public instance or self-host your own from GitHub.
opsec: passive
opsecNote: "Web-Check reads DNS, certificate transparency, archives, and passive sources rather than aggressively probing the target, so it's low-noise. On the public instance your query and the target domain pass through as93.net's server; self-host if you need the lookup to stay entirely private, and use a sock-puppet session either way."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Popular open-source project by Alicia Sykes (Lissy93) with a transparent, auditable codebase and a self-host option; it aggregates authoritative sources (DNS, CT logs, WHOIS).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- Web-Check as93
- Lissy93 web-check
tags:
- domain-and-ip-research
- infrastructure
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Web-Check

> Enter a domain and get ~30 infrastructure checks on one page — DNS, SSL/TLS, headers, server stack, open ports, hosting, and archive history — in about 20 seconds.

## When to use
You have a `domain` and want a single consolidated picture of its infrastructure before deciding where to dig: who hosts it (`ip-address`), what tech it runs, its DNS and mail configuration, TLS posture, associated domains, and historical snapshots. It's the fast first-pass recon dashboard that saves you running ten separate tools. Infrastructure-focused, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://web-check.as93.net/ (or your self-hosted instance) and enter the target `domain`.
2. Wait ~20s while it runs its checks; scroll the card grid.
3. Read the high-value cards: DNS records, IP/hosting (`ip-address`), SSL certificate + CT-log history, HTTP security headers, server/tech stack, DNSSEC, and archive/Wayback data.
4. Pivot: take the hosting `ip-address` into reverse-IP/passive-DNS tools, or a CT-log-discovered subdomain into deeper enumeration.
5. Self-host for repeated/private use or to hit its API programmatically.

## Inputs → Outputs
- **In:** `domain` (or URL)
- **Out:** hosting `ip-address`, associated `domain`s/subdomains, DNS/SSL/header/tech details, archive history
- **Empty/negative result looks like:** cards that fail or return "no data" — a domain behind Cloudflare will mask the origin IP, and some checks time out; treat blanks as "not resolvable here," not as absence.

## Gotchas & OpSec
- CDN/proxy fronting (Cloudflare) hides the true origin `ip-address` — corroborate with historical DNS/CT data rather than trusting the surface IP.
- The public instance rate-limits and routes your query through as93.net; self-host for privacy or bulk use.
- Individual checks depend on third-party APIs that can be down — a failed card isn't a finding.

## Overlaps ("do both")
- Pairs with focused tools like [[dns-dumpster]] (subdomains), [[ipinfo-map]] (IP geolocation), and [[favicon-hasher]] (shared-infra pivots) — Web-Check gives the overview, those go deep on one facet.

## Trust & verifiability
`trust: trusted` — a well-regarded, MIT-licensed open-source tool aggregating authoritative sources; because it's auditable and self-hostable, you can verify exactly how each figure is derived.
