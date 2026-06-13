---
id: selector-discipline
name: pattern-selector-discipline
description: Use throughout — keep a selector log where every value carries its type, provenance, and confidence, so the investigation is auditable, reversible, and safe to hand off.
type: pattern
phase: pivot
pivotFrom: []
pivotTo: []
summary: The selector log is the durable state of an investigation — a table where every selector is a row carrying value, type, provenance (which tool, which source, when), and a confidence label (confirmed/likely/candidate). This discipline is what makes a case auditable, lets you back out a wrong turn, and lets a teammate or agent pick up exactly where you stopped. Most OSINT failures are not missing tools; they're a lost track of what was confirmed versus guessed. The log fixes that.
missingPersonsRelevance: high
whenToUse: From the first seed selector to the final report — continuously.
steps:
- Give every selector a row — value, type (name/username/image/...), provenance (tool + source + when), confidence (confirmed/likely/candidate).
- Never write a bare value — a selector without provenance and confidence is indistinguishable from a guess later.
- Update confidence as evidence arrives — a candidate becomes confirmed only when verification passes; the label changes, the history stays.
- Make the log the source of truth for pivoting — pivot off confirmed selectors first; treat candidates as provisional.
- Carry the labels into every handoff and into the report — confidence must travel with the value.
signals:
- You can answer "how do I know this?" for any selector instantly by reading its row.
- You can cleanly back out a wrong branch because every downstream selector traces to the one that broke.
pitfalls:
- Keeping selectors in your head — memory silently upgrades candidates to facts.
- Recording a value without its provenance/confidence — you can't later tell a confirmed fact from a hopeful guess.
- Letting a candidate's confidence "drift up" through use rather than through evidence (the quiet form of forcing the match).
toolsUsed: []
evidence: []
trust: trusted
relatedStrategies:
- phase-pivot
- phase-verification
- antipattern-forcing-the-match
- phase-reporting
tags:
- core
- provenance
- discipline
- cross-cutting
source: ''
---

# Pattern: Selector discipline (the selector log)

## The move
Keep one table that is the investigation's memory. Every selector — seed or discovered — is a row:

`value | type | provenance (tool + source + when) | confidence (confirmed/likely/candidate)`

That's it. The discipline is that **nothing** lives outside the log and **no value** is ever bare.

## Why it's the backbone
Three payoffs, all load-bearing:
- **Auditable** — for any claim you can answer "how do I know this?" by pointing at a row. That's what makes a report (`[[phase-reporting]]`) trustworthy.
- **Reversible** — when a branch turns out wrong, every selector downstream traces back to the one that broke, so you can cleanly prune instead of unravelling the whole case.
- **Handoff-safe** — a teammate, or an agent in the next turn, can pick up the exact state. The log *is* the durable state of the investigation.

## Confidence is the critical field
The label `confirmed | likely | candidate` is the single most important thing the log carries, because the whole tree's worst failure is treating a guess as a fact. Confidence only rises when `[[phase-verification]]` passes — never through mere repetition or use. A candidate that "drifts up" to confirmed because you kept building on it is the quiet form of `[[antipattern-forcing-the-match]]`, and the log is what makes that drift visible and preventable.

## In practice
Pivot off `confirmed` selectors first. Treat `candidate`s as provisional and flag them for verification. And whenever a selector leaves your hands — into a downstream pivot, a teammate, the report — its confidence label goes with it. A value without its confidence is a trap for whoever receives it.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | pivot |
| pivot | any → any |
| MP relevance | high |
