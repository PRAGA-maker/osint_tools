---
id: octosearch-dootech-com
name: OctoSearch
description: Use when you want to search GitHub repositories starred by people you follow — a personal discovery tool over your own GitHub network's curated stars.
url: https://octosearch.dootech.com/
category: search-engines
path:
- search-engines
bestFor: Searching repositories starred by the GitHub accounts you follow.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free tool; requires connecting/authenticating with your GitHub account to read who you follow.
opsec: passive
opsecNote: It reads your own GitHub following/stars via authentication; connect a research/sock-puppet GitHub account rather than a personal one, since you are granting it access to your account context.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A small third-party developer tool built on the GitHub API; it surfaces GitHub's public star data, scoped to your own follow graph.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- OctoSearch
- octosearch.dootech.com
tags:
- github
- code-search
- developer-tools
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# OctoSearch

> A niche GitHub companion: search across the repositories that the people *you* follow on GitHub have starred — a curated discovery layer over your own network's stars.

## When to use
Its scope is narrow and self-referential: it searches repos starred by the accounts your GitHub user follows, so it's a discovery/curation tool for a developer's own network rather than a way to investigate an arbitrary target. It earns a place here mainly for completeness — if you (or a monitored sock-puppet account) deliberately follow a cluster of accounts around a subject's community, their collective stars can hint at tooling and interests. For directly investigating a person's own GitHub, use GitHub's native search instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://octosearch.dootech.com/ and connect a (sock-puppet) GitHub account.
2. It builds an index of repositories starred by the accounts that user follows.
3. Search keywords/topics; results are the starred repos matching them within that follow graph.
4. Pivot: surfaced repositories (`domain`/URLs) and their owners can hint at a community's tooling and interests; move to native GitHub search to profile a specific person.

## Inputs → Outputs
- **In:** keywords (scoped to repos starred by accounts you follow)
- **Out:** matching repository links (`domain`) from within your GitHub follow graph
- **Empty/negative result looks like:** no results — nothing in your followees' stars matches, or you follow too few accounts; this reflects your network, not GitHub as a whole.

## Gotchas & OpSec
- Human-in-the-loop: GitHub authentication is required — use a research account.
- Scope limitation: it only ever sees *your* followees' stars, so it cannot be pointed at an unrelated target's activity — that's GitHub search's job.
- Low direct investigative value; treat it as a supplementary community-discovery aid.

## Overlaps ("do both")
- Pairs with GitHub's native code/user search — GitHub search investigates a target's own repos, commits and profile directly, while OctoSearch only curates your follow graph's stars.

## Trust & verifiability
`trust: community` — a small third-party tool over the public GitHub API; the star data is GitHub's own, so verify any repo/owner directly on GitHub.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | octosearch-dootech-com |
| category | search-engines |
| selectorsIn → selectorsOut |  → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
