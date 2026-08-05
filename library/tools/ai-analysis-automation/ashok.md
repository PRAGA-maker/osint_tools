---
id: ashok
name: Ashok
description: Use when you have a `domain`/URL (or GitHub `username`) and want a fast one-command recon sweep — returns subdomains, tech/CMS, DNS, open ports, headers, and dork/Wayback hits.
url: https://github.com/ankitdobhal/Ashok
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Running a quick multi-technique reconnaissance sweep over a target domain from one CLI.
selectorsIn:
- domain
- username
selectorsOut:
- domain
- ip-address
- employer-org
status: live
pricing: free
costNote: Open source under Apache-2.0; free to run locally or via Docker.
opsec: active
opsecNote: Port scanning (Nmap), banner grabbing, and header extraction connect directly to the target's infrastructure and are logged there. Google dorking and Wayback crawling are passive. Run active modules from a disposable VPS/VPN, not an attributable IP, and only against targets you are authorised to assess.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A popular open-source recon toolkit; auditable code but a wrapper over other tools, so verify individual findings against their primary sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Ashok recon
tags:
- Tools collections/toolkits
- recon
- domain-recon
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Ashok

> A "recon Swiss army knife" CLI: one command fans out across subdomain discovery, tech/CMS fingerprinting, DNS, port scanning, dorking, GitHub extraction, and Wayback crawling for a target.

## When to use
You have a `domain` or URL (or a GitHub `username`) tied to a subject or organisation and want a fast, breadth-first infrastructure picture before drilling in with specialist tools. Ashok bundles the common reconnaissance techniques so you can go from a bare domain to subdomains, hosting/tech, open ports, and archived pages in a single run.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/ankitdobhal/Ashok` and install (Python, or run the Docker image); Nmap must be present for port scanning.
2. Run against a target, e.g. `python ashok.py -d target.com` (see `--help` for module flags: subdomains, dorking, GitHub, ports, headers, banner, DNS, Wayback).
3. Read the output (JSON available for some modules): subdomains, detected CMS/tech, DNS records, open ports/banners, and dork/Wayback hits.
4. Pivot: subdomains and IPs feed infrastructure mapping; GitHub extraction feeds developer/`employer-org` OSINT; Wayback hits feed content archaeology.

## Inputs → Outputs
- **In:** `domain`/URL, or GitHub `username`
- **Out:** subdomains, `ip-address`es, tech/CMS, DNS records, open ports, HTTP headers, dork and Wayback results
- **Empty/negative result looks like:** sparse output for a well-locked-down or tiny target, or module errors if a dependency (Nmap, API access) is missing — not proof the surface is clean.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must supply dependencies and choose which modules to run.
- OpSec: **mixed** — dorking/Wayback are passive, but port scanning and banner grabbing touch the target and are logged. Run active modules from disposable infrastructure and only with authorisation.
- It wraps other tools, so quality tracks its dependencies; corroborate key findings against the underlying source (Nmap, crt.sh, Wayback).

## Overlaps ("do both")
- Pairs with dedicated subdomain/cert tools (e.g. crt.sh) and the Wayback Machine — Ashok gives a fast first sweep, those give deeper, authoritative coverage of each dimension.

## Trust & verifiability
`trust: community` — open source and widely used, but a convenience wrapper. Treat its aggregated output as a starting map and confirm anything decisive against the primary data source for that technique.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ashok |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, username → domain, ip-address, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
