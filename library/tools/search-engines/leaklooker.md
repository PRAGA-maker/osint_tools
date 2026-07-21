---
id: leaklooker
name: LeakLooker
description: Use when you have a `domain`/keyword and want to discover exposed, unauthenticated databases and services associated with it — returns `ip-address`, `domain`.
url: https://github.com/woj-ciech/LeakLooker
category: search-engines
path:
- search-engines
bestFor: Finding open/unauthenticated databases and services (Elasticsearch, MongoDB, Kibana, S3, etc.) tied to a keyword or organisation.
selectorsIn:
- domain
- employer-org
selectorsOut:
- ip-address
- domain
status: degraded
pricing: free
costNote: Free and open-source (Python 3); requires your own BinaryEdge.io API key (free tier available) to run queries.
opsec: active
opsecNote: Do NOT connect to or download from any exposed database you find — that can be unlawful access. LeakLooker only discovers via BinaryEdge's index (so you don't touch the targets during search), but keep it to discovery, log your authorisation, and route through a sock-puppet key/account.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Well-known tool by researcher woj-ciech, but the original repo was archived in 2020 (read-only); detection logic may be stale — the maintained successor is LeakLooker-X (GUI).
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
relatedTools:
- socialpath
aliases:
- LeakLooker CLI
tags:
- exposed-databases
- binaryedge
- infrastructure
- cli
- toddington
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# LeakLooker

> A discovery tool for the internet's open doors — it surfaces unauthenticated databases and dashboards (Elasticsearch, MongoDB, Kibana, GitLab, S3…) via BinaryEdge, so you can spot data exposures tied to a target.

## When to use
An infrastructure/exposure-hunting tool. When investigating an organisation or domain and you want to know whether it (or a related host) has left a database or admin panel open to the internet, LeakLooker queries BinaryEdge's scan index for exposed services and returns the hosts. Useful for assessing a subject-organisation's data-exposure footprint and for finding leaked data stores in authorised research — it is not a person-lookup tool.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/woj-ciech/LeakLooker and install Python 3 dependencies.
2. Paste your BinaryEdge API key where the README/code indicates.
3. Run it and choose the service type(s) to hunt (Elasticsearch, MongoDB, Kibana, CouchDB, GitLab, Jenkins, S3, directory listings, etc.); filter by keyword/organisation.
4. Review the returned hosts (`ip-address` / `domain`) and their exposure summaries in the console.
5. STOP at discovery — record findings and, if authorised, report the exposure; do not access the data.

## Inputs → Outputs
- **In:** `domain` / `employer-org` keyword to filter the scan index
- **Out:** `ip-address` and `domain` of exposed databases/services matching the filter
- **Empty/negative result looks like:** no matching exposed services in BinaryEdge's index — meaning nothing indexed as open right now, not a guarantee the org has no exposures.

## Gotchas & OpSec
- Human-in-the-loop: you must supply a BinaryEdge API key.
- OpSec: **active/legal-sensitive** — discovery via the index is passive toward the target, but *connecting to* an open database is likely unlawful. Keep to discovery and stay inside your authorisation.
- The main repo is archived (2020) so signatures may be outdated; consider the maintained LeakLooker-X GUI, and expect some queries to break as services evolve.

## Overlaps ("do both")
- Complements broader exposure/recon platforms (Shodan/Censys-style search) — LeakLooker is a focused BinaryEdge-driven finder for open data stores; the big scanners give wider service and certificate context.

## Trust & verifiability
`trust: community` — a respected researcher's open-source tool, but archived and BinaryEdge-dependent; verify any exposure directly (within authorisation) and prefer the maintained successor for current detections.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leaklooker |
| category | search-engines |
| selectorsIn → selectorsOut | domain, employer-org → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
