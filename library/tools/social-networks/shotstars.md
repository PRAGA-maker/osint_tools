---
id: shotstars
name: Shotstars
description: Use when you have a GitHub repo or `username` and want to analyse its stargazers for fake/inflated stars and overlapping accounts — returns social-profile and associate leads.
url: https://github.com/snooppr/shotstars
category: social-networks
path:
- social-networks
bestFor: Auditing a GitHub project's star history and stargazer accounts to spot artificial inflation and clusters of linked/overlapping users.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free and open-source (GPL-3.0). No paid tier. An optional free GitHub token raises the API rate limit from ~6K to ~500K stars/hour.
opsec: passive
opsecNote: Shotstars reads GitHub's public API for star/stargazer data; it does not contact the repo owner or notify anyone, so it is passive. If you authenticate with a GitHub token the calls are tied to that account — use a sock-puppet GitHub token, not your real one, if attribution matters.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Open-source project by snooppr (same author as Snoop); actively released (v4.x in 2026). Community-maintained, self-hostable, and its outputs are reproducible from public GitHub data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- snoop
- snoop-2
aliases:
- snooppr/shotstars
- GitHub star analyzer
tags:
- github
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Shotstars

> An open-source CLI that analyses a GitHub repository's stargazers — detecting fake-star inflation and surfacing the accounts (and overlaps between them) behind a project.

## When to use
You have a GitHub project or a `username` and you want to understand the real accounts and network around it: which users starred it, whether the stars look organic or bought, and which stargazers overlap across a suspect's other repos. In an investigation this maps a developer subject's GitHub ecosystem — collaborators, sockpuppets, and linked accounts — and flags manufactured popularity that would otherwise mislead a credibility assessment.

## How to use it (`bestInteractionPattern`: cli)
1. Clone/download from https://github.com/snooppr/shotstars (runs on Linux, Windows, macOS, Android/Termux).
2. (Optional) supply a free GitHub personal access token to lift the API rate limit for large repos.
3. Run it against a target repository URL (or use its scan history/keyword mode).
4. Read the generated CLI + HTML report: star history graphs (by date/month/year/hour/day-of-week), "fake stars"/"aggressive marketing" metrics, JSON on user activity, and a list of users overlapping across repositories.
5. Pivot: overlapping/stargazer `username`s become `social-profile` leads to run through username-search and GitHub-profile tools; clusters of linked accounts are `associate` leads.

## Inputs → Outputs
- **In:** a GitHub repository URL or `username`/handle
- **Out:** `social-profile` (stargazer accounts), `associate` (overlapping/clustered users), and an inflation/authenticity assessment
- **Empty/negative result looks like:** a small or organic star graph with no overlap clusters — meaning no inflation signal and no obvious linked-account network, not a tool failure.

## Gotchas & OpSec
- Rate limits: without a token, large repos hit GitHub's API cap quickly; use a throwaway token to scan big projects.
- Its "fake star" metrics are heuristics (timing spikes, account overlap), not proof — treat a flag as a lead to investigate, not a verdict.
- Passive against the subject; only your GitHub token (if used) is attributable.

## Overlaps ("do both")
- Pairs with `[[snoop]]` (same author) — Snoop hunts a `username` across many sites while Shotstars maps the account network specifically around a GitHub project.

## Trust & verifiability
`trust: community` — it is an actively maintained open-source tool whose findings derive entirely from public GitHub API data, so any result can be reproduced and checked against the live repo.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shotstars |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
