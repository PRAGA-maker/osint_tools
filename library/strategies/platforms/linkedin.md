---
id: linkedin
name: platform-linkedin
description: Use when the subject is an adult with a professional footprint — strong for real name, employer, education, and location, but profile views are NOTIFIED by default, making it an opsec minefield.
type: technique
phase: pivot
pivotFrom: [name, social-profile, employer-org]
pivotTo: [name, employer-org, geolocation, associate, image]
platforms: [linkedin]
summary: LinkedIn is the best platform for an adult's real name, employer, education, career timeline, and metro-area location — all under real-name culture that aids disambiguation. It's weak for minors and people outside the professional world. The defining opsec hazard is that LinkedIn NOTIFIES users when you view their profile by default, so a careless logged-in look tips the subject off. Browse via private/anonymous mode or cached/Google-indexed copies, never a traceable logged-in view of the target.
missingPersonsRelevance: medium
whenToUse: The subject is an adult likely to have a professional/educational profile.
steps:
  - Search name + employer/school/location — real-name culture and these filters make disambiguation strong (`[[pivot-name-to-accounts]]`).
  - Harvest the professional selectors — current/past employers, education, metro-area location, career timeline.
  - Read the connection graph for colleagues and classmates as associates (passively).
  - Use Google-indexed or cached profile copies — view the data WITHOUT a notified profile view.
  - Pull the profile photo for a face — a clear, real-name-attached headshot is a strong face-search seed.
signals:
  - Name + employer + metro converge on one specific professional identity.
  - The headshot (real-name-attached) confirms a face you had from elsewhere.
pitfalls:
  - Profile views are notified by default — a logged-in look tips off the subject (`[[antipattern-contaminating-the-subject]]`).
  - Weak/absent for minors and non-professionals — don't expect a footprint for a teen.
  - Career data can be stale or aspirational — date employers/titles against the timeline.
toolsUsed: [linkedin-search, google-cache, rocketreach]
evidence: []
trust: trusted
relatedStrategies: [pivot-name-to-accounts, antipattern-contaminating-the-subject, pivot-image-to-face, phase-opsec]
tags: [platform, linkedin, professional, real-name, opsec-sensitive]
source: ""
---

# Platform: LinkedIn

## What's publicly enumerable
LinkedIn is the strongest platform for an **adult's professional identity**: real name, current and past **employers**, **education**, **career timeline**, and **metro-area location** — all under real-name culture that makes disambiguation easy. The trade-off: it's **weak or absent for minors** and anyone outside the professional world, so it's a `medium`-relevance, situational tool, not a first stop in a runaway-teen case.

## The good pivots
- **Name + employer/school/location search** — excellent disambiguation (`[[pivot-name-to-accounts]]`).
- **Professional selectors** — employer (`employer-org`), education, and a metro location, plus a career timeline.
- **Connection graph** — colleagues and classmates as associates.
- **Headshot → face** — a clear, real-name-attached photo is a high-quality face-search seed (`[[pivot-image-to-face]]`).

## Gotchas
- **Staleness** — career data can be outdated or aspirational; date it against the timeline.
- **Minor/non-professional gaps** — expect nothing for a teen.

## OpSec (the defining hazard)
**LinkedIn notifies users by default when you view their profile.** A single careless logged-in look at the subject tips them off — the most common LinkedIn contamination (`[[antipattern-contaminating-the-subject]]`). Mitigate by viewing through **private/anonymous browsing mode** (LinkedIn's setting), **Google-indexed or cached** copies that don't trigger a view notification, or a sock puppet — never a traceable logged-in view of the target. This is the platform where the *act of looking* is itself the risk. `[[phase-opsec]]`.

---
## Metadata
| field | value |
|---|---|
| type | technique |
| platform | linkedin |
| MP relevance | medium |
| tools | linkedin-search, google-cache, rocketreach |
