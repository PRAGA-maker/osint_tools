---
id: robtex
name: Robtex
description: Use when you have a `domain`, `ip-address`, hostname, or ASN and want its DNS records plus historical domain↔IP relationships — returns related `domain`s and `ip-address`.
url: https://robtex.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: DNS/IP relationship mapping and historical (passive-DNS) lookups for a domain, IP, hostname, or ASN.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free web lookups for basic DNS/IP data; deeper history and API access are paid, and some features prompt for an account.
opsec: passive
opsecNote: Robtex serves cached/historical DNS data from its own store — it doesn't actively probe the target, so it's passive. Your queries are logged by Robtex and the free tier is rate-limited.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running free DNS/IP research service; its passive-DNS history is genuinely useful but coverage/freshness vary and it is not an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- robtex-com
aliases:
- Robtex
tags:
- dns
- passive-dns
- ip
- whois
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Robtex

> A free DNS/IP research console: type a domain or IP and see its records, its neighbours, and how the two have been linked over time.

## When to use
You have a `domain`, `ip-address`, hostname, or ASN and want to map the infrastructure around it — current DNS records, which domains have shared an IP, name-server relationships, and historical domain↔IP associations. Useful for attributing infrastructure, finding co-hosted sites, and building a picture of how a target's hosting has changed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://robtex.com/ and enter the `domain`, `ip-address`, hostname, or AS number.
2. Read the results: A/MX/NS records, the IP's other hostnames, shared name servers, and a graph of related nodes.
3. Follow the historical/relationship links to see prior domain↔IP pairings (passive-DNS style).
4. Note that deeper history and bulk/API access are behind the paid tier.
5. Pivot: co-hosted `domain`s and related `ip-address`es feed reverse-DNS, WHOIS, and hosting lookups.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, hostname, or ASN
- **Out:** DNS records, related `domain`s and `ip-address`es, name-server links, and historical relationships
- **Empty/negative result looks like:** sparse data — Robtex hasn't observed much for that target, or the free tier is hiding history behind the paywall; corroborate with a dedicated passive-DNS provider.

## Gotchas & OpSec
- Free tier is limited and rate-limited; the richest history and any automation need the paid API.
- Passive-DNS coverage is partial and can be stale — absence of a relationship isn't proof one never existed.
- OpSec: passive; Robtex answers from its own store, so nothing touches the target.

## Overlaps ("do both")
- Pair with other passive-DNS and reverse-DNS tools ([[hacker-target-reverse-dns]]) — each observes different resolvers, so their histories complement rather than duplicate. Sibling: [[robtex-com]].

## Trust & verifiability
`trust: community` — a well-known free service, but its data is observational passive-DNS, not authoritative; verify anything decisive against live DNS/WHOIS.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | robtex |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
