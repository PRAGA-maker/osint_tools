---
id: aort
name: AORT
description: Use when you have a `domain` and want one command to enumerate its subdomains, ports, endpoints and harvested emails — returns related `domain`s and `email`s.
url: https://github.com/D3Ext/AORT
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-shot domain reconnaissance (subdomains + ports + Wayback endpoints + email harvest) from a single CLI run.
selectorsIn:
- domain
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free and open source (MIT); install cost is only the pip package or a git clone.
opsec: active
opsecNote: AORT actively touches the target — DNS zone-transfer attempts, port scans and live subdomain probing generate traffic to the target's own infrastructure. Run from a disposable VPS/IP, not your attributable network, and stick to passive modes if you must stay quiet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source project by D3Ext with public commit history and a userbase in the bug-bounty community; you can read the code before running it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- All in One Recon Tool
- D3Ext AORT
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# AORT

> A single-command domain recon wrapper: point it at a domain and it enumerates subdomains, scans common ports, pulls Wayback endpoints and harvests emails in one pass.

## When to use
You have a `domain` tied to a subject (a personal site, a small business, an org they run) and want a fast, broad map of its attack/footprint surface — subdomains that reveal other services, exposed ports, historical endpoints from the Wayback Machine, and any emails advertised on it. Best as a quick first sweep before drilling into individual findings.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install aort` (or `git clone https://github.com/D3Ext/AORT && cd AORT && pip3 install -r requirements.txt`).
2. See options: `python3 AORT.py -h`.
3. Dump subdomains only (quieter): `python3 AORT.py -d example.com`.
4. Full recon: `python3 AORT.py -d example.com --all` — adds port scan, WAF detection, subdomain-takeover checks, Wayback endpoints and email harvesting.
5. Pivot: feed discovered subdomains into a hosting/WHOIS lookup, and harvested `email`s into email-OSINT tools.

## Inputs → Outputs
- **In:** a `domain`
- **Out:** list of subdomains (`domain`), open ports, historical endpoints, harvested `email`s, WAF/takeover flags
- **Empty/negative result looks like:** a locked-down domain returns few or no subdomains and no emails — that is a real signal (small footprint), not a failure; cross-check with a second enumerator before concluding.

## Gotchas & OpSec
- Requires Python 3 and network egress; some checks depend on optional API keys for fuller subdomain sources.
- OpSec: **active** — zone transfers, port scans and live probing hit the target directly and can be logged. Use a throwaway IP; prefer the passive `-d` mode when stealth matters.
- Results overlap with other enumerators and can include stale Wayback endpoints (404 today) — verify before acting.

## Overlaps ("do both")
- Pairs with any dedicated subdomain-enumeration or WHOIS tool — AORT is breadth-first and convenient, but a specialist enumerator (with more data sources/API keys) will surface subdomains AORT's built-in sources miss.

## Trust & verifiability
`trust: community` — open-source and auditable; the outputs (DNS records, open ports, archived URLs) are independently reproducible, so confidence comes from re-checking findings rather than from the tool itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aort |
