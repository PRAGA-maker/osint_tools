---
id: scan4all
name: scan4all
description: Use when you have a target `domain`/`ip-address` range and want a fast all-in-one vulnerability and port scan — returns open ports, fingerprints, and PoC-based vuln findings.
url: https://github.com/hktalent/scan4all
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: High-speed combined port scanning, fingerprinting, and vulnerability detection (nuclei/nmap-integrated).
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free and open-source (BSD-3); Go tool (`go install github.com/GhostTroops/scan4all@latest`; the hktalent repo is the same project). No account.
opsec: active
opsecNote: Highly ACTIVE — it port-scans, fingerprints, brute-forces and fires thousands of PoCs directly at the target, which is loud and unambiguously logged/alertable. Only run against systems you are explicitly authorised to test; scope it and route through controlled infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source offensive scanner (hktalent/GhostTroops) integrating nuclei/nmap/vscan; findings need verification, and running it is an intrusive act requiring authorisation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- scan4all
- GhostTroops scan4all
tags:
- domains-ip-infrastructure
- vulnerability-scanner
- port-scan
- cli
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# scan4all

> A fast, all-in-one offensive scanner — port scanning, web fingerprinting, and thousands of nuclei PoCs in one Go binary. Powerful and very loud; authorised targets only.

## When to use
You are conducting an authorised assessment of a `domain` or `ip-address` range and want a rapid, consolidated picture: open ports/services, web fingerprints, and known-vulnerability findings via an integrated PoC/nuclei engine. It folds nmap/nuclei/vscan-style capabilities into one tool for speed.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/GhostTroops/scan4all@latest` or grab a release binary (the hktalent repo redirects to the same project).
2. Run against authorised targets: `scan4all -l targets.txt` (accepts IP/CIDR/URL/file); `scan4all -h` for options; export JSON/CSV/Elasticsearch.
3. Read the output: open ports/services (`ip-address`), fingerprints, and vuln findings with their PoC references.
4. Pivot: confirmed services/`domain`s feed deeper manual testing; each vuln finding must be verified before reporting.

## Inputs → Outputs
- **In:** `domain`, `ip-address`/CIDR, or a target file
- **Out:** open ports/services, web fingerprints, and PoC-based vulnerability findings
- **Empty/negative result looks like:** all ports filtered / no PoC matches — a hardened or well-firewalled target, or the scan was blocked; not proof of no vulnerabilities.

## Gotchas & OpSec
- Extremely ACTIVE and intrusive (scanning + brute-force + PoCs) — authorisation is mandatory; it will trip IDS/WAF and be logged.
- Automated PoCs produce false positives — verify every finding manually.
- High volume can disrupt fragile targets; throttle and scope carefully.

## Overlaps ("do both")
- Overlaps with `[[finalrecon]]`, `[[dnsrecon]]` (recon) and nuclei/nmap directly — scan4all bundles them for speed; drop to the individual tool for careful, verifiable depth on a specific finding.

## Trust & verifiability
`trust: community` — a capable open-source aggregator of other engines; because it automates PoCs, treat findings as leads to confirm, and remember that running it is an intrusive, authorisation-gated action.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scan4all |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
