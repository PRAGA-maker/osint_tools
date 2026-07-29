---
id: eyewitness
name: EyeWitness
description: Use when you have a list of `domain`s/URLs/IPs and want automated screenshots plus header/title capture to triage many web services fast — returns image and metadata-exif leads.
url: https://github.com/ChrisTruncer/EyeWitness
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- tools
bestFor: Bulk-screenshotting and fingerprinting a large list of web services to triage which are worth investigating.
selectorsIn:
- domain
- ip-address
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Free, open-source (Python). Ships in Kali; install via the repo's setup script.
opsec: active
opsecNote: ACTIVE — EyeWitness makes real HTTP(S) requests to every target to grab screenshots and headers, so your IP appears in each target's server logs. Use a VPN/proxy or Tor routing, throttle, and only point it at hosts you're authorized to enumerate. Not a passive tool despite feeling like "just screenshots".
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely-used, well-known recon tool by Chris Truncer (FortyNorth Security); mature and broadly trusted in the security community.
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
- EyeWitness
tags:
- screenshotting
- web-recon
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# EyeWitness

> A recon workhorse that takes a big list of web targets and returns a browsable report of screenshots, page titles, and server headers — so you can eyeball hundreds of sites in minutes instead of opening each.

## When to use
You have many web targets — a list of `domain`s/subdomains (e.g. from `[[cert4recon]]`/Amass), URLs, or `ip-address`:port pairs — and need to see what each actually serves without visiting them one by one. EyeWitness screenshots every host, records headers/titles, groups similar pages, and flags default-credential login panels. Ideal after subdomain/port enumeration to prioritize which of a subject's or organization's web assets deserve a closer look.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/ChrisTruncer/EyeWitness and run its `setup.sh` (or use the Kali package).
2. Prepare an input list — a plain URL/host file, or Nmap/Nessus XML.
3. Run: `eyewitness --web -f targets.txt -d report_dir` (route through a proxy/VPN first).
4. Open the generated HTML report: screenshots, titles, headers, and category groupings.
5. Pivot: interesting panels/logos → identify the org/software; a login page → note tech stack; screenshots → visual matching across a subject's infrastructure.

## Inputs → Outputs
- **In:** a list of `domain`s/URLs/`ip-address`:port (or Nmap/Nessus XML)
- **Out:** per-host screenshot (`image`), page title and server headers (`metadata-exif`-style fingerprint), grouped HTML report
- **Empty/negative result looks like:** blank/timeout entries for hosts with no web service, filtering, or TLS errors — means no reachable web app there (from your vantage), not that the host is down for everyone.

## Gotchas & OpSec
- **Active tool** — every target logs your requests; use a proxy/VPN and only scan authorized hosts.
- Large lists are slow and can trip rate-limits/WAFs; tune threads and timeouts.
- Headless-browser rendering can miss heavily JS-driven pages.

## Overlaps ("do both")
- Downstream of subdomain enumeration (`[[cert4recon]]`, Amass, subfinder) and port scanning — those find the hosts, EyeWitness shows you what they serve.

## Trust & verifiability
`trust: community` — mature, widely-used security tool from a known author; screenshots and headers are captured live, so the report reflects real target state at scan time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eyewitness |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
