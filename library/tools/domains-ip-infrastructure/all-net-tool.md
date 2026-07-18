---
id: all-net-tool
name: All Net Tool
description: Use when you have a `domain` or `ip-address` and want quick network diagnostics — returns WHOIS, traceroute, DNS, and proxy/anonymity check results.
url: http://all-nettools.com/index.htm
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A classic web-based toolbox for WHOIS, traceroute, DNS lookups, and proxy/anonymity testing.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free web tools; no account required.
opsec: active
opsecNote: Some tools (traceroute, ping, port scan) send packets to the target host from the service's servers, not yours — that shields your IP but is still an active probe against the subject's infrastructure. WHOIS/DNS lookups are passive. Choose the tool to match the OpSec you need.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing (pre-2010) network-tools site; the lookups are standard utilities, but it's an ad-supported third party, so verify critical results against authoritative sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- all-nettools.com
- AllNetTools ToolBox
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- all-net-tools-toolbox-blacklist-checker
- all-net-tools-toolbox-domain-information
- all-net-tools-toolbox-traceroute
---

# All Net Tool

> A veteran web-based network toolbox (all-nettools.com "ToolBox"): WHOIS, traceroute, DNS, ping, port scan, and a proxy/anonymity test — run from the site's servers so your own IP stays back.

## When to use
You have a `domain` or `ip-address` and want fast, no-install network diagnostics: who owns/registered a domain (WHOIS), the network path to a host (traceroute), its DNS records, or whether an IP is reachable. Also handy for the "SmartWhois"/anonymity-test tools to sanity-check your own proxy/VPN before an operation. A convenient one-stop when you don't want to run CLI tools locally.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://all-nettools.com/ and go to the ToolBox.
2. Pick the tool: WHOIS, DNS lookup, traceroute, ping, port scan, or proxy/anonymity test.
3. Enter the `domain` or `ip-address` and run it.
4. Read the output: registrant/registrar and dates (WHOIS), hop path and latency (traceroute), records (DNS), open ports, etc.
5. Pivot: WHOIS registrant/nameservers feed host attribution; a traceroute's final hops locate the hosting network; confirm findings in an authoritative WHOIS/DNS source.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** WHOIS record, DNS records, traceroute path, port/ping status (`domain`/`ip-address` attribution)
- **Empty/negative result looks like:** a timeout or "no data" — the host may block probes, the WHOIS may be privacy-protected, or the tool's data may be stale; corroborate before concluding.

## Gotchas & OpSec
- Active tools (traceroute/ping/port scan) probe the target host — they run from the service's IP, not yours, but they still touch the subject's infrastructure; use WHOIS/DNS when you must stay passive.
- It's an older, ad-supported site; WHOIS/DNS data can lag authoritative registries — treat as a quick check, not a system of record.
- OpSec: mixed — passive for record lookups, active for network probes.

## Overlaps ("do both")
- Pairs with authoritative WHOIS/DNS services and its own sibling tools ([[all-net-tools-toolbox-domain-information]], [[all-net-tools-toolbox-traceroute]], [[all-net-tools-toolbox-blacklist-checker]]) — use those for the specific lookup and a registry-grade source to confirm.

## Trust & verifiability
`trust: community` — a reputable but ageing third-party toolbox. The utilities are standard and their raw output is genuine, but for anything decisive re-run the query against an authoritative registry/DNS resolver.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | all-net-tool |
