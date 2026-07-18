---
id: hurricane-electric-internet-services
name: Hurricane Electric Internet Services
description: Use when you have an `ip-address`, `domain` or ASN and want its network context — returns the owning ASN, announced prefixes, peers, reverse-DNS and co-hosted `domain`s.
url: https://bgp.he.net
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Mapping an IP/domain to its ASN, network prefixes, peers and the other domains hosted on the same IP.
selectorsIn:
- ip-address
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free public BGP/network toolkit; no account needed.
opsec: passive
opsecNote: Hurricane Electric answers from its own routing/DNS data, so the target host is never contacted by you — the lookup is invisible to them. HE sees your query; a clean session suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hurricane Electric is a major global network operator; its BGP toolkit reflects live routing-table and DNS data, authoritative for network/ASN relationships (reverse-DNS co-hosting lists can lag).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- hurricane-electric-bgp-toolkit
aliases:
- bgp.he.net
- HE BGP Toolkit
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Hurricane Electric Internet Services

> The bgp.he.net toolkit — the fast way to see the network behind an IP or domain: its ASN, the prefixes it lives in, who peers with it, and what else is hosted alongside it.

## When to use
You have an `ip-address` or `domain` (from a header trace, a WHOIS pivot, a site you're profiling) and want its **network context** rather than its registrant. HE tells you which ASN/organisation owns the address space, what prefixes are announced, the reverse-DNS name, and — via reverse-DNS/IP history — **other domains on the same IP** (potential co-owned or co-hosted sites). This is core infrastructure mapping: it links a host to a provider and to sibling sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://bgp.he.net.
2. Enter an `ip-address`, `domain`, or `AS number` in the search box.
3. Read the result:
   - **IP/host page** — owning ASN/org, the prefix it's in, reverse DNS, and lists of domains resolving to that IP.
   - **ASN page** — all announced prefixes, IPv4/IPv6 space, peers/upstreams, and originated routes.
   - **DNS tab** — A/AAAA/MX/NS records for a domain.
4. Pivot: co-hosted domains become new targets; the ASN/org shows the hosting provider (useful for takedown/attribution); peers map the provider's connectivity.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, or ASN
- **Out:** owning ASN/org, announced prefixes, peers, reverse-DNS, and co-hosted `domain`s (`ip-address` ↔ `domain` mappings)
- **Empty/negative result looks like:** an IP with no reverse DNS and few/no co-hosted domains (common on dedicated or cloud IPs), or a domain that resolves to a shared CDN (so co-hosting lists are huge and non-indicative). Interpret cloud/CDN hosting with care.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — HE queries routing/DNS data, not the target host.
- **Shared hosting/CDN caveat:** hundreds of unrelated domains can share one IP (shared hosting) or resolve to Cloudflare/CDN IPs that hide the origin — co-hosting is a lead, not proof of common ownership.
- Reverse-DNS/domain-on-IP data can be stale; corroborate a co-hosting claim with WHOIS/passive DNS.

## Overlaps ("do both")
- Pairs with WHOIS tools (`[[whois-search-com]]`, `[[mx-toolbox-whois-lookup]]`) — HE gives the *network* (ASN, prefixes, co-hosting), WHOIS gives the *registrant*; together they profile who and where. Feed a traced IP from `[[ip2location-free-email-header-tracer]]` in here.

## Trust & verifiability
`trust: trusted` — first-party routing data from a major backbone operator; ASN/prefix/peering data is authoritative, with the usual caveat that reverse-DNS co-hosting is indicative, not definitive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hurricane-electric-internet-services |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
