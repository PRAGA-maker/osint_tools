---
id: time-graphics
name: Time.Graphics
description: Use when you have dated events from an investigation and want to visualize them as an interactive timeline — returns a shareable chronology that exposes gaps and overlaps.
url: https://time.graphics
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building an interactive investigative timeline from dated events to reveal sequence, gaps and overlaps.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier lets you build and share timelines online; Premium adds exports (PDF/image), private-by-default, larger timelines and extra features.
opsec: passive
opsecNote: You enter data you've already gathered; the tool doesn't query any subject. Beware the default visibility — timelines can be public or link-accessible, so set sensitive case timelines to private and avoid putting live-case PII on a third-party server.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established online timeline maker (listed in the Bellingcat toolkit) used widely in research and education; it's a visualization aid, so reliability depends on the data you enter, not the tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- time.graphics
- time graphics
tags:
- bellingcat-toolkit
- timeline
- visualization
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# Time.Graphics

> A free online timeline maker for investigations: drop your dated events onto an interactive chronology and the sequence, gaps, and overlaps that a list hides become obvious.

## When to use
You have assembled a set of dated events — sightings, posts, transactions, travel, court dates — and need to see them in order to reason about a subject's movements or a case's chronology. Time.Graphics turns those events into an interactive, zoomable timeline you can annotate and share, which is how you spot the gap where the trail goes cold, or the overlap that contradicts a claimed alibi.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://time.graphics and start a new timeline (free tier needs no signup to begin).
2. Add each dated event with its date/time, a label, and optional notes, media, or source link.
3. Group or colour events by type (e.g. social posts vs. sightings vs. financial) to read patterns.
4. Zoom and pan to inspect dense periods; set the timeline to **private** if it holds sensitive data.
5. Pivot: a visible gap tells you which date range to investigate next; an overlap flags a contradiction to resolve. Export (Premium) for the case file.

## Inputs → Outputs
- **In:** dated events you've already collected (no live selector)
- **Out:** an interactive, shareable timeline visualization — an analytical artifact, not new person data
- **Empty/negative result looks like:** a sparse timeline — usually means you need more dated evidence, not that the tool failed.

## Gotchas & OpSec
- It visualizes; it does not verify. Each event is only as trustworthy as your source for it — cite sources in the notes.
- Default sharing can make a timeline public or link-accessible; set sensitive investigations to private and avoid uploading live-case PII to a third party.
- Passive: nothing here contacts a subject.

## Overlaps ("do both")
- Complements `[[gephi]]` — Gephi maps *who connects to whom*, Time.Graphics maps *what happened when*; together they cover the relational and temporal structure of a case.

## Trust & verifiability
`trust: community` — a well-regarded, widely-used visualization tool; conclusions drawn from a timeline are only as sound as the sourced events you feed it, so keep provenance in the notes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | time-graphics |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
