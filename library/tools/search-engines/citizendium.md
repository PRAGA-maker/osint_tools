---
id: citizendium
name: Citizendium
description: Use when you have a `name` or topic and want an expert-authored encyclopedia entry as a Wikipedia cross-check — returns articles with contributor real-name accountability.
url: https://en.citizendium.org/
category: search-engines
path:
- search-engines
bestFor: A secondary, real-name-authored encyclopedia to cross-reference a topic or person against Wikipedia — small and largely static, but occasionally holds an entry Wikipedia lacks.
selectorsIn:
- name
selectorsOut:
- name
status: degraded
pricing: free
costNote: Free to read; no account needed. Editing requires real-name registration, but the project is largely dormant.
opsec: passive
opsecNote: Reading Citizendium queries only its own server — nothing reaches any target. No login to read; standard research-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A real-name, expert-guided wiki encyclopedia founded as a Wikipedia alternative; its accountability model is a plus, but the project is small and largely inactive, so coverage is sparse and articles can be dated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- en.citizendium.org
tags:
- toddington
- curated-directory
- specialty-search
- encyclopedia
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Citizendium

> A real-name, expert-guided encyclopedia founded as a Wikipedia alternative — small and mostly static now, but a useful secondary reference where it has coverage, with contributors held to real-name accountability.

## When to use
As a background/reference cross-check, not a primary OSINT source. When researching a `name` (usually a notable person or subject-matter figure) or a topic, Citizendium occasionally offers an entry Wikipedia doesn't, or a differently-framed one, and its real-name authorship means contributions carry more accountability than anonymous wiki edits. Use it to corroborate or contrast an encyclopedic summary — then rely on primary sources for anything actionable. It won't have entries on ordinary private individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.citizendium.org/ and search the `name` or topic.
2. Read the article, noting it may be older than the equivalent Wikipedia page.
3. Compare against Wikipedia and other references — divergences are worth understanding, not automatically trusting either way.
4. Follow the article's cited sources to primaries.
5. Pivot: cited sources and named people → your real OSINT tools; use the entry only for orientation.

## Inputs → Outputs
- **In:** `name` / topic
- **Out:** an expert-authored encyclopedia article naming people, places, and sources
- **Empty/negative result looks like:** no article — very common, since coverage is limited; absence here means nothing about the subject, only that this small encyclopedia hasn't covered it.

## Gotchas & OpSec
- **Small and largely dormant** — coverage is sparse and many articles are years out of date; treat it as a bonus reference, not a reliable index.
- Only covers notable/encyclopedic subjects — no data on private individuals.
- Encyclopedic summaries are secondary sources — verify facts against the primaries they cite.
- Fully passive.

## Overlaps ("do both")
- Complements Wikipedia and other encyclopedias — cross-reference an entry across them for a fuller, more current picture, and go to cited primary sources for anything you'll act on.

## Trust & verifiability
`trust: community` — a real-name, expert-guided wiki (an accountability improvement over anonymous editing), but its dormancy and thin coverage mean you should confirm anything important against current primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | citizendium |
| category | search-engines |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
