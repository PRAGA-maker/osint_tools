---
id: ipv6-cidr-report
name: IPv6 CIDR Report
description: Use when you have an `ip-address` (IPv6) or ASN and want to understand the global IPv6 routing table — returns per-AS IPv6 prefix allocations and aggregation data.
url: https://www.cidr-report.org/v6/as2.0/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ipv6
bestFor: Mapping which autonomous system announces an IPv6 prefix and how the global IPv6 routing table is aggregated.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free long-running public BGP-analysis report; no account needed.
opsec: passive
opsecNote: Fully passive — you read a periodically-generated report built from public BGP data. No target is contacted and nothing is logged against your subject. This is routing-table intelligence, not host contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Geoff Huston / APNIC, a foundational and widely-cited source for BGP routing-table analysis.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- ipv4-cidr-report
aliases:
- CIDR Report IPv6
- cidr-report.org
tags:
- bgp
- ipv6
- routing
- asn
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# IPv6 CIDR Report

> The IPv6 view of the long-running CIDR Report: which autonomous systems announce which IPv6 prefixes, and how well the global routing table is aggregated.

## When to use
You have an IPv6 `ip-address` or an ASN and want routing-layer context — which autonomous system originates a given IPv6 prefix, how many prefixes an AS announces, and how the global IPv6 table is structured. Useful when attributing infrastructure to a network operator or understanding the routing footprint behind an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cidr-report.org/v6/as2.0/.
2. Browse the per-AS IPv6 aggregation report, or look up the AS that originates your prefix.
3. Read the allocation/aggregation figures — announced prefixes, potential aggregation, originating AS.
4. Cross-reference the ASN with a WHOIS/RIR lookup to name the operator.
5. Pivot: the originating AS ties an IPv6 range to a network operator for further infrastructure mapping.

## Inputs → Outputs
- **In:** IPv6 `ip-address`/prefix or ASN
- **Out:** originating AS, per-AS IPv6 prefix counts and aggregation stats (`ip-address` ranges)
- **Empty/negative result looks like:** a prefix not present — it may be unrouted/unadvertised in the global table, or newly allocated; check an RIR whois for allocation status.

## Gotchas & OpSec
- It reflects the *global BGP routing table*, not internal or private addressing.
- The report is generated periodically — data is near-current, not real-time.
- ASN → operator mapping needs a separate RIR/WHOIS lookup.

## Overlaps ("do both")
- Pairs with RIR WHOIS (ARIN/RIPE/APNIC) and BGP tools (bgp.he.net) — the CIDR Report gives aggregation/origination context while those name the operator and show peering.

## Trust & verifiability
`trust: trusted` — a foundational APNIC/Geoff Huston resource built from public BGP data; figures are reproducible from the global routing table.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipv6-cidr-report |
