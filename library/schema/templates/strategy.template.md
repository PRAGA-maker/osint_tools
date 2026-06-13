---
# --- Required ---
id: example-strategy
name: Example Strategy
description: Use when <situation> — turns a <pivotFrom> into a <pivotTo>.
type: pattern
summary: One paragraph — the move and why it works.
missingPersonsRelevance: high
# --- Strongly encouraged ---
phase: pivot
pivotFrom: [username]
pivotTo: [face, name]
platforms: []
whenToUse: Concrete trigger condition.
steps:
  - First action.
  - Second action.
toolsUsed: []
signals:
  - What tells you it's working.
pitfalls:
  - The tempting wrong turn.
evidence: []
trust: community
relatedStrategies: []
tags: []
source: ""
---

# Example Strategy

## The move
What you do, in two sentences. Name the pivot: `pivotFrom` → `pivotTo`.

## When to use
The case state that triggers this. What must be true first.

## Steps
1. ...
2. ...
(Reference tools by id: `[[tool-id]]`.)

## Signals it's working
- ...

## Pitfalls / antipattern adjacency
- ...  (If this is an `antipattern`, lead with the failure and the why.)

## Evidence
- CTF writeup / solved case / article links that demonstrate it.

---
## Metadata
<!-- generated from frontmatter -->
| field | value |
|---|---|
| type | pattern |
| phase | pivot |
| pivot | username → face, name |
| MP relevance | high |
| tools used | — |
