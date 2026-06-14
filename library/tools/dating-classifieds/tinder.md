---
id: tinder
name: Tinder
description: Use when a subject likely uses the dominant swipe-dating app — surface a recent photo, age, approximate location, and bio via geolocation-based discovery.
url: https://tinder.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a subject's dating profile (recent photo, age, approximate area, bio) on the most widely used swipe-dating app.
input: Profile details, preferences, geolocation (set via app/web)
output: Nearby swipe profiles with photos, age, distance/approximate location, bio, and linked Instagram/Spotify where shown
selectorsIn: [name, geolocation, image, dob]
selectorsOut: [image, geolocation, physical-description, dob, social-profile]
status: live
pricing: freemium
costNote: Free to register and swipe; Tinder Plus/Gold/Passport add features like changing location. No payment needed to view nearby profiles in your area.
opsec: active
opsecNote: Highly location- and behavior-tracked. You must be (or appear) near the target area; right-swiping can notify/match the subject. Use a sock-puppet account/device and a neutral photo; assume location and engagement are logged.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: Tinder is the dominant, real swipe-dating app (Match Group); entry reasoned from well-known function, not re-verified. Web app exists but the product is primarily mobile.
missingPersonsRelevance: high
coverage: [global]
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: [dating, swipe, mobile, match-group]
source: arf-seed
lastVerified: ''
enrichment: full
---

# Tinder

> The dominant global swipe-dating app — surfaces nearby profiles with recent photos, age, approximate distance, and sometimes linked Instagram/Spotify, useful for placing a subject in an area.

## When to use
You suspect the subject uses Tinder and you have a photo (`image`), approximate age (`dob`), and a target area (`geolocation`). Tinder shows nearby users, so it can geofence a person, yield a recent self-photo and `physical-description`, and occasionally expose a linked `social-profile` (Instagram/Spotify). Valuable in missing-persons cases for recent activity and movement.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Tinder on a sock-puppet device (or use the web app at tinder.com) and register a sock-puppet account.
2. Set age/gender filters and a search radius; your shown profiles are based on your current location, so you must be near the target area (Passport/location features cost money or may break terms).
3. Swipe/browse nearby profiles; inspect photos, age, distance, bio, and any linked Instagram/Spotify.
4. Pivot: run profile `image`s through reverse-image/face search; follow a linked Instagram handle to widen identity; use distance to refine `geolocation`.

## Inputs → Outputs
- **In:** `image`, approximate `dob`/age, target `geolocation`
- **Out:** profile `image`, approximate `geolocation` (distance), self-reported `physical-description`, age/`dob`, linked `social-profile`
- **Empty/negative result looks like:** no nearby match — strongly dependent on your set location and filters; absence usually means you are not searching near the subject, not that they are absent.

## Gotchas & OpSec
- Human-in-the-loop: app/web account login and phone verification; photo-verification prompts are common.
- OpSec: active and location-bound. Right-swiping can match and notify the subject. Use a dedicated account/device and neutral photo; do not message from a real account.
- You cannot search by name/username — discovery is purely nearby + filters.

## Overlaps ("do both")
- Pairs with reverse-image/face search to confirm identity and with [[tantan]] / [[plenty-of-fish-com]] for additional dating coverage.

## Trust & verifiability
`trust: community` — ubiquitous, real platform with well-documented behavior; entry reasons from known function rather than fresh verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tinder |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, geolocation, image, dob → image, geolocation, physical-description, dob, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
