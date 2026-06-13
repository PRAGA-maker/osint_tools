---
id: automation-without-verification
name: antipattern-automation-without-verification
description: Use as a guardrail whenever you act on tool output — a username checker, scraper, or aggregator returns LEADS, and trusting them without opening the actual source imports the tool's false positives into your case.
type: antipattern
phase: verification
pivotFrom: [any]
pivotTo: [any]
summary: Automation-without-verification is treating a tool's output as a finding instead of a lead. Username checkers, scrapers, breach-lookups, and aggregators produce hits fast — and a meaningful fraction of them are false positives, stale, or about a different person. If you pipe that output straight into the report or the next pivot without eyeballing the actual source, you inherit every error the tool made, at machine speed. In missing-persons work this is how a coincidental handle match, a same-name aggregator card, or a dead profile becomes a "confirmed account" — automation amplifies the mistake instead of catching it.
missingPersonsRelevance: high
whenToUse: Every time a tool returns a result you're about to report, link, or pivot from — before you act on it.
steps:
  - Treat every tool hit as UNVERIFIED — enumeration and lookup produce leads, not confirmations.
  - Open the actual source — load the profile/page the tool pointed to and read it yourself.
  - Match it to the source of truth — same face, same interests, same circle as your seed data — before attributing it to the subject.
  - Discard false positives explicitly — a hit that doesn't corroborate is noise, not a quiet maybe.
  - Record the manual verification (what you checked) so a reviewer sees the hit was eyeballed, not trusted blindly.
signals:
  - Every tool hit in your report was opened and matched to the subject by hand before you trusted it.
  - You dropped checker hits that turned out to be a different person on inspection.
pitfalls:
  - Reporting a username checker's hits as the subject's accounts without opening any of them.
  - Trusting an aggregator card or breach result because the tool returned it (see over-trusting people-search).
  - Acting on a face-comparison score alone for a low-quality/angled photo with no human sanity check.
  - Confusing a long list of hits with progress — volume of leads is not validated identity.
toolsUsed: [Sherlock, WhatsMyName, Spiderfoot]
evidence: []
trust: trusted
relatedStrategies: [enumeration-is-not-validation, Tool minimalism: manual investigation over tool-feeding, antipattern-over-trusting-people-search-aggregators, antipattern-forcing-the-match, phase-verification]
tags: [automation, tooling, verification, false-positive, cognitive]
source: ""
---

# Antipattern: Automation without verification

## The tempting wrong move
You run a username checker (or a scraper, a breach-lookup, an aggregator) and it returns a clean list of hits. You copy the list into your notes as the subject's accounts and pivot from them — the tool did the work, so the work is done.

## Why it fails
A tool returns **leads, not findings**, and a meaningful fraction of them are wrong: a coincidental handle owned by someone else, a stale or dead profile, a same-name aggregator card, a face score on a bad photo. Pipe that output straight into the report or the next pivot and you inherit every one of those errors — and because automation is fast, you inherit them *at machine speed*, building a wide, confident, partly-wrong picture before any human ever looked at the actual source. This is the machine-scale version of `[[antipattern-forcing-the-match]]`: the tool's hit *feels* like confirmation, so you skip the step that would catch the false positive. "Enumeration is not validation" (`[[Enumeration is not validation]]`) is exactly this rule — the checker establishes that a handle *exists* on a site, never that it belongs to your subject.

## The fix: open the source, match it by hand
1. **Unverified by default.** Treat every hit — checker, scraper, aggregator, face score — as a lead to verify, not a fact.
2. **Open the actual source.** Load the profile or page the tool pointed to and read it yourself. The point of `[[Tool minimalism: manual investigation over tool-feeding]]` is that the real work is human inspection; the tool just surfaces candidates.
3. **Match to the source of truth.** Same face, same interests, same circle as your seed data before you attribute it to the subject. An aggregator card gets the same scrutiny — see `[[antipattern-over-trusting-people-search-aggregators]]`.
4. **Discard explicitly.** A hit that doesn't corroborate is noise; drop it rather than letting it linger as a quiet maybe.
5. **Record the check.** Note what you eyeballed, so the report shows the hit was verified, not trusted blindly.

## Tell
If a result is in your case because *a tool returned it* and not because *you opened it and matched it*, it isn't verified — it's borrowed risk. The bar is the `[[phase-verification]]` one: a human looked at the source and confirmed it against the seed. Tools find; you confirm.

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | verification |
| MP relevance | high |
| related | enumeration-is-not-validation, Tool minimalism: manual investigation over tool-feeding |
