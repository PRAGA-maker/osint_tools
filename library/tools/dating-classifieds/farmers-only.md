---
id: farmers-only
name: Farmers Only
description: Use when a subject has a rural/agricultural background and you want to check for a profile on this US niche dating site by `username` or `image`.
url: https://www.farmersonly.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Checking for a rural/agricultural-community dating profile (US)
selectorsIn:
- username
- image
- geolocation
selectorsOut:
- social-profile
- physical-description
- geolocation
status: live
pricing: freemium
costNote: Free to register and browse; messaging requires a paid membership.
opsec: active
opsecNote: Requires an account to view full profiles; your puppet profile is visible. Activity is logged.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: FarmersOnly is a real US niche dating site; per-subject presence is case-specific and unverified.
missingPersonsRelevance: low
coverage:
- us
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
- niche
- rural
- arf-seed
source: arf-seed
lastVerified: ''
enrichment: full
---

# Farmers Only

> A US niche dating site for rural/agricultural communities — a targeted check when a subject's background fits that demographic.

## When to use
Use it when a subject is tied to rural/farming life in the US and you have a `username`, `image`, or a regional `geolocation` to match. It is a low-priority, niche pivot: useful precisely because of its demographic focus, not its reach.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a sock-puppet account and log in (full profile views require an account).
2. Search/browse by state/region; match photos and handles to your subject.
3. Inspect a candidate profile for self-disclosed location and a `physical-description`.
4. Pivot: confirmed photo → reverse-image search; handle → username enumeration.

## Inputs → Outputs
- **In:** `username`, `image`, `geolocation`
- **Out:** `social-profile`, `physical-description`, approximate `geolocation`
- **Empty/negative result looks like:** no match in the region; small base means absence is weak evidence.

## Gotchas & OpSec
- Human-in-the-loop: account login; messaging paywalled.
- OpSec: active — your puppet profile is visible to members; never contact the subject. (Note: viewing requires login, so this is not a purely passive lookup.)

## Overlaps ("do both")
- Pairs with mainstream apps (`[[badoo]]`, `[[bumble]]`) and reverse-image search; use this only when the rural-demographic fit is strong.

## Trust & verifiability
`trust: unverified` — a genuine niche US platform, but coverage is small and per-case results must be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | farmers-only |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, image, geolocation → social-profile, physical-description, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
