---
id: us-twitter-trend-calendar
name: US Twitter Trend Calendar
description: Use when you have a date and want to know what was trending on X/Twitter (and Google) in the US then — returns ranked historical trending keywords by day for context and timeline work.
url: https://us.trend-calendar.com/
category: social-networks
path:
- social-networks
bestFor: Looking up what topics/hashtags trended on a specific past date to contextualise a post, event, or timeline.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free to browse the daily archive; no account needed.
opsec: passive
opsecNote: You read a public trends archive — you enter no target selector and touch no one's account, so it leaks nothing. Purely passive background research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent trend-archiving site (not X/Twitter or Google); useful for context but its capture cadence and completeness are unofficial and unaudited.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Trend Calendar US
- us.trend-calendar.com
tags:
- Social Media
- Twitter
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# US Twitter Trend Calendar

> A day-by-day archive of what trended on X/Twitter and Google in the US — a context layer for placing a post, hashtag, or event on the timeline.

## When to use
You have a `date` (from a post timestamp, a last-seen day, an EXIF capture) and want to know what was dominating US X/Twitter and Google that day. It helps you interpret an ambiguous post ("was #X a global event or a personal reference?"), spot which hashtag a subject was riding, and build a timeline of the public backdrop around a disappearance or event. It's a **context** tool, not a person-finder — it profiles the day, not the individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://us.trend-calendar.com/.
2. Use the top menu to pick the year (archive runs back to 2022), then the month, then click the specific day in the calendar.
3. Read the ranked lists of X/Twitter trending keywords and Google trending searches for that date, each with timestamps.
4. Pivot: a trend that matches a subject's post explains the reference and dates it; identify the exact hashtag to search on X-search tools; use the daily backdrop to corroborate or question a claimed timeline.

## Inputs → Outputs
- **In:** a `date` (no personal selector)
- **Out:** ranked US trending keywords/hashtags and Google trends for that day (context, not a person selector)
- **Empty/negative result looks like:** a missing or sparse day — the archive didn't capture that date; try the adjacent day or a mainstream news archive for the same date.

## Gotchas & OpSec
- Human-in-the-loop: none; browse-only.
- OpSec: fully passive — no selector entered, no account touched.
- It reflects *aggregate* US trends, not a specific person's feed; don't over-read a trend as evidence about an individual. Coverage is US-scoped and unofficial.

## Overlaps ("do both")
- Pairs with X/Twitter search and news-archive tools — the trend calendar tells you *what* the day was about; the search tools find the specific posts and people within it.

## Trust & verifiability
`trust: community` — an unofficial third-party archive; treat its trend lists as context to corroborate against news and platform search, not as an authoritative record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-twitter-trend-calendar |
| category | social-networks |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
