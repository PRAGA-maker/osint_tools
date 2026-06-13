---
id: intake
name: phase-intake
description: Use at the very start of a case — capture the seed selectors, the case constraints, and what "found" even means before you touch a single tool.
type: pattern
phase: intake
pivotFrom: [any]
pivotTo: [any]
summary: Intake is where you turn a messy prompt ("find this person") into a structured case — a clean list of seed selectors with provenance, the case objective, the time window, and the legal/ethical guardrails. Skipping intake is the root cause of most wasted investigations: you pivot on a selector that was never confirmed, or you chase the wrong "found" definition. Intake is cheap and pays for itself within the first hour.
missingPersonsRelevance: high
whenToUse: Before any pivoting — the moment a case lands, prompt-given or otherwise.
steps:
  - Write down the objective in one sentence and define "found" for THIS case (current location? proof of life? a verified active account? an identity behind a handle?).
  - Extract every seed selector from the prompt/source and type each one (name, username, image, phone, city...). Put each in the selector log with its provenance.
  - Mark each seed confirmed vs unconfirmed — a name "from the case file" is confirmed; a username "someone said is theirs" is a candidate.
  - Record hard constraints — time window of disappearance, jurisdiction, the subject's age (minor changes everything), and the platform/source the case originated on.
  - State the guardrails before you start — passive-first, no contact with the subject or associates, no contaminating the trail (see `opsec`).
signals:
  - You can state the objective and the "found" definition without re-reading the prompt.
  - Every seed selector has a type, a provenance, and a confidence — no bare strings.
pitfalls:
  - Treating a prompt-supplied selector as confirmed when it was itself a guess (a "known username" that was never verified poisons everything downstream).
  - Not defining "found" — you waste time over-investigating, or stop too early.
  - Missing that the subject is a minor — it raises the safety bar and constrains what you may publish or contact.
toolsUsed: []
trust: trusted
relatedStrategies: [phase-triage, phase-pivot, pattern-selector-discipline, phase-opsec]
tags: [core, setup]
source: ""
---

# Phase: Intake

## The move
Convert a vague ask into a structured case. Out of intake you should hold: a one-sentence **objective**, an explicit **"found" definition**, a **selector log** of every seed with type/provenance/confidence, and the **constraints** (time window, jurisdiction, the subject's age, origin platform).

## Why it matters
Every later phase consumes the selector log. If a seed enters unconfirmed and you forget that, every pivot off it inherits a guess — the same failure as `[[antipattern-forcing-the-match]]`, just seeded at the start instead of the middle. Intake is where you make the provenance discipline real before there's any momentum to lose.

## Define "found"
"Find this person" is not an objective. Decide what ends the case: a current city, a confirmed active account proving recent life, the real identity behind a handle, or a confirmed associate who can be contacted by the proper authority. The definition determines which pivots are worth running and when you stop.

## The seed selector log
Same row format you'll use throughout: `value | type | provenance | confidence | confirmed?`. Seeds get rows too. A name from an official case file is `confirmed`; "their Instagram is probably @x" is a `candidate`. This distinction is the whole game.

## Constraints set the rules
- **Age** — a minor raises the safety bar and limits what you may contact or publish.
- **Time window** — anchors the timeline (`[[pattern-timeline-anchoring]]`); a post from before the disappearance means something different than one after.
- **Origin platform** — tells you where the richest selectors probably leak first.

## Where to go next
Hand the structured case to `[[phase-triage]]` to decide what's actually workable and in what order.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | intake |
| pivot | any → any |
| MP relevance | high |
