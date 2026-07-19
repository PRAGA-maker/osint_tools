---
id: argumentsearch-com
name: ArgumentSearch (args.me)
description: Use when you have a controversial topic or claim and want pro/con arguments mined from debate portals — a research/reasoning aid, not a people-search selector tool.
url: http://argumentsearch.com/
category: search-engines
path:
- search-engines
bestFor: Retrieving structured pro and con arguments on a debatable topic for background reasoning; negligible direct value for locating a person.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free academic search engine; no account required.
opsec: passive
opsecNote: Passive academic search over a fixed argument corpus. You submit a topic string to a research service; no target selector is involved, so there is no subject-side footprint. Standard query-logging by the host applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Academic tool (args.me / ULB argument-search research line) indexing arguments from debate sites; a reasoning aid, not an investigative data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- args.me
- ULB Argument Search Engine
tags:
- search-engine
- academic
- argument-mining
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# ArgumentSearch (args.me)

> An academic "argument search engine" that returns pro/con arguments on a controversial topic — useful for background reasoning, essentially irrelevant for finding a specific person.

## When to use
Reach for this only when you need structured arguments *for and against* a debatable proposition (e.g. to frame a report or understand a contested issue around a case), not to locate or enrich a subject. It does not take a name, email, or any personal selector and returns no identifying data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://argumentsearch.com/.
2. Type a topic or claim (e.g. "should facial recognition be banned").
3. Read the output: a ranked list of stance-labelled arguments (pro/con) mined from debate portals, each with its source.
4. Pivot: follow an argument's source link if you need the original context; there is no person-level pivot from here.

## Inputs → Outputs
- **In:** a free-text topic/claim (no personal selector)
- **Out:** ranked pro/con arguments with source attributions
- **Empty/negative result looks like:** a topic with no indexed arguments returns an empty list — expected for niche or non-controversial queries.

## Gotchas & OpSec
- This is a reasoning/research tool, not an OSINT data source; do not expect any personally identifying output.
- Human-in-the-loop: none.
- OpSec: passive; only your topic query is seen by the host.

## Overlaps ("do both")
- Stands alone; no meaningful overlap with people-search tools in this library.

## Trust & verifiability
`trust: community` — a maintained academic project; arguments are attributed to their debate-portal sources, so verify any factual claim at the linked origin.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | argumentsearch-com |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
