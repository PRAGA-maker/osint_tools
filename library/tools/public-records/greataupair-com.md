---
id: greataupair-com
name: GreatAuPair
description: Use when you have a `name` and suspect the subject works or seeks work in childcare/eldercare — returns a social-profile with location, job type, and photo.
url: https://www.greataupair.com/
category: public-records
path:
- public-records
bestFor: Finding a caregiver's public profile (au pair, nanny, tutor, senior-care) by browsing/searching the platform.
selectorsIn:
- name
- address
selectorsOut:
- social-profile
- geolocation
- image
status: live
pricing: freemium
costNote: Free to sign up and browse candidate/family profiles; contacting members and premium features require a paid subscription.
opsec: active
opsecNote: Browsing public listings is passive, but seeing full profiles and searching effectively needs a (free) account, which ties queries to it — use a sock-puppet account. Contacting a member notifies them, so stop at reading the profile.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate, long-running caregiver-matching marketplace; profiles are self-created by users, so names, photos, and locations are self-asserted.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
aliases:
- Great Au Pair
tags:
- professionlicensing
- Profession & Licensing Sites
- caregiver
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# GreatAuPair

> A global caregiver-matching marketplace (au pairs, nannies, tutors, senior-care, pet/house sitters) whose public member profiles can place a subject by location and occupation.

## When to use
You have a `name` and a lead that the subject is or was a caregiver — an au pair, nanny, tutor, personal assistant, or senior-care worker — or is a family that hires them. GreatAuPair members create public-facing profiles with a photo, first name, city/country, availability, and a bio, which can confirm a subject's location and line of work or generate a lead where mainstream people-search comes up empty. Especially useful for young people abroad on au-pair placements.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.greataupair.com/ and use "Find an Au Pair" / "Find a Job" to browse listings, filtered by country/region and job type.
2. Create a **free sock-puppet account** if search/profile view is gated; browse candidate or family showcases.
3. Open a matching profile: read the photo, first name, location, languages, availability, and bio for corroborating detail.
4. Do **not** message the member (that notifies them and burns your cover). Screenshot the public profile instead.
5. Pivot: a photo → reverse-image search; a city + first name + bio detail → cross-reference with social profiles.

## Inputs → Outputs
- **In:** `name` (usually first name + location) or an `address`/region to browse
- **Out:** `social-profile` (member profile), `geolocation` (stated city/country), `image` (profile photo)
- **Empty/negative result looks like:** no matching profile in the searched region/job type — the subject may not use this platform, or the profile is set private/expired. Absence is not disproof.

## Gotchas & OpSec
- Profiles are self-asserted; treat name, age, photo, and location as claims to corroborate.
- Full member details and contact require a paid subscription; the free tier is enough to view public profiles and photos.
- OpSec: use a sock-puppet account; contacting a member is active and alerts them.

## Overlaps ("do both")
- Pairs with mainstream people-search and social enumeration — this reaches a niche occupational population (caregivers, often expats) those may miss.

## Trust & verifiability
`trust: community` — an established, legitimate marketplace, but every profile field is user-supplied; verify before relying on it as identity evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | greataupair-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address → social-profile, geolocation, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial) |
