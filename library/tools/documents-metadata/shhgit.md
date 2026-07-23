---
id: shhgit
name: shhgit
description: Use when you have an `employer-org`/`domain` keyword and want to catch secrets pushed to public git in real time — returns leaked credentials and the commits exposing them.
url: https://github.com/eth0izzle/shhgit
category: documents-metadata
path:
- documents-metadata
bestFor: Real-time monitoring of public GitHub/GitLab/Bitbucket for freshly-committed secrets and credentials.
selectorsIn:
- employer-org
- domain
selectorsOut:
- email
- domain
status: degraded
pricing: free
costNote: Free and open source; self-hosted. Needs GitHub API token(s). NOTE — the project is officially no longer maintained; the code still runs but receives no updates.
opsec: passive
opsecNote: shhgit consumes the public GitHub events firehose and matches locally — it never contacts the target org, so the subject sees nothing. Your API token(s) attribute the polling to your account. Any live secret you find is a responsible-disclosure matter — report/rotate, never use it.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: docker
trust: community
trustNote: Well-known secret-scanning tool, but the maintainer has explicitly discontinued it and moved to a commercial offering. Signature set is frozen, so newer token formats slip through; verify hits manually.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- gitgraber
- the-endorser
aliases:
- eth0izzle/shhgit
tags:
- github
- secrets
- monitoring
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# shhgit

> A self-hosted engine that watches the public git firehose (GitHub/GitLab/Bitbucket) in real time and flags commits containing secrets — API keys, private keys, tokens. Powerful, but officially discontinued.

## When to use
You want to catch credentials the moment they're pushed to public git, filtered to keywords tied to a target `employer-org`/`domain`. shhgit streams new commits and signature-matches them live, giving you exposure as it happens rather than after the fact. Because it's unmaintained, treat it as one input alongside a maintained scanner.

## How to use it (`bestInteractionPattern`: docker)
1. Clone the repo and run it (Docker is the easiest path); supply one or more GitHub API tokens in the config.
2. Optionally tune the signature/keyword set to your target org, brands, and `domain`.
3. Start it — the web UI / console streams matches from the live commit feed as they're detected.
4. Triage every hit: confirm the flagged string is a real, active secret (many are placeholders, revoked, or test values).
5. Pivot: leaked internal `email`/`domain`/host strings feed infrastructure and contact mapping; a live key triggers responsible disclosure, not use.

## Inputs → Outputs
- **In:** keyword/signature filters — `employer-org`, brand, `domain`
- **Out:** public commits containing matched secrets, plus exposed internal `email`/`domain` strings
- **Empty/negative result looks like:** a quiet stream with no matches — nothing leaking for your filters right now, or your token is rate-limited/expired, or the frozen signatures don't cover the leaked format. Confirm the token and broaden filters.

## Gotchas & OpSec
- **Officially unmaintained**: signatures are frozen and miss newer token types; pair it with an actively-developed scanner.
- Human-in-the-loop: **GitHub API token(s)** are required, and rate limits bound throughput.
- Ethics/legal: finding live credentials obliges responsible handling — report and rotate, never authenticate with them.

## Overlaps ("do both")
- Pairs with `[[gitgraber]]` (keyword-driven GitHub monitoring) and maintained scanners (trufflehog, gitleaks) — shhgit watches the live firehose; history scanners dig full repos. Combine for real-time + retrospective coverage.

## Trust & verifiability
`trust: community` — a respected but discontinued tool. Still useful as a *lead generator* for live leaks; every hit needs manual verification, and its coverage of modern secrets is incomplete due to frozen signatures.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shhgit |
| category | documents-metadata |
| selectorsIn → selectorsOut | employer-org, domain → email, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | yes (api-key) |
