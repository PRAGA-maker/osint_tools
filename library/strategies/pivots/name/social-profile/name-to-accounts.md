---
id: name-to-accounts
name: pivot-name-to-accounts
description: Use when you have a real name (ideally plus one disambiguator) and want the subject's social accounts — search platforms and people-search engines, then disambiguate hard because names are not unique.
type: technique
phase: pivot
pivotFrom: [name]
pivotTo: [social-profile, username, image, employer-org, associate]
platforms: [facebook, linkedin, instagram, twitter]
summary: A real name is a weak selector on its own — thousands of people share one — but a name plus a single disambiguator (city, school, employer, age, a relative) becomes workable. You search the name across platforms and people-search engines, then spend most of your effort DISAMBIGUATING the results down to the one person. The output of a confirmed profile is rich: a face, handles, associates, an employer. Names are the most common seed in thin-selector cases, which is exactly why disambiguation discipline matters most here.
missingPersonsRelevance: high
whenToUse: You hold a real name, best paired with at least one disambiguator (city, school, employer, age, relative).
steps:
  - Pair the name with a disambiguator before searching — "name + city/school/employer" filters thousands down to a handful.
  - Search the name on platforms with people-directory features (Facebook, LinkedIn) and via people-search engines.
  - Generate candidate usernames from the name (first.last, flast, initials + year) and feed them to handle enumeration (`[[username-reuse-enumeration]]`).
  - Disambiguate every candidate against your disambiguators and any face/photo you hold — discard the ones that don't fit.
  - Harvest selectors from confirmed profiles (face, handles, associates, employer) and recurse.
signals:
  - A candidate profile matches the name AND an independent disambiguator (right city + right age) — convergence.
  - A name-derived username turns out to be a real reused handle across platforms.
pitfalls:
  - Treating a name match as the person — common names guarantee collisions; a name alone is never a confirmation.
  - Searching the bare name with no disambiguator and drowning in results (this is the thin-selector trap).
  - Anchoring on a name match while ignoring a face or location that doesn't fit (see `[[antipattern-forcing-the-match]]`).
toolsUsed: [pipl, thatsthem, fastpeoplesearch, facebook-search]
evidence: []
trust: trusted
relatedStrategies: [username-reuse-enumeration, pivot-network-triangulation, antipattern-forcing-the-match, playbook-thin-selectors-name-city, antipattern-paywall-rabbit-hole]
tags: [name, social, disambiguation]
source: ""
---

# Name → Social profiles (name-to-accounts)

## The move
Turn a real name into the subject's accounts. The search is the easy 20%; the **disambiguation** is the 80%. A name returns a crowd — your job is to filter that crowd down to one person using everything else you hold.

## A name needs a disambiguator
On its own, "Sarah Johnson" is nearly useless — thousands of them. Pair it with *one* discriminating fact — a city, a school, an employer, an age, a relative's name — and the search space collapses from thousands to a handful. Always attach a disambiguator before searching; if you have none, you're in a thin-selector case (`[[playbook-thin-selectors-name-city]]`) and should plan accordingly.

## Where to search
- **Directory-style platforms** — Facebook and LinkedIn let you search by name and filter by location/employer/school, which is exactly the disambiguation you need.
- **People-search engines** — aggregate public records and surface relatives, ages, and prior cities. Useful, but watch the `[[antipattern-paywall-rabbit-hole]]` — most "free" results tease you toward a paid wall.
- **Name → username** — derive likely handles (`first.last`, `flast`, initials+year) and run them through `[[username-reuse-enumeration]]`; people often base handles on their real name.

## Disambiguate, then harvest
Every candidate is matched against your disambiguators and any face you hold, and the non-fitting ones are discarded — not explained away. Anchoring on the name while waving off a wrong city or face is `[[antipattern-forcing-the-match]]`, and names are where that's most tempting because the partial match feels so close. Once a profile is confirmed, harvest it: face, handles, associates, employer — then recurse.

---
## Metadata
| field | value |
|---|---|
| type | technique |
| pivot | name → social-profile, username, image, employer-org, associate |
| platforms | facebook, linkedin, instagram, twitter |
| MP relevance | high |
| tools | pipl, thatsthem, fastpeoplesearch, facebook-search |
