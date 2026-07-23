---
id: aquatone
name: Aquatone
description: Use when you have a `domain` (or a list of discovered hosts) and want a fast visual map of its web attack surface — returns HTTP screenshots, response headers, and a clustered HTML report.
url: https://github.com/michenriksen/aquatone
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Screenshotting and clustering a large list of hosts to eyeball a target's web footprint quickly.
selectorsIn:
- domain
selectorsOut:
- domain
- employer-org
status: degraded
pricing: free
costNote: Free and open source (MIT); pre-compiled Go binary, runs locally. No cost.
opsec: active
opsecNote: Aquatone makes real HTTP(S) requests to every host to capture screenshots and headers, so your IP lands in each target's web/server logs. This is active reconnaissance — route it through a VPN/proxy or a throwaway VPS for anything sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely-used open-source recon tool by Michael Henriksen; note the GitHub repo was archived (read-only) in Jan 2023, so it is unmaintained though still functional.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- birdwatcher
- gitrob
aliases:
- aquatone
- michenriksen/aquatone
tags:
- subdomain-recon
- screenshots
- attack-surface
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Aquatone

> A classic Go recon tool that takes a pile of hosts and gives you a visual, clustered report of every web page — the fastest way to eyeball a target's web attack surface. (Archived/unmaintained but still works.)

## When to use
You have a `domain` and a set of subdomains/IPs (from enumeration or a scan) and want to *see* what's running without clicking through hundreds of URLs. Aquatone visits each host, screenshots it, grabs response headers, and clusters visually-similar pages so login portals, parked pages, dashboards, and dev panels jump out. Reach for it after subdomain discovery, as the triage step before deciding where to dig.

## How to use it (`bestInteractionPattern`: cli)
1. Download the pre-compiled binary for your OS from the GitHub releases and put it on your PATH (requires Chrome/Chromium for screenshots).
2. Pipe a list of hosts into it, e.g. `cat hosts.txt | aquatone` (it accepts output from Amass, Nmap, `subfinder`, etc.).
3. Let it probe each host and capture screenshots + headers.
4. Open the generated `aquatone_report.html` — pages are clustered by similarity, with response headers and a list of responsive URLs.
5. Pivot: interesting hosts (portals, panels, exposed services) feed deeper investigation; the header/server data hints at `employer-org`/hosting.

## Inputs → Outputs
- **In:** `domain` / a list of hosts, domains, or IPs (typically piped from an enumeration tool)
- **Out:** PNG screenshots, raw response headers/bodies, a clustered HTML report, and a text list of responsive URLs
- **Empty/negative result looks like:** hosts that don't respond on HTTP(S) produce no screenshot — they're down, filtered, or non-web, not necessarily nonexistent.

## Gotchas & OpSec
- Archived Jan 2023: no updates or bug fixes; some modern TLS/JS-heavy sites may render imperfectly. It still works for the common case.
- Needs a headless Chrome/Chromium available locally.
- OpSec: **active** — every host is contacted from your IP. Use a VPN/VPS for sensitive targets and pace large runs to avoid tripping WAFs.

## Overlaps ("do both")
- Sits downstream of subdomain enumeration and upstream of manual review. Pair with `[[gitrob]]` for source-leak recon and `[[birdwatcher]]`; combine with a live-host prober so you only screenshot hosts that are actually up.

## Trust & verifiability
`trust: community` — a well-regarded open-source tool with inspectable code, but unmaintained since 2023; verify anything security-relevant and prefer a maintained alternative if you hit rendering bugs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aquatone |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
