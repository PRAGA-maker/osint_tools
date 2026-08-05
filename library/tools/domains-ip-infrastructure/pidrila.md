---
id: pidrila
name: Pidrila
description: Use when you have a `domain`/URL and want to discover hidden or unlinked paths, directories and files on the web server — returns a list of live URLs (attack surface / content).
url: https://github.com/enemy-submarine/pidrila
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast async content/path discovery on a target web server via wordlist brute-forcing.
selectorsIn:
- domain
selectorsOut:
- domain
status: degraded
pricing: free
costNote: Free and open-source (GPLv2); no cost. Prototype-stage, last tagged release v0.1.0 (Nov 2020) — lightly maintained.
opsec: active
opsecNote: Active and noisy — it fires many concurrent requests directly at the target server, so it will appear in the target's access logs and may trip WAF/rate limits. Only run against infrastructure you are authorised to test; route through a proxy/VPN (it supports HTTP/SOCKS proxies).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source project on GitHub; small codebase, readable, but a prototype with limited activity — verify behaviour before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- PIDRILA
- Python Interactive Deepweb-oriented Rapid Intelligent Link Analyzer
tags:
- Domain/IP/Links
- Website analyze
- path-scanner
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Pidrila

> A fast asynchronous web path scanner — point it at a domain and it brute-forces directories and files to reveal unlinked content and attack surface.

## When to use
You have a `domain` or URL tied to a subject or organisation and want to enumerate content that isn't reachable from the front page: admin panels, backup files, staging paths, exposed directories. It is an active-recon content-discovery tool, in the same family as dirsearch/gobuster/ffuf.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and set up: `git clone https://github.com/enemy-submarine/pidrila && cd pidrila && pip install -r requirements.txt`.
2. Run against a single target: `python3 pidrila.py -u https://target.example`.
3. Tune with flags: wordlist, concurrent-connection limit, timeout, custom User-Agent, and `--proxy` (HTTP/SOCKS). Batch mode accepts a list of URLs.
4. Read the logged output for discovered live paths; feed interesting URLs into manual review or a broader web-recon workflow.

## Inputs → Outputs
- **In:** `domain` / target URL (+ a path wordlist)
- **Out:** `domain` (discovered live URLs/paths on the server)
- **Empty/negative result looks like:** all requests 404/timeout → nothing discovered with that wordlist; try a larger/different wordlist or confirm the host is up before concluding there is no hidden content.

## Gotchas & OpSec
- Active and loud: this generates a burst of traffic straight at the target — authorisation and a proxy are mandatory.
- Prototype maturity (last release 2020) — results and stability lag behind actively maintained scanners; status marked `degraded`.
- Quality of findings depends entirely on the wordlist you supply.

## Overlaps ("do both")
- Interchangeable-in-spirit with other path scanners (dirsearch, ffuf, gobuster); if Pidrila misses or is unstable, one of those maintained tools will usually do the same job more reliably.

## Trust & verifiability
`trust: community` — open-source and inspectable, but an unmaintained prototype; treat discovered paths as leads to confirm manually, and prefer a maintained scanner for production work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pidrila |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
