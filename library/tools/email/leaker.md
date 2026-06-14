---
id: leaker
name: Leaker
description: Use when you want a command-line client to query breach/leak databases by email, username, or domain — returns linked credentials/identifiers from configured sources.
url: https://github.com/vflame6/leaker
category: email
path:
- email
bestFor: Scriptable CLI breach lookups by email/username/domain.
selectorsIn:
- email
- username
- domain
selectorsOut:
- email
- username
- password
- domain
status: unknown
pricing: free
costNote: Open-source CLI is free; the breach data sources/APIs it queries may themselves require keys or paid access.
opsec: passive
opsecNote: Runs locally and queries remote breach sources over the network; the subject is not notified. Whatever backend API you point it at sees your queries — use a research key/account.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: Open-source breach-search CLI by GitHub user vflame6, harvested from awesome-osint. Code is inspectable on GitHub but the project's maintenance status and which backends it queries are not independently verified here.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases: []
tags:
- data-breach-search-engines
- cli
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Leaker

> Open-source command-line breach-search client — queries leak/breach databases by email, username, or domain from the terminal for scriptable, repeatable lookups.

## When to use
You have one or many subject `email`s, `username`s, or `domain`s and want to run breach lookups programmatically/in bulk rather than clicking a web UI. Useful in missing-persons work when triaging a list of candidate accounts or automating recurring checks. Reach for it when you need CLI/scriptable output and are comfortable supplying API keys for whatever breach backends it supports.

## How to use it (`bestInteractionPattern`: cli)
1. Clone/install from https://github.com/vflame6/leaker (read the repo README for exact install and supported sources).
2. Configure any required API keys/credentials for the breach backends it queries.
3. Run the CLI with the `email`/`username`/`domain` selector(s).
4. Parse the output (often JSON/text) and pivot newly found emails/usernames into [[leakcheck]], [[intelligence-x-2]], or social-profile searches.

## Inputs → Outputs
- **In:** `email`, `username`, `domain`
- **Out:** breach hits with linked `email`/`username`/`password`/`domain`, depending on configured backends
- **Empty/negative result looks like:** no records returned — selector absent from the configured sources, not proof of no exposure.

## Gotchas & OpSec
- Human-in-the-loop: you must read the README and likely supply API keys; capabilities depend entirely on which backends are wired in.
- OpSec: passive toward the subject; your queries flow to whatever remote backend it uses — use research-only keys, not personal accounts.

## Overlaps ("do both")
- Pairs with [[leakcheck]] (which has its own API) — Leaker can orchestrate multiple sources from one CLI while LeakCheck gives source-named web results.

## Trust & verifiability
`trust: unverified` — community open-source tool; code is public on GitHub but maintenance status, backend reliability, and data provenance are not confirmed here. Review the source before running and corroborate any hit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leaker |
| category | email |
| selectorsIn → selectorsOut | email, username, domain → email, username, password, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes |
