---
id: dns-dumpster
name: DNS Dumpster
description: Use when you have a `domain` and want its DNS footprint — returns subdomains, MX/TXT/host records, resolving `ip-address`es and an infrastructure map.
url: https://dnsdumpster.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- passivedns
bestFor: Passive subdomain enumeration and infrastructure mapping for a domain without touching the target's own servers.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free web tool from Hacker Target; heavy/automated use is nudged toward their paid API, but interactive lookups are free.
opsec: passive
opsecNote: DNS Dumpster answers from Hacker Target's own passive-DNS and scan data, so your lookup does not send DNS queries or probes to the target's nameservers — the subject sees nothing. Your query is logged by dnsdumpster.com; use a sock-puppet session if you don't want the domain of interest tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by Hacker Target, a long-established infrastructure-recon vendor; results are aggregated from their scanning/passive-DNS sources and may lag or miss very new subdomains.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- dnsdumpster
- Hacker Target DNS Dumpster
tags:
- passive-dns
- subdomain-enum
- infrastructure
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# DNS Dumpster

> Hacker Target's free passive-DNS mapper: give it a domain, get back the subdomains, mail/name servers, and hosting IPs it already knows about — without pinging the target.

## When to use
You have a `domain` (a personal site, a small business, a vanity domain tied to a subject) and want to enumerate its subdomains, mail infrastructure, and the `ip-address`es it resolves to — as a starting point for hosting/geolocation pivots. Because it's passive, it's safe to run before you decide whether to interact with the target at all. Infrastructure-focused, so missing-persons relevance is low unless the domain is directly the subject's.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dnsdumpster.com/ in a clean/sock-puppet browser session.
2. Enter the target `domain` (e.g. `example.com`) and submit.
3. Read the results: host (A) records with resolving IPs, MX records, TXT records, NS records, and a visual/downloadable infrastructure map and Excel/host list.
4. Pivot: take an interesting `ip-address` into an IP-geolocation or reverse-IP tool, or feed a discovered subdomain into deeper recon.

## Inputs → Outputs
- **In:** `domain`
- **Out:** subdomains (`domain`), resolving `ip-address`es, MX/TXT/NS records, infrastructure graph, exportable host list
- **Empty/negative result looks like:** only the apex A and MX rows with no extra subdomains — means Hacker Target's data set has nothing more, not that no subdomains exist. Confirm with active enumeration if it matters.

## Gotchas & OpSec
- Data is from Hacker Target's passive sources; brand-new or well-hidden subdomains may be absent, and stale records may linger. It is a lead generator, not authoritative.
- Interactive use is free but rate-limited; bulk/programmatic pulls push you to their paid API.
- OpSec: passive toward the target, but your query is logged by dnsdumpster.com — use a burner session for sensitive domains.

## Overlaps ("do both")
- Pairs with reverse-IP and geolocation tools like [[ipinfo-map]], and with bulk IoC triage such as [[cyberbro]] — DNS Dumpster surfaces the infrastructure, those tools locate and score the individual hosts.

## Trust & verifiability
`trust: community` — operated by the established Hacker Target service; treat every subdomain/IP as a lead to verify with a live resolver before acting, since the passive data can be incomplete or dated.
