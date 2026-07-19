---
id: onioff
name: Onioff
description: Use when you have one or more `.onion` URLs and want to check which are live and grab basic metadata — a Python CLI that probes onion services over Tor.
url: https://github.com/k4m4/onioff
category: dark-web
path:
- dark-web
- discovery
bestFor: Batch-checking a list of .onion addresses for availability and basic response metadata before manual investigation.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (MIT). Requires Python 3 and a working local Tor.
opsec: active
opsecNote: Probing an onion address makes a real connection to that hidden service over Tor, which the service operator can observe. Route strictly through Tor, never leak your clearnet IP, and run from an isolated VM — treat every probed .onion as potentially hostile/illegal content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An open-source utility by Nikolaos Kamarinakis (700+ stars, MIT). Last released 2018 and not archived — functional but dated; verify it still runs against current Tor/Python.
missingPersonsRelevance: medium
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
- onioff
- k4m4/onioff
tags:
- dark-web
- onion
- cli
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Onioff

> A small pure-Python CLI that inspects `.onion` URLs over Tor — a quick triage step to see which hidden-service addresses in a list are alive before you spend time investigating them.

## When to use
You have a set of `.onion` addresses — harvested from a paste, a forum, a breach, or a crawl — and want to know which are currently reachable and their basic response metadata, without opening each by hand. Onioff batches that availability check through Tor, letting you prune a candidate list down to live services worth manual review. It is a triage/discovery aid, not a content search.

## How to use it (`bestInteractionPattern`: cli)
1. In an isolated VM with Tor running, clone the repo and `pip3 install -r requirements.txt` (Python 3).
2. Ensure Tor is correctly configured (SOCKS proxy) so onioff routes through it.
3. Run against a single URL or a file of URLs; use its flags to show only active sites and to write results to an output file.
4. Review which addresses responded and their metadata; take live ones into a hardened browser for manual, careful inspection.
5. Pivot: live onion services feed dark-web content review and cross-referencing; dead ones are dropped.

## Inputs → Outputs
- **In:** `domain` (one or many `.onion` URLs, inline or from a file)
- **Out:** per-URL availability + basic response metadata (which `domain`s are live)
- **Empty/negative result looks like:** all URLs report unreachable — onion services are frequently transient, or your Tor config is wrong; retry later and confirm Tor works before concluding the sites are dead.

## Gotchas & OpSec
- Human-in-the-loop: none once configured, but correct Tor setup is mandatory.
- OpSec: **active** — each probe connects to the hidden service, observable by its operator. Use Tor only, isolate with a VM, and never expose your clearnet IP. Assume probed content may be illegal.
- The tool is from 2018; dependency/Tor changes may need fixes. A run failure usually means an environment issue, not that all targets are down.

## Overlaps ("do both")
- Pairs with dark-web crawlers/search engines that discover onion addresses — onioff then triages which of those are actually live.

## Trust & verifiability
`trust: community` — a popular open-source MIT tool, fully auditable on GitHub, though unmaintained since 2018; its output (live/dead + metadata) is directly checkable against a manual Tor visit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onioff |
| category | dark-web |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
