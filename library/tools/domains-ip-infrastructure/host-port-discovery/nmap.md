---
id: nmap
name: Nmap
description: Use when you have a `domain`/`ip-address` and want its open ports, services and OS — the canonical port scanner returning live hosts, `ip-address`es and service banners.
url: https://nmap.org/download.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- host-port-discovery
bestFor: Discovering live hosts, open ports, running services/versions and OS fingerprints on an authorized target network.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free and open source (Nmap Public Source License). Cross-platform CLI (with the Zenmap GUI); no account.
opsec: active
opsecNote: Nmap sends packets directly to the target — it is unambiguously ACTIVE and appears in the target's firewall/IDS logs; aggressive timing/version/OS scans are loud and can trigger alerts or blocks. Only scan systems you are explicitly authorized to test. If you must reduce noise, use slower timing, fewer ports, and scan from disposable infrastructure — but authorization, not stealth, is the real safeguard.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: The de facto industry-standard network scanner (Gordon Lyon / Insecure.Org), open source and audited for decades; results are authoritative for what the network exposed at scan time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- Network Mapper
- nmap
tags:
- port-scan
- recon
- infrastructure
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Nmap

> The canonical network scanner — maps live hosts, open ports, service versions and OS fingerprints. Infrastructure recon for authorized assessments, not a people-finder.

## When to use
You have a `domain` or `ip-address` (or a range) that you are **authorized** to assess and want to know what it exposes: which hosts are up, what ports are open, what services/versions run, and a best-guess OS. In OSINT/investigation terms it's for characterizing a subject's or organization's authorized-scope infrastructure and attack surface — not for finding a person. Reach for it after passive recon, when active confirmation is permitted.

## How to use it (`bestInteractionPattern`: cli)
1. Install Nmap from nmap.org (Windows/macOS/Linux) — confirm you have authorization for the target first.
2. Resolve/confirm the target `domain`/`ip-address` or range.
3. Run a scan, e.g. `nmap -sV <target>` (service/version), add `-O` for OS detection, `-p-` for all ports, `-sC` for default scripts; tune `-T` timing.
4. Read the output: open ports, service banners/versions, OS guess, and host `ip-address`es.
5. Pivot: service versions feed vulnerability lookups; discovered hosts/IPs feed geolocation/ASN and further mapping.

## Inputs → Outputs
- **In:** `domain` / `ip-address` (or CIDR range)
- **Out:** live hosts, open ports, service/version banners, OS fingerprint, resolved `ip-address`es
- **Empty/negative result looks like:** all ports filtered/closed or host "down" — a firewall may be dropping probes (not proof the host is offline); adjust technique within your authorized scope.

## Gotchas & OpSec
- **Active and loud:** every scan hits the target and is logged; only scan with explicit authorization.
- Firewalls/IDS can block or feed misleading results; interpret "filtered" carefully.
- OS/version detection is a best guess, not ground truth — corroborate before relying on it.

## Overlaps ("do both")
- Pairs with passive tools like Shodan/Censys (which report exposure without you sending packets) and with `[[server-status-pwn]]` and vulnerability scanners — use passive recon first, Nmap to actively confirm within scope.

## Trust & verifiability
`trust: trusted` — the long-established, open-source industry-standard scanner; its observations are authoritative for the network's state at scan time, subject only to filtering/evasion by the target.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nmap |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
