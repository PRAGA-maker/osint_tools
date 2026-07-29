---
id: masscan
name: Masscan
description: Use when you have an `ip-address` or IP range and want to find open ports fast — an internet-scale asynchronous port scanner returning live hosts and open ports.
url: https://github.com/robertdavidgraham/masscan
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- host-port-discovery
bestFor: Very fast open-port discovery across a single host or large IP ranges.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free and open-source (Robert Graham); build from source, no account.
opsec: active
opsecNote: Masscan is loud and active — it sends packets directly to every target IP/port, appears in the target's firewall/IDS logs, and at high rates can disrupt networks. It also spoofs nothing about you: the source IP is yours unless you route through infrastructure you control. Only scan hosts you are authorised to scan; unauthorised scanning may be unlawful.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A well-known, widely-used open-source scanner from a reputable author (Robert David Graham); actively maintained.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- masscan
tags:
- port-scanner
- host-discovery
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Masscan

> An internet-scale port scanner: nmap-like output at extreme speed — point it at an IP or range and get open ports back in seconds, but it's active and noisy.

## When to use
An infrastructure tool, not a people-finder. When your case has narrowed to a specific server/`ip-address` (a host tied to a subject's site, a suspect service) that you are **authorised** to probe, and you want to know quickly what ports/services it exposes. The open-port profile tells you what the host runs (web, mail, remote-access), which feeds service-level investigation.

## How to use it (`bestInteractionPattern`: cli)
1. Build: clone the repo, `make && make install` (Linux, needs gcc/make).
2. Scan a host/range for ports: `masscan -p80,443,8000-8100 <ip-or-CIDR> --rate 1000`.
3. Keep `--rate` sane (default is aggressive) to avoid disruption and detection.
4. Output to a parseable format: `-oJ out.json` (or `-oX` nmap-compatible).
5. Pivot: feed open web ports into HTTP fingerprinting, and confirmed services into deeper (authorised) enumeration.

## Inputs → Outputs
- **In:** `ip-address` / IP range + port list
- **Out:** live hosts and their open ports (`ip-address` + ports)
- **Empty/negative result looks like:** no open ports reported — the host is down/filtered, a firewall drops your probes, or your rate/timeout was too aggressive to get replies.

## Gotchas & OpSec
- **Active and noisy** — you will appear in logs; only scan authorised targets and mind the legal line.
- High rates can overwhelm networks/NAT — throttle `--rate`.
- Masscan finds ports fast but does light service detection; follow up with nmap `-sV` on the hits for detail.

## Overlaps ("do both")
- Pairs with nmap (masscan for fast wide port discovery, nmap for deep service/version detection on the found ports) and with passive alternatives like Shodan/Censys when you must **not** touch the target — use those first if OpSec forbids active scanning.

## Trust & verifiability
`trust: community` — mature, open-source, reputable author; results are directly reproducible and verifiable against the target (with authorisation).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | masscan |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
