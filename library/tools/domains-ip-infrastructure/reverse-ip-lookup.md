---
id: reverse-ip-lookup
name: Reverse IP Lookup
description: Use when you have an `ip-address` and want the other domains hosted on it — returns the `domain` neighbours sharing that server, exposing linked or co-located sites.
url: https://osint.sh/reverseip/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Finding every domain that resolves to a given IP, to reveal sibling sites, shared hosting neighbours, or a subject's other properties.
selectorsIn:
- ip-address
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free browser tool on the osint.sh suite; heavy/bulk use may be rate-limited toward its paid API.
opsec: passive
opsecNote: You query osint.sh's cached hosting data, not the target server, so the lookup doesn't touch the subject's infrastructure. osint.sh sees which IP you're researching.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of the well-known free osint.sh toolset; data is drawn from passive DNS/hosting datasets that can be incomplete or stale, so treat neighbour lists as leads.
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
- osint.sh reverse IP
tags:
- Domain/IP/Links
- reverse-ip
- passive-dns
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Reverse IP Lookup

> Turn an IP into the list of domains hosted on it — a fast way to find a subject's *other* sites, or the neighbours sharing their server.

## When to use
You have an `ip-address` — from a honeypot-link hit, a mail header, a WHOIS/DNS record, or a domain you already resolved — and want to know **what else lives there**. On a dedicated server or VPS the co-hosted domains are often the same owner's other properties (a strong pivot); on shared hosting they're unrelated tenants (noise). Either way it maps the neighbourhood around an IP.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/reverseip/.
2. Enter the target `ip-address` and run the lookup.
3. Read the returned `domain` list — every hostname the dataset shows resolving to that IP.
4. Judge the result: a handful of thematically related domains ⇒ likely same owner (dedicated/VPS); hundreds of unrelated domains ⇒ shared hosting, low attribution value.
5. Pivot promising domains into WHOIS, and re-resolve them to confirm they still point at the IP.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** `domain` list of co-hosted sites
- **Empty/negative result looks like:** "no domains found" — the dataset has no reverse records for that IP (common for CDN/cloud IPs and fresh hosts); absence isn't proof the IP hosts nothing.

## Gotchas & OpSec
- **Shared vs dedicated is everything:** a long neighbour list on shared hosting means nothing; a short list on a dedicated IP is gold. Check the hosting type before attributing.
- Reverse-IP data is dataset-dependent and lags reality; corroborate with a second passive-DNS source.
- CDNs (Cloudflare, etc.) put thousands of unrelated sites behind one IP — reverse IP is useless there.
- Passive toward the target; only osint.sh learns your query.

## Overlaps ("do both")
- Pairs with WHOIS and passive-DNS/domain-history tools: reverse IP finds the co-located domains, and those tools tell you who owns each and whether the co-location is meaningful.

## Trust & verifiability
`trust: community` — a reputable free OSINT utility surfacing third-party hosting datasets; reliable as a lead source, but always re-resolve and cross-check before treating a neighbour as linked.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reverse-ip-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
