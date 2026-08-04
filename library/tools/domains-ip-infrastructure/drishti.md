---
id: drishti
name: Drishti
description: Use when you have a `domain`, `ip-address`, or Instagram handle and want a quick all-in-one recon dump — returns DNS, reverse-IP, ports, headers, and Instagram profile data.
url: https://github.com/indiancyberops/Drishti
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A no-API-key, menu-driven first-pass recon toolkit bundling DNS, IP, port, header, and Instagram lookups.
selectorsIn:
- domain
- ip-address
- username
selectorsOut:
- domain
- ip-address
- image
- social-profile
status: live
pricing: free
costNote: Free and open source (MIT); requires no API keys.
opsec: active
opsecNote: Several modules (port scanning, traceroute, HTTP header grabs, reverse-IP) send traffic directly to the target's infrastructure and can be logged by it. The Instagram module queries Instagram. Run from a VPN/disposable host and avoid the active modules if you need to stay quiet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community-authored Node.js toolkit (indiancyberops), MIT-licensed and auditable but small (few commits); it wraps public lookup services, whose accuracy varies — verify anything important with a dedicated tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Drishti OSINT toolkit
tags:
- domain-recon
- ip-lookup
- instagram
- multi-tool
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Drishti

> A menu-driven Node.js recon toolkit that bundles a grab-bag of lookups — DNS, reverse-IP, ports, headers, hash decrypt, and Instagram profile pulls — behind one CLI, no API keys.

## When to use
You have a `domain`, `ip-address`, or an Instagram `username` and want a fast, scriptable sweep across several basic recon services without opening each one in a browser. Drishti is a convenience wrapper — good for a quick first pass to see what low-hanging data exists before reaching for specialist tools.

## How to use it (`bestInteractionPattern`: cli)
1. Install Node.js, then clone: `git clone https://github.com/indiancyberops/Drishti`.
2. From the directory, run `node main.js` (works on Linux, Windows, and Termux).
3. Pick a module from the menu:
   - **Domain/IP:** DNS lookup, reverse-IP, IP geolocation, traceroute, port scan, HTTP headers.
   - **Instagram:** profile info lookup and profile-picture (`image`) download.
   - **Utility:** URL expand/shorten, hash decrypt.
4. Read the module output and pivot: reverse-IP `domain`s → other sites on the host; Instagram profile `image` → reverse-image search; open ports → service enumeration.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or Instagram `username`
- **Out:** DNS records / `domain`s, `ip-address` data, open ports, headers, Instagram `social-profile` + profile `image`
- **Empty/negative result looks like:** a module erroring or returning blanks — Drishti depends on third-party endpoints that go down or change, so a failure often means the upstream service moved, not that no data exists; retry with a dedicated tool.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must install Node.js and clone locally (`localInstall`).
- OpSec: **active** — port scans, traceroute, header grabs, and reverse-IP touch the target's infrastructure and are logged; the Instagram module hits Instagram. Use a VPN/disposable host; skip active modules for stealth.
- It's a thin wrapper over public services of varying reliability — treat results as leads and confirm critical findings with purpose-built tools.

## Overlaps ("do both")
- Pairs with dedicated DNS/WHOIS and Instagram-OSINT tools — Drishti is breadth-first and convenient, while specialist tools go deeper and are more current on any single lookup.

## Trust & verifiability
`trust: community` — open MIT code you can read, but small and dependent on third-party endpoints; verify anything you'll rely on against an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | drishti |
