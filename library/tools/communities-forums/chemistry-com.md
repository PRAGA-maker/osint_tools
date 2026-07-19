---
id: chemistry-com
name: Chemistry.com
description: Use when you have a `username`, `name`, or `image` and want to check for a matching profile on the Chemistry.com dating site — returns a social-profile with photos and location.
url: http://chemistry.com
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a subject keeps a Chemistry.com dating profile and extracting its photos, first name, age, and location.
selectorsIn:
- username
- name
- image
selectorsOut:
- social-profile
- geolocation
status: live
pricing: freemium
costNote: Free to register and browse via personality-match results; messaging and full features are paywalled. Searching requires a (free) logged-in account.
opsec: active
opsecNote: Searching/browsing requires an account, and viewing a profile can surface a "viewed you" signal — that is ACTIVE and can alert the subject. Use a dedicated sock-puppet account, never an attributable identity, and expect activity logging.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A Match Group dating site; profiles are self-created and unverified, aliases and non-original photos are common, so treat every field as claimed.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- Chemistry
- chemistry.com dating
tags:
- dating
- social-networking
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Chemistry.com

> A Match Group dating site — check whether a subject maintains a profile here and pull its photos, first name, age, and stated location.

## When to use
You have a `username`, real `name`, or reference `image` and want to see if the subject is on Chemistry.com. A matched profile yields photos (feed to reverse-image/face search), a first name, age, and stated city/region — useful for confirming presence, current location, or a reused handle/photo across dating platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a dedicated sock-puppet account at http://chemistry.com (free registration; browsing/matching requires login).
2. Use the location/age match filters aligned to your other intel, or compare candidate profiles against a reference `image`.
3. Read the profile: photos, first name, age, stated `geolocation`, and self-description.
4. Pivot: run profile photos through reverse-image/face tools to link other accounts; a reused username feeds cross-platform enumeration; stated location narrows other searches.

## Inputs → Outputs
- **In:** `username`, `name`, or `image`
- **Out:** `social-profile` (photos, first name, description), stated `geolocation`
- **Empty/negative result looks like:** no matching profile — the subject may not use the platform or uses details you don't have; absence isn't proof.

## Gotchas & OpSec
- ACTIVE: searching needs a login and profile views may notify the owner. Never use a real account.
- Profiles are self-reported, often with aliases, approximate locations, and non-original photos — corroborate before trusting.
- Human-in-the-loop: account login required.

## Overlaps ("do both")
- Pairs with reverse-image/face search and `[[seeking-arrangement]]` — this finds the dating profile, those confirm the person and link other accounts; check multiple dating platforms.

## Trust & verifiability
`trust: community` — a real platform but entirely user-generated, unverified content; every detail is a lead to corroborate, not evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chemistry-com |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name, image → social-profile, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
