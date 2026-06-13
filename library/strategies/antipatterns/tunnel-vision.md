---
id: tunnel-vision
name: antipattern-tunnel-vision
description: Use as a guardrail when one lead has captured all your attention — fixating on a single platform or thread while cheap pivots elsewhere sit un-run is how investigations stall.
type: antipattern
phase: pivot
pivotFrom: []
pivotTo: []
summary: Tunnel vision is committing depth-first to one lead — one platform, one profile, one thread — before exhausting the cheap breadth available everywhere else. It feels productive because you're working hard, but you're working a single branch that a 30-second pivot elsewhere might have made irrelevant, and you stop seeing the other selectors you already hold. It's the most common way a case quietly grinds to a halt, and its fix is structural, not motivational.
missingPersonsRelevance: high
whenToUse: Any time one lead has all your attention and you haven't run the cheap pivots off your other selectors.
steps:
- Notice the symptom — you've been on ONE platform/profile/thread for a while and your selector count hasn't moved.
- Stop and re-read the selector log — list everything you hold, not just the thing in front of you.
- Run the cheap passive pivot off every OTHER selector before returning to the deep one.
- Re-decide from the full field — maybe the deep lead is still best, but now it's a choice, not a default.
- If the lead truly stalled, abandon it for breadth rather than digging the same hole harder.
signals:
- Time is passing and the selector count is flat — effort without expansion.
- You can't remember the last time you looked at your other selectors.
pitfalls:
- Mistaking effort for progress — grinding one dead branch feels like work but isn't yielding.
- Sunk-cost digging — "I've spent so long on this profile, it must pay off" keeps you in the hole.
- Confusing this with legitimate enrichment — going deep on a CONFIRMED node is correct (see `[[phase-enrichment]]`); tunnel vision is going deep on an UNCONFIRMED or low-value one.
toolsUsed: []
evidence: []
trust: trusted
relatedStrategies:
- pattern-breadth-before-depth
- phase-pivot
- phase-enrichment
- antipattern-forcing-the-match
tags:
- cognitive
- breadth
- safety
source: ''
---

# Antipattern: Tunnel vision

## The tempting wrong move
You find a promising lead — one platform, one profile, one thread — and you go all-in on it. You scroll every post, chase every sub-thread, refresh for new replies. It *feels* like diligent work. Meanwhile, three other selectors in your log haven't had even their cheapest pivot run.

## Why it fails
Effort is not progress. A single branch worked depth-first can swallow an hour while a 30-second pivot off another selector — a cross-platform handle check, a reverse image search — would have surfaced the actual break or shown your deep branch to be a dead end. Worse, fixation narrows perception: while tunneled in, you literally stop considering the other selectors you already hold. And sunk cost makes it self-reinforcing — "I've invested so much in this profile, it has to pay off" is the sentence that keeps you in the hole.

## The fix: breadth, structurally
The cure isn't "try harder to stay balanced" — discipline-by-willpower fails at exactly the tempting moment. It's the *rule* in `[[pattern-breadth-before-depth]]`: run the cheap passive pivot off **everything you hold** before deepening **anything**. Re-read the selector log, fire the breadth pass, then re-decide which lead to deepen *from the full field*. Now depth is a choice, not a default you fell into.

## Not the same as enrichment
Going deep is not always tunnel vision. Deepening a **confirmed** node — mining its posts, tags, and archives — is correct and necessary (`[[phase-enrichment]]`). The antipattern is going deep on an **unconfirmed** or low-value lead, and going deep *before* you've looked at the breadth. Confirmed + chosen-from-the-field = enrichment; unconfirmed + fell-into-it = tunnel vision.

## Tell
If time is passing and your **selector count is flat**, you're tunneled. Expansion is the metric; raw effort is not. Stop, list what you hold, and run the cheap edges. (Tunnel vision often travels with `[[antipattern-forcing-the-match]]` — the one lead you've fixated on is also the one you start forcing to be the subject.)

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | pivot |
| MP relevance | high |
| related | pattern-breadth-before-depth, antipattern-forcing-the-match |
