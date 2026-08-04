---
id: tcp-ip-utils-domain-neighbors
name: TCP/IP Utils - Domain Neighbors
description: Use when you have a `domain` or `ip-address` and want the other domains sharing that IP/host (reverse IP) — returns neighboring `domain`s for infrastructure clustering.
url: https://dnslytics.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- neighbor-domains
bestFor: Finding co-hosted "neighbor" domains on the same IP to link a subject's related sites.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free web lookups and reports with a daily limit; more page views, monitoring and premium data require a paid plan. Ad-hoc reverse-IP checks are free.
opsec: passive
opsecNote: DNSlytics answers from its own crawled/DNS database, so your lookup never touches the subject's server — it is passive. You do reveal the queried domain/IP to DNSlytics; use a sock-puppet account if you register for higher limits.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established DNS/IP intelligence provider with 10+ years of historical data; results are database-derived and should be corroborated, since shared hosting can co-locate unrelated sites.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- dnslytics-com
- search-dnslytics-com
aliases:
- DNSlytics
- tcpiputils domain neighbors
- reverse IP lookup
tags:
- domains-ip-infrastructure
- reverse-ip
- neighbor-domains
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# TCP/IP Utils - Domain Neighbors

> A reverse-IP / "domain neighbors" lookup (now served via DNSlytics): given an IP or domain, list the other domains hosted on the same address.

## When to use
You have a `domain` or `ip-address` and want to know what else lives on that IP — the classic reverse-IP "neighbors" pivot. When a subject runs several sites off one dedicated server or a small hosting footprint, the neighbor list can reveal their other projects, aliases, or a network of related sites. It's most powerful against dedicated/VPS IPs; on big shared hosts or CDNs the neighbor list is noise (thousands of unrelated tenants).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://dnslytics.com/ (the successor host for tcpiputils' domain-neighbors function).
2. Enter the target `domain` or `ip-address` and choose the reverse-IP / domain-neighbors report.
3. Read the list of domains resolving to the same IP, plus supporting data (nameservers, MX, history).
4. Judge the hosting type: a handful of thematically-related neighbors on a dedicated IP is a strong signal; thousands on a shared host is not.
5. Pivot: take promising neighbor `domain`s into WHOIS, Wappalyzer (shared analytics IDs), and content review to confirm common ownership.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** neighboring `domain`s on the same IP, plus DNS/host context (`ip-address`, nameservers, MX)
- **Empty/negative result looks like:** only the queried domain returned (dedicated single-site IP), or a truncated list behind the free-tier cap. On shared hosting expect a long, mostly-irrelevant list — that's a limitation, not a finding.

## Gotchas & OpSec
- Human-in-the-loop: none, but interpreting shared-vs-dedicated hosting is a judgement call.
- OpSec: **passive** — served from DNSlytics' database, no contact with the subject's server.
- Reverse-IP is only meaningful on dedicated IPs. Behind Cloudflare/shared hosting, co-location does **not** imply common ownership — always corroborate before linking sites.

## Overlaps ("do both")
- Pairs with `[[wappalyzer]]` (shared analytics/tracking IDs) and WHOIS tools — reverse-IP finds candidate neighbors, and those independently confirm whether the same person actually owns them.

## Trust & verifiability
`trust: community` — a reputable long-standing DNS/IP database, but neighbor lists are only as current as its crawl and can conflate co-tenants. Treat neighbors as leads to verify, not proof of common ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tcp-ip-utils-domain-neighbors |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
