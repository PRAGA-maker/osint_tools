---
id: isp-tools
name: ISP.Tools
description: Use when you have a `domain`/`ip-address` and want to probe it from many global vantage points — runs ping, MTR, DNS, portscan, and MTU tests from worldwide probes, returning reachability and `ip-address` intel.
url: https://www.isp.tools
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Distributed network diagnostics — ping/MTR/DNS/portscan a target from probes around the world to see how it responds from different locations.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free web-based distributed diagnostics; no account.
opsec: active
opsecNote: The probes — not your machine — originate the traffic to the target, so active tests (ping/portscan) reach the target from ISP.Tools' infrastructure rather than your IP, which shields you. ISP.Tools still logs your query, and you should only scan hosts you're authorized to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A recognised free network-diagnostics service; the results are standard protocol tests (ping/DNS/traceroute), so they're as reliable as the underlying probes.
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
- isp.tools
tags:
- domain-and-ip-research
- network-diagnostics
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# ISP.Tools

> Distributed network diagnostics from probes worldwide — ping, MTR, DNS, smokeping, MTU detection, and portscan a target from many locations at once, without the traffic originating from you.

## When to use
You have a `domain` or `ip-address` and want to understand its network behaviour: is it reachable, from where, with what latency and routing, which ports are open, and does DNS resolve consistently across regions? Because the tests run from ISP.Tools' global probes, you also get **geographic diversity** (spot geo-blocking / anycast differences) and a degree of separation — the target sees the probe's IP, not yours.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.isp.tools.
2. Enter the target `domain`/`ip-address` and pick a tool: ping, MTR/traceroute, DNS lookup, smokeping, MTU detect, or portscan.
3. Select probe location(s) to run the test from one or several worldwide vantage points.
4. Read the results: reachability/latency, the network path (MTR), resolved `ip-address`/records (DNS), or open ports (portscan).
5. Pivot: resolved IPs → reverse-IP/hosting; routing anomalies or geo-differences → deeper infrastructure analysis.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** reachability/latency, route hops, DNS records/`ip-address`, open ports
- **Empty/negative result looks like:** timeouts / no response — the host blocks ICMP, is down, or is firewalled; a filtered portscan isn't proof nothing runs there.

## Gotchas & OpSec
- **Probe-sourced, not you-sourced:** active tests hit the target from ISP.Tools' IPs, which is a genuine OpSec benefit — but still only test what you're authorized to.
- Results reflect the probe's network view, not yours; a path/latency from Frankfurt won't match your local route.
- ISP.Tools logs your queries; it's not anonymous to the service.

## Overlaps ("do both")
- Complements Hurricane Electric / BGP looking-glass tools and single-vantage utilities: ISP.Tools' edge is multi-location probing, so use it to compare how a target responds across regions before drilling in with a focused tool.

## Trust & verifiability
`trust: community` — a well-regarded free diagnostics service running standard protocol tests; results are reproducible and verifiable against other network tools.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | isp-tools |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
