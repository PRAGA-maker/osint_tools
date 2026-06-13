---
id: scope-creep-beyond-the-ask
name: antipattern-scope-creep-beyond-the-ask
description: Use as a guardrail when an interesting-but-irrelevant thread pulls you off the mission — chasing curiosity instead of the defined question burns the clock and dilutes the report.
type: antipattern
phase: triage
pivotFrom: [any]
pivotTo: [any]
summary: Scope creep is following threads because they're interesting rather than because they advance the defined question. A juicy sub-plot — a feud in the comments, an associate's unrelated drama, a tangential mystery — pulls your attention away from locating the subject. It feels like investigating, but it spends a finite time budget on findings the case doesn't need, and it pads the report with noise that buries the signal. In missing-persons work, where time is the scarcest resource and the mission is narrow (find this person), scope creep is one of the quietest ways a search underperforms.
missingPersonsRelevance: high
whenToUse: Any time a thread is pulling you in and you haven't checked it against the case's defined question and success criteria.
steps:
  - State the mission in one sentence — what question am I answering, and what is explicitly OUT of scope?
  - Test the thread against it — does this advance LOCATING the subject, or is it just interesting?
  - If out of scope, note it and drop it — park a one-line breadcrumb in case it matters later, then return to the mission.
  - Re-check success criteria — am I past the point where the case is "answered enough"?
  - Keep the report tight — exclude tangents that don't bear on the defined question.
signals:
  - You can restate why the current thread advances finding the subject, in one sentence.
  - Your time is going to threads that map to the mission, not to interesting tangents.
pitfalls:
  - Following an associate's unrelated drama because it's compelling.
  - Endless expansion with no defined end (no success criteria, so nothing ever closes).
  - Padding the report with tangential findings that bury the relevant ones.
  - Confusing legitimate breadth (cheap pivots off your selectors) with chasing irrelevant rabbit holes.
toolsUsed: []
evidence: []
trust: trusted
relatedStrategies: [Plan the mission and define red lines before you start, antipattern-tunnel-vision, Submit steadily and pivot on a timer to avoid rabbit holes, phase-triage, antipattern-doxxing-collateral-people]
tags: [scope, time-management, triage, discipline, cognitive]
source: ""
---

# Antipattern: Scope creep beyond the ask

## The tempting wrong move
A thread off to the side is *fascinating* — a comment-section feud, an associate's unrelated mess, a small mystery that has nothing to do with where the subject is. You follow it, because following threads is what investigating feels like.

## Why it fails
It feels like work, but it spends a **finite time budget** on findings the case doesn't need. The defined question is narrow — *locate this person* — and an interesting tangent advances it not at all. Two costs follow. First, the clock: in a time-boxed search every minute on a curiosity is a minute not spent on the cheap pivot that might have broken the case. Second, the report: tangents pad it with noise, and a reviewer who has to wade through irrelevant sub-plots is slower to act on the signal that matters. Without a stated mission and success criteria, the investigation simply has no edge that tells you to stop — so it doesn't.

## Not the same as breadth
This is *not* `[[pattern-breadth-before-depth]]`. Running the cheap passive pivot off every selector you hold is disciplined breadth that serves the mission. Scope creep is following threads that *don't map to the question at all*. Breadth expands your selector graph toward the subject; scope creep wanders away from it. (And its opposite failure, over-committing to one in-scope lead, is `[[antipattern-tunnel-vision]]` — both are fixed by checking the thread against the mission.)

## The fix: define the ask, test against it, drop the rest
1. **One-sentence mission.** Per `[[Plan the mission and define red lines before you start]]`: what question am I answering, and what is explicitly out of scope?
2. **Test every thread.** Does this advance *locating the subject*? If not, it's a tangent.
3. **Breadcrumb and return.** Park a one-line note in case it matters later, then go back to the mission — and let the cadence rule in `[[Submit steadily and pivot on a timer to avoid rabbit holes]]` pull you out.
4. **Check success criteria.** Know when the case is answered enough to stop.
5. **Keep the report tight.** Exclude tangents — and avoid dragging uninvolved people in, which is `[[antipattern-doxxing-collateral-people]]`.

## Tell
If you can't say in one sentence how the current thread helps *find the subject*, you've left the ask. Interesting is not the bar; relevant-to-the-mission is. Park it and come back to the question. This is `[[phase-triage]]` discipline applied continuously.

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | triage |
| MP relevance | high |
| related | Plan the mission and define red lines before you start, antipattern-tunnel-vision |
