---
id: preceden
name: Preceden
description: Use when you have a set of dated events from an investigation and want to lay them out as a shareable visual timeline — returns a timeline chart (analysis/presentation aid, no subject PII).
url: https://www.preceden.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Turning a case's dated events into a clear, shareable visual timeline for analysis or presentation.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier allows unlimited timelines with up to 10 events each; paid tiers ($10+/mo) unlock unlimited events, export, and collaboration.
opsec: passive
opsecNote: You enter your own case events into a hosted service — treat the data as leaving your control. Do NOT upload sensitive PII or case details to the cloud version; use generic labels, keep timelines private/password-protected, or build the timeline in a local tool instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established commercial timeline-maker (since 2010); reliable as a visualization aid, but a third-party host — mind what case data you put in it.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- preceden.com
tags:
- infographics-and-data-visualization
- timeline
- analysis
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Preceden

> A web-based timeline maker: feed it dated events (or a text description its AI turns into events) and it renders a clean, layered, shareable timeline — a way to see and present the sequence of a case.

## When to use
Your investigation has accumulated dated events — sightings, posts, transactions, communications — and the sequence matters more than any single point. Preceden lays them on a visual timeline so overlaps, gaps, and patterns become obvious, and produces something you can share in a report. It is an analysis/presentation aid; it holds only the events you enter, not any looked-up subject data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at https://www.preceden.com/ (free tier: unlimited timelines, up to 10 events each).
2. Add events with dates/date-ranges (or use the AI generator to draft a timeline from a text summary), grouping them into layers.
3. Arrange, colour, and label; set the timeline to private/password-protected.
4. Export or share (export/collaboration features are paid) for your report.
5. Pivot: gaps or clustered events on the timeline point to periods that need more collection.

## Inputs → Outputs
- **In:** your own dated case events (or a text description) — no subject lookups
- **Out:** a visual, shareable timeline chart
- **Empty/negative result looks like:** a sparse or misleading timeline if event dates are uncertain — flag approximate dates explicitly rather than implying false precision.

## Gotchas & OpSec
- Human-in-the-loop: a free account is required; the free tier caps events at 10 per timeline.
- OpSec: passive but **cloud-hosted** — data you enter leaves your machine. Do not put sensitive PII or case specifics into the hosted version; use generic labels or a local timeline tool for confidential work.
- The AI generator can misdate or invent events — verify every AI-generated entry against your source.

## Overlaps ("do both")
- Pairs with the OSoMe [[trends-tool]] and social-media timelines — those establish *when* things happened online, Preceden assembles those dates into one coherent case chronology; do both to build and then present a timeline.

## Trust & verifiability
`trust: community` — a durable commercial tool that reliably does visualization, but it is a third-party host. Trust the chart you build from verified dates; never treat an AI-drafted timeline as sourced until you have checked each event.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | preceden |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
