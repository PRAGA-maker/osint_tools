---
id: osintdojo-com
name: osintdojo.com
description: Use when you have a `username`/`name` on a platform (e.g. Pinterest) and want a methodology map of every pivot available — returns a visual guide toward `social-profile`s, not live data.
url: https://www.osintdojo.com/diagrams/pinterest
category: social-networks
path:
- social-networks
bestFor: Free platform-by-platform OSINT flowcharts showing how to pivot from one selector to the next.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free educational resource; diagrams viewable as embedded SVG and downloadable PDF, no account.
opsec: passive
opsecNote: This is reference/training material — reading it touches only osintdojo.com and reveals nothing about any target. OpSec risk lives in the techniques it describes (some require logging into a platform or probing profiles); apply sock-puppet discipline when you execute the steps.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: OSINT Dojo is a respected, widely-cited educational project; the diagrams are curated methodology, not a live data feed, and platform surfaces shift over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINT Dojo
- osintdojo diagrams
tags:
- pinterest
- Pinterest Related Sites
- methodology
- training
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# osintdojo.com

> OSINT Dojo's platform diagrams: visual flowcharts that map, for a given platform, every selector you can start from and every pivot it unlocks. A planning aid, not a lookup tool.

## When to use
You're starting an investigation on a specific platform (the linked diagram is Pinterest; others exist) and want to know *what is enumerable and in what order* before you touch it. Given a `username` or `name`, the diagram shows the pivots — profile → boards/pins → linked accounts → images → location clues — so you can plan which concrete tools to use. Best used at the top of a platform-specific workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.osintdojo.com/diagrams/pinterest (browse the site for other platform diagrams and learning resources).
2. Read the flowchart: each node is a data point; arrows show how one selector leads to the next.
3. For each pivot you want to run, pick a live tool from this library that actually performs it.
4. Execute those steps with sock-puppet discipline where they require login/probing.
5. Cross-reference other Dojo diagrams for adjacent platforms when the subject reuses a handle elsewhere.

## Inputs → Outputs
- **In:** the platform selector you hold — `username` or `name` — as your starting node
- **Out:** a structured pivot map pointing toward `social-profile`s, images, and location leads; **no live data itself**
- **Empty/negative result looks like:** N/A — it's static reference material. The real "miss" is when a mapped pivot yields nothing once you run it with a live tool.

## Gotchas & OpSec
- Human-in-the-loop: none to read; the techniques it describes need your judgement and often a puppet account.
- OpSec: reading is **passive**; the described actions can be active (logging into or probing a platform). Never use a real account.
- Diagrams age as platforms change privacy/surfaces — treat older editions as directional, not exhaustive.

## Overlaps ("do both")
- Same role as `[[osint-github-com]]` (sinwindie's attack-surface docs) — both map *what* to pivot; pair either with the live platform tools that do the pulling.

## Trust & verifiability
`trust: trusted` — a well-regarded educational resource. It is guidance, not verified data; confirm each pivot with a primary source when you run it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintdojo-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
