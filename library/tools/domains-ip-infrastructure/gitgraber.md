---
id: gitgraber
name: gitGraber
description: Use when you have an `employer-org` or `domain` and want to catch secrets/tokens leaked to GitHub in real time — returns leaked credentials and the files exposing them.
url: https://github.com/hisxo/gitGraber
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Monitoring public GitHub in near-real-time for API keys and secrets tied to a target org/keyword.
selectorsIn:
- employer-org
- domain
selectorsOut:
- email
- domain
status: degraded
pricing: free
costNote: Free and open source (Python3). Needs a free GitHub API token to run searches; last substantive update ~2019, so expect some detection patterns to be dated.
opsec: passive
opsecNote: gitGraber searches GitHub's public index for your keywords — it never contacts the target org, so the subject sees nothing. Your GitHub token ties the searches to your account, and viewing a leaked secret is a sensitive act; handle any discovered credential responsibly (report/rotate, don't use).
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Popular, widely referenced secret-monitoring tool, but inactive since ~2019 — its built-in service patterns (AWS, GCP, Stripe, Twilio…) may miss newer token formats. Verify hits manually.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- shhgit
aliases:
- hisxo/gitGraber
tags:
- github
- secrets
- monitoring
source: osintambition-social
lastVerified: '2026-07-23'
enrichment: full
---

# gitGraber

> A Python CLI that watches GitHub in near-real-time for keyword-matched secrets — AWS/GCP keys, Stripe/Twilio tokens, and anything tied to a target org or domain — with alerting to Slack/Discord/Telegram.

## When to use
You're assessing an organisation's exposure (or hunting a target's infrastructure) and want to catch credentials its developers accidentally push to public GitHub. Feed it the `employer-org` name, product names, or `domain` as keywords; it flags freshly-indexed files that appear to contain matching secrets. It monitors *new* leaks rather than scanning full history.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install the Python3 requirements; generate a free GitHub personal access token and configure it.
2. Put your target keywords (org name, brand, `domain`) in the keywords file.
3. Run in monitoring mode (`-k <keywords> -q <query>`), optionally wiring `-s`/`-d`/`-tg` for Slack/Discord/Telegram alerts.
4. Triage each hit — the tool matches patterns, so confirm a flagged string is a real, live secret (many are examples, revoked, or false positives).
5. Pivot: a leaked internal `email`/`domain`/hostname feeds infrastructure mapping and contact discovery; a live key is a responsible-disclosure matter, not something to use.

## Inputs → Outputs
- **In:** keywords — `employer-org`, brand, or `domain`
- **Out:** GitHub files containing matched secrets, plus exposed internal `email`/`domain` strings
- **Empty/negative result looks like:** no matches while monitoring — either nothing is leaking for those keywords right now, or your patterns are too narrow / GitHub search rate-limited you. Broaden keywords and confirm the token works.

## Gotchas & OpSec
- Human-in-the-loop: a **GitHub API token** is required, and GitHub search rate limits throttle heavy runs.
- **Dormant since ~2019**: detection signatures lag current token formats — it will miss newer secret types. Supplement with a maintained scanner.
- Ethics: discovering live credentials obliges responsible handling (report/rotate). Never authenticate with a found secret.

## Overlaps ("do both")
- Pairs with `[[shhgit]]` and maintained scanners (trufflehog, gitleaks) — gitGraber watches new pushes by keyword; history scanners dig the full repo. Combine for both fresh and historical coverage.

## Trust & verifiability
`trust: community` — a well-known but unmaintained tool. Reliable as a *lead generator*; every hit needs manual verification, and its coverage of modern secret formats is incomplete.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gitgraber |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org, domain → email, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
