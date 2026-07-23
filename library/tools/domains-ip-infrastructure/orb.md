---
id: orb
name: orb
description: Use when you have a `domain` and want a broad automated footprint — one CLI run gathers WHOIS, subdomains, DNS records, and (active) port/service scans, returning linked `domain` and `ip-address` intel.
url: https://github.com/epsylon/orb
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Broad one-shot footprinting of a domain — WHOIS, subdomains, DNS, and optional port scan bundled into a single report.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free, open-source Python tool (epsylon/orb); needs Python 3, some pip libs, and the nmap binary for active scans.
opsec: active
opsecNote: Passive modules (WHOIS, search-engine, DNS, subdomains) don't touch the target, but orb's port/service scanning connects directly to the target host and lands in its logs. Only scan infrastructure you're authorized to test, and run active scans through a controlled egress.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: By epsylon (author of UFONet); a real but niche, lightly-maintained footprinting tool — verify its module output against dedicated tools before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- dome
aliases:
- epsylon/orb
tags:
- footprinting
- recon
source: gh-topic-footprinting
lastVerified: '2026-07-23'
enrichment: full
---

# orb

> A single-command footprinting tool: point it at a domain and it fans out across WHOIS, DNS, subdomains, search engines, and (optionally) an nmap port scan, dumping everything into a report.

## When to use
You have a `domain` (or an `ip-address`) and want a **fast, broad first pass** that collects the obvious infrastructure facts in one go rather than running WHOIS, dig, a subdomain finder, and nmap separately. Good for the opening recon phase on a target's website or mail domain; its findings then feed more precise tools.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/epsylon/orb && cd orb`, install the Python deps (ddgs, python-whois, dnspython, python-nmap, requests) and ensure `nmap` is on the system.
2. Run against a target ("spell"): `python3 orb.py -t example.com` (see `--help` for module toggles and multi-TLD options).
3. Choose scope: keep it to **passive** modules (WHOIS/DNS/subdomains/search) for a stealthy pass, or enable **active** port scanning when authorized.
4. Read the per-target report written to `reports/` (text and optional JSON): WHOIS, A/NS/MX/TXT records, discovered subdomains, open ports/banners, any CVE hits.
5. Pivot: subdomains → resolve to `ip-address`; IPs → reverse-IP and hosting; open services → targeted follow-up.

## Inputs → Outputs
- **In:** `domain` (or `ip-address`)
- **Out:** `domain` (subdomains), `ip-address` (resolutions), DNS records, WHOIS, open ports/services
- **Empty/negative result looks like:** sparse report — no subdomains, WHOIS privacy-protected, no open ports responding — meaning a locked-down or CDN-fronted target, not a tool failure.

## Gotchas & OpSec
- **Active scanning is loud and legally gated** — port scans hit the target directly; don't run them without authorization.
- Niche and not heavily maintained; individual modules can lag or break — cross-check important findings with dedicated tools (crt.sh, dig, nmap directly).
- Search-engine modules can trip rate limits/CAPTCHAs on heavy use.

## Overlaps ("do both")
- Pairs with [[dome]] — orb gives a broad multi-signal footprint; Dome goes deeper specifically on subdomain enumeration (21 sources + brute force). Use orb for the sweep, Dome to exhaust the subdomain surface.

## Trust & verifiability
`trust: community` — a genuine open-source tool from a known author, but niche and lightly maintained; treat it as a convenient aggregator whose outputs you confirm with authoritative sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | orb |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
