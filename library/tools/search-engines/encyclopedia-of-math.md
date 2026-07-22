---
id: encyclopedia-of-math
name: Encyclopedia of Mathematics
description: Use when you have a mathematical term or named theorem/person and want an authoritative definition — returns wiki articles with concepts, references, and attributions.
url: https://www.encyclopediaofmath.org
category: search-engines
path:
- search-engines
bestFor: Looking up rigorous definitions of mathematical concepts and the people/works a theorem is attributed to.
selectorsIn:
- name
selectorsOut:
- name
status: live
pricing: free
costNote: Free, open wiki (maintained by the European Mathematical Society and Springer); no account needed to read.
opsec: passive
opsecNote: Passive reference lookup with no per-subject query; ordinary web browsing, nothing to leak beyond standard logging.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Curated academic wiki backed by the EMS/Springer with editorial oversight; far more reliable than an open-edit wiki for its subject.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Encyclopedia of Math
- encyclopediaofmath.org
- EoM
tags:
- toddington
- curated-directory
- specialty-search
- reference
- mathematics
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Encyclopedia of Mathematics

> An authoritative, editor-reviewed wiki of mathematics — a niche reference for defining technical terms and tracing which mathematician a concept is named after.

## When to use
An investigation surfaces a mathematical term, a named theorem, or a claimed area of expertise and you need an authoritative definition or attribution — for example, to sanity-check an academic's stated specialism, understand jargon in a leaked document, or find the person/work behind an eponymous result. This is a subject-reference tool, not a people-search: its OSINT use is context and verification, not locating individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.encyclopediaofmath.org and search the term or name.
2. Read the article for the rigorous definition, related concepts, and the references/attributions (often naming the originating mathematician and key papers).
3. Use the attributions and citations as leads back to a `name` and their published work.
4. Pivot: an attributed `name` feeds academic/people search; cited works feed literature tools to place a person in a field.

## Inputs → Outputs
- **In:** a mathematical term / named theorem / `name`
- **Out:** an authoritative definition plus attributions naming the associated mathematician(s) (`name`) and references
- **Empty/negative result looks like:** no article for the term — either it is outside mathematics, misspelled, or too niche. Absence here says nothing about a person; use a general academic search instead.

## Gotchas & OpSec
- Scope is strictly mathematics; it will not help with people outside that context.
- It documents concepts and their originators, not living individuals' whereabouts — treat it as verification/background only.

## Overlaps ("do both")
- Pairs with Google Scholar and general encyclopedias — this gives the rigorous, vetted definition and attribution; those place the associated person and their current work.

## Trust & verifiability
`trust: trusted` — an editor-reviewed academic reference backed by the EMS and Springer, so definitions and attributions are reliable; its limitation is scope, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | encyclopedia-of-math |
| category | search-engines |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
