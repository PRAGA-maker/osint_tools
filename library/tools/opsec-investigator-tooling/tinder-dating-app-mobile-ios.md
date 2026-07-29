---
id: tinder-dating-app-mobile-ios
name: Tinder (iOS Dating App)
description: Use when you have a subject who may be active on dating apps and want to find their Tinder profile, photos, and self-reported details — returns `social-profile`, `image`, and `physical-description`.
url: https://apps.apple.com/ca/app/tinder/id547702041
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Locating a person's dating-app presence to harvest recent photos, first name, age, distance, and volunteered bio details.
selectorsIn:
- name
- geolocation
selectorsOut:
- social-profile
- image
- physical-description
status: live
pricing: freemium
costNote: Free to install and browse within your area; discovery is limited by radius/age filters unless you pay for Tinder Plus/Gold to expand range and location.
opsec: active
opsecNote: Tinder is a live social platform — creating an account and swiping generates activity, and appearing in a target's stack can alert them. Always use a fully separate sock-puppet account, device/profile, and location. Never message the target. Screenshotting a match may be visible in some flows; assume interactions can surface.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: unverified
trustNote: Official Tinder app (Match Group); the app is legitimate, but any profile you find is self-reported and unverified.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
aliases:
- Tinder dating app
- Tinder iOS
tags:
- dating-app
- social-profile
- add-ons-apps-extensions
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Tinder (iOS Dating App)

> The largest dating app — used in OSINT as a source of recent self-published photos, first names, ages, and rough location for a subject who dates online.

## When to use
You have a `name`/first name and an approximate `geolocation` and want to check whether the subject maintains a dating presence. Tinder profiles volunteer current `image`s, age, first name, distance, and free-text bios (job, school, interests) — high-value corroboration and fresh photos when other footprints are stale. Best when you already have a location narrow enough to set the search radius.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Tinder on a clean sock-puppet device/profile with a throwaway account **not** linked to your real identity.
2. Set the app's location to the subject's area (Tinder Passport / device location on the sock device) and set the age/gender filters to match.
3. Swipe through the stack looking for the subject; read the bio, note photos, first name, age, and any linked Instagram/Spotify.
4. Capture only what's needed and stop — do not match or message.
5. Pivot: photos feed reverse-image search; a linked Instagram/Spotify handle feeds username OSINT; a workplace/school in the bio feeds people-search.

## Inputs → Outputs
- **In:** `name` (first name) + `geolocation`
- **Out:** `social-profile` (Tinder + any linked handles), `image` (recent photos), `physical-description`, plus age/first-name/bio detail
- **Empty/negative result looks like:** subject never appears in the stack — could mean no account, out of your set radius/age band, already swiped past, or hidden; absence is not proof of no account.

## Gotchas & OpSec
- **Active and potentially visible**: swiping right on the target can create a match and notify them. Keep to left-swipes/observation; never engage.
- Discovery is bounded by radius, age, and the day's card queue — you may simply never be shown the person even if they're active.
- Everything is self-reported: names, ages, and jobs can be false; treat photos as the most reliable element and verify via reverse-image search.
- Requires a phone-number-verified login — use a burner number, not your own.

## Overlaps ("do both")
- Pair with reverse-image search and username-enumeration tools — Tinder surfaces the photos and handles; those confirm identity and connect the dating profile to the subject's wider footprint.

## Trust & verifiability
`trust: unverified` — the app itself is the official Match Group product, but individual profiles are entirely self-authored and unvetted, so anything found must be independently corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tinder-dating-app-mobile-ios |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, geolocation → social-profile, image, physical-description |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
