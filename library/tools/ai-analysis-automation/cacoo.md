---
id: cacoo
name: Cacoo
description: Use when you have a set of entities and links (people, accounts, addresses) and want to build a shareable link-analysis/relationship diagram — returns a visual map of associate connections, not new data.
url: https://nulab.com/cacoo/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Collaborative online diagramming to lay out and share an investigation's entity-relationship / link chart.
selectorsIn:
- name
- associate
selectorsOut:
- associate
status: live
pricing: freemium
costNote: Free plan (limited sheets/collaborators); paid plans unlock more sheets, history, and team features. A free account is required.
opsec: passive
opsecNote: A cloud SaaS — any diagram you create is stored on Nulab's servers and shared with anyone you invite. Do not put real subject PII or case identifiers into a cloud diagram unless policy allows; prefer pseudonyms, or use an offline tool for sensitive maps.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Commercial product by Nulab (also makers of Backlog/Typetalk); the platform is legitimate, but it is a drawing canvas, not a data source.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- Nulab Cacoo
tags:
- infographics-and-data-visualization
- link-analysis
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Cacoo

> A collaborative online diagramming canvas — a lightweight, browser-based way to draw and share the link chart of an investigation.

## When to use
You have already gathered entities and their relationships — a subject, their `associate`s, phones, addresses, accounts — and you want to lay them out visually so a team can see the structure and collaborate in real time. Cacoo is an output/sensemaking tool: it organizes what you know, it does **not** discover anything new about a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up for a free account at the URL and create a new diagram (flowchart/network/mind-map template).
2. Add nodes for each entity and connect them with labeled edges (e.g. "employed by", "sibling", "co-located").
3. Invite collaborators to edit/comment in real time; use folders to keep separate cases apart.
4. Export the finished chart to PNG/PDF/SVG for a report, or keep it live for ongoing case work.
5. Pivot: the diagram itself becomes the reference map that guides which selectors still need enrichment.

## Inputs → Outputs
- **In:** entities and relationships you already hold (`name`s, `associate` links, accounts, places).
- **Out:** a shareable visual `associate`/entity-relationship diagram — a representation, not new intelligence.
- **Empty/negative result looks like:** nothing to visualize yet — the canvas can't generate connections you haven't supplied; it only renders what you enter.

## Gotchas & OpSec
- It is a **cloud** service: diagrams live on Nulab's servers and are visible to invitees — avoid real PII on sensitive cases; use pseudonyms or an offline tool.
- Free plan caps the number of sheets/collaborators; large teams hit the paywall quickly.
- No investigative data is produced here — don't mistake a tidy diagram for verified facts.

## Overlaps ("do both")
- Overlaps with dedicated link-analysis suites (Maltego-style graphing) and with [[tableau-public]] — Cacoo is the free, general drawing canvas; those add data-driven graphing and quantitative analysis.

## Trust & verifiability
`trust: trusted` — a legitimate commercial SaaS by Nulab; but it stores/asserts nothing about people, so verifiability rests entirely on the data you feed in.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cacoo |
