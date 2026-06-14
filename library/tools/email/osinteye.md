---
id: osinteye
name: OSINTEye
description: Use when you have an email or username and want to run a self-hosted recon tool that checks account existence and breach exposure from the command line — returns linked accounts and breach hits.
url: https://github.com/atiilla/OsintEye
category: email
path:
- email
bestFor: Self-hosted CLI email/username recon and account/breach checks.
selectorsIn:
- email
- username
selectorsOut:
- social-profile
- username
- name
status: unknown
pricing: free
costNote: Open-source on GitHub; free to run. Some checks may need third-party API keys.
opsec: active
opsecNote: Depending on enabled modules, account-existence checks may probe target platforms; treat as active. Run from a non-attributable environment.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: OSINTEye (github.com/atiilla/OsintEye) is an open-source OSINT recon tool. Capabilities depend on the current repo state; inspect the README before relying on specific features.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- OsintEye
tags:
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# OSINTEye

> An open-source command-line OSINT recon tool for checking where an email/username is registered and surfacing breach exposure.

## When to use
You have an `email` or `username`, prefer running checks locally (no third-party portal logging your subject), and want account-existence and breach results from a scriptable CLI.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `github.com/atiilla/OsintEye` and read the README for current modules/requirements.
2. Install dependencies; add any required API keys.
3. Run a lookup against the `email`/`username`.
4. Read linked accounts / breach hits; pivot confirmed handles to a broader sweep (`[[osint-rocks]]`) and people search (`[[pipl]]`).

## Inputs → Outputs
- **In:** `email`, `username`
- **Out:** `social-profile`, `username`, `name`
- **Empty/negative result looks like:** no module hits, or modules erroring because upstream sites/APIs changed.

## Gotchas & OpSec
- Human-in-the-loop: some modules need API keys.
- Open-source tools drift as target sites change — verify the repo is current; expect some broken modules.
- OpSec: marked active — existence checks can touch the subject's platforms. Run from a clean/VPN environment with a sock account where keys are needed.

## Overlaps ("do both")
- Pairs with `[[osint-rocks]]` (hosted equivalent) and `[[osintcat]]` for breach coverage.

## Trust & verifiability
`trust: community` — open-source repo; auditable code but unmaintained risk. Confirm features in the README before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osinteye |
| category | email |
| selectorsIn → selectorsOut | email, username → social-profile, username, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes |
