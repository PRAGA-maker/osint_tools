---
id: single-source-confirmation
name: antipattern-single-source-confirmation
description: Use as a guardrail whenever a "second source" turns out to echo the first — corroboration requires INDEPENDENT signals, and a fact circulating between sources that all copied each other is still one source.
type: antipattern
phase: verification
pivotFrom: [any]
pivotTo: [any]
summary: Single-source confirmation is the illusion of corroboration produced when several sources all trace back to the same origin. A news article, three aggregator cards, and a Reddit thread can all "agree" on a fact simply because they all copied it from one place — or because one profile's bio, photo, and pinned post all say the same thing. Counting echoes as independent confirmations gives you false confidence and lets a single original error harden into "verified." In missing-persons work this is how a wrong age, a wrong city, or a misidentified profile becomes treated as settled fact across the whole case.
missingPersonsRelevance: high
whenToUse: Any time you're about to call a fact "confirmed" because more than one source says it — check whether those sources are actually independent.
steps:
  - For each supporting source, trace it to its origin — who first asserted this, and did the others copy it?
  - Collapse the echoes — sources that share one origin count as ONE source, not many.
  - Require a genuinely independent second signal — a different origin, a different modality (face, geo, records), not a restatement.
  - If every "confirmation" traces to one origin, downgrade the fact to candidate and keep verifying.
  - Record WHICH independent sources support a confirmed fact, so the independence is auditable later.
signals:
  - Your "three sources" all phrase the fact identically — a sign they share one origin.
  - One profile corroborating itself (bio + photo + post all say the same thing) is being counted as multiple signals.
  - The fact is everywhere but you can't name two origins that arrived at it separately.
pitfalls:
  - Treating aggregator cards as independent when they all ingest the same upstream dataset.
  - Counting a news article and the social posts the article was based on as two sources.
  - Mistaking volume of mentions for weight of evidence — a viral wrong fact is still wrong.
  - Self-corroboration: one profile's own fields are not multiple witnesses.
toolsUsed: []
evidence: []
trust: trusted
relatedStrategies: [Verification by independent cross-referencing, antipattern-forcing-the-match, antipattern-over-trusting-people-search-aggregators, phase-verification, Establish a source of truth before pivoting]
tags: [verification, cognitive, corroboration, false-positive]
source: ""
---

# Antipattern: Single-source confirmation

## The tempting wrong move
You want to confirm a fact — the subject's age, their city, that a profile is theirs. You find it stated in a news article, then on two people-search cards, then in a forum post. Four sources agree. You mark it confirmed and move on.

## Why it fails
Agreement is not independence. All four "sources" may trace to a single origin: the article was written from the family's social posts, the aggregator cards both ingest the same upstream voter dataset, and the forum post is quoting the article. That's **one source wearing four hats**. The same trap operates inside a single profile — when a bio, a photo caption, and a pinned post all say the same thing, that's the profile corroborating *itself*, which is one signal, not three. Count the echoes as confirmations and you give a single original error the authority of consensus. In missing-persons work that's how a wrong age propagates into every age-filtered search, or a misidentified profile gets treated as settled and everything downstream inherits the mistake.

## The fix: trace origins, then collapse the echoes
1. **Trace.** For each supporting source, ask who *first* asserted the fact and whether the others merely copied it.
2. **Collapse.** Sources sharing one origin count as **one**. Three restatements of an article are the article.
3. **Demand a different origin.** Real corroboration comes from an *independent* path — ideally a different modality: a face match confirming what a name match suggested, a tagged check-in confirming what an address record claimed. This is the `[[Verification by independent cross-referencing]]` rule: two unrelated signals, not one signal said twice.
4. **Record the independence.** Log which genuinely separate sources support a confirmed fact, so a reviewer can audit that it wasn't an echo chamber.

## Tell
If your three sources all *say it the same way*, you probably have one source. The question is never "how many places say this?" — it's "how many *independent* ways did I arrive at this?". One is not enough; the same one repeated is still one. (This rides alongside `[[antipattern-forcing-the-match]]`: the fact you most want to be true is the one you'll most readily accept on an echo.)

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | verification |
| MP relevance | high |
| related | Verification by independent cross-referencing, antipattern-forcing-the-match |
