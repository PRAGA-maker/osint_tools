---
id: github-trending-archives
name: GitHub Trending Archives
description: Use when you want to know which repos/developers trended on GitHub on a past date — returns dated archives of GitHub's trending lists for historical developer/project research.
url: https://github.com/willin/github-trending
category: social-networks
path:
- social-networks
bestFor: Looking up historical GitHub "trending" repositories and developers for a specific date.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source GitHub repository; browse or clone the archive. No account beyond viewing GitHub.
opsec: passive
opsecNote: Reading/cloning a public GitHub repo of historical data — no target is queried or notified. Passive; browse logged out to avoid tying the lookup to your GitHub identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community-maintained archive of GitHub's trending pages; update cadence depends on the maintainer and may lapse, so recent dates can be missing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- willin/github-trending
- github daily trending archive
tags:
- Github
- developer-osint
- archive
- Social Media
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# GitHub Trending Archives

> A dated archive of GitHub's "trending" lists — reconstruct which repositories and developers were prominent on a given day, which the live GitHub trending page won't show.

## When to use
You're researching a developer or project and want historical prominence: did this repo/`username` trend, and when? GitHub's own trending page only shows "now," so this archive fills the gap — useful for timelining when a project or person gained attention, corroborating a developer's activity/reputation over time, or discovering the repos that were hot in a period of interest.

## How to use it (`bestInteractionPattern`: cli)
1. Open or clone the repo at https://github.com/willin/github-trending.
2. Browse the `archives`/`data` folders, organised by date/language.
3. Find the target date (or scan a range) to see the trending repositories and developers then.
4. Note the `username`/repo entries of interest and open their GitHub profiles for detail.
5. Pivot: a surfaced `username`/repo feeds developer OSINT — [[gitstar-ranking]], commit-email harvesters, and username checkers.

## Inputs → Outputs
- **In:** a date/range (and optionally a language) — plus the `username`/repo you're checking for
- **Out:** dated lists of trending repositories and developer `username`s / `social-profile` links
- **Empty/negative result looks like:** the date isn't covered (archive gaps or lapsed updates) or your target simply never trended — absence is not evidence about the developer, only about trending.

## Gotchas & OpSec
- Coverage depends on the maintainer — recent dates may be missing if updates lapsed; check the latest committed archive.
- "Trending" is GitHub's own opaque metric; not appearing means "didn't trend," not "inactive."
- Passive; browse logged out.

## Overlaps ("do both")
- Pairs with [[gitstar-ranking]] and other GitHub OSINT — this gives the historical trending snapshot, those give current prominence and the developer's wider footprint.

## Trust & verifiability
`trust: community` — a community archive of GitHub's public trending pages. Reliable for the dates it covers; verify any developer/repo detail on GitHub itself, and check the archive's freshness before trusting recent coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-trending-archives |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
