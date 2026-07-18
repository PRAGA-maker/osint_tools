---
id: github-dorks
name: github-dorks
description: Use when you have a `username`, org, or `domain` and want to hunt exposed secrets/sensitive files in their GitHub repos — returns matching code hits (leaked keys, configs, emails).
url: https://github.com/techgaun/github-dorks
category: search-engines
path:
- search-engines
- code-search
bestFor: Running a curated set of GitHub search "dorks" against a target's repos to surface leaked credentials, configs, and personal data.
selectorsIn:
- username
- domain
selectorsOut:
- email
- password
- document-id
status: live
pricing: free
costNote: Free and open-source; requires a free GitHub personal access token for API access (no paid tier).
opsec: active
opsecNote: Every dork runs a real GitHub code-search query under your token, which GitHub logs against your account. It does not notify repo owners, but tie the token to a research GitHub account, not your primary identity, and mind GitHub's API rate limits.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source helper (techgaun/github-dorks) wrapping GitHub's own code search with a public dork list; the technique is standard, results are only leads and can include false positives.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- github-dorks
- GitHub dorking
tags:
- code-search
- secrets
- github
- arf-seed
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# github-dorks

> A CLI that fires a curated list of GitHub search "dorks" at a user, org, or repo to surface accidentally committed secrets — API keys, passwords, `.env` files, private emails, and internal docs.

## When to use
You have a subject's GitHub `username`/org or a `domain` they're tied to, and you want to know what sensitive material leaked into their (or their employer's) public repositories. Developers routinely commit API keys, config files, and personal emails/addresses by accident; those hits both expose credentials and pivot to real identities (a committer's email, an internal hostname, a document). Use it to mine a person's code footprint for identity and infrastructure leads.

## How to use it (`bestInteractionPattern`: cli)
1. Clone/install: `pip install gitrob`-style — actually `git clone https://github.com/techgaun/github-dorks && cd github-dorks`, then `pip install -r requirements.txt`.
2. Create a GitHub personal access token (read-only) on a research account and export it: `export GH_TOKEN=...`.
3. Run against a repo/user: `github-dorks -u <username>` or `-r <owner/repo>`. It iterates the built-in dork list (patterns like `filename:.env`, `password`, `aws_access_key_id`).
4. Review each hit in context on GitHub — many are false positives (examples, placeholders); confirm the secret/data is real.
5. Pivot: a leaked `email` → email/people search; committer identities → real names; internal hostnames/`domain`s → infrastructure mapping.

## Inputs → Outputs
- **In:** `username` / org / `domain` / repo
- **Out:** code-search hits containing `email`s, `password`s/keys, config `document-id`s
- **Empty/negative result looks like:** no matches for the dorks — the target's public repos have no obvious leaks (or they're in private repos you can't see); it is not proof nothing was ever committed.

## Gotchas & OpSec
- Human-in-the-loop: needs a GitHub API token; without one you hit tight anonymous rate limits.
- **Active**: queries are logged under your token — use a research account.
- High false-positive rate: dorks match documentation and test fixtures too; always verify a hit is a live secret before acting.
- Only sees public repos; private-repo leaks are invisible here.

## Overlaps ("do both")
- Complements broader secret-scanning and code-search tooling; run it alongside a general web/code search so leaks GitHub's own index misses (or that other engines cache) are caught.

## Trust & verifiability
`trust: community` — an open-source wrapper over GitHub's authoritative code search; the mechanism is transparent and hits are verifiable directly on GitHub, but the dork list is community-curated and yields leads, not conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-dorks |
| category | search-engines |
| selectorsIn → selectorsOut | username, domain → email, password, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
