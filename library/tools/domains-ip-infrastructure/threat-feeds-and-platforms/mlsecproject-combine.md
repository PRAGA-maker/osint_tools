---
id: mlsecproject-combine
name: mlsecproject / combine
description: Use when you have a set of threat-intel feeds and want them fetched and normalized into one IOC dataset — returns unified CSV/CRITs indicator output.
url: https://github.com/mlsecproject/combine
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Pulling multiple public threat-intel feeds and normalizing their indicators (IPs, domains) into a single structured dataset.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: degraded
pricing: free
costNote: Free and open-source (Python); no account or key. You run it locally.
opsec: passive
opsecNote: It fetches public threat feeds to wherever you run it, then processes them locally — no target is probed. The fetches reveal your IP to the feed hosts; run from a controlled egress if that matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: An open-source project from MLSec Project (mlsecproject/combine); the code is public and inspectable, but it is old and unmaintained (Python 2-era), so expect broken feed URLs and dependency friction.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- combine
- MLSec combine
tags:
- threat-intelligence
- ioc
- cli
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# mlsecproject / combine

> A Python CLI that gathers many public threat-intel feeds and normalizes their indicators into one dataset — feed plumbing, now aged.

## When to use
You want to aggregate scattered public threat feeds (IP/domain blocklists, IOC lists) into a single normalized table for enrichment or correlation, rather than parsing each feed's format by hand. In an investigation this is infrastructure/IOC groundwork — turning raw feeds into `ip-address`/`domain` indicators you can cross-reference — not a people-search step.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/mlsecproject/combine and set up a (legacy) Python environment per the README — expect to pin old dependencies.
2. Configure the feed list (the repo ships a default set; prune dead URLs — many will have rotted).
3. Run the harvester to fetch feeds, then the normalizer to produce unified output (CSV or CRITs-compatible format).
4. Load the normalized IOCs into your enrichment/correlation workflow.
5. Pivot: an indicator `domain`/`ip-address` → passive-DNS, WHOIS-history, and reputation tools for context.

## Inputs → Outputs
- **In:** configured threat-feed URLs (public IOC lists)
- **Out:** normalized indicator dataset (`ip-address`/`domain`) in CSV or CRITs format
- **Empty/negative result looks like:** empty output or fetch errors — most commonly dead feed URLs or Python 2/dependency breakage rather than "no indicators"; check which feeds still resolve.

## Gotchas & OpSec
- Staleness: `status: degraded` — the project is unmaintained and predates Python 3-era tooling, so setup and default feeds need modernizing; treat it as a starting scaffold, not a turnkey product.
- Feed rot: bundled feed URLs decay over time; curate your own list.
- OpSec: passive — it consumes public feeds and processes locally; nothing targets a subject.

## Overlaps ("do both")
- Pairs with maintained threat-intel platforms (MISP, OpenCTI) and [[openhunting-io]] — combine is a lightweight normalizer; the platforms give storage, sharing, and current feeds it lacks.

## Trust & verifiability
`trust: unverified` — open-source and auditable, but old and unmaintained; verify its output against a live threat-intel source and don't rely on its default feed list being current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mlsecproject-combine |
