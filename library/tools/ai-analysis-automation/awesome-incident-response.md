---
id: awesome-incident-response
name: awesome-incident-response
description: Use when you need a curated index of digital-forensics and incident-response (DFIR) tools to pick the right one for a task — a reference list, not a lookup tool itself.
url: https://github.com/meirwah/awesome-incident-response
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Discovering vetted DFIR/forensics tools by category from one curated list.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source curated list on GitHub.
opsec: passive
opsecNote: It is a static reference document — reading it touches only GitHub and reveals nothing about a target. OpSec depends on which listed tools you then use and how.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known, community-maintained "awesome" list (meirwah and contributors); links out to third-party tools you must vet individually.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- awesome DFIR
tags:
- related-awesome-lists
- dfir
- forensics
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# awesome-incident-response

> A curated GitHub index of digital-forensics and incident-response tooling, organised by category — a jumping-off point for finding the right DFIR tool, not an investigative source in itself.

## When to use
You have a forensics/IR task (memory analysis, disk imaging, log/timeline analysis, malware triage) and want a vetted shortlist of tools for it rather than searching blind. This list points you to the tools; it collects no data about anyone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/meirwah/awesome-incident-response.
2. Browse the table of contents by category (e.g. Memory Forensics, Disk Image Creation, Log Analysis, Timeline Tools).
3. Follow the link to a candidate tool; vet its maintenance, licence, and platform before use.
4. Return for adjacent categories as the investigation broadens.
5. Pivot: the chosen tool is where the actual work happens — this list only routes you there.

## Inputs → Outputs
- **In:** none (a topic/task you are shopping tools for)
- **Out:** none as a selector — links to categorised DFIR tools
- **Empty/negative result looks like:** N/A — it is a reference; a gap means the list does not cover that niche, not a failed query.

## Gotchas & OpSec
- Curated but not exhaustive or freshly-audited — verify each linked tool independently.
- It is DFIR-focused, adjacent to but not the same as people-OSINT; use it for the forensics side of a case.

## Overlaps ("do both")
- Complements the OSINT-specific awesome lists and toolkit collections; use each for its domain.

## Trust & verifiability
`trust: community` — reputable community list; trust flows only as far as the individual tools it links, which you must vet yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-incident-response |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
