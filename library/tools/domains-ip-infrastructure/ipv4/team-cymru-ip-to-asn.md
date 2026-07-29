---
id: team-cymru-ip-to-asn
name: Team Cymru IP to ASN
description: Use when you have an `ip-address` and want its ASN, announcing network/organization and BGP prefix — returns ip-address, domain (network owner) and employer-org leads.
url: https://asn.cymru.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ipv4
bestFor: Mapping an IP (or bulk IPs) to its ASN, BGP prefix, and announcing organization.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- employer-org
status: live
pricing: free
costNote: Free public service from Team Cymru (via web, WHOIS, and DNS interfaces). No account or key.
opsec: passive
opsecNote: Fully passive — you query Team Cymru's BGP/WHOIS dataset, never the target IP. The lookup does not touch the subject's host, so it leaves no trace on their side; only Team Cymru sees your query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Team Cymru is a long-standing, authoritative provider of BGP/ASN data widely relied on across the security industry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- team-cyru-ip-to-asn-lookup
- totalhash
aliases:
- Team Cymru IP to ASN
- asn.cymru.com
tags:
- ip-research
- asn
- bgp
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Team Cymru IP to ASN

> The authoritative IP→ASN mapping service — turn an IP into the network that announces it: ASN, BGP prefix, and the owning organization.

## When to use
You have an `ip-address` (from a log, an email header, a resolved domain, a connection) and want to know who runs the network it lives on: the Autonomous System Number, the covering BGP prefix, and the org/ISP name. This is the fastest way to attribute an IP to a hosting provider, ISP, or organization and to group many IPs by network — a core step when mapping a subject's or a site's infrastructure. Bulk lookups are supported via the WHOIS/netcat interface.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://asn.cymru.com/ and paste the `ip-address` (single or list) into the lookup.
2. Read the result: ASN, the announcing organization/AS name, the BGP prefix, country, and allocation registry.
3. For scripting/bulk, use the WHOIS interface: `whois -h whois.cymru.com " -v 8.8.8.8"` (or the DNS interface).
4. Note the ASN and org name.
5. Pivot: the ASN → enumerate all prefixes that org announces (map their full IP footprint); the org name → hosting/ISP identification; group a set of IPs by ASN to spot shared infrastructure.

## Inputs → Outputs
- **In:** one or many `ip-address` values
- **Out:** ASN, announcing organization/AS name (`employer-org`), covering BGP prefix (`ip-address` range), country, registry
- **Empty/negative result looks like:** "NA"/no ASN for an IP that isn't globally routed (bogon, private, or unannounced space) — meaning it's not in the public BGP table, not that the lookup failed.

## Gotchas & OpSec
- Maps to the *announcing* network, which may be an upstream/transit provider, not the end user — confirm with WHOIS/RIR data for the specific allocation.
- Reflects current (or specified historical) BGP state; routing can change.
- OpSec: fully passive; the target host is never contacted.

## Overlaps ("do both")
- Pairs with RIR WHOIS (ARIN/RIPE/etc.), BGPView, and `[[totalhash]]` — Team Cymru is the quick, bulk-friendly ASN mapper; RIR WHOIS gives the granular allocation/registrant.

## Trust & verifiability
`trust: trusted` — Team Cymru is an authoritative, industry-standard source for BGP/ASN data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | team-cymru-ip-to-asn |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
