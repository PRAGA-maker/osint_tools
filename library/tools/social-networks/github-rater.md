---
id: github-rater
name: Github Rater
description: Use when you have a GitHub `username` and want a quick aggregated view of that profile's public activity — returns a summarised stats snapshot.
url: https://aykutsarac.github.io/github-rater/
category: social-networks
path:
- social-networks
bestFor: Getting a fast, aggregated snapshot of a GitHub account's public stats (repos, followers, languages, activity) from a username.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free client-side web app; no login. It reads the public GitHub REST API in your browser.
opsec: passive
opsecNote: The lookup runs in your browser against GitHub's public API; the target is not notified. Unauthenticated GitHub API calls are rate-limited by IP, so heavy use may temporarily block you — use a clean session if concerned.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small third-party front-end over GitHub's public API; it only reformats data GitHub already exposes, so the underlying facts are as reliable as GitHub itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- GitHub Profile Rater
tags:
- Social Media
- Github
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Github Rater

> A lightweight browser tool that scores/summarises a GitHub profile from its public API — a quick triage view, not a deep investigation.

## When to use
You have a GitHub `username` and want a fast overview of the account before deciding whether to dig in: how many repos and followers, primary languages, and rough activity level. It is a triage convenience — everything it shows comes straight from GitHub's public API — so reach for it to size up an account quickly, then move to the profile itself and dedicated GitHub-OSINT tooling for anything substantive (commit emails, timelines, co-contributors).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://aykutsarac.github.io/github-rater/.
2. Enter the target's GitHub `username`.
3. Read the aggregated stats/score (repos, followers, languages, activity).
4. Pivot: go to the live profile and use a deeper tool (commit-email extractors, contribution-timeline analysers) to pull identifying data this summary does not surface.

## Inputs → Outputs
- **In:** `username` (GitHub handle)
- **Out:** `social-profile` — an aggregated stats snapshot of the account
- **Empty/negative result looks like:** an error or empty card means the username doesn't exist on GitHub or the public API rate-limited your IP — retry later or from a clean session.

## Gotchas & OpSec
- It is a novelty aggregator: it only re-presents public GitHub API data and adds no new intelligence — do not treat its "rating" as an OSINT finding.
- Unauthenticated GitHub API limits (60 req/hr/IP) can block repeated lookups.
- OpSec: passive; the account owner is not notified.

## Overlaps ("do both")
- Complements deeper GitHub-OSINT tools — use this for a 5-second size-up, then a commit-email/timeline tool for the data that actually identifies a person.

## Trust & verifiability
`trust: community` — a thin third-party wrapper over GitHub's public API; the numbers are GitHub's own, but the tool itself is unofficial and unaudited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-rater |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
