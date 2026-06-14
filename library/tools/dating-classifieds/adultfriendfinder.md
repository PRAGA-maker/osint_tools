---
id: adultfriendfinder
name: AdultFriendFinder
description: Use when you have a `username`, `image`, or rough `geolocation` and want to check whether a subject maintains an adult-dating profile — search by handle, photo, or location.
url: https://www.adultfriendfinder.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Checking for an adult-dating profile by username, photo, or location
selectorsIn:
- username
- image
- geolocation
selectorsOut:
- social-profile
- username
- physical-description
status: live
pricing: freemium
costNote: Free account to browse; messaging and full search filters are largely behind a paid membership.
opsec: active
opsecNote: Viewing profiles requires an account; the platform logs your activity and may notify members of views. Use a sock-puppet account, never a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Mainstream adult-dating platform; OSINT value depends on the subject having an account and is not independently verified per-case.
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
aliases:
- AFF
tags:
- dating
- adult
- arf-seed
source: arf-seed
lastVerified: ''
enrichment: full
---

# AdultFriendFinder

> A large adult-oriented dating/hookup network where a subject may keep a profile, reachable by username, photo, or location filtering.

## When to use
Use it when you have a `username`, a profile `image`, or an approximate `geolocation` for a subject and want to confirm or discover an adult-dating presence. A matching profile can yield a `physical-description`, reused handle (`username`), partner/`associate` hints, and recent-activity signals that place the subject in a city.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a dedicated sock-puppet account (never personal) and log in.
2. Use member search to filter by username, gender/age, and location; use reverse-image checks off-platform to match the profile photo.
3. Inspect a candidate profile for reused handles, photos, distinguishing marks, and "last online" / location.
4. Pivot: feed a confirmed `username` into cross-platform enumeration and the photo into reverse-image search.

## Inputs → Outputs
- **In:** `username`, `image`, `geolocation`
- **Out:** `social-profile`, reused `username`, `physical-description`
- **Empty/negative result looks like:** no profile, or generic profiles that don't match the subject's photo/handle — common handles produce false positives, so corroborate.

## Gotchas & OpSec
- Human-in-the-loop: account login required; most search filters and all messaging are paywalled (payment-wall-partial).
- OpSec: active. Profile views can be visible to members; never contact the subject; use an isolated puppet identity, VPN, and a burner email.

## Overlaps ("do both")
- Pairs with reverse-image search and username-enumeration tools — those find the same person across mainstream platforms the dating site won't reveal.

## Trust & verifiability
`trust: unverified` — a real, well-known platform, but whether any given subject has a profile (and the accuracy of that profile) is case-specific and unverified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | adultfriendfinder |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, image, geolocation → social-profile, username, physical-description |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
