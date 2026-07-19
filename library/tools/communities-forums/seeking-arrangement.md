---
id: seeking-arrangement
name: Seeking (SeekingArrangement)
description: Use when you have a `username`, `name`, or `image` and want to check for a matching profile on the Seeking dating platform — returns a social-profile with photos and location.
url: https://www.seeking.com
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a subject maintains a profile on the Seeking ("sugar dating") platform and extracting its photos, location, and self-description.
selectorsIn:
- username
- name
- image
selectorsOut:
- social-profile
- geolocation
status: live
pricing: freemium
costNote: Free to register and browse profiles; messaging and some features are paywalled. Profile search requires a (free) logged-in account.
opsec: active
opsecNote: Searching requires an account, and browsing a profile can trigger a "viewed you" notice depending on settings — that is ACTIVE and can alert the subject. Use a dedicated sock-puppet account, never a real or attributable identity, and expect the platform to log your activity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A large commercial dating platform; profiles are self-created and unverified, and people commonly use aliases and stock or altered photos, so treat everything as claimed, not confirmed.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- SeekingArrangement
- Seeking.com
tags:
- dating
- social-networking
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Seeking (SeekingArrangement)

> The "sugar dating" platform formerly branded SeekingArrangement — a place to check whether a subject keeps a dating profile and to pull its photos, stated location, and self-description.

## When to use
You have a `username`, real `name`, or a reference `image` and you want to see if the subject is active on Seeking. A matched profile yields photos (feed them to reverse-image and face tools), a stated city/region, age, and lifestyle claims — useful for confirming presence, current location, or a reused handle/photo across platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a dedicated sock-puppet account at https://www.seeking.com (registration is free; searching requires being logged in).
2. Search by username/handle, or browse the location/age filters that match your other intel; for an `image`, compare candidate profiles against your reference photo.
3. Read the profile: photos, stated `geolocation` (city/region), age, and free-text description.
4. Pivot: run profile photos through `[[reverse-image]]`/face search to link to other platforms; a reused username feeds cross-platform enumeration; stated location narrows other searches.

## Inputs → Outputs
- **In:** `username`, `name`, or `image`
- **Out:** `social-profile` (photos, description), stated `geolocation`
- **Empty/negative result looks like:** no matching profile — the subject may simply not use the platform, or uses a handle/photos you don't have; absence is not proof.

## Gotchas & OpSec
- ACTIVE: searching needs a login and profile views may notify the owner. Never use a real account.
- Profiles are self-reported and often use aliases, approximate locations, and non-original photos — corroborate before trusting any field.
- Human-in-the-loop: account login required.

## Overlaps ("do both")
- Pairs with reverse-image and face-search tools — this finds the profile, those confirm the person behind the photos and link to other accounts.

## Trust & verifiability
`trust: community` — a real, large platform, but entirely user-generated, unverified content; every detail is a claim to corroborate, not evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seeking-arrangement |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name, image → social-profile, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
