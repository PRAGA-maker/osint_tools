---
id: nazar
name: NAZAR
description: Use when you have a `username`, `ip-address` or `domain` and want to run several basic recon modules from one CLI — returns social-profile, ip-address and domain data.
url: https://github.com/MR-NULL666/NAZAR
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A single lightweight CLI menu bundling basic recon (Instagram lookup, IP/reverse-IP, DNS, port scan, headers).
selectorsIn:
- username
- ip-address
- domain
selectorsOut:
- social-profile
- ip-address
- domain
status: degraded
pricing: free
costNote: Free and open source, no API keys required. Small hobby project — last release (1.0.6) dated 2021; dormant but installable.
opsec: active
opsecNote: Modules like port scan, traceroute and header detection send packets directly from your host to the target, which is logged there; the Instagram/DNS/reverse-IP modules go through third-party services. Run from a VPN/VPS you're willing to burn, and don't point the active scanners at infrastructure you're not authorised to probe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Minimal single-author toolkit (a few commits, ~20 stars, dormant since 2021) that wraps public services and standard network tools. Nothing here is authoritative; verify every module's output at its original source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- NAZAR OSINT toolkit
- MR-NULL666/NAZAR
tags:
- Tools collections/toolkits
- recon
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# NAZAR

> A small no-API-key OSINT CLI menu that bundles a handful of basic recon modules (Instagram profile, IP / reverse-IP, DNS, port scan, headers, URL expand, hash decrypt) behind one command.

## When to use
You want a quick, self-contained CLI to run a few elementary lookups without wiring up separate tools or keys — a fast first pass on a `username`, `ip-address`, or `domain`. Treat it as a convenience launcher for basic checks, not a serious investigative platform; each module just fronts a public service or a standard network utility.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo from GitHub and follow its README to install (runs on Termux/Android, Linux — tested on Kali — and Windows x64; needs Node.js).
2. Launch the tool to get the numbered menu, then pick a module: Instagram lookup/DP download, IP + reverse-IP, DNS resolve, port scan, HTTP header detect, URL shorten/expand, hash decrypt, traceroute, device info.
3. Enter the selector the module asks for (`username`, `ip-address`, or `domain`).
4. Read the result and — because sourcing is opaque and dated — confirm anything actionable directly at the underlying service.
5. Pivot: an Instagram hit feeds cross-platform username search; an IP/DNS/port result feeds infrastructure mapping.

## Inputs → Outputs
- **In:** `username`, `ip-address`, or `domain` (per module)
- **Out:** `social-profile` (Instagram), `ip-address` / reverse-IP + geo, `domain`/DNS records, open ports, HTTP headers
- **Empty/negative result looks like:** a module erroring or returning blank — often because the third-party endpoint it calls has changed or died since 2021. Fall back to a maintained equivalent.

## Gotchas & OpSec
- **Dormant since 2021** — modules that depend on external APIs (especially the Instagram lookup) are the first to break; expect some to fail.
- Active modules (port scan, traceroute) touch the target directly and are logged there — only run them against systems you're authorised to test, from a burner VPS/VPN.
- No verification layer: outputs are only as good as the upstream service; corroborate before acting.

## Overlaps ("do both")
- Redundant with dedicated single-purpose tools (a proper reverse-IP service, a maintained username searcher, `nmap`). Prefer those for anything important; use NAZAR only for a fast, low-stakes first look.

## Trust & verifiability
`trust: unverified` — a tiny, dormant hobby toolkit wrapping public services. Fine for quick throwaway checks; never rely on it as a source of record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nazar |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, ip-address, domain → social-profile, ip-address, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
