---
id: ghostrecon
name: GhostRecon
description: Use when you have a `username`, `email`, `phone`, `ip-address`, or `domain` and want a scripted recon sweep — returns social profiles, network/IP data, and lookups from bundled modules.
url: https://github.com/KawaCoder/GhostRecon
category: people-search
path:
- people-search
bestFor: Running a bundled set of recon lookups (username/email/phone/IP/domain) from one Linux CLI.
selectorsIn:
- username
- email
- phone
- ip-address
- domain
selectorsOut:
- social-profile
- ip-address
- phone
status: live
pricing: free
costNote: Free and open source (Mozilla Public License 2.0); self-hosted, no service fees. Some bundled modules may call third-party APIs that have their own limits.
opsec: active
opsecNote: Some modules (port scans, IP/domain probes, account checks) touch the target's infrastructure or third-party services directly. Run from a disposable VPS/VPN, review each module's behavior before use, and don't assume everything it does is passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community GitHub project (~300 stars, MPL-2.0, last release v2.0 in 2024); it wraps other tools/APIs, so verify each module's data source and freshness before trusting output.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- sherlock
- recon-ng
aliases:
- ghostrecon
- Grecon
tags:
- framework
- multi-tool
- cli
source: gh-topic-osint-framework
lastVerified: '2026-07-18'
enrichment: full
---

# GhostRecon

> A compact Linux OSINT/recon CLI that bundles username, email, phone, IP, and domain lookups behind one `Grecon` command.

## When to use
You are working a target from one of several selectors — a `username`, `email`, `phone`, `ip-address`, or `domain` — and want a fast, scripted first pass rather than running each lookup by hand. GhostRecon packages multiple recon modules (social-account checks, network/port probes, basic lookups) into a single terminal tool. Treat it as a convenience aggregator and a starting point that flags leads to verify in dedicated tools, not as an authoritative source.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/KawaCoder/GhostRecon` (verify you're on the real KawaCoder repo).
2. Run the installer: `sudo ./install.sh` (it's ~85% shell, 15% Python; installs dependencies).
3. Launch with `Grecon` and pick the module for your selector (username / email / phone / IP / domain).
4. Read module output; each surfaces different data (found accounts, open ports, geolocation, etc.).
5. Pivot: take any hit — a matched `social-profile`, an `ip-address`, a `phone` — into a dedicated, higher-trust tool to confirm before acting on it.

## Inputs → Outputs
- **In:** `username`, `email`, `phone`, `ip-address`, or `domain`
- **Out:** `social-profile` (matched accounts), `ip-address`/network data, `phone` lookups — depending on the module run
- **Empty/negative result looks like:** a module returning no hits or erroring on a missing dependency/expired API — absence here reflects the bundled module's coverage, not a definitive "nothing exists."

## Gotchas & OpSec
- **Active by default for some modules:** port scans and direct probes touch the target/infrastructure — run behind a VPN/VPS and know which module does what.
- It wraps third-party tools/APIs whose reliability and legality vary; a broken or rate-limited upstream silently degrades results.
- Community code with a small maintainer base — audit `install.sh` and module scripts before running with privileges; the author states it's "for educational purposes only."
- Overlaps heavily with more mature frameworks; often faster to reach for those directly.

## Overlaps ("do both")
- Pairs with `[[sherlock]]` (deeper, better-maintained username enumeration) and `[[recon-ng]]` (a full modular recon framework) — use GhostRecon for a quick multi-selector sweep, then those for depth and reliability on the leads it surfaces.

## Trust & verifiability
`trust: community` — an unaffiliated open-source project that aggregates other tools; each result is only as trustworthy as the underlying module's source, so verify before relying on anything it reports.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghostrecon |
| category | people-search |
| selectorsIn → selectorsOut | username, email, phone, ip-address, domain → social-profile, ip-address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
