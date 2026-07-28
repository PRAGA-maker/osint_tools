---
id: tiki-toki
name: Tiki-Toki
description: Use when you have a set of dated events and want to build a shareable interactive timeline to visualise a subject's activity — an analysis/presentation tool, no selectors out.
url: https://www.tiki-toki.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building interactive, multimedia timelines to organise and present an investigation's chronology.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free account allows one fully-functional web timeline. Paid tiers add multiple/private timelines, group editing, and offline (desktop) export.
opsec: passive
opsecNote: You author a timeline from data you already hold; the tool doesn't query the subject, so building it is passive. BUT a free-tier timeline is web-hosted and public by default — do not put sensitive case detail, PII, or an active investigation's findings into a public timeline. Use private (paid) timelines or a self-hosted alternative for anything confidential.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial timeline-authoring service. It's a presentation/analysis aid, not a data source — there is no external data to trust or verify, only what you enter.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- time-graphics
- timelinejs
tags:
- infographics-and-data-visualization
- timeline
- analysis
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Tiki-Toki

> A web-based interactive timeline maker (with a 3D view and image/video embedding) — for turning scattered dated findings into a navigable chronology you can review or present.

## When to use
Late in an investigation you have events with dates — sightings, posts, transactions, travel — and want to see them on one timeline to spot gaps, sequences, and correlations, or to present the chronology to a team. This is an analysis/output tool; it produces a timeline, not new selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free account and start a timeline (free tier = one timeline).
2. Add events with dates, titles, descriptions, and embedded images/video/links from your evidence.
3. Colour-code and group events (e.g. by source, location, or actor) to reveal patterns.
4. Use the linear or 3D view to review the sequence; share the web link if collaborating.
5. Keep the underlying evidence in your case file — the timeline is a view, not the source of record.

## Inputs → Outputs
- **In:** dated events you supply (no external lookup)
- **Out:** an interactive, shareable timeline (no personal selectors)
- **Empty/negative result looks like:** n/a — output quality is purely a function of the data you enter.

## Gotchas & OpSec
- **Public by default on the free tier:** a shared timeline can be indexed. Never publish sensitive case data; use private/paid timelines or an offline tool for confidential work.
- Web-hosted on a third party — the vendor holds your content; treat accordingly for privacy.
- Requires an account (`account-login`).

## Overlaps ("do both")
- Alternatives with different trade-offs: `[[time-graphics]]` (also web, generous free tier) and `[[timelinejs]]` (open-source, self-hostable — better when data must stay private). Pick by confidentiality need.

## Trust & verifiability
`trust: community` — a commercial authoring tool, not a data source. Nothing to verify beyond your own inputs; the caution is confidentiality, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tiki-toki |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | (dated events) → (interactive timeline) |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
