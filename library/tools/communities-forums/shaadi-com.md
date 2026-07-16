---
id: shaadi-com
name: Shaadi.com
description: Use when you have a `name`, `dob`, or partial details of a South-Asian subject and want a matrimonial profile — returns a `social-profile` with photos, community, city and family details.
url: https://www.shaadi.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a subject's matrimonial (marriage-seeking) profile in the Indian/South-Asian community, rich in personal and family detail.
selectorsIn:
- name
- dob
selectorsOut:
- social-profile
- image
- physical-description
- associate
status: live
pricing: freemium
costNote: Free to register and browse/search profiles; contacting members and viewing some details requires a paid membership.
opsec: active
opsecNote: Profile search requires a (free) registered account, and Shaadi shows members "who viewed your profile" — viewing a subject can alert them. Use a sock-puppet account and profile; never browse from a real/attributable account. Consider that direct contact is intrusive — stay at passive viewing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A large, established matrimonial platform, but profile content is self-reported and unverified (ages, jobs, photos are routinely embellished); treat details as leads.
missingPersonsRelevance: high
coverage:
- in
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- Shaadi
- shaadi.com
tags:
- toddington
- curated-directory
- matrimonial
- south-asian
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Shaadi.com

> The largest South-Asian matrimonial network — profiles here are unusually detailed (photos, community, caste, city, family, education, income), making it a rich people-search surface for Indian-diaspora subjects.

## When to use
Your subject is from the Indian/South-Asian community and may be seeking or have sought a marriage match. You have a `name`, approximate `dob`/age, city, or community and want to find their matrimonial profile. These profiles voluntarily disclose far more than ordinary social media — recent `image`s, `physical-description`, education, occupation, hometown, and family (`associate`) details — which can corroborate identity, location, and relationships in a missing-persons case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free sock-puppet account (search is gated behind login) at https://www.shaadi.com.
2. Use the search/filters: gender, age range (from `dob`), religion/community, mother tongue, and city to narrow.
3. Browse results without expressing interest or messaging; note the profile ID, photos, and self-listed details.
4. Cross-read details (city, community, education, family) against what you already know to confirm identity.
5. Pivot: photos → reverse-image/face search; hometown/community → local records; family names (`associate`) → people-search.

## Inputs → Outputs
- **In:** `name`, approximate `dob`/age, community/city
- **Out:** matrimonial `social-profile` — `image`s, `physical-description`, education/occupation, city, family/`associate` details
- **Empty/negative result looks like:** no matching profile in the filters — the subject never used the platform, used different details, or set a private profile; absence proves nothing about their other accounts.

## Gotchas & OpSec
- Human-in-the-loop: search needs a (free) account-login; use a sock puppet, and note Shaadi surfaces profile viewers — viewing can alert the subject.
- Self-reported and often embellished — ages, jobs, and even photos may be aspirational or fake; corroborate before relying on any field.
- Some details/photos are hidden until you're a paid member or the member accepts contact — don't pay or contact unless justified; that's active and intrusive.

## Overlaps ("do both")
- Pairs with reverse-image/face tools (run the profile photos) and with other regional matrimonial/social sites — many South-Asian subjects appear on more than one matrimonial platform.

## Trust & verifiability
`trust: unverified` — a real, large platform hosting self-reported data with no identity verification; treat every profile detail as a lead to confirm, not a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shaadi-com |
| category | communities-forums |
| selectorsIn → selectorsOut | name, dob → social-profile, image, physical-description, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
