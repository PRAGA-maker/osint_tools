---
id: thin-selectors-name-city
name: playbook-thin-selectors-name-city
description: Use when all you have is a real name and a city — an ordered sequence for the hardest common case, built around disambiguation and avoiding the paid-people-search trap.
type: playbook
phase: triage
pivotFrom: [name, geolocation]
pivotTo: [social-profile, username, image, associate, any]
summary: A name plus a city is the thinnest realistic seed — the name isn't unique and the city only narrows it. The whole case is disambiguation: combine the two into searches that filter the crowd, derive candidate usernames and find a face to break collisions, and resist the people-search paywall that feels like the only door. Expectations should be set honestly at intake — this case type has a real chance of not converging, and recognizing that early prevents hours lost in paid dead-ends.
missingPersonsRelevance: high
whenToUse: Your only workable selectors are a real name and a location (city/region), with no photo, handle, email, or phone.
steps:
  - Set expectations at triage — a name+city may not converge; say so and plan a time-box (`[[phase-triage]]`).
  - Combine name + city in every search — directory platforms (Facebook/LinkedIn) let you filter by location, which is your main disambiguator (`[[pivot-name-to-accounts]]`).
  - Add any second disambiguator you can infer — likely age, school, employer, a relative's surname — each one collapses the crowd further.
  - Derive candidate usernames from the name and enumerate them — a reused handle breaks the name collision (`[[username-reuse-enumeration]]`).
  - Find a face early — once you have any candidate photo, it becomes the strongest disambiguator across the remaining name-matches.
  - Avoid the paid-people-search rabbit hole — work the free social/image breadth first; pay deliberately or not at all (`[[antipattern-paywall-rabbit-hole]]`).
signals:
  - A name-match in the right city also matches a second disambiguator (age/school/relative) — convergence on one person.
  - A name-derived username turns out to be real and reused, breaking the collision.
pitfalls:
  - Defaulting to paid people-search because it feels like the only lead — usually the lowest-yield, highest-cost move here.
  - Forcing the first plausible name-match in the right city as the subject without a second signal (`[[antipattern-forcing-the-match]]`).
  - Not setting expectations — grinding a genuinely non-convergent case as if a break is guaranteed.
toolsUsed: [facebook-search, fastpeoplesearch, whatsmyname-web, pimeyes]
evidence: []
trust: trusted
relatedStrategies: [pivot-name-to-accounts, username-reuse-enumeration, antipattern-paywall-rabbit-hole, antipattern-forcing-the-match, phase-triage]
tags: [playbook, thin-selectors, disambiguation, name]
source: ""
---

# Playbook: Thin selectors — name + city

## When this applies
Your only workable selectors are a **real name** and a **location**, with no photo, handle, email, or phone. It's the hardest common case: the name is shared by thousands and the city only narrows the field. The entire game is **disambiguation** — filtering the crowd down to one person — and knowing when the crowd won't filter.

## Set expectations first (this is part of the playbook)
Be honest at triage: a name+city case has a real chance of **not converging**. Saying that up front, and setting a time-box, is what keeps you from the slow death of chasing paid records for hours. An honest "insufficient selectors to confirm" is a legitimate outcome, not a failure. `[[phase-triage]]`.

## The ordered sequence
1. **Combine name + city in every query.** Directory-style platforms (Facebook, LinkedIn) let you filter by location — that location filter is your primary disambiguator. `[[pivot-name-to-accounts]]`.
2. **Infer a second disambiguator.** Likely age band, a school, an employer, a relative's surname — anything. Each one collapses the remaining crowd. Two disambiguators usually get you to a handful.
3. **Derive and enumerate usernames.** Turn the name into likely handles (`first.last`, `flast`, initials+year) and run them across platforms — a reused handle cleanly breaks a name collision. `[[username-reuse-enumeration]]`.
4. **Get a face early.** The moment you have any candidate photo, it becomes the strongest discriminator across all the remaining name-matches — a face resolves what text disambiguators leave ambiguous. From there, `[[pivot-image-to-face]]` and reverse image can extend it.

## The trap to avoid
The **paid people-search rabbit hole** is most seductive exactly here, because the paywall feels like the only door when you're thin. It's usually the lowest-yield, highest-cost move. Exhaust the free social/image breadth first; if you pay at all, do it deliberately and once. `[[antipattern-paywall-rabbit-hole]]`.

And because every lead is a name-match in a plausible city, this is prime territory for `[[antipattern-forcing-the-match]]` — the first plausible hit *feels* like them. Require a second independent signal (a face, a relative, an age) before promoting anyone.

---
## Metadata
| field | value |
|---|---|
| type | playbook |
| phase | triage → pivot |
| MP relevance | high |
| tools | facebook-search, fastpeoplesearch, whatsmyname-web, pimeyes |
