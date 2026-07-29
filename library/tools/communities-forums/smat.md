---
id: smat
name: SMAT
description: Use when you have a `username`, keyword, or narrative and want to search and chart its spread across fringe/alt platforms (Telegram, 4chan, Gab, Bitchute, VK, etc.) — returns social-profile and associate leads.
url: https://www.smat-app.com/timeline
category: communities-forums
path:
- communities-forums
bestFor: Keyword/timeline search and activity charts across many fringe and alt-tech social platforms at once.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free web tool (Social Media Analysis Toolkit), maintained as a public-interest project. No account required.
opsec: passive
opsecNote: Passive — SMAT queries its own collected datasets, so you don't touch the platforms or accounts directly. Searches run against archived/aggregated data; your query stays with SMAT. Good for studying extremist/fringe content without visiting the source platforms yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Public-interest research tool widely used by journalists/researchers; coverage depends on which platforms/datasets it currently ingests, which changes over time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Social Media Analysis Toolkit
- smat-app.com
tags:
- forums
- fringe-platforms
- disinformation
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# SMAT

> The Social Media Analysis Toolkit — search terms, channels, and users across a swath of fringe/alt-tech platforms and see, as a timeline, when and where a narrative surged.

## When to use
You have a `username`, keyword, hashtag, or narrative and want to trace it across the harder-to-search corners of the internet — Telegram, 4chan, Gab, Bitchute, VK, Gettr, Rumble and similar — where normal search fails. SMAT charts activity over time and lets you drill into the underlying posts, so you can spot when a term spiked, which platforms carried it, and which accounts drove it. Strong for extremism, disinformation, and coordinated-behavior research; not a mainstream people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.smat-app.com/timeline.
2. Enter a search term (keyword, `username`, hashtag) and pick the platform(s) and date range.
3. Read the activity **timeline/charts** to see volume over time and by platform.
4. Switch to the content/results view to read the actual posts behind a spike.
5. Pivot: a driving `username` → search that handle on other platforms and people tools; a spike date → correlate with real-world events; recurring accounts → map the `associate` cluster.

## Inputs → Outputs
- **In:** keyword / `username` / hashtag + platform(s) + date range
- **Out:** activity timeline and volume charts, matching posts/channels (`social-profile`), recurring accounts/communities (`associate`)
- **Empty/negative result looks like:** flat timeline / no results — the term isn't in SMAT's ingested data, the platform isn't currently covered, or the date range is empty; absence reflects coverage gaps, not proof of no activity.

## Gotchas & OpSec
- Coverage is platform- and dataset-dependent and shifts over time — check which platforms are currently supported.
- Data is archived/aggregated; very recent posts may lag and deleted content may persist or drop.
- OpSec: passive — you query SMAT's datasets, not the source platforms.

## Overlaps ("do both")
- Complements mainstream social search and Telegram-specific tools — SMAT's edge is breadth across fringe platforms; use platform-native tools for depth on any single one.

## Trust & verifiability
`trust: community` — respected public-interest research tool; results are only as complete as its current ingestion, so treat coverage as partial and verify key posts at the source when possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | smat |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
