---
id: over-trusting-people-search-aggregators
name: antipattern-over-trusting-people-search-aggregators
description: Use as a guardrail before you treat a people-search result as fact — aggregators merge, stale, and mis-attribute records, so an address or relative they print is a lead to corroborate, never a confirmed datum.
type: antipattern
phase: enrichment
pivotFrom: [name, phone, address]
pivotTo: [address, associate, phone]
summary: People-search aggregators (TruePeopleSearch, US Phone Book, Spokeo-class sites) present a clean, confident card — relatives, addresses, phones — that *looks* authoritative. But that card is stitched together from heterogeneous public datasets of different ages and qualities, and the merge logic routinely fuses two same-name strangers, carries addresses years out of date, and lists "relatives" who are really co-occurrences in a dataset. Taking the card at face value imports all of that error into your case at once. In a missing-persons context this manufactures a confident wrong household, a wrong relative to contact, or a wrong city to search.
missingPersonsRelevance: high
whenToUse: Any time a people-search engine returns a relative, address, or phone you're about to act on, link into a flag, or hand to law enforcement.
steps:
  - Treat every field on the card as a CANDIDATE keyed to a name, not a confirmed fact about your subject.
  - Check the merge — does the card mix ages, cities, or middle names that can't all be one person? That's two people fused.
  - Date the record — aggregators rarely show recency; an address can be a decade stale and useless as a current search anchor.
  - Corroborate each kept field against an independent source (a social profile's own city, a tagged check-in, a second records source) before promoting it.
  - Note the source and the corroboration in the report so a reviewer sees it was a people-search lead, not ground truth.
signals:
  - You're about to submit a relative or address flag sourced from one aggregator card with no second signal.
  - The card lists relatives whose ages or locations don't cohere into a single real family.
  - You're searching a city solely because an aggregator printed it, with no fresh activity tying the subject there.
pitfalls:
  - "TruePeopleSearch says they're related, so they're related" — the link may be a dataset co-occurrence, not kinship.
  - Anchoring the whole geographic search on a stale address the subject left years ago.
  - Using a US-centric aggregator for an international subject and trusting its empty or wrong result.
  - Letting one merged card's wrong middle name or DOB propagate into every downstream pivot.
toolsUsed: [TruePeopleSearch, US Phone Book]
evidence: []
trust: trusted
relatedStrategies: [antipattern-forcing-the-match, antipattern-single-source-confirmation, Corroborate relatives and connections with people-search before submitting, phase-verification, enumeration-is-not-validation]
tags: [people-search, public-records, enrichment, cognitive, verification]
source: ""
---

# Antipattern: Over-trusting people-search aggregators

## The tempting wrong move
A people-search engine hands you a tidy card: full name, current address, three phone numbers, five relatives. It looks like the answer. So you lift the address as the subject's home, the top "relative" as family to investigate, and a phone as theirs — and you build forward on all of it.

## Why it fails
That card is not a record; it's a *merge*. Aggregators stitch together voter files, marketing data, old court records, and scraped social data of wildly different ages and qualities, then guess that they describe one person. The merge logic regularly fuses two same-name strangers into a single card, carries an address that's a decade stale, and labels as "relatives" people who merely co-occur in a dataset. Trust the card and you import every one of those errors at once — and in this domain the failure isn't abstract: you get a confident *wrong household*, a *wrong relative to contact*, and a *wrong city to search*, each of which can waste the search and, if acted on, harm an uninvolved person.

## The fix: lead, then corroborate, then promote
1. **Lead, not fact.** Every field is a candidate keyed to a *name*, not a confirmed attribute of your *subject*. The aggregator is a pointer, not a witness.
2. **Read the merge.** If ages, cities, or middle names on one card can't all belong to one human, the card has fused two people — split them before using either.
3. **Date it.** These sites rarely surface recency. An address with no recent activity tying the subject to it is not a current search anchor.
4. **Second source, then keep.** Corroborate each kept field independently — the subject's own profile city, a tagged check-in, a second records source — exactly the `[[phase-verification]]` bar of two unrelated signals. This is the corroboration step in `[[Corroborate relatives and connections with people-search before submitting]]`, not a substitute for it.

## Tell
If your sentence is "the people-search says X, so X," stop — that's `[[antipattern-single-source-confirmation]]` wearing an authoritative-looking UI. An aggregator card is one stale, merge-prone source. It opens leads; it never closes them.

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | enrichment |
| MP relevance | high |
| related | antipattern-single-source-confirmation, phase-verification |
