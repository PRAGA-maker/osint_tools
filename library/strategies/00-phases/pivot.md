---
name: phase-pivot
description: Use during the core of an investigation — expand a thin selector set into new selectors breadth-first, logging every edge.
type: pattern
phase: pivot
pivotFrom: [any]
pivotTo: [any]
summary: The pivot phase is the engine of the investigation. You hold a set of confirmed selectors (name, username, photo, city...) and systematically convert each into new selectors using the tools tree, recording every hop so the graph is auditable and reversible. Breadth before depth: enumerate cheap pivots from everything you have before tunneling into any single lead.
missingPersonsRelevance: high
whenToUse: After triage, once you have at least one workable selector and have decided the case is actionable.
steps:
  - List every selector you currently hold and mark each confirmed vs unconfirmed.
  - For each confirmed selector, look up its outbound pivots in `pivots/<selector>/` and run the cheap/passive ones first.
  - Write each new selector you discover into the selector log with its provenance (which tool, which source, confidence).
  - Re-queue every NEW selector for its own pivots. Stop expanding a branch when it stops yielding or when it leaves the subject's identity (verification fails).
  - Prefer passive pivots; defer anything active/HITL (captcha, login) into a batch you do deliberately.
signals:
  - Selector count is growing and new selectors keep re-confirming the same person (timeline, location, associates all cohere).
  - Independent selectors converge on the same account/identity — that convergence IS your verification.
pitfalls:
  - Depth-first tunneling into the first interesting lead before exhausting cheap breadth (see `antipatterns/tunnel-vision`).
  - Adding a selector without provenance — you can't later tell if it's confirmed or a guess.
  - Letting an unverified selector spawn a whole sub-investigation that's actually a different person.
toolsUsed: []
trust: trusted
relatedStrategies: [phase-triage, phase-verification, pattern-selector-discipline]
tags: [core, graph]
---

# Phase: Pivot

## The move
You are growing a graph. Nodes are **selectors** (a username, a face, a city, a phone). Edges are **pivots** (tool-driven conversions of one selector into another). The pivot phase is disciplined graph expansion: breadth-first, provenance-logged, verification-gated.

## Why breadth-first
Cheap passive pivots (username enumeration, reverse image, "name + city" people search) take seconds and frequently hand you the break. If you tunnel depth-first into the first juicy lead, you spend an hour on a branch that a 30-second pivot elsewhere would have made irrelevant. Run *every* cheap outbound edge from *everything you hold* before you go deep on any one.

## The selector log (non-negotiable)
Every selector gets a row: `value | type | provenance (tool+source) | confidence | confirmed?`. This is what makes the investigation auditable, lets you back out a wrong turn, and — in a team/agent context — lets another worker pick up where you stopped. An agent should treat this log as durable state.

## Where to go
- Look up outbound edges in `pivots/<from-selector>/`.
- Anything requiring login/captcha/manual judgment: batch it, don't let it stall breadth (`bestInteractionPattern` + `humanInLoop` on the tool tells you which).
- The instant a new selector stops re-confirming the same person, suspect a wrong branch and run `phase-verification`.

## Pitfalls
See `[[antipattern-tunnel-vision]]` and `[[antipattern-forcing-the-match]]`. The pivot phase fails far more often from cognitive error than from missing tools.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | pivot |
| pivot | any → any |
| MP relevance | high |
