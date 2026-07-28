---
id: tik-tok
name: Tik-tok
description: Use when you need to present investigation events as a clean vertical timeline — returns an embeddable, mobile-friendly timeline (a visualization library, not subject data).
url: https://datanews.github.io/tik-tok
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building simple, mobile-friendly vertical timelines to visualise a sequence of events.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (JavaScript library on GitHub).
opsec: passive
opsecNote: Investigator-side visualization. It runs client-side from data you supply (a spreadsheet/CSV of events) and involves no target interaction. Keep the underlying case data local; if you publish the timeline, review it for anything sensitive first.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open-source timeline library by DataNews (a newsroom data team); mature enough to use but a small, journalism-oriented utility, not an OSINT-specific tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Tik Tok timeline
- datanews tik-tok
tags:
- infographics-and-data-visualization
- timeline
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Tik-tok

> A small JavaScript library for building clean, mobile-friendly vertical timelines — a presentation tool for laying out an investigation's events in order (unrelated to the TikTok app).

## When to use
This is a **visualization/output tool**, not a lookup. Reach for it when you've assembled a chronology — a subject's movements, a sequence of posts, the phases of an incident — and want to present it as a readable vertical timeline in a report or web page.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://datanews.github.io/tik-tok for the docs/examples and the GitHub link.
2. Prepare your events (it reads from a Google Sheet/CSV or inline HTML) with dates and descriptions.
3. Include the library's JS/CSS and point it at your data.
4. Style and embed the resulting timeline in your report or page.
5. Pivot: the timeline is a deliverable — feed it the dated facts your other tools produced.

## Inputs → Outputs
- **In:** none (a dataset of dated events you supply — not an OSINT selector)
- **Out:** none (a rendered timeline visualization, not subject data)
- **Empty/negative result looks like:** an empty timeline — a data/formatting issue (bad dates or missing sheet), not an investigative result.

## Gotchas & OpSec
- Purely presentation — it discovers nothing; it only displays what you give it.
- Small, journalism-oriented library; check the GitHub repo for current maintenance before depending on it.
- Any timeline you publish inherits the sensitivity of the events in it — sanitise before sharing.

## Overlaps ("do both")
- Pairs with link-analysis/mind-mapping tools (e.g. [[tobloef-com]]) — timelines show *when*, graphs show *how things connect*; use both to present a case.

## Trust & verifiability
`trust: community` — a stable open-source visualization library; it has no data-quality dimension of its own, since accuracy depends entirely on the events you feed it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tik-tok |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
