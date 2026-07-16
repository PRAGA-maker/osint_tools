---
id: tinder-2
name: Tinder
description: Use when you have a subject's approximate location and rough identity and want to find their dating-app profile within a radius — returns social-profile, image, physical-description and approximate geolocation.
url: https://www.gotinder.com
category: social-networks
path:
- social-networks
bestFor: Locating a subject's Tinder dating profile by browsing within their geographic area and age band; extracting photos, bio and approximate distance.
selectorsIn:
- name
- image
selectorsOut:
- social-profile
- image
- physical-description
- geolocation
status: live
pricing: freemium
costNote: Free to create an account and swipe within limits; paid tiers (Tinder+/Gold/Platinum, and "Passport") unlock changing your location to browse another city and remove daily swipe caps.
opsec: active
opsecNote: Tinder is fully interactive. You must create an account and appear in the local swiping pool yourself; "liking" or matching the subject notifies them and exposes your puppet profile. Use a convincing sock-puppet account with puppet photos and a burner number, browse (do not match) the target, and be aware your set location can leak your own approximate area.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: Mainstream dating platform (Match Group); profiles are self-created, lightly verified at best, so identity and photos are not guaranteed genuine.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Tinder
- gotinder.com
tags:
- major-social-networks
- dating
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- look-by-username-replace-username-in-this-case-mark
- tinder-usernames
---

# Tinder

> The dominant location-based dating app — not searchable by name, but browseable within a geographic radius, so it can place a subject's dating profile, photos and rough location.

## When to use
You have a subject you believe uses dating apps, and you know their approximate location and roughly what they look like or their age. Tinder has no name search — you discover people by swiping through a pool filtered by distance, age and gender near a chosen location. Reach for it to confirm a subject maintains a dating profile, harvest additional `image`s (often different from their other socials), read a self-written bio, and get an approximate `geolocation` (Tinder shows distance from your set position).

## How to use it (`bestInteractionPattern`: mobile-app)
1. Create a **sock-puppet** Tinder account (burner phone number, puppet photos) — never your own.
2. Set the app's location to the subject's suspected area (a paid "Passport" feature lets you relocate to another city); set the age/gender/distance filters to match.
3. Swipe through the local pool looking for the subject; match on photos, first name (Tinder shows first name only), and age.
4. When you find them, read the bio and photos and note the displayed distance (`geolocation`) — but do NOT swipe right/match, which would alert them.
5. Extract photos (`image`), any linked Instagram/Spotify, and self-described details (`physical-description`, interests).
6. Pivot: photos feed reverse-image search; a linked Instagram/username feeds cross-platform search.

## Inputs → Outputs
- **In:** approximate location + `name`/`image` to recognise the subject (no direct search)
- **Out:** `social-profile` (Tinder profile), `image` (photos), `physical-description` (age, bio, linked interests), `geolocation` (approximate distance from your set location)
- **Empty/negative result looks like:** you never encounter the subject in the swipe pool — expected, since you only see a filtered local subset and they may be hidden, inactive, or outside your filters. Absence proves nothing.

## Gotchas & OpSec
- **No search:** discovery is radius-and-filter browsing only; finding a specific person is slow and probabilistic.
- **Active exposure:** you are a real participant in the local pool; matching notifies the target. Stay in "look, don't touch" mode and use a disposable puppet.
- Self-set location can reveal your own approximate whereabouts to others; distance figures are coarse and manipulable.

## Overlaps ("do both")
- Pairs with `[[meetme]]` and reverse-image tools — check multiple location-based dating/social apps for the same person, and run any harvested photo through reverse-image search to link identities.

## Trust & verifiability
`trust: community` — a mainstream platform, but profiles are self-asserted and minimally verified; confirm any match with photo analysis and other selectors before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tinder-2 |
| category | social-networks |
| selectorsIn → selectorsOut | name, image → social-profile, image, physical-description, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
