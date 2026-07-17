---
id: zoosk
name: Zoosk
description: Use when you suspect a subject has a dating profile and have a `name`/`username`/`image` — Zoosk is a large mainstream dating app whose public-facing profiles may confirm handles, photos and rough location.
url: https://www.zoosk.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Checking a large mainstream dating platform for a subject's profile (photos, age, area, reused handle).
selectorsIn:
- name
- username
- image
selectorsOut:
- social-profile
- image
- geolocation
status: live
pricing: freemium
costNote: Free to create an account and browse to a degree; messaging and some search/filtering need a paid subscription. Meaningful search requires being logged in.
opsec: active
opsecNote: Dating-site search is ACTIVE — you generally must register and browse, and Zoosk shows "who viewed you," so visiting a profile can notify the target. Always use a sock-puppet account with a non-attributable photo/email, and expect that viewing may be visible.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Zoosk is a real, large dating platform, but any given profile is self-created and unverified; identity and photos may be false or catfished.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- zoosk.com
tags:
- dating
- identity
- person-search
source: metaosint
lastVerified: '2026-07-17'
enrichment: full
---

# Zoosk

> A large mainstream dating app — worth checking when a subject may date online, since a profile can confirm a reused handle, current photos, age and general area.

## When to use
You're building a picture of a subject who may use dating apps, and you have a `name`, a `username`/handle they reuse, or a face `image` to match. Dating profiles are valuable OSINT: they carry recent self-chosen photos (good for reverse-image pivots and face matching), a stated age/`dob`-range, a general location (`geolocation`), and lifestyle details — and people often recycle the same handle and photos across platforms. Zoosk is one of the larger, longer-running apps, so it's a reasonable one to check alongside the bigger players.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a **sock-puppet** Zoosk account (burner email, non-attributable photo, location near the search area) — meaningful browsing/search needs a login.
2. Use search/filters (age, location, gender) to narrow toward the subject; the free tier limits filtering, so you may be browsing.
3. Compare candidate profiles against what you know — photos (run them through reverse-image search), handle, age, area, phrasing that matches other profiles.
4. Do **not** message from the sock puppet unless your engagement authorises contact; remember Zoosk surfaces profile views to users.
5. Pivot: profile photos → reverse-image/face tools; reused handle → cross-platform username tools; stated area → geolocation.

## Inputs → Outputs
- **In:** `name`, `username`, or a face `image`
- **Out:** candidate `social-profile` (photos `image`, age range, general `geolocation`, bio details)
- **Empty/negative result looks like:** no plausible match — the subject may not use Zoosk (check other apps), may have paused/hidden the profile, or may be outside your account's search radius. Absence is weak evidence given how gated dating search is.

## Gotchas & OpSec
- **Active + notifying:** login required, and profile views can alert the target — sock puppet is mandatory; assume visits may be seen.
- Profiles are self-created and unverified — photos may be stolen/old, details fabricated or catfished. Corroborate before trusting.
- Real search power is behind a paywall; the free tier is limited. Weigh whether a subscription is worth it versus checking more platforms.

## Overlaps ("do both")
- Check multiple dating platforms, not just one — coverage barely overlaps between apps. Pair with reverse-image/face tools on any profile photo and with username tools on a reused handle.

## Trust & verifiability
`trust: unverified` — Zoosk the platform is legitimate and sizeable, but individual profiles are self-asserted and unverified. Treat a match as a lead requiring photo/handle corroboration, never as confirmed identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zoosk |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username, image → social-profile, image, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
