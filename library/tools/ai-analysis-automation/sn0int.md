---
id: sn0int
name: sn0int
description: Use when you have a `domain`, `email`, `ip-address`, or `username` and want to run automated recon modules that expand it — returns subdomains, social-profile, geolocation, breaches, and more.
url: https://github.com/kpcyrd/sn0int
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Modular, semi-automatic OSINT recon — seed an entity, run community modules to enrich and pivot it in a local graph.
selectorsIn:
- domain
- email
- ip-address
- username
selectorsOut:
- domain
- social-profile
- geolocation
- ip-address
status: live
pricing: free
costNote: Free and open source (GPLv3+); packaged for Arch, Homebrew, Debian/Ubuntu, Alpine, NixOS, and Docker. Some modules call third-party APIs that may need your own keys.
opsec: active
opsecNote: Modules make real network requests — resolving domains, hitting APIs, fetching profiles — from your host, so activity is attributable to your IP. Modules run sandboxed, but review what each does before running; route through a VPN/proxy and use API keys not tied to your identity. Add targets to scope deliberately to avoid over-collecting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-regarded open-source framework by kpcyrd with an active module registry; modules are community-contributed, so vet third-party ones.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- sn0int
- kpcyrd/sn0int
tags:
- osint-framework
- recon-automation
- package-manager
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# sn0int

> A semi-automatic OSINT framework and package manager — seed an entity, run sandboxed modules to enrich and pivot it, and build up an investigation graph locally.

## When to use
You have a starting selector — a `domain`, `email`, `ip-address`, or `username` — and want to automate the tedious expansion: harvest subdomains from certificate transparency, mass-resolve and geo/ASN-enrich IPs, find social profiles for accounts, check breaches, parse phone numbers and image metadata. sn0int structures all of this as installable modules over a local entity store, so results become new pivot points. Strong for repeatable, scriptable recon in people- and infrastructure-centric investigations.

## How to use it (`bestInteractionPattern`: cli)
1. Install via your package manager (`brew install sn0int`, Arch/Debian, or Docker).
2. `sn0int` opens a shell; `pkg install <module>` (or `pkg quickstart`) to get modules from the registry.
3. Add targets to scope: `add domain example.com` / `add email a@b.com`, etc. (`selectorsIn`).
4. Run modules (`run <module>`) to enrich, then run follow-up modules on the new entities; query the local DB (`select ...`) to read results (`selectorsOut`).

## Inputs → Outputs
- **In:** `domain`, `email`, `ip-address`, `username` (and other entities: phone, image, netblock, crypto address)
- **Out:** `domain`/subdomains, `social-profile` (accounts), `geolocation` (geoip), `ip-address`, breach hits, image/phone metadata — stored as linked entities
- **Empty/negative result looks like:** a module returns no new entities — either the target has no exposed data on that vector, or the module needs an API key/quota it lacks; check module requirements.

## Gotchas & OpSec
- Human-in-the-loop: none inherently, but some modules need API keys you supply.
- OpSec: **active** — modules hit the network from your host; use a VPN/proxy, isolate API keys, and read a module's source before running it (it's sandboxed but still acts on your behalf).
- Community modules vary in quality/freshness; prefer well-maintained ones and verify surprising results independently.

## Overlaps ("do both")
- Complements one-shot recon tools (theHarvester, Amass, Sherlock) — sn0int orchestrates similar collection as pluggable modules over a persistent graph, so use it to tie point tools together and pivot, and use the specialists when you need their depth.

## Trust & verifiability
`trust: community` — a respected open-source project (GPLv3+) with an active registry, but individual modules are community-authored; the framework is trustworthy, so weight results by which module produced them and confirm the important ones.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sn0int |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, email, ip-address, username → domain, social-profile, geolocation, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
