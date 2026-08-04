---
id: xray
name: XRay
description: Use when you have a `domain` and want automated subdomain discovery with port/banner and Shodan enrichment — returns subdomains, open ports and service `ip-address` details.
url: https://github.com/evilsocket/xray
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: One-shot recon of a domain — subdomain brute force plus Shodan/port/banner enrichment in a local web UI.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: degraded
pricing: free
costNote: Free and open-source (GPL-3.0). Note the original Go repo is archived/legacy; the author points to a Rust reimplementation as the maintained successor.
opsec: active
opsecNote: XRay performs DNS brute force against the target and makes direct banner-grabbing connections to discovered services, so it touches the target's infrastructure and can appear in their logs. Use only against assets you are authorized to test, ideally from an attributable-safe host; the Shodan-backed portions are passive but the local enumeration is not.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known tool by evilsocket (Simone Margaritelli); 2k+ stars, GPL source. The original repo is archived — treat it as legacy and prefer the maintained Rust successor.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- ditto
aliases:
- evilsocket/xray
tags:
- domains-ip-infrastructure
- subdomains
- recon
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# XRay

> A local recon tool that brute-forces subdomains and enriches what it finds with Shodan, port scans and banner grabs, surfacing results in a browser UI. The original Go version is archived — usable, but legacy.

## When to use
You have a target `domain` and want a single tool that both discovers subdomains and enriches them (open ports, service banners, Shodan history) rather than stitching several tools together. XRay is handy for authorized recon where you want a quick, browsable map of a domain's exposed surface. Because the Go repo is archived, reach for it when the successor isn't set up, and prefer the maintained Rust reimplementation for new work.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go get github.com/evilsocket/xray/cmd/xray` (legacy Go build), or clone and build; alternatively run the maintained Rust successor linked from the repo.
2. (Optional but recommended) export a Shodan API key, and a ViewDNS key, so XRay can pull open ports and historical DNS instead of only brute-forcing.
3. Run against the target: `xray -shodan-key <KEY> -domain target.com` — supply a subdomain wordlist for the brute-force stage.
4. Open the local web UI (default `http://localhost:8080`) and watch results populate: discovered subdomains, resolved `ip-address`es, open ports, banners, SSL certs, robots.txt entries.
5. Pivot: feed discovered subdomains/IPs into deeper service fingerprinting, and treat Shodan-surfaced ports/banners as leads for the target's tech stack.

## Inputs → Outputs
- **In:** `domain` (+ optional Shodan/ViewDNS API keys and a wordlist)
- **Out:** subdomain `domain`s, resolved `ip-address`es, open ports, service banners, SSL/robots metadata (shown in a local web UI)
- **Empty/negative result looks like:** few or no subdomains resolved (wordlist mismatch or a small target), and empty Shodan sections when no key is set. Empty ≠ "no attack surface"; it often means "not with this wordlist / no Shodan key."

## Gotchas & OpSec
- Human-in-the-loop: none in operation, but you must build/install it (systems software, not a website).
- OpSec: **active** — the brute-force and banner-grabbing stages hit the target directly and can be logged. Only run against authorized assets; the Shodan lookups are the passive part of the workflow.
- Legacy status: the original Go repo is archived ("LEGACY code") and dependencies may not build cleanly on modern toolchains; the author's Rust reimplementation is the maintained path.

## Overlaps ("do both")
- Overlaps with wordlist-driven enumerators fed by `[[seclists-dns-subdomains]]` and with dedicated Shodan tooling — XRay bundles brute force + enrichment in one place, while those give you finer control over each stage.

## Trust & verifiability
`trust: community` — a well-known open-source project from a reputable author (evilsocket), GPL-licensed and inspectable. Downgraded operationally because the Go repo is archived; verify against the maintained successor before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xray |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
