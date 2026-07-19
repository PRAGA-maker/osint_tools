---
id: github-release-stats
name: Github Release Stats
description: Use when you have a GitHub repo (a `username`/org + repo) and want its per-release download counts and release metadata — returns download totals and release info to gauge a project's reach and activity.
url: https://tooomm.github.io/github-release-stats/
category: social-networks
path:
- social-networks
bestFor: Quickly seeing how many times each release of a GitHub project was downloaded, and basic release metadata.
selectorsIn:
- username
selectorsOut: []
status: live
pricing: free
costNote: Free static (GitHub Pages) tool that queries the public GitHub API in your browser. No account for normal use; unauthenticated GitHub API calls are rate-limited (~60/hr).
opsec: passive
opsecNote: It calls the public GitHub API from your browser for public repo data — nothing about your subject is disclosed to a third party beyond GitHub itself. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small open-source community tool hosted on GitHub Pages; it just formats the official GitHub API's numbers, so the underlying data is authoritative even though the tool is unofficial.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- github-release-stats
- GitHub release download counts
tags:
- Social Media
- Github
- release-stats
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Github Release Stats

> A one-page tool that shows per-release download counts for any public GitHub repo — a quick read on a project's reach.

## When to use
You're profiling a developer or a project's footprint and want a fast, quantitative sense of a repo's reach: how many times each release binary was downloaded, when releases shipped, and basic release metadata. It's a supporting/context signal when a subject maintains software — corroborating activity and popularity — rather than a person-finder itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tooomm.github.io/github-release-stats/.
2. Enter the repo `owner` (a GitHub `username`/org) and repository name.
3. Read the per-release download counts, release dates, and asset details it pulls from the GitHub API.
4. If you hit the unauthenticated rate limit, wait or supply a token where supported.
5. Pivot: the repo owner's GitHub profile → other repos, contribution timeline, linked email/social; download patterns → activity timeline.

## Inputs → Outputs
- **In:** `username`/org + repo name
- **Out:** per-release download counts, release dates, asset metadata
- **Empty/negative result looks like:** zero or no data means the repo has no *release* assets (many repos ship only source, which GitHub doesn't count as downloads), the repo is private/renamed, or you hit the API rate limit — not necessarily that the project is unused.

## Gotchas & OpSec
- Human-in-the-loop: none; just mind the ~60/hr unauthenticated GitHub API limit.
- Download counts cover **release binary assets only** — clones and source-zip downloads aren't counted, so low numbers don't mean low usage.
- It's an unofficial formatter of official data; verify surprising figures directly against the repo's Releases page/API.

## Overlaps ("do both")
- Pairs with a GitHub profile review and code-search — this quantifies release reach; the profile/commit history and code search build out the person behind the project.

## Trust & verifiability
`trust: community` — a small open-source GitHub Pages tool that surfaces the official GitHub API's numbers; the data is authoritative even though the wrapper is unofficial, so cross-check via GitHub directly if a figure matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-release-stats |
| category | social-networks |
| selectorsIn → selectorsOut | username → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
