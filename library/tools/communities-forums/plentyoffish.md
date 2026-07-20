---
id: plentyoffish
name: PlentyOfFish
description: Use when you have a `username`, `name`, or photo and want to check a major dating platform for a subject's profile — returns `social-profile`, `physical-description`, location, and `image` for cross-matching.
url: http://www.pof.com/
category: communities-forums
path:
- communities-forums
bestFor: Locating a subject's dating profile (photos, self-description, approximate location) on a large free dating platform.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- physical-description
- image
status: live
pricing: freemium
costNote: Free to create an account and browse/search profiles; premium upgrades exist but basic search is free.
opsec: active
opsecNote: Searching requires an account, and viewing a profile can register a "visitor" notification to the target — this is ACTIVE and can tip off the subject. Always use a sock-puppet account, sock-puppet photos, and a clean IP. Never message the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: PlentyOfFish (owned by Match Group) is a legitimate major dating platform; profile content is self-created and can be fake, aged, or aspirational.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- POF
- pof.com
tags:
- toddington
- curated-directory
- online-communities-blogs
- dating
source: toddington-resources
lastVerified: '2026-07-20'
relatedTools:
- plenty-of-fish-com
---

# PlentyOfFish

> A large free dating platform — searchable for a subject's dating profile, which can expose current photos, a self-description, and an approximate location.

## When to use
You have a `username`, `name`, age/location, or a photo and want to check whether a subject has a PlentyOfFish (POF) profile. Dating profiles are high-value: recent `image`s (great for reverse-image and face matching), a `physical-description`, approximate city/region, interests, and sometimes a reused handle that links to other accounts. In a missing-persons context, an active/recently-active dating profile can indicate the person is alive and roughly where — but the interaction is active and must be handled carefully.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a sock-puppet POF account (neutral profile, sock-puppet photos) on a clean IP/browser.
2. Use POF's search filters (age, gender, location, keywords) to narrow toward the subject; POF's search is relatively open compared to swipe-only apps.
3. Compare candidate profiles by photo (reverse-image them), handle, self-described details, and location.
4. Note last-active indicators and any reused `username`.
5. Pivot: reverse-image the profile `image`s; run the handle through username-enumeration; corroborate location with other sources. Do **not** message the subject.

## Inputs → Outputs
- **In:** `username`, `name`, age/location, or `image`
- **Out:** `social-profile`, profile `image`s, `physical-description`, approximate location, reused handle
- **Empty/negative result looks like:** no matching profile in the searched area — common; the person may not use POF or may restrict visibility; absence is weak evidence.

## Gotchas & OpSec
- **Active** and account-gated: viewing profiles can trigger a "viewed you" notice — sock-puppet everything; never contact the target.
- Profiles are self-created and often stale or embellished — corroborate photos and claims.
- Match Group platforms share signals; over-interacting can surface your puppet elsewhere.

## Overlaps ("do both")
- Pairs with reverse-image/face tools and username-enumeration — POF supplies fresh photos and a handle; those confirm identity and find the subject's other accounts. See also `[[plenty-of-fish-com]]`.

## Trust & verifiability
`trust: community` — a legitimate platform, but user-generated profile content; treat photos as the strongest signal (verify via reverse image) and text as claims.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | plentyoffish |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, physical-description, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
