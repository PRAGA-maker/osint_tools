---
id: badoo
name: Badoo
description: Use when you have a `username`, `image`, or `geolocation` and want to find a subject's profile on one of the largest global dating/people-nearby apps.
url: https://badoo.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Locating a dating profile on a very large global "people nearby" network
selectorsIn:
- username
- image
- geolocation
selectorsOut:
- social-profile
- username
- physical-description
- geolocation
status: live
pricing: freemium
costNote: Free to register and browse nearby users; boosts, see-who-likes-you, and some filters are paid.
opsec: active
opsecNote: Requires an account; "encounters"/likes are visible to others and location is core to the product. Use a sock-puppet account and spoof/limit location carefully.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: mobile-app
trust: unverified
trustNote: Badoo is a major, real dating platform; per-subject presence is case-specific and unverified.
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

# Badoo

> One of the largest global dating / "people nearby" apps — a high-coverage place to check for a subject's profile and approximate location.

## When to use
Use it when you have a `username`, profile `image`, or an approximate `geolocation` for a subject. Badoo's large international user base and location-centric design make it useful for placing someone in an area and confirming a reused handle, photos (`physical-description`), and a rough `geolocation`.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Badoo (or use the web app) and register a dedicated sock-puppet account; set location to the subject's suspected area where the product allows.
2. Browse "Encounters"/People Nearby and search; match against the subject's known photos and handle.
3. Inspect a candidate profile for distance, last-active, photos, and self-disclosed details.
4. Pivot: confirmed photo → reverse-image search; confirmed handle → username enumeration.

## Inputs → Outputs
- **In:** `username`, `image`, `geolocation`
- **Out:** `social-profile`, reused `username`, `physical-description`, approximate `geolocation`
- **Empty/negative result looks like:** no nearby match or only generic profiles; distance is fuzzy and "last active" can be stale — corroborate before placing the subject.

## Gotchas & OpSec
- Human-in-the-loop: account required; some discovery features paywalled.
- OpSec: active — your likes/views can be visible; location is central. Never like/contact the subject; use a clean puppet account and consider a privacy-respecting device.

## Overlaps ("do both")
- Pairs with `[[bumble]]`, `[[hinge]]`, and reverse-image search — overlapping user bases mean a subject absent on one may appear on another.

## Trust & verifiability
`trust: unverified` — Badoo is a real, major platform, but whether a given subject has a profile and how current it is must be verified per case.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | badoo |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, image, geolocation → social-profile, username, physical-description, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes |
