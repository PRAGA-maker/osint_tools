---
id: nmap-online
name: Nmap Online (osint.sh)
description: Use when you have a `domain` or `ip-address` and want a quick browser-based Nmap port scan without a local install — returns open ports and detected services.
url: https://osint.sh/nmap/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-click online Nmap scan of a host's common ports from the OSINT.sh toolset.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free tool in the OSINT.sh suite; no account required.
opsec: active
opsecNote: The scan is issued from OSINT.sh's servers, so your own IP is not what hits the target — but a scan still reaches the target and can appear in its logs as scanner traffic. Only scan hosts you're authorized to probe; the scope is limited to common ports.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of the widely-used free OSINT.sh toolkit; a thin hosted Nmap front-end whose results are reproducible with a local Nmap.
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
- osint.sh nmap
- online nmap
tags:
- port-scan
- nmap
- infrastructure
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Nmap Online (osint.sh)

> A hosted, one-click Nmap port scan for a domain or IP, part of the free OSINT.sh toolset.

## When to use
You have a `domain` or `ip-address` and want a fast check of which common ports are open and what services respond, but you're on a machine where installing or running Nmap isn't practical. Good for confirming a host is live and getting a quick service fingerprint before deeper infrastructure work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/nmap/.
2. Enter the target `domain` or `ip-address`.
3. Run the scan and wait for it to complete.
4. Read the list of open ports and identified services.
5. Pivot: an open web port feeds domain/DNS tooling; an unusual open service is worth deeper (authorized) investigation.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** open ports and detected services (and the resolved `ip-address`)
- **Empty/negative result looks like:** no open ports reported — the host may be firewalled or offline, or the scan is limited to common ports only; not proof nothing is running.

## Gotchas & OpSec
- **Active:** the scan reaches the target and may be logged; only scan authorized hosts.
- Scope is limited to common ports — for a full sweep use a local Nmap you control.
- Results are only as current as the moment of the scan.

## Overlaps ("do both")
- Pairs with other online scanners (e.g. `[[online-port-scanner]]`) — run both if one front-end is rate-limited or too shallow, since their default methods differ.

## Trust & verifiability
`trust: community` — a hosted wrapper around the standard Nmap engine within the popular OSINT.sh suite; anything important is re-verifiable with a local Nmap run.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nmap-online |
