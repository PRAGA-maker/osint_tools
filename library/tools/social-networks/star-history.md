---
id: star-history
name: Star History
description: Use when you have a GitHub repo (from a subject's `username`) and want its star trajectory — returns a star-count-over-time chart as a signal of when a project drew attention.
url: https://star-history.com
category: social-networks
path:
- social-networks
bestFor: Charting a GitHub repository's star growth over time to see when and how fast it gained attention.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to generate star-history charts; an optional GitHub token raises the API rate limit for heavy use.
opsec: passive
opsecNote: You query GitHub's public star data via a third-party site; the repo owner is not notified. If you supply a personal GitHub token to lift rate limits, use a research account's token, never a primary one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A popular independent tool over GitHub's public API; the star timeline is reproducible from GitHub data, though it's peripheral (project attention, not identity).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- star-history.com
tags:
- Social Media
- Github
- repo-metrics
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Star History

> Chart how a GitHub repository's stars grew over time — a quick read on when a project caught on, and how sharply.

## When to use
You're profiling a subject's GitHub presence and want context on their projects: Star History plots a repo's star count over its full history, revealing when it gained traction (a launch, a viral moment, a mention). It's peripheral to identity — it tells you about a *project's* attention curve, not the person — but the timing of a spike can corroborate an event (a conference talk, a Show HN, press) and help you prioritize which of a subject's repos actually mattered. Best treated as supporting colour on an already-identified GitHub footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://star-history.com and enter one or more `owner/repo` slugs from the subject's account.
2. Read the star-over-time chart; note inflection points (sudden growth) and their dates.
3. Correlate spikes with external events (talks, posts, releases) to build a timeline.
4. Pivot: the repo and its owner feed GitHub commit-metadata and cross-platform handle tools; a dated spike anchors a timeline.

## Inputs → Outputs
- **In:** a GitHub repo (`owner/repo`) tied to a `username`/`social-profile`
- **Out:** star-count-over-time chart → attention timeline for that `social-profile`'s project
- **Empty/negative result looks like:** a flat, near-zero line — the repo never gained stars, so there's no attention signal to read.

## Gotchas & OpSec
- Human-in-the-loop: none; heavy use may hit GitHub's API limit — supply a research-account token if needed.
- Stars measure attention, not authorship or identity — don't over-interpret.
- It charts one repo at a time (or a few); it doesn't profile the whole account.

## Overlaps ("do both")
- Pairs with `[[repos-timeline]]` and GitHub commit-metadata tools — this shows a project's attention curve, those map the account's activity and extract identity signals.

## Trust & verifiability
`trust: community` — a popular third-party visualizer over GitHub's public API; the star timeline is reproducible, but it's peripheral project-metadata, not identity evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | star-history |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
