---
id: osint-explorer
name: OSINT-Explorer
description: Use when you have a `username`/`email`/`domain`/`ip-address` and want a scripted recon sweep — returns aggregated `social-profile`, `domain`, and `ip-address` results.
url: https://github.com/gowthamaraj/OSINT-Explorer
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A lightweight self-hosted framework that chains common recon lookups from one interface.
selectorsIn:
- username
- email
- domain
- ip-address
selectorsOut:
- social-profile
- domain
- ip-address
status: live
pricing: free
costNote: Free and open source; self-hosted (your own compute). Some underlying lookups may need free API keys.
opsec: passive
opsecNote: Mostly passive database/API lookups, but depending on the modules enabled it may hit third-party services that log the selector you query. Run from an isolated environment and review which modules make active requests before pointing it at a sensitive target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small single-maintainer GitHub project (low star count); auditable but modest and not widely battle-tested — treat as a convenience wrapper over better-known tools.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- gowthamaraj/OSINT-Explorer
tags:
- framework
- multi-tool
- recon
source: gh-topic-osint-framework
lastVerified: '2026-07-28'
enrichment: full
---

# OSINT-Explorer

> A small open-source OSINT framework that bundles common recon lookups (username, email, domain, IP) behind one interface — a convenience wrapper, not a heavyweight platform.

## When to use
You want a quick, self-hosted sweep across several selector types without invoking each tool by hand. Point OSINT-Explorer at a `username`, `email`, `domain`, or `ip-address` and it runs the bundled modules and aggregates the results. Best as a fast first pass before reaching for larger, more capable frameworks.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/gowthamaraj/OSINT-Explorer and install its dependencies.
2. Add any free API keys the modules require.
3. Run it against a selector (`username`/`email`/`domain`/`ip-address`) per the repo's usage docs.
4. Read the aggregated output; treat each module's result as a lead.
5. Pivot: promising hits feed the dedicated, deeper tool for that selector (e.g. a full username-enumeration or passive-DNS tool).

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, or `ip-address`
- **Out:** aggregated `social-profile`s, related `domain`s, and `ip-address` data
- **Empty/negative result looks like:** thin or empty module output — the framework only surfaces what its (limited) modules cover; absence here is not absence everywhere.

## Gotchas & OpSec
- Small, lightly-maintained project — coverage and reliability are below mature frameworks; verify anything important with a primary tool.
- Bundled modules vary in whether they're passive or make active third-party calls — audit before use on a sensitive target.
- Overlaps heavily with larger multi-tools; use it for speed, not completeness.

## Overlaps ("do both")
- Pairs with heavier frameworks and per-selector specialists — OSINT-Explorer gives a fast wide sweep, while dedicated tools (username enumerators, passive-DNS, IP-reputation) go deep where it flags something.

## Trust & verifiability
`trust: community` — an auditable but modest single-maintainer wrapper; it only re-exposes other sources, so its accuracy is that of the underlying modules — corroborate independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-explorer |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email, domain, ip-address → social-profile, domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
