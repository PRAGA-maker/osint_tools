---
id: spark-com
name: Spark.com
description: Use when a subject may use a relationship-oriented dating site — search Spark by area/age/interests to surface a profile photo, bio, and approximate location.
url: https://spark.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a subject's profile on a serious-relationship dating site (photo, age, approximate city, self-described traits).
input: Profile details, preferences, location, compatibility filters
output: Recommended/searched profiles with photos, age, approximate location, and bio text
selectorsIn: [name, username, geolocation, image, dob]
selectorsOut: [username, image, geolocation, physical-description, dob]
status: unknown
pricing: freemium
costNote: Free to register and browse; messaging/visibility typically behind a paid tier. No payment needed for basic OSINT viewing.
opsec: active
opsecNote: Browsing requires a logged-in account and may register you as a profile visitor. Use a sock-puppet account and assume the subject could be alerted that someone viewed them.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Spark.com is a known relationship-dating brand (historically a Spark Networks property), but its current liveness/operator is uncertain — set status unknown and verify before relying on it.
missingPersonsRelevance: high
coverage: [us]
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: [American Singles]
tags: [dating, profiles, relationships]
source: arf-seed
lastVerified: ''
enrichment: full
---

# Spark.com

> Relationship-oriented dating site — useful for surfacing a subject's dating profile (photo, age, area, self-description) on a compatibility-based platform. (Current operating status uncertain.)

## When to use
You suspect the subject uses serious-relationship dating and you have a `username`, approximate age (`dob`), `geolocation`, or a photo. Good for a recent self-photo, self-reported `physical-description`, and an approximate city. In missing-persons work this can reveal recent activity, relocation, or a new partner.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register/sign in with a sock-puppet account (browsing requires login).
2. Use search/compatibility filters: set location, age range, and interests; if a `username` lookup exists, try it, otherwise match on age + location + photo.
3. Open candidate profiles for photo, age, approximate location, "last active", and bio.
4. Pivot: run the profile `image` through reverse-image/face search; compare a reused handle and bio details to other social accounts.

## Inputs → Outputs
- **In:** `username`, `name`, `geolocation`, `image`, approximate `dob`/age
- **Out:** `username`, profile `image`, approximate `geolocation`, self-reported `physical-description`, age/`dob`
- **Empty/negative result looks like:** no matching profile, or — if the platform has wound down — a thin/empty member base; treat absence cautiously and confirm the site is still active.

## Gotchas & OpSec
- Human-in-the-loop: account login required.
- OpSec: active. Viewing profiles can flag you as a visitor. Use a dedicated sock puppet with a neutral photo.
- Liveness uncertain: verify the site still operates before drawing conclusions from empty results.

## Overlaps ("do both")
- Pairs with broader dating-profile search ([[plenty-of-fish-com]]) and reverse-image/face search to confirm identity.

## Trust & verifiability
`trust: unverified` — recognizable dating brand but current operator/availability not confirmed; status set to unknown pending verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spark-com |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username, geolocation, image, dob → username, image, geolocation, physical-description, dob |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
