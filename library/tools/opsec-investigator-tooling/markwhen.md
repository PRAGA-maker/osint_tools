---
id: markwhen
name: MarkWhen
description: Use when you have a set of time-stamped events from an investigation and want a shareable visual timeline — write events as plain text/Markdown and it renders an interactive timeline you can export.
url: https://markwhen.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Turning a text list of dated events into a graphical, exportable investigation timeline.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web editor (open source); no account needed to create and export a timeline.
opsec: passive
opsecNote: The web editor processes your text in-browser; content stays local unless you use the share-link/cloud feature. For sensitive case data, self-host or keep to local export and avoid generating a public share link.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Open-source timeline tool with a public project; it is analysis/visualization plumbing, not a data source, so trust concerns are about where you store your notes, not data accuracy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Markwhen
- markwhen.com
tags:
- NOOSINT tools
- timeline
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# MarkWhen

> A text-to-timeline tool: write dated events in a simple Markdown-like syntax and MarkWhen renders an interactive, exportable timeline — ideal for laying out the chronology of an investigation.

## When to use
You've gathered time-bound facts — posts, sightings, transactions, travel, account-creation dates — and need to see and share them on a timeline. Writing events as plain text (rather than dragging boxes in a diagram tool) makes it fast to build and easy to version-control your chronology. It's an analysis/presentation aid, not a data source: it organizes what you already found.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://markwhen.com/ and use the editor.
2. Write events in the MarkWhen syntax, e.g. `2023-04-01: account created` or ranges `2023-04/2023-06: active posting period`; group with sections and tag with `#labels`.
3. Watch the timeline (and optional calendar/map views) render live beside your text.
4. Export as `.svg` / `.png` / `.mw`, or generate a share link.
5. Pivot: the timeline itself becomes a report exhibit; gaps or clusters it reveals guide where to dig next.

## Inputs → Outputs
- **In:** your own dated events, written as text (not a subject selector)
- **Out:** an interactive visual timeline → exportable `.svg`/`.png`/`.mw` or a share link
- **Empty/negative result looks like:** nothing renders — usually a syntax/date-format error in an event line; fix the date format and it appears.

## Gotchas & OpSec
- It visualizes only what you enter — accuracy is entirely on your sourcing; it neither verifies nor fetches data.
- Share links / cloud save put your notes on their service; for sensitive cases keep to local export or self-host the open-source version.
- OpSec: passive — but mind where your case chronology is stored.

## Overlaps ("do both")
- Pairs with any evidence-collection workflow — tools like `[[markwhen]]` sit at the end of the chain, turning the dated findings from your lookups into a coherent, shareable narrative.

## Trust & verifiability
`trust: unverified` — an open-source visualization utility rather than a data provider; the only trust question is where your notes live, which you control by exporting locally or self-hosting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | markwhen |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
