---
id: thelordeye
name: TheLordEye
description: Use when you have a device/service query or `ip-address` and want internet-connected devices matching it — returns webcams, routers, IoT and their `ip-address`/`geolocation` via the Shodan API.
url: https://github.com/rlyonheart/thelordseye
category: search-engines
path:
- search-engines
bestFor: A lightweight CLI wrapper over the Shodan API for querying internet-exposed devices (webcams, routers, smart TVs, ICS) and looking up individual IPs.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- geolocation
status: live
pricing: freemium
costNote: The tool itself is free/open-source, but it requires a Shodan.io API key — Shodan has a limited free tier and paid plans for higher quotas.
opsec: passive
opsecNote: Queries run against Shodan's pre-collected scan dataset, so the target device is not contacted directly from your machine — reconnaissance is passive. Your Shodan account (tied to the API key) logs your queries.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Small open-source CLI by GitHub user rlyonheart; it is a thin front-end over the official Shodan API, so result quality equals Shodan's.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- 0xdork
- thedevilseye
- thorndyke
- criminal-ip-search
aliases:
- thelordseye
- the lord's eye
tags:
- Tools for Google
- IOT (ip search engines)
- shodan
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# TheLordEye

> A minimal command-line front-end to the Shodan API — run a device query or IP lookup from the terminal and export the matching internet-exposed hosts.

## When to use
You want Shodan-style results (internet-connected devices: webcams, routers, smart TVs, industrial controllers) but prefer a scriptable CLI over the web UI, or you want to pipe results into other tooling. Give it a Shodan search query or a specific `ip-address` and it returns matching hosts with their location and service details — useful when infrastructure or exposed devices are the pivot.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/rlyonheart/thelordseye`.
2. Install dependencies: `pip install -r requirements.txt` and `chmod +x eye`.
3. Authenticate once with your Shodan key: `./eye --auth <your-shodan-api-key>` (stored locally in `.auth`).
4. Query devices: `./eye --query "webcamxp"` (any Shodan filter/query), or look up a host: `./eye --ip <ip-address>`.
5. Export results to a file or raw JSON with the output flags; pivot the returned `ip-address`/`geolocation`/ports into infra tools.

## Inputs → Outputs
- **In:** a Shodan device query, or an `ip-address`/`domain`
- **Out:** matching hosts — `ip-address`, `geolocation`, open ports/services, banners
- **Empty/negative result looks like:** zero results (query too narrow, or your Shodan tier can't see it) or an auth error (missing/invalid API key). No results is not proof the device isn't online — Shodan only knows what it has scanned.

## Gotchas & OpSec
- Human-in-the-loop: you must supply a **Shodan API key**; the free Shodan tier is quota-limited, so heavy use needs a paid plan.
- Passive toward targets, but Shodan logs your account's queries.
- It's a thin wrapper — if it breaks, the same queries work in the official Shodan CLI/web. Being a small third-party repo, review the code before running.

## Overlaps ("do both")
- Pairs with `[[criminal-ip-search]]` and `[[thedevilseye]]` — different scanners/datasets index different hosts; run the same query across them.
- Related recon CLIs: `[[0xdork]]`, `[[thorndyke]]`.

## Trust & verifiability
`trust: community` — an unaffiliated open-source CLI over the official Shodan API; the underlying data is Shodan's (authoritative for what it scanned). Verify any specific host by re-querying Shodan directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thelordeye |
| category | search-engines |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
