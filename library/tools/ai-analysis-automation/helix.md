---
id: helix
name: Helix
description: Use when you have a `username` or `email` and want a mapped identity graph — returns cross-platform accounts, linked domains, and inferred relationships.
url: https://github.com/thalha-a9/helix
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Automated identity mapping — enumerate a handle across 700+ sites and pivot recursively into a visual relationship graph.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
- domain
- associate
status: live
pricing: free
costNote: Free and open-source (MIT); core features need no API keys. Optional AI false-positive filtering can use free OpenRouter/NVIDIA NIM tiers.
opsec: active
opsecNote: Modules actively touch third-party services — username checks hit 700+ sites, certificate-transparency and Wayback queries touch external infra, and GitHub commit-email extraction pulls repos. Run from a sock-puppet identity/VPN; the volume of automated requests can be logged by the platforms probed. Nothing notifies the subject directly, but the footprint is real.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An open-source community project (actively maintained, recent releases); powerful but its inferences (perceptual-hash avatar matches, timezone-from-commits) produce probable links, not proof — verify each edge.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Helix OSINT
- thalha-a9/helix
tags:
- username-enumeration
- identity-mapping
- automation
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Helix

> An asynchronous OSINT identity mapper: give it a username or email and it enumerates accounts across 700+ platforms, pivots on aliases, matches avatars by perceptual hash, and plots the whole web of relationships as an interactive graph.

## When to use
You have a `username` or `email` and want to go beyond "does this handle exist" to a mapped identity: cross-platform accounts, links pulled from bios, domains via certificate transparency, emails from GitHub commits, and inferred connections — all recursively pivoted and visualized. Best when you need breadth fast and a graph to reason over, then human verification of each edge.

## How to use it (`bestInteractionPattern`: cli)
1. Clone github.com/thalha-a9/helix and install (Python; MIT-licensed, no API keys for core use).
2. Run it against a `username` and/or `email`, optionally enabling modules (cert-transparency, Wayback, GitHub, AI verification).
3. It writes results to `results/`: an interactive HTML D3 graph plus JSON/CSV/TXT reports.
4. Pivot: follow high-confidence edges (matched avatars, bio links, shared domains) into the specific platform tools; treat inferred edges (timezone, hash matches) as leads to confirm manually.

## Inputs → Outputs
- **In:** `username` and/or `email`
- **Out:** `social-profile`s across platforms, linked `domain`s, `associate`/relationship edges, timeline data
- **Empty/negative result looks like:** sparse graph / mostly false-positive nodes — common for generic handles; the AI filter reduces but doesn't eliminate noise, so a thin graph means "little found," not a mapped person.

## Gotchas & OpSec
- Username enumeration across 700+ sites is noisy — expect false positives; the perceptual-hash and timezone inferences are probabilistic and need verification.
- ACTIVE and high-volume: it hammers many third parties; use a VPN/sock-puppet and be mindful of rate limits and ToS.
- Run in an isolated environment; review what each module actually queries.

## Overlaps ("do both")
- Complements single-purpose username checkers (Sherlock/Maigret-style) and email-OSINT tools — Helix orchestrates breadth and visualization; use focused tools to confirm the individual hits it surfaces.

## Trust & verifiability
`trust: community` — a capable open-source framework; the raw account hits are checkable, but its inferred relationships are hypotheses to verify before you rely on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | helix |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email → social-profile, domain, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
