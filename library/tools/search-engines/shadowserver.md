---
id: shadowserver
name: Shadowserver Dashboard
description: Use when you have an `ip-address`, ASN, or country and want threat-exposure context — returns aggregate stats on scanned, compromised, and vulnerable devices (per-network detail requires owning the network).
url: https://dashboard.shadowserver.org/
category: search-engines
path:
- search-engines
bestFor: Network-level threat intelligence — exposure/compromise statistics by country and ASN.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free public dashboard for aggregate statistics; free per-network daily reports are available only to verified network owners/CERTs (the granular per-IP data is not an open lookup).
opsec: passive
opsecNote: The public dashboard shows aggregate scan/honeypot data and never contacts a target host. Detailed per-network reports require Shadowserver to verify you own/administer that netblock, which identifies you to them. Reading the dashboard is anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Shadowserver is a respected nonprofit security foundation whose internet-wide scanning data is used by CERTs and network operators worldwide.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- shadowserver-foundation
- shodan
- greynoise
aliases:
- Shadowserver
- dashboard.shadowserver.org
tags:
- threat-intel
- infrastructure
- scanning
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Shadowserver Dashboard

> A nonprofit's internet-wide security telemetry: the public dashboard shows aggregate statistics on scanned, honeypot-observed, vulnerable, and compromised devices by country, ASN, and device type.

## When to use
You're profiling infrastructure — an `ip-address`, an ASN, or a country/region — and want context on its threat exposure: how many devices there are running vulnerable services, showing up in honeypots, or acting as C2/compromised hosts. It's an infrastructure-intelligence and situational-awareness source, not a person-finder; use it to characterize a hosting network or country's exposure, or (if you administer a network) to get per-IP compromise reports.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dashboard.shadowserver.org/ and choose a statistic set (general scans, IoT devices, attacks, honeypot, vulnerable/compromised).
2. Filter/visualize by country, ASN, device type, or CVE; use the map/tree-map/time-series views to see where exposure concentrates.
3. Read the aggregate counts to characterize the network/region in question — this is population-level data, not a per-arbitrary-IP lookup.
4. To get actionable per-IP detail, subscribe to Shadowserver's free daily reports — but that requires verifying you own or are the CERT for the netblock.
5. Pivot: for per-host detail on infrastructure you don't own, use `[[shodan]]`/`[[greynoise]]`; use Shadowserver for the macro exposure picture.

## Inputs → Outputs
- **In:** `ip-address`/ASN/country as a filter context
- **Out:** aggregate `ip-address`-population stats — counts of scanned/vulnerable/compromised devices by geography, network, and type
- **Empty/negative result looks like:** a filter with negligible counts — few observed devices for that ASN/country/type in Shadowserver's telemetry; not proof of no exposure, only of nothing in their datasets.

## Gotchas & OpSec
- The open dashboard is **aggregate** — it does not let the public look up an arbitrary single IP's compromise status; that data is gated to verified network owners.
- Best treated as infrastructure/threat context, with low direct relevance to locating a person.
- OpSec: **passive** for the dashboard; requesting network reports identifies you and requires proof of ownership.

## Overlaps ("do both")
- Pairs with `[[shodan]]` and `[[greynoise]]` — those give per-host service/behaviour detail Shadowserver's public tier won't, while Shadowserver gives the macro compromise landscape; combine for both scales.

## Trust & verifiability
`trust: trusted` — Shadowserver is a well-established security nonprofit and its scanning telemetry is an industry reference; the public tier's limitation is granularity (aggregate), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shadowserver |
| category | search-engines |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
