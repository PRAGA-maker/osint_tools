---
id: commits-top
name: Commits.top
description: Use when you have a country/city and want the most active GitHub developers there — returns ranked `social-profile`s (GitHub usernames) by contribution activity for that location.
url: https://commits.top/
category: social-networks
path:
- social-networks
bestFor: Finding and ranking the most active GitHub users in a given country or city by public contribution count.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
- username
- name
status: live
pricing: free
costNote: Free to browse; data is derived from public GitHub activity. No account needed.
opsec: passive
opsecNote: You browse pre-computed public rankings; no GitHub user is queried directly or notified. Fully passive. Standard web logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent ranking site built from public GitHub contribution data. Rankings reflect self-declared profile locations, so a developer's listed country may be aspirational or stale.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- github-search
- github-user-search
aliases:
- commits.top
tags:
- github
- developers
- ranking
- geolocation
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Commits.top

> A leaderboard of the most active GitHub developers per country/city — a way to enumerate prominent coders tied to a location.

## When to use
You're looking for developers associated with a particular country or city, or you want to place a known GitHub-active subject within their local developer scene. Commits.top ranks GitHub users by public contribution activity, grouped by the location on their profile. Use it to enumerate candidate `social-profile`s for a region (e.g. "top developers in Latvia"), to check whether a subject appears in their country's ranking, or to discover a real name attached to a highly-active account. Niche, but useful when a case centres on a developer/tech subject in a specific place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://commits.top/.
2. Select a country (and, where available, a city) to view its ranked list of GitHub users.
3. Read the ranked entries: GitHub `username`, contribution counts, and often a display `name`.
4. Open a profile of interest on GitHub to confirm and enrich.
5. Pivot: each GitHub `username`/`social-profile` feeds cross-platform username search, and the linked GitHub profile often exposes an `email`, personal site, or real `name` for further work.

## Inputs → Outputs
- **In:** `geolocation` (a country/city)
- **Out:** ranked `social-profile`/`username` (GitHub accounts), often a display `name`
- **Empty/negative result looks like:** a subject not appearing in their country's list means they simply aren't among the most-active ranked users (or their profile location differs) — not that they lack a GitHub account.

## Gotchas & OpSec
- Location is based on the user's self-declared GitHub profile field — it can be blank, fake, or outdated, so rankings miss people and misplace others.
- It surfaces only *highly active* accounts; ordinary users won't appear.
- OpSec: fully passive; you read a precomputed leaderboard, touching no individual account.

## Overlaps ("do both")
- Pairs with `[[github-search]]` / `[[github-user-search]]` — use those to search GitHub by keyword/username directly, and Commits.top when you want the location-ranked "who's most active here" view instead.

## Trust & verifiability
`trust: community` — an independent ranking from public GitHub data. Contribution counts are objective, but the location grouping depends on self-reported profile fields; confirm any individual by opening their actual GitHub profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | commits-top |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → social-profile, username, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
