---
id: reconspider
name: reconspider
description: Use when you have an `ip-address`, `email`, `phone`, `domain`, or `username` and want a one-console recon sweep across many sources — returns aggregated results (geolocation, profiles, related identifiers).
url: https://github.com/bhavsec/reconspider
category: search-engines
path:
- search-engines
bestFor: Running multi-selector OSINT lookups (IP, email, phone, domain, username) from a single Python framework.
selectorsIn:
- email
- phone
- ip-address
- domain
- username
selectorsOut:
- email
- ip-address
- geolocation
- social-profile
- phone
status: degraded
pricing: free
costNote: Free, open-source Python framework. Some modules call third-party APIs that may need free keys, and several depend on services that change over time.
opsec: passive
opsecNote: Most modules query third-party databases/APIs rather than the target directly, so it's largely passive — but some checks (e.g. a domain/IP scan) touch the target's infrastructure. Review what each module does before running, and route through a VPN. API-backed modules leak your queries to those providers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community Python OSINT framework; it aggregates third-party sources whose reliability and availability vary, and the project's maintenance is intermittent, so modules break.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- bhavsec/reconspider
tags:
- osint-framework
- python
- ip-lookup
- email-lookup
source: gh-topic-reconnaissance
lastVerified: '2026-07-17'
enrichment: full
---

# reconspider

> A one-console Python recon framework — feed it an IP, email, phone, domain, or username and it fans the query out across multiple OSINT modules and aggregates the results.

## When to use
You have one of several selector types and want a quick, broad first-pass sweep without manually visiting a dozen sites: an `ip-address` to geolocate and characterize, an `email`/`phone` to check across sources, a `domain` to profile, or a `username` to look up. reconspider bundles these lookups behind one CLI, which is convenient for early reconnaissance — treat its output as leads to verify, not conclusions, since it's an aggregator of variable third-party sources.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/bhavsec/reconspider`, then install requirements (Python 3). Add any API keys the config requests.
2. Launch the console and choose the module matching your selector (IP, phone, email, domain, username).
3. Enter the value; let the modules query their sources and print aggregated output.
4. Read results critically — note which module produced each fact and whether that source is currently working.
5. Pivot: geolocated IPs → mapping; surfaced profiles → the relevant selector tools; verify every hit against a primary source before relying on it.

## Inputs → Outputs
- **In:** `ip-address`, `email`, `phone`, `domain`, or `username`
- **Out:** aggregated recon data — `geolocation`, `ip-address` details, `social-profile`s, related `email`/`phone`
- **Empty/negative result looks like:** modules erroring, returning nothing, or requiring a missing API key — often because an upstream source changed or is rate-limited. An empty result here is frequently a broken module, not a true negative.

## Gotchas & OpSec
- **Maintenance/degradation:** it depends on third-party APIs and scrapers that drift; expect some modules to be broken on any given day, and prefer a maintained fork if available.
- It's a convenience aggregator — always confirm findings with the authoritative dedicated tool for that selector.
- OpSec: **mostly passive**, but domain/IP-scanning modules can touch the target's infrastructure and API modules expose your queries to providers — know what you're running.

## Overlaps ("do both")
- Overlaps with dedicated single-purpose tools (IP geolocation, email/username enumerators, WHOIS); use reconspider for a fast first sweep, then the specialized tool for authoritative confirmation.

## Trust & verifiability
`trust: community` — an unaffiliated open-source framework aggregating third-party sources of mixed reliability; useful for breadth, but every result needs verification against a primary source, and modules may be non-functional.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reconspider |
| category | search-engines |
| selectorsIn → selectorsOut | email, phone, ip-address, domain, username → email, ip-address, geolocation, social-profile, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
