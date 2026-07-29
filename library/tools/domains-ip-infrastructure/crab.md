---
id: crab
name: Crab
description: Use when you have a `domain`/`ip-address` and want a one-command port scan plus WHOIS/IP-info and OS guess — returns open ports, ip-address and domain registration detail.
url: https://github.com/N0tA1dan/Crab
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quick combined port scan + WHOIS/IP lookup + OS detection against a single host.
selectorsIn:
- domain
- ip-address
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free/open-source (GPL-3.0) Python tool; no account or key.
opsec: active
opsecNote: Active — port scanning sends packets directly to the target host, which is visible in the target's logs/IDS and may be treated as hostile. Only scan systems you are authorised to test, from a research/VPN egress; the WHOIS/IP-info portion is passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Community single-author Python project (~24 stars) with a GPL-3.0 licence and an unlawful-use disclaimer; small and unaudited.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- webosint
aliases:
- N0tA1dan/Crab
tags:
- Domain/IP/Links
- Domain/IP investigation
- port-scanner
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Crab

> A small Python CLI that bundles a port scanner with IP-info, WHOIS lookup and (beta) OS detection for a single host.

## When to use
You have a `domain` or `ip-address` tied to a subject/organisation and want a fast, combined read on it — which ports/services are open, the registrant/registry WHOIS, basic IP info, and a rough OS guess — from one command. Infrastructure-focused; minimal direct people-finding value, but useful for characterising a host you've already tied to a subject.

## How to use it (`bestInteractionPattern`: cli)
1. Requirements: Python 3+, pip, git. Clone the repo, `cd src`, `pip install -r requirements.txt`.
2. Run `python crab.py` and choose an action; port scanning takes a target and timeout, e.g. `python crab.py -sA [target] [timeout_seconds]`.
3. Read results: open ports/services, IP information, WHOIS/registrar details, OS-detection guess (beta).
4. Distinguish the **active** scan (open ports) from the **passive** WHOIS/IP lookup — run only the passive parts if you must stay quiet.
5. Pivot: registrar/WHOIS fields feed domain-ownership research; open services feed further infrastructure mapping.

## Inputs → Outputs
- **In:** `domain` or `ip-address` (+ timeout for scans)
- **Out:** open ports/services, `ip-address` info, `domain` WHOIS/registrar data, OS guess
- **Empty/negative result looks like:** all ports filtered/closed (firewalled host), or redacted/privacy WHOIS — expected, not a failure.

## Gotchas & OpSec
- Human-in-the-loop: none, but scanning is your legal/opsec responsibility.
- OpSec: **active** for port scans — packets reach the target and may trigger alerts; only scan authorised targets from a controlled egress.
- OS detection is beta/unreliable; treat it as a hint. As a small unaudited script, verify anything important against dedicated tools.

## Overlaps ("do both")
- Pairs with `[[webosint]]` — WEBOSINT for passive WHOIS/DNS/subdomain context, Crab when you specifically need an active port/service view of a host.

## Trust & verifiability
`trust: unverified` — a small single-author tool; cross-check open-port and WHOIS results with an authoritative scanner/registry before acting, and only scan systems you're permitted to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crab |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → ip-address, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
