---
id: bumble
name: Bumble
description: Use when you have an `image`, first `name`, or `geolocation` and want to check for a subject's profile on Bumble's location-based dating app.
url: https://bumble.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Locating a dating profile on a large location-based app (women-message-first)
selectorsIn:
- image
- name
- geolocation
selectorsOut:
- social-profile
- physical-description
- geolocation
status: live
pricing: freemium
costNote: Free to swipe/match; Bumble Boost/Premium add filters, spotlight, and see-who-likes-you.
opsec: active
opsecNote: Requires an account; profiles surface by location and your swipes can result in matches/visibility. Bumble shows only first names and approximate distance.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: mobile-app
trust: unverified
trustNote: Bumble is a real, major dating app; per-subject presence and profile accuracy are case-specific and unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- dating
- arf-seed
source: arf-seed
lastVerified: ''
enrichment: full
---

# Bumble

> A large location-based dating app (women message first) — useful for confirming a subject's photos and approximate area, but profiles expose only a first name and rough distance.

## When to use
Use it when you have a profile `image`, a first `name`, and an approximate `geolocation`, and want to check whether the subject is active on Bumble. Value is mainly photo/`physical-description` confirmation and rough location placement; Bumble does not expose surnames or handles, so it is corroborating rather than identifying.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Bumble and register a sock-puppet account; set discovery filters (age, distance) and location to the subject's suspected area.
2. Swipe/browse and watch for a profile whose photos match your subject; note first name, age, and listed distance.
3. Avoid right-swiping the subject (that creates a match/notification); screenshot for comparison only.
4. Pivot: confirmed photo → reverse-image search to recover a full identity Bumble withholds.

## Inputs → Outputs
- **In:** `image`, first `name`, `geolocation`
- **Out:** `social-profile`, `physical-description`, approximate `geolocation`
- **Empty/negative result looks like:** profile never appears in your stack (location/filters too narrow or subject inactive) — absence is weak evidence given algorithmic surfacing.

## Gotchas & OpSec
- Human-in-the-loop: account required; advanced filters paywalled.
- OpSec: active — swiping can create matches and notify the subject; never message them. Use a clean puppet account; be aware location is core to surfacing.

## Overlaps ("do both")
- Pairs with `[[hinge]]`, `[[badoo]]`, and reverse-image search — overlapping audiences and the photo pivot recover what Bumble hides.

## Trust & verifiability
`trust: unverified` — Bumble is real and widely used, but you cannot confirm a subject's presence without observing a matching profile, and its first-name-only design limits attribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bumble |
| category | dating-classifieds |
| selectorsIn → selectorsOut | image, name, geolocation → social-profile, physical-description, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes |
