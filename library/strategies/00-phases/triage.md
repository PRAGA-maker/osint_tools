---
id: triage
name: phase-triage
description: Use right after intake — score the seed selectors by yield and cost so you run the highest-value pivots first instead of the first one you thought of.
type: pattern
phase: triage
pivotFrom: [any]
pivotTo: [any]
summary: Triage is prioritization. You hold a set of seed selectors of wildly different value — a clear face photo is gold, a common first name is nearly worthless — and triage decides the order of attack. The principle is yield-over-cost breadth-first: run the cheap, high-yield, passive pivots from your strongest selectors before anything expensive, slow, or active. Good triage is the difference between breaking a case in the first ten minutes and burning an hour on a dead branch.
missingPersonsRelevance: high
whenToUse: After intake, before pivoting — to order the work.
steps:
  - Rank each seed selector by expected yield (how many new selectors it likely unlocks) and uniqueness (a rare handle beats a common name).
  - Rank each candidate pivot by cost — passive/free/instant first, login/captcha/paid last.
  - Build an attack order — highest-yield × lowest-cost pivots first; defer anything active into a deliberate later batch.
  - Sanity-check actionability — is there at least one selector unique enough to converge on one person? If every seed is generic, say so and adjust expectations.
  - Flag the unconfirmed seeds — schedule their verification before you build much on top of them.
signals:
  - Your first three moves are all cheap, passive, and run off your most unique selector.
  - You can articulate WHY a given pivot is first ("rare handle → cross-platform enum is seconds and usually unlocks a face").
pitfalls:
  - Starting with the selector you find most interesting rather than the most unique/highest-yield one.
  - Front-loading an expensive or active pivot (paid people-search, anything requiring login) before exhausting free breadth.
  - Declaring a case actionable when every seed is generic (common name, stripped photo, no location) — that's a thin-selector case, handle it as one.
toolsUsed: []
trust: trusted
relatedStrategies: [phase-intake, phase-pivot, pattern-breadth-before-depth, playbook-thin-selectors-name-city]
tags: [core, prioritization]
source: ""
---

# Phase: Triage

## The move
Order the work. Not every selector is worth the same: a sharp face photo or a rare handle can crack a case in one pivot; a common first name and a big city cannot. Triage scores selectors by **yield × uniqueness** and pivots by **cost**, then sequences them so the cheapest highest-value moves run first.

## Yield and uniqueness
- **Yield** — how many new selectors a pivot likely produces. A confirmed social profile is a selector factory (face, name, email, associates); a phone lookup might give you one name.
- **Uniqueness** — how close the selector gets you to *one* person. `@a_very_specific_handle_1997` converges; "John" does not. Prioritize unique selectors because their pivots actually confirm identity.

## Cost ordering (cheap first)
Passive, free, instant → login/captcha/manual-review → paid/legal-gated. This is the same breadth-first logic as `[[pattern-breadth-before-depth]]`: spend seconds before minutes before dollars. A 30-second cross-platform enumeration can make an hour of paid lookups irrelevant.

## Actionability check
Before committing, ask: is any seed unique enough to converge on one person? If yes, you have a normal case. If every seed is generic, you have a **thin-selector** case — drop into `[[playbook-thin-selectors-name-city]]` and set expectations accordingly. Honesty here prevents the slow death of chasing a name match across millions of people.

## Where to go next
Hand the ordered attack plan to `[[phase-pivot]]`. Keep the unconfirmed seeds flagged for early `[[phase-verification]]`.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | triage |
| pivot | any → any |
| MP relevance | high |
