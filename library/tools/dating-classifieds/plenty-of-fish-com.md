---
id: plenty-of-fish-com
name: Plenty Of Fish.com
description: Use when a subject may have a dating profile — search POF by username/area/age to surface a photo, self-description, and approximate location.
url: https://www.pof.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a subject's dating profile (photo, age, approximate city, self-described traits) on a large free dating platform.
input: Username, age range, location, profile filters
output: Matching/suggested profiles with photos, age, approximate location, and bio text
selectorsIn: [username, name, geolocation, image, dob]
selectorsOut: [username, image, geolocation, physical-description, dob]
status: live
pricing: freemium
costNote: Free to create an account and browse/search profiles; premium (Match Group) adds messaging/visibility features not needed for basic OSINT viewing.
opsec: active
opsecNote: Requires a logged-in account to browse; viewing a profile can mark you as a visitor and POF nudges users about who viewed them. Use a sock-puppet account and assume the subject may be alerted.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: POF is a large, real Match Group dating platform; entry reasoned from known function, not re-verified. Username-based search is limited by the platform.
missingPersonsRelevance: high
coverage: [global]
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: [POF, PlentyOfFish]
tags: [dating, profiles, match-group]
source: arf-seed
lastVerified: ''
enrichment: full
---

# Plenty Of Fish.com

> Large free dating platform (Match Group) — useful for surfacing a subject's dating profile, photos, age, and approximate location when other channels go cold.

## When to use
You suspect the subject uses online dating and you have a `username`, an approximate age (`dob`), `geolocation`, or a photo (`image`). Good for pulling a recent self-photo, a self-described `physical-description`, and a city. In missing-persons work, a dating profile can reveal recent activity, a new partner (`associate`), or a relocation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create/sign in with a sock-puppet account (browsing requires login).
2. Use search filters: set the location, age range, and gender; refine by keywords. If you have a `username`, try the username/profile lookup — note POF's direct username search is limited, so age+location+photo matching is often the practical path.
3. Open candidate profiles for photo, age, approximate distance/city, "last online", and bio text.
4. Pivot: run the profile `image` through reverse-image/face search; compare bio details and a reused handle against other social profiles.

## Inputs → Outputs
- **In:** `username`, `name`, `geolocation`, `image`, approximate `dob`/age
- **Out:** `username`, profile `image`, approximate `geolocation`, self-reported `physical-description`, age/`dob`
- **Empty/negative result looks like:** no profile matching the filters, or many look-alikes — a single photo match is not confirmation without corroboration.

## Gotchas & OpSec
- Human-in-the-loop: account login required; expect occasional verification challenges.
- OpSec: active. Viewing profiles can surface you in the subject's "viewed me" list. Use a dedicated sock puppet, neutral photo, and assume the subject may be notified.
- Location is approximate; profiles can be stale or fake.

## Overlaps ("do both")
- Pairs with reverse-image/face search to confirm the person, and with username-pivot tools to link the dating handle to other accounts.

## Trust & verifiability
`trust: community` — real, well-known platform; entry reasons from documented behavior rather than fresh verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | plenty-of-fish-com |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name, geolocation, image, dob → username, image, geolocation, physical-description, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
