---
id: nox
name: NOX
description: Use when you have an email/username and want to query a breach-data search framework — but verify this specific repo before relying on it.
url: https://github.com/nox-project/nox-framework
category: email
path:
- email
bestFor: Self-hosted breach/leak lookups by email or username (unverified repo).
selectorsIn:
- email
- username
selectorsOut:
- social-profile
- name
- phone
status: unknown
pricing: free
costNote: Open-source code if the repo exists; data-source access may carry its own cost.
opsec: passive
opsecNote: A local breach-search tool queries indexed leak data; passive against the target, but pointing it at third-party APIs may log your queries.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: Tagged as a data-breach search engine in awesome-osint, but the github.com/nox-project/nox-framework repo could not be confirmed; named "NOX" is ambiguous across many projects. Do not assume capabilities.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: false
aliases: []
tags:
- data-breach-search-engines
source: awesome-osint
lastVerified: ''
enrichment: full
---

# NOX

> A purported open-source breach/leak search framework — identity unverified; treat with caution.

## When to use
You hold an `email` or `username` and want to run a self-hosted tool that searches breach/leak corpora for linked `social-profile` / `name` / `phone`. Only reach for this after confirming the repo is real and maintained; otherwise prefer a known equivalent.

## How to use it (`bestInteractionPattern`: cli)
1. Confirm the repository exists and inspect its README before running anything.
2. Clone and install dependencies per the repo instructions.
3. Provide any required API keys for downstream breach-data providers.
4. Run a lookup against an `email`/`username` and read the linked records.
5. Pivot confirmed accounts to a username sweep (`[[osint-rocks]]`) or breach checks (`[[osintcat]]`).

## Inputs → Outputs
- **In:** `email`, `username`
- **Out:** `social-profile`, `name`, `phone` (claimed — unverified)
- **Empty/negative result looks like:** no records returned, or the repo cannot be located at all (likely here).

## Gotchas & OpSec
- Human-in-the-loop: probably needs API keys for any real breach data source.
- OpSec: passive against the subject; queries may be logged by upstream providers. Run from a sock/dedicated environment.
- Do NOT fabricate confidence: the named repo is unconfirmed.

## Overlaps ("do both")
- Pairs with `[[osintcat]]` and `[[osint-rocks]]` which provide confirmed breach/account search paths.

## Trust & verifiability
`trust: unverified` — harvested from awesome-osint's data-breach list, but the specific GitHub repo and its feature set could not be confirmed. Verify before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nox |
| category | email |
| selectorsIn → selectorsOut | email, username → social-profile, name, phone |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes |
