---
id: facebook
name: platform-facebook
description: Use when the subject or their family is on Facebook — strong for real names, family graphs, and older demographics; much is locked down now, so the family network is often the better entry.
type: technique
phase: pivot
pivotFrom: [name, social-profile, image, phone, email]
pivotTo: [name, associate, image, geolocation, employer-org]
platforms: [facebook]
summary: Facebook is the strongest platform for REAL NAMES and FAMILY graphs, and it skews older — so even when a young subject isn't there, their parents and relatives usually are. Privacy lockdown has reduced what's directly visible on a target's own profile, which makes network triangulation through relatives the more reliable entry. Name+location search, the friends/family graph, tagged photos, life events, and check-ins are the high-value reads. Real-name culture makes it the best name-disambiguation venue.
missingPersonsRelevance: high
whenToUse: The subject or (importantly) their family is likely on Facebook.
steps:
  - Search name + location — Facebook's real-name culture and location filter make it the best name-disambiguation venue (`[[pivot-name-to-accounts]]`).
  - Pivot to family if the subject is locked down — parents/relatives are often older Facebook users with open profiles (`[[pivot-network-triangulation]]`).
  - Read the family graph for surnames and relationships — "family" listings and tagged relatives confirm identity and expand associates.
  - Harvest tagged photos, life events, check-ins, and employer/school fields — these leak face, location, timeline, and org.
  - Try reverse-lookup pivots — a phone/email may resolve to a profile via account-recovery hints (passive, careful).
signals:
  - A relative's open profile names and tags the subject, confirming identity and surname.
  - Name + location + a tagged family member converge on one specific person.
pitfalls:
  - Subject's own profile is often fully locked — don't conclude "not on Facebook"; pivot to family.
  - Account-recovery probing can notify the subject — keep email/phone reverse-lookups passive (`[[antipattern-contaminating-the-subject]]`).
  - Common names still collide — Facebook helps disambiguation but doesn't remove it; require a second signal.
toolsUsed: [facebook-search, intelligence-x, pipl]
evidence: []
trust: trusted
relatedStrategies: [pivot-name-to-accounts, pivot-network-triangulation, antipattern-contaminating-the-subject, antipattern-forcing-the-match]
tags: [platform, facebook, real-name, family, high-yield]
source: ""
---

# Platform: Facebook

## What's publicly enumerable
Facebook's distinguishing strengths are **real names** and **family graphs**, plus an **older demographic**. Real-name culture makes it the best venue for disambiguating a name (search filters by city, school, employer). And because parents and relatives skew older — and older users lock down less — a young subject who isn't on Facebook usually still has a fully-visible family there. That family network is frequently the better entry than the subject's own (often locked) profile.

## The good pivots
- **Name + location search** — the premier name-disambiguation move (`[[pivot-name-to-accounts]]`).
- **Family triangulation** — when the subject is locked down, pivot to relatives whose open profiles name, tag, and photograph them (`[[pivot-network-triangulation]]`). The "family" listings hand you surnames and relationships directly.
- **Profile fields** — tagged photos (face), check-ins and life events (location + timeline), employer/school (`employer-org`).
- **Reverse lookups** — a phone or email can resolve to a profile via account-recovery hints; keep these **passive**.

## Gotchas
- **Lockdown** — a target's own profile is often almost entirely private now. "Nothing visible" is not "not on Facebook" — pivot to family.
- **Name collisions** persist — Facebook *aids* disambiguation but doesn't finish it; require a second signal (`[[antipattern-forcing-the-match]]`).
- **Stale data** — old life events and employers may be outdated.

## OpSec
Don't send friend requests, message, or use account-recovery flows that *email/text* the subject — those tip them off (`[[antipattern-contaminating-the-subject]]`). Browse from a clean sock puppet; Facebook's "People You May Know" can surface you to the target from a weakly-separated account. See `[[phase-opsec]]`.

---
## Metadata
| field | value |
|---|---|
| type | technique |
| platform | facebook |
| MP relevance | high |
| tools | facebook-search, intelligence-x, pipl |
