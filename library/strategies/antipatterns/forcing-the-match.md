---
id: forcing-the-match
name: antipattern-forcing-the-match
description: Use as a guardrail whenever a lead "feels right" — the urge to confirm an identity on thin evidence is the most common way OSINT investigations go wrong.
type: antipattern
phase: verification
pivotFrom: []
pivotTo: []
summary: Confirmation bias makes a plausible match feel certain. You find an account that *could* be the subject, you want it to be, and you start treating it as confirmed — then every later pivot inherits the error and you build an elaborate, confident, wrong identity. This is the single most damaging failure mode in missing-persons OSINT because it produces false reports about real people.
missingPersonsRelevance: high
whenToUse: Any time you're about to promote a candidate selector to "confirmed," especially when it would unlock an exciting next step.
steps:
- Notice the feeling of wanting it to be true — that's the trigger to slow down, not speed up.
- State the match as a falsifiable claim ("this @handle is the subject") and actively try to DISPROVE it.
- Require at least two INDEPENDENT corroborating selectors (e.g. face AND location, not two facts from the same profile).
- If you can't disprove it and independent signals agree, promote it — but log the confidence, not just the value.
signals:
- You're reasoning "it must be them because..." instead of "it's them only if..."
- The whole case suddenly depends on one unverified hop.
- You're ignoring a detail that doesn't fit (age off by years, wrong city, mismatched timeline).
pitfalls:
- One profile corroborating itself (bio says the same thing the photo implies) is ONE signal, not two.
- Anchoring on a name match while ignoring a face/location mismatch.
- In a team/agent context, passing a "confirmed" selector downstream without its confidence — the next worker can't see it was a guess.
toolsUsed: []
evidence: []
trust: trusted
relatedStrategies:
- phase-verification
- username-reuse-enumeration
- antipattern-tunnel-vision
tags:
- cognitive
- verification
- safety
source: ''
---

# Antipattern: Forcing the match

## The tempting wrong move
You find an account that *could* be the subject. It fits the vibe. You want the case to break here. So you quietly upgrade "candidate" to "confirmed" and keep pivoting — building real downstream work on a guess.

## Why it fails
Confirmation bias is asymmetric: once you believe a match, you notice everything that fits and discount everything that doesn't. Every subsequent pivot inherits the unverified assumption, so by the time the contradiction surfaces you've built a confident, detailed, *wrong* identity — and in this domain that means a false statement about a real, vulnerable person. The cost of a false positive here is not a wasted hour; it's harm and lost credibility.

## The fix: try to disprove it
1. **Restate as falsifiable**: "@handle is the subject" — now hunt for the fact that breaks it (wrong age, wrong city, timeline that can't coexist).
2. **Two independent signals**: corroboration must come from *separate* sources. Face match + independently-sourced location beats five facts scraped off the one profile you're trying to confirm.
3. **Log confidence, not just the value.** A selector is `confirmed | likely | candidate`, and that label travels with it to every downstream pivot and into the report.

## Tell
If your internal sentence is "it **must** be them because…", stop. The correct sentence is "it **is** them only if…". The first is forcing; the second is verifying.

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | verification |
| MP relevance | high |
| related | phase-verification, antipattern-tunnel-vision |
