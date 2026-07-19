---
id: whtop
name: WHTop
description: Use when you have a `domain` or `ip-address` and want to know where a site is hosted — returns hosting provider, IP geolocation, DNS and linked-account info.
url: http://www.whtop.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Identifying a website's hosting provider, IP location, and associated infrastructure via a free reverse-lookup directory.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- geolocation
status: live
pricing: free
costNote: Core hosting directory and reverse IP/domain lookup tools are free and public; paid options are only for hosting companies managing their own listings.
opsec: passive
opsecNote: Lookups query WHTop's directory and public IP/DNS data, not the target's server directly, so the site owner isn't alerted by your query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large web-hosting review directory (since 2004) with free lookup tools; the infrastructure data is derived from public sources and is generally reliable for hosting attribution, not authoritative WHOIS.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- whtop.com
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- hosting
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# WHTop

> A web-hosting directory whose free lookup tools tell you where a site is hosted — provider, IP geolocation, DNS, and linked accounts — useful for infrastructure attribution around a domain.

## When to use
You have a `domain` (from a subject's website, email, or a suspicious link) or an `ip-address` and want to understand the hosting behind it: which provider and country hosts it, the IP's geolocation, and associated DNS/social signals. This helps cluster infrastructure, gauge where an operator is based, and corroborate other domain findings — infrastructure context rather than direct person data (hence low MP relevance).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.whtop.com and open its lookup tools (hosting checker / IP lookup).
2. Enter the domain or IP address.
3. Read the results: hosting company, IP geolocation (country/region/city, ISP), IPv4/IPv6 detail, DNS records, and any linked-account info surfaced.
4. Note the provider and location; compare against WHOIS and other infrastructure findings to cluster related sites.
5. Pivot: hosting provider/IP → abuse-contact and other domains on the same host; IP `geolocation` → rough operator region; DNS → related subdomains/services.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** hosting provider, IP `geolocation`, DNS info, and associated-account signals
- **Empty/negative result looks like:** generic CDN/proxy results (e.g. Cloudflare) that mask the true host, or no data for an obscure IP — a CDN in front of a site hides its origin, so treat "hosted by Cloudflare" as inconclusive and use passive-DNS/history tools to find the origin.

## Gotchas & OpSec
- CDNs/proxies (Cloudflare, etc.) obscure the real host; WHTop then shows the CDN, not the origin server.
- IP geolocation is approximate and reflects the datacenter, not any person's location.
- Directory/review content is commercial; the free lookup utilities are the OSINT-relevant part.
- OpSec: passive — queries hit WHTop and public data, not the target's server.

## Overlaps ("do both")
- Complements WHOIS and passive-DNS tools — WHTop gives quick hosting attribution; use WHOIS for registrant data and passive DNS to defeat CDN masking and find the true origin.

## Trust & verifiability
`trust: community` — a long-running directory with reliable-but-derived infrastructure data; confirm hosting attribution against a second source (passive DNS, direct IP checks), especially when a CDN is in play.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whtop |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
