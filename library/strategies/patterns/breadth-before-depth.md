---
id: breadth-before-depth
name: pattern-breadth-before-depth
description: Use as the governing rhythm of an investigation — run every cheap pivot off everything you hold before tunneling into any single lead; it's the structural defense against tunnel vision.
type: pattern
phase: pivot
pivotFrom: [any]
pivotTo: [any]
summary: Breadth-before-depth is the core operating rhythm: enumerate all the cheap, passive pivots from all your current selectors FIRST, and only go deep on a lead after that breadth pass. A 30-second pivot elsewhere frequently makes an hour-long deep dive irrelevant, and exhausting breadth first is the structural (not just willpower-based) defense against tunnel vision. The exception is enrichment: once a node is CONFIRMED, deliberate depth on it is correct — breadth-first applies to choosing WHICH lead to deepen, not to forbidding depth.
missingPersonsRelevance: high
whenToUse: At the start of every pivot round and whenever you feel the pull to dive into one exciting lead.
steps:
  - List every selector you currently hold (read the selector log).
  - Run the cheap, passive outbound pivot from EACH one before deepening any (cross-platform enum, reverse image, name+disambiguator search).
  - Log every new selector with provenance, then re-queue it for its own breadth pass — breadth recurses.
  - Only after the breadth pass, pick the single highest-value CONFIRMED lead and go deep (enrichment).
  - If a deep dive stalls, return to breadth rather than digging harder in the same hole.
signals:
  - Your selector count jumps quickly in the first minutes as cheap pivots fire in parallel.
  - The lead you eventually deepen was chosen from a full field, not just the first thing you saw.
pitfalls:
  - Diving into the first interesting lead before exhausting cheap breadth (this IS tunnel vision — see `[[antipattern-tunnel-vision]]`).
  - Confusing this with "never go deep" — confirmed-node enrichment is depth and is correct (see `[[phase-enrichment]]`).
  - Spending minutes on an expensive pivot while a free one elsewhere sits un-run.
toolsUsed: []
evidence: []
trust: trusted
relatedStrategies: [phase-pivot, phase-triage, antipattern-tunnel-vision, phase-enrichment]
tags: [core, rhythm, doctrine, cross-cutting]
source: ""
---

# Pattern: Breadth before depth

## The rhythm
Run every cheap pivot off everything you hold *before* you go deep on anything. This is the heartbeat of the pivot phase: a wide, fast, parallel sweep of low-cost passive edges, and only then a deliberate dive into the single best lead it surfaced.

## Why breadth wins
Cheap pivots are cheap and high-variance: a 30-second cross-platform enumeration, a reverse image search, a name+city lookup. Any one of them might hand you the break. If you tunnel into the first juicy lead instead, you can burn an hour on a branch that a free pivot elsewhere would have made irrelevant — you just didn't run it yet. Breadth-first guarantees you've at least *seen* the whole field before committing expensive attention to any part of it. It's the same logic that orders triage (`[[phase-triage]]`): yield over cost, cheap first.

## It's structural anti-tunnel-vision
Discipline-by-willpower fails; structure works. Making "exhaust cheap breadth first" a *rule* removes the moment of temptation where you'd otherwise dive headlong into one shiny lead. That's why this pattern is the structural counterpart to `[[antipattern-tunnel-vision]]` — the antipattern names the failure, this pattern is the habit that prevents it.

## Breadth recurses
Each new selector you find triggers its own breadth pass before anyone deepens it. The graph grows wide at every level. You stop expanding a branch only when it stops yielding or fails verification.

## The deliberate exception: enrichment
Breadth-first is not "never go deep." Once a node is **confirmed**, going deep on it — mining every post, tag, and archive — is exactly right; that's `[[phase-enrichment]]`. The rule governs *which* lead you deepen and *when*: you choose it from a full field after the breadth pass, not impulsively from the first thing you saw. And if a deep dive stalls, the move is to return to breadth, not to dig the same hole harder.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | pivot |
| pivot | any → any |
| MP relevance | high |
