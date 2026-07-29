---
id: ipv4-cidr-report
name: IPv4 CIDR Report
description: Use when you have an ASN or want to understand a network's global routing footprint — returns the AS's announced prefixes, aggregation stats, and routing-table context.
url: https://www.cidr-report.org/as2.0/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ipv4
bestFor: Analysing the global BGP routing table by Autonomous System — which prefixes an AS announces and how its address space is aggregated.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- employer-org
status: live
pricing: free
costNote: Free public routing-analysis report (maintained by Geoff Huston/APNIC). No account.
opsec: passive
opsecNote: A read-only aggregate report built from public BGP data — you submit nothing about a target and touch no target infrastructure. Only your visit to the report is seen.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-standing, authoritative routing report widely cited by network operators. Reflects public BGP announcements accurately; it describes networks, not individuals.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bgp-he-net
- viewdns-info
- db-ip
- ipv6-cidr-report
aliases:
- CIDR Report
- cidr-report.org
tags:
- bgp
- asn
- routing
- ipv4
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# IPv4 CIDR Report

> The classic global BGP routing analysis: for an Autonomous System, which IP prefixes it announces, how efficiently it aggregates, and how it fits into the wider routing table.

## When to use
You've resolved a subject's infrastructure to an ASN (from an IP-geo/WHOIS lookup) and want to understand that network's footprint — the full set of IPv4 prefixes it announces, its aggregation profile, and routing-table context. It answers "what address space does this AS control and route." It's a network-analysis tool at the ASN/prefix level, not a per-host or per-person lookup; missing-persons relevance is indirect.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cidr-report.org/as2.0/.
2. Browse the aggregation report, or look up a specific AS number to see its announced prefixes and potential aggregation ("gain").
3. Read the AS detail: total prefixes announced, more-specific announcements, and aggregation opportunities (a rolling 7-day snapshot).
4. Use it to scope which IP ranges belong to/behind a target organisation's AS.
5. Pivot: take prefixes/ASN into `[[bgp-he-net]]` for peering/relationships, reverse-IP/`[[viewdns-info]]` for domains in those ranges, and `[[db-ip]]` to geolocate specific IPs.

## Inputs → Outputs
- **In:** an ASN (or IP prefix context) — resolved from `ip-address`/WHOIS.
- **Out:** `ip-address` prefixes announced by the AS and `employer-org` (the AS's org context), plus aggregation/routing stats.
- **Empty/negative result looks like:** an AS announcing no prefixes (dormant/transit-only) or a private/unrouted ASN — meaning nothing globally routed to analyse.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — public BGP data; you disclose nothing.
- Aggregate/coarse: it operates at the AS/prefix level, not individual hosts. Announcements are a 7-day snapshot and can fluctuate with connectivity issues — don't over-read short-term deltas.
- It tells you what an AS *routes*, not who uses each IP; combine with host-level tools for specifics.

## Overlaps ("do both")
- Overlaps with `[[bgp-he-net]]` (Hurricane Electric BGP) — a friendlier interface for ASN prefixes, peers, and relationships; use it alongside for the same routing questions.
- Feeds `[[viewdns-info]]`/`[[db-ip]]` — turn discovered prefixes/ASNs into domains and geolocation.

## Trust & verifiability
`trust: trusted` — an authoritative, long-running routing report from a respected source (APNIC/Geoff Huston). It accurately reflects public BGP announcements; just remember it describes networks, not people.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipv4-cidr-report |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
