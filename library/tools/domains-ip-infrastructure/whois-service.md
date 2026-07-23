---
id: whois-service
name: WHOIS Service
description: Use when you have an `ip-address` (or domain) and want reverse-IP / co-hosted domains and rough geolocation — returns domain, ip-address, address.
url: https://whoismind.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reverse-IP lookup — enumerating other domains hosted on the same IP as a target.
selectorsIn:
- ip-address
- domain
selectorsOut:
- domain
- ip-address
- address
status: live
pricing: freemium
costNote: Free web lookups, no account. Ad-supported, with paid/bulk data upsells; the interactive reverse-IP and IP-geo tools need no payment.
opsec: passive
opsecNote: Queries hit WhoisMind's servers, not the target's infrastructure, so the subject sees nothing. Assume WhoisMind logs your query IP; use a VPN if you need to keep your own origin private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party aggregator of WHOIS / IP / reverse-DNS data of unknown provenance; reverse-IP results can be stale or noisy on shared hosts. Corroborate before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whoismind
aliases:
- WhoisMind
- whoismind.com
tags:
- Domain/IP/Links
- Domain/IP investigation
- reverse-ip
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# WHOIS Service

> WhoisMind — a free reverse-IP and IP-geolocation aggregator: given an IP, list the other domains parked on it; given a domain, get its resolved IP, ISP and rough location.

## When to use
You have an `ip-address` resolved from a target `domain` and want to know what *else* lives on that host — sibling sites, a shared reseller, or a co-located personal project that pivots back to the subject. Also handy as a quick, no-login IP-geo/ISP check when you don't want to spin up a heavier tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://whoismind.com/ .
2. For reverse-IP: paste the target `ip-address` into the IP / reverse-IP lookup — it returns the domains it believes share that address, plus ISP/ASN and geolocation.
3. For a domain: enter the `domain` to see its registration snapshot and resolved IP, then feed that IP back into the reverse lookup.
4. Read the output critically: on shared hosting or a CDN, one IP can front thousands of unrelated domains — treat the list as leads, not confirmed associations.
5. Pivot: interesting sibling domains feed a registrant lookup (`[[whoismind]]`); the IP-geo/ISP feeds infrastructure mapping.

## Inputs → Outputs
- **In:** `ip-address` (best), or `domain`
- **Out:** `domain` (co-hosted sites), `ip-address`, ISP/ASN, coarse `address` (city/region-level geolocation)
- **Empty/negative result looks like:** a bare IP-geo card with no or a single co-hosted domain — meaning either a dedicated host or simply that WhoisMind has no reverse data for it, not proof the site stands alone.

## Gotchas & OpSec
- Reverse-IP on shared hosting / Cloudflare is noise: the "co-hosted" list reflects the front-end IP, not real co-tenancy. Verify a suspected link independently.
- Data provenance and freshness are opaque; records can lag months behind reality.
- OpSec: **passive** — nothing touches the subject; only your own query is exposed to WhoisMind.

## Overlaps ("do both")
- Pairs with `[[whoismind]]` (same provider's registrant/WHOIS view) — run the domain lookup there and the reverse-IP here to cover both directions.

## Trust & verifiability
`trust: community` — a free ad-supported aggregator with undocumented sourcing; fine for generating pivots, but always corroborate a reverse-IP "match" with a second source before treating two domains as related.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whois-service |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → domain, ip-address, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
