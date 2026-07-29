---
id: robotsdisallowed
name: RobotsDisallowed
description: Use when you have a `domain` and want a high-signal wordlist of paths site owners hide in robots.txt — returns candidate directories for content discovery.
url: https://github.com/danielmiessler/RobotsDisallowed
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- vulnerabilities
bestFor: Seeding a directory/content-discovery scan with paths that real sites explicitly disallowed in robots.txt.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free, MIT-licensed text files on GitHub; clone or download, no account needed.
opsec: passive
opsecNote: The wordlist itself is inert — reading it touches no target. It becomes active only when you feed it to a fuzzer (gobuster/ffuf) against a live host, which does generate request logs on that host. OpSec scope belongs to the scanner you pair it with, not this list.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by Daniel Miessler (also SecLists); 1.5k+ stars. Data is aggregated from public robots.txt files of top sites. Last data refresh March 2019, so it is a static, dormant-but-usable corpus.
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
- seclists
- seclists-dns-subdomains
aliases:
- RobotsDisallowed wordlist
tags:
- wordlist
- content-discovery
- web-recon
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# RobotsDisallowed

> A curated wordlist built from the `Disallow:` entries of the world's top websites — the paths owners told crawlers to avoid, which are exactly the paths worth probing.

## When to use
You are enumerating a subject's `domain` or web asset and want to discover hidden admin panels, backup directories, upload paths, or login endpoints. Instead of a generic brute-force list, this gives you paths that real operators flagged as sensitive — a much higher hit rate per request. Reach for it when mapping infrastructure tied to a person or organisation you are investigating.

## How to use it (`bestInteractionPattern`: cli)
1. Clone or download: `git clone https://github.com/danielmiessler/RobotsDisallowed`.
2. Pick a list: `curated.txt` (~500 hand-filtered high-value paths like `admin`, `login`, `backup`, `password`) is the recommended default; `top1000.txt` / `top10000.txt` trade precision for coverage.
3. Feed it to a content-discovery tool against the target, e.g. `ffuf -w curated.txt -u https://target.example/FUZZ` or `gobuster dir -w curated.txt -u https://target.example`.
4. Read the output: HTTP 200/301/403 responses mark paths that exist. A 403/401 on an interesting path (e.g. `/admin`) still confirms it is present.
5. Pivot: discovered login/admin panels feed vulnerability triage; discovered upload or file directories can leak documents/metadata worth pulling into `[[seclists]]`-driven follow-up.

## Inputs → Outputs
- **In:** `domain` (target host to scan against)
- **Out:** list of live directory/file paths on that host (attack-surface leads, not personal-data selectors)
- **Empty/negative result looks like:** the fuzzer returns only 404s across the whole list — the host has a small footprint or a catch-all; switch to a larger list or a subdomain sweep.

## Gotchas & OpSec
- Human-in-the-loop: none for the list; the scanner you pair it with may need rate-limit tuning to avoid WAF blocks.
- OpSec: **passive** as a file, but the scan it drives is loud. Only run against assets you are authorised to test; a directory brute-force is unambiguously visible in the target's access logs.
- The data is from 2019 — path fashions drift, but core sensitive-directory names (admin/backup/config) are durable.

## Overlaps ("do both")
- Pairs with `[[seclists]]` — SecLists is the broader wordlist arsenal; RobotsDisallowed is the specialised, higher-precision content-discovery list. Run curated.txt first for quick wins, then a SecLists directory list for depth.
- Combine with `[[seclists-dns-subdomains]]` to enumerate hosts first, then hunt directories on each.

## Trust & verifiability
`trust: community` — well-known author, transparent provenance (aggregated public robots.txt), but a static 2019 snapshot rather than a live-maintained service. Verify hits directly; the list only suggests where to look.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | robotsdisallowed |
