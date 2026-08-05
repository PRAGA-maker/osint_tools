---
id: timeline
name: TimelineJS (Knight Lab)
description: Use when you have a set of dated case events (in a spreadsheet) and want an interactive, embeddable visual timeline — returns a shareable timeline you host yourself (analysis aid, no subject PII).
url: https://timeline.knightlab.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building an interactive, embeddable timeline of case events from a Google Sheet, hosted on your own page.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (Northwestern University Knight Lab); the tool is free, though the default workflow uses a Google Sheet.
opsec: passive
opsecNote: The standard workflow puts your event data in a Google Sheet and generates a public embed — treat both as leaving your control. For sensitive cases, self-host the open-source TimelineJS and supply a local JSON data file instead of a shared Google Sheet, and keep the embed private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by Northwestern University's Knight Lab; open source and widely used in journalism, so the tool itself is reputable — provenance risk is only in where you host the data.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- storymap
- timeline-js3
- twxplorer
aliases:
- TimelineJS
- Knight Lab Timeline
- TimelineJS3
tags:
- infographics-and-data-visualization
- timeline
- analysis
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# TimelineJS (Knight Lab)

> Northwestern Knight Lab's open-source timeline builder: fill a spreadsheet with dated events and it renders an interactive, embeddable, media-rich timeline — the journalism-grade way to lay out a case chronology.

## When to use
Your investigation has a sequence of dated events — sightings, posts, transactions, filings — and you want to both analyse the order and present it. TimelineJS turns a structured spreadsheet into a scrollable, media-embedding timeline. Unlike hosted timeline SaaS, it is open source and self-hostable, so it is the better choice when case data must stay under your control. It holds only the events you enter; it looks nothing up.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://timeline.knightlab.com and copy the template Google Sheet (for sensitive work, plan to self-host instead — see step 4).
2. Fill each row with a dated event: date(s), headline, text, and optional media/link.
3. Generate the embed and view the interactive timeline.
4. **For confidential cases:** deploy the open-source TimelineJS3 on your own page and feed it a local JSON data file rather than a shared Google Sheet, keeping the embed off the public web.
5. Pivot: gaps or clusters on the timeline flag periods needing more collection; the finished timeline drops into a case report.

## Inputs → Outputs
- **In:** a spreadsheet/JSON of dated case events (no subject lookups)
- **Out:** an interactive, embeddable visual timeline
- **Empty/negative result looks like:** a broken/empty timeline from malformed dates or an unshared sheet — check date formatting and sheet publishing; uncertain dates should be labelled approximate, not faked precise.

## Gotchas & OpSec
- Human-in-the-loop: the default flow needs a Google account/Sheet; self-hosting avoids that.
- OpSec: passive but the **default workflow is cloud + public embed** — self-host with a local data file for anything sensitive; never put confidential PII in a shared Google Sheet.
- It is a presentation tool: it renders what you enter, so the analysis and date-verification are on you.

## Overlaps ("do both")
- Pairs with [[preceden]] and [[storymap]] — Preceden is a quicker hosted alternative, StoryMap adds geography; TimelineJS wins when you need open-source, self-hosted control. Use the OSoMe [[trends-tool]] to pin down when online events happened before plotting them.

## Trust & verifiability
`trust: trusted` — a reputable, open-source Knight Lab project used across journalism. The tool is sound; the only caution is data provenance — self-host to keep sensitive events off Google's servers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | timeline |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
