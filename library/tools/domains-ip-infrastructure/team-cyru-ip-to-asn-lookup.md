---
id: team-cyru-ip-to-asn-lookup
name: Team Cymru IP to ASN Lookup
description: Use when you have an `ip-address` and want to know which network (ASN) and registrant announce it — returns the owning autonomous system, allocation country, and BGP prefix.
url: http://whois.cymru.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Mapping an IP (or bulk list of IPs) to its ASN, network owner, and allocation date.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- employer-org
status: live
pricing: free
costNote: Free public whois/DNS/netcat interface run by Team Cymru; no account or key required.
opsec: passive
opsecNote: You query Team Cymru's whois server, not the target host, so the IP you are researching never sees a connection from you. Team Cymru sees your query source; the bulk-whois netcat method keeps volume off the public web form.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Team Cymru is a widely-trusted internet-security nonprofit whose IP-to-ASN mapping is a standard reference used across the industry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- team-cymru-ip-to-asn
- totalhash
aliases:
- Team Cymru IP to ASN
- whois.cymru.com
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
- asn
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Team Cymru IP to ASN Lookup

> Team Cymru's IP-to-ASN mapping service: hand it an IP and it tells you which network operator announces that address and where it is allocated.

## When to use
You have an `ip-address` — from an email header, a server log, an image EXIF upload, a chat leak — and you need the network context: which Autonomous System (ASN) and organization owns/announces it, the BGP prefix, the country, and the allocation date. This tells you whether an IP belongs to a residential ISP, a hosting/VPS provider, a corporate network, or a VPN/proxy, which shapes every downstream attribution step.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://asn.cymru.com/ and paste one or more IP addresses into the lookup form.
2. Read the result row: ASN, BGP prefix, country code (CC), registry, allocation date, and the AS name (the announcing organization).
3. Note the AS name — a residential ISP suggests a real subscriber (subpoena target), while a hosting/VPN AS means the IP is likely infrastructure, not the person.
4. For many IPs, use the documented bulk whois interface: `whois -h whois.cymru.com " -v 8.8.8.8"` or pipe a list via netcat to `whois.cymru.com 43`.
5. Pivot: an ISP + geolocation feeds a legal request; a hosting AS feeds reverse-DNS and passive-DNS to find co-hosted domains.

## Inputs → Outputs
- **In:** `ip-address` (single or bulk)
- **Out:** ASN, AS name (`employer-org`/network owner), BGP prefix (`ip-address` range), country, allocation date
- **Empty/negative result looks like:** "NA" fields or no ASN — a bogon, unallocated, or private (RFC1918) address that is not globally routable.

## Gotchas & OpSec
- ASN ownership is the *network* that announces the IP, not necessarily the end user; a corporate-looking AS name can still be a reseller's block.
- The web form is fine for a handful of IPs; for lists use the whois/netcat bulk interface so you don't hammer the page.
- OpSec: **passive** — the lookup never touches the target IP, so there is no risk of tipping off the host.

## Overlaps ("do both")
- Pairs with `[[team-cymru-ip-to-asn]]` (same provider, alternate interface) and reverse/passive-DNS tools — ASN gives the network, passive DNS gives the domains co-located on it, and together they scope the infrastructure around an IP.

## Trust & verifiability
`trust: trusted` — Team Cymru is a respected internet-security nonprofit; its ASN mapping is derived directly from BGP routing data and is a standard cross-checkable reference.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | team-cyru-ip-to-asn-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
