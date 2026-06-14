---
id: tantan
name: Tantan
description: Use when an East-Asia / Chinese-diaspora subject may use a Tinder-style swipe app — surface a profile photo, age, and approximate location via geolocation-based matching.
url: https://int.tantanapp.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a subject's dating profile (photo, age, approximate area) on the leading China/Asia-focused swipe dating app.
input: Profile information, location, age/gender preferences
output: Suggested nearby matches with photos, age, distance/approximate location, and short bios
selectorsIn: [name, geolocation, image, dob]
selectorsOut: [image, geolocation, physical-description, dob]
status: live
pricing: freemium
costNote: Free to register and swipe; premium adds boosts/location change. No payment needed to view nearby profiles.
opsec: active
opsecNote: Mobile-first, location-driven matching. You must run the app from a device near the target area (or spoof location), and swiping can surface you to the subject. Use a sock-puppet device/account; assume location and behavior are logged.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: Tantan is a large, real China/Asia dating app (the "Chinese Tinder", owned by Momo); entry reasoned from known function, not re-verified. Web URL is mostly a landing page — the product is the mobile app.
missingPersonsRelevance: high
coverage: [cn, asia]
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: [探探]
tags: [dating, swipe, china, asia, mobile]
source: arf-seed
lastVerified: ''
enrichment: full
---

# Tantan

> The leading China/Asia "swipe" dating app (owned by Momo) — surfaces nearby profiles with photo, age, and approximate distance for subjects in East-Asian or Chinese-diaspora contexts.

## When to use
You suspect an East-Asia-based or Chinese-speaking subject uses swipe dating, and you have a photo (`image`), approximate age (`dob`), and a target area (`geolocation`). The app shows nearby users, so it can place a person in a locality and yield a recent self-photo and `physical-description`.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install the Tantan app on a sock-puppet device and register a sock-puppet account; the web URL is essentially a landing page.
2. Set age/gender filters and (if needed and permitted) a location near the target area; begin swiping to browse nearby profiles.
3. Inspect candidate profiles for photo, age, distance, and bio. Tantan is location-centric, so distance helps geofence the subject.
4. Pivot: run the profile `image` through reverse-image/face search; corroborate age/area against other platforms.

## Inputs → Outputs
- **In:** `image`, approximate `dob`/age, target `geolocation`
- **Out:** profile `image`, approximate `geolocation` (distance from you), self-reported `physical-description`, age/`dob`
- **Empty/negative result looks like:** no nearby match — heavily dependent on your set location; absence likely means you are not searching near the subject, not that they are absent.

## Gotchas & OpSec
- Human-in-the-loop: app install + account login; phone-number verification is common.
- OpSec: active and mobile-bound. Profiles surface to nearby users including the subject; swiping right can notify/match. Use a dedicated device/account and a neutral photo. Spoofing location may violate terms.
- The app and much of its content are oriented to Chinese-language users.

## Overlaps ("do both")
- Pairs with reverse-image/face search to confirm identity, and with other regional dating apps to widen coverage.

## Trust & verifiability
`trust: community` — large, real platform with well-documented behavior; entry reasons from known function rather than fresh verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tantan |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, geolocation, image, dob → image, geolocation, physical-description, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
