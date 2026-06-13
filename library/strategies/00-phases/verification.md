---
id: verification
name: phase-verification
description: Use continuously — every new selector is a candidate until independent signals confirm it still refers to the same person; this phase is the safety rail of the whole tree.
type: pattern
phase: verification
pivotFrom: []
pivotTo: []
summary: Verification is not a step at the end — it runs throughout, gating every promotion of a selector from candidate to confirmed. The core rule is two independent corroborating signals from separate sources. In missing-persons work the cost of a false positive is not a wasted hour; it's a confident false statement about a real, vulnerable person. Verification is the discipline that prevents the whole tree's most dangerous failure mode.
missingPersonsRelevance: high
whenToUse: Every time you're about to treat a candidate selector as confirmed, and again whenever a branch stops cohering.
steps:
- State the claim as falsifiable ("@handle is the subject") and try to DISPROVE it before you try to confirm it.
- Require two INDEPENDENT signals from separate sources — face match AND independently-sourced location beats five facts off one profile.
- Check the contradictions actively — age, city, timeline, physical description; a single hard mismatch can kill a match that ten soft ones supported.
- Promote with a confidence label (confirmed | likely | candidate), and make that label travel with the selector to every downstream pivot and into the report.
- Re-verify when a branch stops cohering — that's the early warning that you forked onto a different person.
signals:
- Two genuinely independent selectors converge on the same identity — convergence IS the confirmation.
- You tried hard to disprove the match and couldn't.
pitfalls:
- One source corroborating itself (bio says what the photo implies) counts as ONE signal, not two.
- Anchoring on a strong name match while explaining away a face or location mismatch (see `[[antipattern-forcing-the-match]]`).
- Passing a "confirmed" selector downstream without its confidence — the next worker or pivot can't see it was a guess.
toolsUsed: []
trust: trusted
relatedStrategies:
- antipattern-forcing-the-match
- pattern-selector-discipline
- phase-pivot
- phase-enrichment
tags:
- core
- verification
- safety
source: ''
---

# Phase: Verification

## The move
Continuously gate the promotion of selectors from **candidate** to **confirmed**. Verification is not a final checkpoint — it interleaves with every pivot. The instant a new selector wants to become "the subject's," it has to earn it.

## The rule: two independent signals
Corroboration must come from *separate* sources. A face match plus an independently-sourced location is two signals. A bio, a photo, and a username all read off the *one* profile you're trying to confirm is **one** signal wearing three hats. Convergence of genuinely independent selectors is the strongest confirmation you can get — and it's usually free, because your other pivots already produced the second signal.

## Try to disprove it first
Restate the match as a falsifiable claim and hunt for the fact that breaks it: an age off by years, a city that can't coexist with the timeline, a physical description that doesn't fit. A single hard contradiction outweighs a pile of soft "feels right" signals. This is the inverse of `[[antipattern-forcing-the-match]]`, which is what verification exists to prevent.

## Confidence travels
Every selector carries a label — `confirmed | likely | candidate` — and the label moves with it everywhere: into the next pivot, into a teammate's or agent's hands, into the final report. A value without its confidence is a trap, because downstream nobody can tell a fact from a guess. See `[[pattern-selector-discipline]]`.

## The cost asymmetry
This is missing-persons work. A false positive is a confident, detailed, *wrong* statement about a real and often vulnerable person — harm, not just wasted time. That asymmetry is why verification is the strictest discipline in the tree and why it gates `[[phase-enrichment]]` and `[[phase-reporting]]` both.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | verification |
| pivot | any → any |
| MP relevance | high |
