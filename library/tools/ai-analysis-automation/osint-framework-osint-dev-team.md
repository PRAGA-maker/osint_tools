---
id: osint-framework-osint-dev-team
name: osint-framework (osint-dev-team)
description: Use when you have a `domain`, `ip-address`, `email`, `username` or `phone` and want a self-hosted service to run many recon modules and return results via CLI or REST API — returns domains, hosts, social-profiles and related identifiers.
url: https://github.com/osint-dev-team/osint-framework
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Self-hosted, multi-selector recon that you can drive from a CLI or call as a REST API.
selectorsIn:
- domain
- ip-address
- email
- username
- phone
selectorsOut:
- domain
- ip-address
- social-profile
status: live
pricing: free
costNote: Free and open-source (GPL-2.0). Self-hosted; some modules may need their own API keys.
opsec: active
opsecNote: Runs on your own infrastructure, but its modules make live queries against third-party services and, depending on the module, the target's infrastructure. Deploy on a dedicated research host and treat submitted selectors as disclosed to the upstream services each module calls.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Small community project (~46 stars); verify individual modules still work before relying on output.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- osint-dev-team osint-framework
- osint-recon swiss knife
tags:
- recon
- docker
- rest-api
source: gh-topic-osint-framework
lastVerified: '2026-08-04'
enrichment: full
---

# osint-framework (osint-dev-team)

> A self-hostable "OSINT-RECON Swiss knife": submit a selector via CLI or REST and it runs a battery of recon modules, storing the results for retrieval.

## When to use
You want a private, programmable recon service you can query repeatedly — feed it a `domain`, `ip-address`, `email`, `username`, or `phone` and get back aggregated recon output, either interactively (`cli.py`) or by POSTing to its API from your own tooling. Good when you want automation you control rather than a public web tool.

## How to use it (`bestInteractionPattern`: docker)
1. Clone and start with Docker: `git clone https://github.com/osint-dev-team/osint-framework && cd osint-framework && docker-compose up` (brings up the API on localhost, backed by PostgreSQL + RabbitMQ).
2. Or run the CLI: set up a virtualenv, `pip install` the requirements, then `python3 cli.py` with a target.
3. Submit a target via the REST endpoint (POST a case/selector) and poll the results endpoint (GET) for output.
4. Retrieve results from the results directory / API response.
5. Pivot: surfaced `domain`/`ip-address`/`social-profile` values feed dedicated per-selector tools.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, `email`, `username`, or `phone`.
- **Out:** aggregated recon results — related `domain`s, resolved `ip-address`es, and `social-profile` links — returned via API/CLI and stored to disk.
- **Empty/negative result looks like:** an empty results set or module errors — often a broken/outdated module or a missing key rather than a true negative.

## Gotchas & OpSec
- Requires a small stack (Docker + PostgreSQL + RabbitMQ); more setup than a single script.
- Small, low-star project — modules can bit-rot; test each module against a known target before trusting its output.
- Self-host and lock down the API; don't expose your case data on an open port.

## Overlaps ("do both")
- Overlaps broader platforms like `[[prism]]` and framework `[[recon-ng]]`; choose this when you specifically want a lightweight REST-callable recon service to wire into your own automation.

## Trust & verifiability
`trust: community` — a small community framework; treat aggregated output as leads and verify each finding against the primary source the module drew from.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-framework-osint-dev-team |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, ip-address, email, username, phone → domain, ip-address, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | active |
| human-in-loop | no |
