---
id: reporting
name: phase-reporting
description: Use to package findings — turn the selector graph into a clear, sourced, confidence-labeled writeup that the right authority can act on, without overstating what you know.
type: pattern
phase: reporting
pivotFrom: [any]
pivotTo: [any]
summary: Reporting converts the investigation graph into something actionable and honest. Every claim carries its provenance and confidence; speculation is labeled as such; the chain from seed selectors to conclusion is reconstructable. In a CTF that means a graded submission; in a real case it means a handoff to law enforcement or a search org. The discipline is the same: state what you can support, flag what you can't, and never launder a candidate into a fact.
missingPersonsRelevance: high
whenToUse: When the case objective is met, the time box closes, or you're handing off to someone who will act.
steps:
  - Restate the objective and what "found" meant, then state your conclusion against it plainly.
  - For each load-bearing finding, give value + provenance (which tool, which source, when) + confidence label.
  - Reconstruct the chain — show how seed selectors led to the conclusion so a reader can audit and reproduce it.
  - Separate fact from inference explicitly — "confirmed active account as of <date>" vs "likely lives in <city> because...".
  - Route to the right recipient and scope it — to law enforcement / a search org, not a public post; mind the subject's safety and the minor rule.
signals:
  - A stranger could follow your writeup from seeds to conclusion and re-derive it.
  - Every sentence that asserts something has a source and a confidence behind it.
pitfalls:
  - Stating likelihoods as certainties — dropping the confidence label is how a candidate becomes a "fact" in someone else's hands.
  - Publishing personal data publicly instead of routing it privately to the proper authority (contamination + safety risk).
  - Omitting provenance — an unsourced conclusion can't be acted on or audited, and may be wrong.
toolsUsed: [hunchly]
trust: trusted
relatedStrategies: [phase-verification, pattern-selector-discipline, phase-opsec, antipattern-contaminating-the-subject]
tags: [core, reporting, safety]
source: ""
---

# Phase: Reporting

## The move
Package the graph into an honest, sourced, actionable writeup. The deliverable is not "I found them" — it's a reconstructable chain from the seed selectors to a conclusion, with every load-bearing claim carrying its provenance and confidence.

## Provenance and confidence on every claim
Each finding gets `value | provenance (tool + source + when) | confidence`. This is the same selector-log discipline (`[[pattern-selector-discipline]]`) carried through to the output. The label is what stops a reader from acting on a `candidate` as if it were `confirmed` — the exact failure verification exists to prevent.

## Reconstructable chain
Show the path. Seed → pivot → new selector → verification → conclusion. A grader, a teammate, or an investigator who picks this up should be able to re-derive your result without re-doing your thinking. If you can't show the chain, you can't yet state the conclusion.

## Fact vs inference
Say which is which, out loud. "Confirmed an active TikTok account posting as of <date>" is a fact. "Likely currently in <city> because three recent posts geotag it" is an inference — a good one, but label it. Conflating the two is how writeups overstate and mislead.

## Route it safely
A missing-persons finding goes to the **proper authority** — law enforcement or the sponsoring search organization — privately. It does not go in a public post, a tweet, or a Discord. Publishing personal data is both a safety risk to the subject and a form of contamination (`[[antipattern-contaminating-the-subject]]`), and if the subject is a minor the bar is higher still. Reporting is where `[[phase-opsec]]` pays out.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | reporting |
| pivot | any → any |
| MP relevance | high |
