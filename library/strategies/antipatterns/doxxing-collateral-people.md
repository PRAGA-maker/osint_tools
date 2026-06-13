---
id: doxxing-collateral-people
name: antipattern-doxxing-collateral-people
description: Use as a guardrail before you collect or report on anyone who isn't the subject — exposing uninvolved family, friends, and associates causes real harm, and "legal" does not make it right.
type: antipattern
phase: reporting
pivotFrom: [associate, any]
pivotTo: []
summary: Doxxing collateral people is over-collecting and exposing the bystanders around a subject — relatives, friends, exes, neighbors, the person whose name appeared on a piece of mail — beyond what the case actually needs. It happens naturally because the network IS the pivot surface, so associates' details pile up; but publishing or reporting their addresses, identities, and private facts harms uninvolved people, can endanger them, and corrupts the credibility of the whole report. In missing-persons work the mission is to find the subject, not to compile dossiers on everyone adjacent; legal does not equal right.
missingPersonsRelevance: high
whenToUse: Whenever associate/bystander data accumulates, and especially before any finding about a non-subject enters the report or gets shared.
steps:
  - Apply a need-to-collect test — does this associate's detail advance finding the SUBJECT, or is it just adjacent and interesting?
  - Minimize collection on bystanders to what the mission requires; don't build dossiers on uninvolved people.
  - Before reporting any non-subject fact, weigh the harm to that person against the case value.
  - Redact or omit identifying details of uninvolved third parties in the report.
  - Use associates as a PIVOT (to reach the subject) without EXPOSING them as a target.
signals:
  - Every non-subject detail in your file is there because it actually helps locate the subject.
  - Your report exposes no addresses, identities, or private facts of uninvolved people.
pitfalls:
  - Compiling a full profile on a relative or friend who is not relevant to locating the subject.
  - Publishing a bystander's identity because their name surfaced incidentally (e.g. on in-frame mail).
  - Reporting an unvalidated identity guess about an associate, harming an innocent person.
  - Justifying exposure because the data is public/legal, ignoring the harm it causes.
toolsUsed: []
evidence: []
trust: trusted
relatedStrategies: [Ethics: legal does not equal right, antipattern-contaminating-the-subject, antipattern-scope-creep-beyond-the-ask, phase-reporting, antipattern-forcing-the-match]
tags: [ethics, safety, harm-minimization, reporting, sensitive]
source: ""
---

# Antipattern: Doxxing collateral people

## The tempting wrong move
You're working the subject's network — friends, family, the person whose name showed up on a piece of mail in the background of a photo. The details accumulate, and they're *right there*, so you collect all of it and start writing up the associates' addresses, identities, and private facts alongside the subject's.

## Why it fails — and who it harms
The network is your pivot surface, so bystander data piles up *as a side effect* of doing the work well. But collecting it and **exposing** it are different acts, and the second one harms people who did nothing but be adjacent. Publishing an uninvolved relative's address, an ex's identity, or a neighbor's private facts can endanger them, invite harassment, and — when you've guessed wrong, which `[[antipattern-forcing-the-match]]` makes likely — defame an innocent person entirely. It also corrupts the report: a reviewer who sees you dragging in bystanders discounts the whole thing. As `[[Ethics: legal does not equal right]]` puts it, public availability is not permission; you bear responsibility for the impact of your work on third parties, and the mission is to **find the subject**, not to dossier everyone around them.

## The fix: pivot through people without exposing them
1. **Need-to-collect.** For every non-subject detail, ask whether it advances locating the *subject*. If it's merely adjacent-and-interesting, it's `[[antipattern-scope-creep-beyond-the-ask]]`, not evidence.
2. **Minimize.** Collect on bystanders only what the mission requires; don't build dossiers on the uninvolved.
3. **Weigh harm before reporting.** Before any non-subject fact enters the report, weigh harm to that person against case value.
4. **Redact.** Omit or redact identifying details of uninvolved third parties in the output.
5. **Pivot, don't target.** Use an associate to *reach* the subject (their tagged photo, their public post) without turning them into a published target. And never *contact* them — that's `[[antipattern-contaminating-the-subject]]`.

## Tell
If a person who is not the subject is becoming a *target* of your collection rather than a *path* to the subject, stop. The question for every bystander fact is "does this help find the subject, and does reporting it harm someone who isn't involved?" Find the subject; protect everyone else. This is the `[[phase-reporting]]` bar: validated, mission-relevant, minimized third-party exposure.

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | reporting |
| MP relevance | high |
| related | Ethics: legal does not equal right, antipattern-scope-creep-beyond-the-ask |
