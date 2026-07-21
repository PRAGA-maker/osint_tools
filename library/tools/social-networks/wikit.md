---
id: wikit
name: WIKIT
description: Use when you have a `name` of a notable person, place or organization and want to read its Wikipedia summary from the command line — returns article text (no structured selector output).
url: https://github.com/KorySchneider/wikit
category: social-networks
path:
- social-networks
bestFor: Fast terminal lookup of a Wikipedia summary or full article for a named subject, scriptable into an OSINT pipeline.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source (npm). No account or API key.
opsec: passive
opsecNote: Queries Wikipedia's public API/pages; requests originate from your IP, not the target's, and reveal nothing to the subject. Route through your normal research egress like any web request.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source CLI wrapper (KorySchneider/wikit, ~290 stars); it only reformats Wikipedia, so data quality is Wikipedia's, not the tool's.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- wikit cli
tags:
- Social Media
- Wikipedia
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# WIKIT

> A tiny CLI that prints a Wikipedia summary (or full article) for any query — a scriptable way to pull background on a named public figure or place without opening a browser.

## When to use
You have a `name` — a notable person, company, place, or event — and want quick encyclopedic background inside a terminal workflow (e.g. batch-resolving mentioned entities during a research pass). It is a reader for Wikipedia, so it only helps when the subject is notable enough to have an article; it is not a people-search tool for private individuals.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `npm i wikit -g` (Node.js required).
2. Query: `wikit "empire state building"` prints the lead summary, wrapped to your terminal width.
3. Flags: `-a` full article, `-l <lang>` a different-language Wikipedia (useful for foreign subjects), `-b` open in browser, `-d` disambiguation menu when the name is ambiguous.
4. Pivot: use the article to extract corroborating facts (dates, affiliations, associates) or the correct spelling/language variant of a name to feed other tools.

## Inputs → Outputs
- **In:** `name` (query string)
- **Out:** Wikipedia summary/article text — background context, not a structured selector
- **Empty/negative result looks like:** "no article found" or a disambiguation list — meaning the subject isn't on Wikipedia (very common for private individuals), not that they don't exist.

## Gotchas & OpSec
- Only covers Wikipedia-notable subjects; useless for ordinary missing persons except to research a place, employer, or organization connected to them.
- Ambiguous names return a disambiguation menu — pick with `-d`.
- OpSec: passive; requests hit Wikipedia from your IP, invisible to the subject.

## Overlaps ("do both")
- Pairs with any name-based search tool — use `[[wikit]]` to confirm the correct name form / language and to enrich context on an org or location, then run the identity search elsewhere.

## Trust & verifiability
`trust: community` — an open-source npm wrapper; it faithfully relays Wikipedia, so accuracy and neutrality are exactly Wikipedia's (crowd-edited, cite the underlying references).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikit |
| category | social-networks |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
