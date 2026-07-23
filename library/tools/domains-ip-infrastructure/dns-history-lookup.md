---
id: dns-history-lookup
name: DNS History Lookup
description: Use when you have a domain and want its historical DNS records to uncover past hosting IPs — returns ip-address and domain history that can reveal a site's origin behind later CDN/privacy layers.
url: https://osint.sh/dnshistory/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Revealing a domain's historical A/MX/NS records to find the original hosting IP before a proxy was added.
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: freemium
costNote: Web tools on osint.sh are free with no account; the API is limited to sponsors.
opsec: passive
opsecNote: osint.sh queries its own historical DNS dataset, so the target domain's servers are not contacted by your lookup — passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of osint.sh, a popular free all-in-one OSINT toolkit; historical DNS data is aggregated by a third party, so corroborate critical findings.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- osint.sh DNS history
tags:
- dns
- history
- passive-dns
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# DNS History Lookup

> osint.sh's passive-DNS history tool — see the IPs and records a domain used in the past, often exposing the origin behind a later CDN or privacy layer.

## When to use
You have a `domain` sitting behind Cloudflare/a proxy today, and you want its **original** hosting `ip-address` — historical DNS records frequently captured the real origin before the proxy was added. Also useful for spotting when a site changed hosts, nameservers, or mail providers, which helps cluster related infrastructure and build an attribution timeline. Infrastructure recon, not people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/dnshistory/ and enter the `domain`.
2. Read the historical records: past A (`ip-address`), MX, NS, and TXT entries with the periods they were seen.
3. Look for a pre-CDN origin IP — an early A record pointing at a hosting provider rather than Cloudflare/Akamai is the prize.
4. Note nameserver/mail changes to date infrastructure shifts.
5. Pivot: a candidate origin `ip-address` → [[whois-arin]]/[[ipvoid]] to attribute the host; confirm the origin still serves the site directly.

## Inputs → Outputs
- **In:** a `domain`.
- **Out:** historical DNS records — past `ip-address`es (A), MX, NS, TXT — with rough timeframes.
- **Empty/negative result looks like:** no historical data (a young domain, or one never captured), or history that only ever shows the CDN — meaning the origin was proxied from day one and isn't recoverable here.

## Gotchas & OpSec
- Historical DNS is third-party-aggregated and can be incomplete or stale — treat an "origin" IP as a lead to verify, not proof.
- A domain proxied from the start never leaked its origin, so a clean-looking history isn't a failure of the tool.
- Cross-check with other passive-DNS/CT sources; datasets differ in coverage.

## Overlaps ("do both")
- Pairs with [[netcraft]] (hosting-history timeline) and certificate-transparency search: each dataset captures different snapshots, so combining them recovers more of the origin history.

## Trust & verifiability
`trust: community` — a free third-party toolkit aggregating passive-DNS data; useful and fast, but confirm any origin IP by direct request before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dns-history-lookup |
