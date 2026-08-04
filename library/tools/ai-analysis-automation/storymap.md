---
id: storymap
name: StoryMap (KnightLab)
description: Use when you have a set of `geolocation` points and want to present a case as a guided map narrative — returns an embeddable slide-by-slide story plotted on a map.
url: https://storymap.knightlab.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Turning a sequence of locations/events into a shareable, guided map-based narrative for reporting.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free tool from Northwestern University Knight Lab; authoring requires a (free) Google sign-in to save.
opsec: passive
opsecNote: A presentation tool used at the reporting stage — you assemble known findings into a map. Anything you publish is public, so scrub sensitive PII before sharing an exported story. Authoring stores your project under a Google account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by Northwestern University Knight Lab; widely used in journalism. It is a storytelling/visualization tool, not a data source.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- timeline
- timeline-js3
- twxplorer
aliases:
- StoryMapJS
- Knight Lab StoryMap
tags:
- infographics-and-data-visualization
- mapping
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# StoryMap (KnightLab)

> A free tool for building slide-by-slide narratives plotted on a map — used to present a movement, timeline, or set of locations as a guided story, not to collect data.

## When to use
You have already gathered a set of `geolocation` points — a person's movements, a series of incident sites, a route — and want to communicate them as a clear, guided narrative for a report or briefing. StoryMap is an output/presentation tool at the write-up stage; it finds nothing about a subject, so its investigative relevance is in how you *present* findings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://storymap.knightlab.com and click "Make a StoryMap" (sign in with a free Google account to save).
2. Add slides, each pinned to a location with a title, description, and optional media (image/video/link).
3. Order the slides to walk the reader through the sequence of places/events.
4. Preview the guided map, then publish/embed the shareable story.
5. Pivot: use it to hand off a geographic narrative to colleagues or in a case report; the underlying locations still need verification via mapping/imagery tools.

## Inputs → Outputs
- **In:** `geolocation` points (plus media/text you already hold)
- **Out:** none as a selector — an embeddable, guided map narrative
- **Empty/negative result looks like:** N/A — it is an authoring tool; there is no query that "returns nothing."

## Gotchas & OpSec
- Published stories are public — remove sensitive PII/locations before sharing.
- Authoring requires a Google sign-in; use an appropriate account for the work.
- It presents data you supply; accuracy is entirely on your sourced locations.

## Overlaps ("do both")
- Pairs with `[[timeline-js3]]` (same Knight Lab suite) — StoryMap handles the *where*, TimelineJS the *when*; combine for a case that has both a route and a chronology.

## Trust & verifiability
`trust: trusted` — a well-established Knight Lab/Northwestern tool; because it only visualizes what you input, verifiability rests on the sources of your plotted points.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | storymap |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | geolocation →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
