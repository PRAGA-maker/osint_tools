---
id: intelspy
name: intelspy
description: Use when you have an `ip-address`/`domain`/range and want automated multi-threaded service enumeration and web/SMB scans — returns open ports, services and enumerated infrastructure.
url: https://github.com/maldevel/intelspy
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Automated active recon and service enumeration of a host or network range.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free/open-source (GPLv3) Python 3 tool; no account. It orchestrates external tools (nmap, nikto, gobuster, smbmap), which must be installed.
opsec: active
opsecNote: Active and noisy — it launches port scans, service probes, web content scans and brute-forcing directly against the target. This is unmistakably hostile in logs/IDS; only run against systems you are explicitly authorised to test, from a controlled egress.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community offensive-recon tool (~237 stars, v2) by maldevel; a wrapper that automates well-known scanners.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- maldevel-osint
- crab
aliases:
- maldevel/intelspy
tags:
- network-recon
- scanning
- enumeration
source: gh-topic-intelligence-gathering
lastVerified: '2026-07-29'
enrichment: full
---

# intelspy

> A multi-threaded Python recon orchestrator that maps and enumerates a target network — automating nmap, nikto, gobuster and smbmap end to end.

## When to use
You have an `ip-address`, `domain`, hostname or CIDR range you are **authorised** to assess and want a hands-off active recon pass: live-host detection, port scanning, service enumeration, web content scanning, SMB enumeration, brute-forcing and offline exploit lookup. Infrastructure/penetration-testing focused — no people-finding value; it's for characterising authorised target networks.

## How to use it (`bestInteractionPattern`: cli)
1. Install Python 3 and the external scanners it drives (nmap, nikto, gobuster, smbmap).
2. Run against a target with a project name and working directory, e.g. specify IP/CIDR/hostname plus a profile.
3. It threads through discovery → port/service enumeration → web/SMB scans → optional brute force, writing results to the project dir.
4. Review the per-service output it collects for each host.
5. Pivot: enumerated services/versions feed vulnerability assessment; discovered hostnames feed domain mapping.

## Inputs → Outputs
- **In:** `ip-address`/CIDR or `domain`/hostname (authorised scope)
- **Out:** `ip-address`/`domain` — live hosts, open ports, service/version detail, web and SMB enumeration
- **Empty/negative result looks like:** a fully firewalled/host-down target (no open services) — a valid result, not a tool error.

## Gotchas & OpSec
- Human-in-the-loop: none, but authorisation is mandatory — brute-forcing and probing are involved.
- OpSec: **active and loud** — this will appear as an attack in the target's logs; only run against systems you have written permission to test, from a controlled egress.
- It's a wrapper: results are only as good as the underlying tools, which must be installed and current.

## Overlaps ("do both")
- Heavier-weight sibling to `[[crab]]` — Crab is a quick single-host scan, intelspy automates a full multi-tool enumeration across a range. Pair with `[[maldevel-osint]]` for the same author's passive tooling.

## Trust & verifiability
`trust: community` — a popular community wrapper around standard scanners; the findings come from nmap/nikto/etc., so verify service/version detail against those tools directly and stay within authorised scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelspy |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
