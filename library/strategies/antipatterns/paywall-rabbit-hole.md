---
id: paywall-rabbit-hole
name: antipattern-paywall-rabbit-hole
description: Use as a guardrail around people-search sites — burning time and money chasing teaser results behind a paywall when free pivots would have answered the same question.
type: antipattern
phase: triage
pivotFrom:
- name
- phone
- email
- address
pivotTo: []
summary: People-search engines dangle a teaser — "we found 3 addresses and 5 relatives for this person!" — then wall the actual data behind a payment. The rabbit hole is letting that teaser pull you into paying, re-paying across competing sites, and chasing aggregated public records that are often stale, mismatched, or freely available elsewhere. It burns the two scarcest resources (time and money) on low-confidence data, and it's especially seductive in thin-selector cases where it feels like the only lead. Exhaust free, passive pivots first.
missingPersonsRelevance: medium
whenToUse: Any time a people-search site shows a teaser and asks for payment, especially when you're stuck.
steps:
- Recognize the teaser pattern — a count of "results" with the data itself blurred behind a paywall is a sales funnel, not a finding.
- Run the free pivots first — social search, username enumeration, reverse image, free public-records sites often answer the same question for free.
- Don't pay to confirm a guess — paying to "check" an unverified candidate is forcing-the-match with a credit card.
- Treat any paid aggregate as a CANDIDATE — these records are frequently stale, co-mingled, or wrong; verify independently.
- Time-box people-search entirely — if free routes are exhausted, decide deliberately whether one paid lookup is worth it, then stop.
signals:
- You're about to enter card details to "see the full report" on an unverified lead — stop.
- You've opened your third competing people-search site for the same person.
pitfalls:
- Paying repeatedly across competing sites for the same recycled aggregate data.
- Trusting paid records as fact — aggregators mismatch people and lag reality by years.
- Defaulting to paid lookups in a thin-selector case instead of working the social/image breadth first (see `[[playbook-thin-selectors-name-city]]`).
toolsUsed: []
evidence: []
trust: trusted
relatedStrategies:
- phase-triage
- pattern-breadth-before-depth
- pivot-name-to-accounts
- playbook-thin-selectors-name-city
tags:
- cognitive
- cost
- people-search
- time-management
source: ''
---

# Antipattern: Paywall rabbit hole

## The tempting wrong move
A people-search site tells you it found "3 current addresses, 5 relatives, 2 phone numbers" for your subject — then blurs them and asks for $1.99 (which quietly becomes a subscription). You're stuck, this looks like the answer, so you pay. The data is thin, so you try a competitor. And another. An hour and several charges later you have a pile of stale, half-matching records.

## Why it fails
The teaser is a **sales funnel, not a finding**. The "3 addresses, 5 relatives" count is engineered to make you pay; it says nothing about whether the data is current, correct, or even the right person. Aggregator records are notoriously **stale** (years behind), **co-mingled** (relatives and namesakes merged), and **recycled** (the same public-records feed resold across competing sites, so paying twice buys the same data). You spend the two scarcest resources — **time and money** — to buy low-confidence data you then still have to verify. And paying to "confirm" an unverified candidate is `[[antipattern-forcing-the-match]]` with a credit card: you've now got a sunk cost pushing you to believe it.

## Why it's especially seductive when stuck
In a thin-selector case — a name and a city, nothing more — the paywall *feels* like the only door. That's exactly when the funnel works best. But the higher-yield moves are almost always the free, passive ones you haven't exhausted: social search, username enumeration, reverse image, free public-records portals. See `[[playbook-thin-selectors-name-city]]`.

## The fix
1. **Free and passive first** — `[[pattern-breadth-before-depth]]` applies to money too: spend free pivots before paid ones. A handle enumeration or reverse image search often answers the same question the paywall is teasing.
2. **Never pay to check a guess.** A paid lookup is for a *confirmed* lead you need to extend, not to validate a candidate.
3. **Treat any paid aggregate as a candidate** and verify it independently — it's a lead, not a fact.
4. **Time-box people-search.** Decide up front how much (if any) paid lookup is worth, do it deliberately, and stop. The rabbit hole is the *unbounded* chase across sites.

## Tell
If you're entering card details to "see the full report" on a lead you haven't independently confirmed — or you've opened your third people-search tab for the same person — you're in the hole. Back out to the free breadth.

---
## Metadata
| field | value |
|---|---|
| type | antipattern |
| phase | triage |
| MP relevance | medium |
| related | pattern-breadth-before-depth, playbook-thin-selectors-name-city |
