---
id: skout
name: Skout
description: Use when you have a `username`/`name` or a face and want to check a location-based dating/social app for a matching profile — returns dating `social-profile`s with photos, bio, and approximate location.
url: http://www.skout.com
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a subject has a profile on the Skout location-based dating/social network.
selectorsIn:
- username
- name
- image
selectorsOut:
- social-profile
- image
- geolocation
status: live
pricing: freemium
costNote: Free to use with an account; premium features (boosts, extra visibility) are paid. Browsing profiles requires signing in.
opsec: active
opsecNote: Skout is proximity-based and shows who viewed you — creating an account and browsing can expose YOUR puppet profile and approximate location to others, and viewing a target may notify them. Use a dedicated sock-puppet account, spoof/limit location, and never use a real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: A real, established dating/social app (The Meet Group); profiles are self-created and unverified, and location is user-set/approximate.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
aliases:
- Skout dating app
- skout.com
tags:
- dating
- social-network
- location-based
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Skout

> A location-based dating and social app: a place to check whether a subject maintains a dating profile — with photos, a bio, and an approximate location — under a known handle or face.

## When to use
You have a `username`, `name`, or photo of a subject and want to know if they're on Skout, a proximity-based dating/social network. A matching profile can yield additional photos, a self-written bio (interests, age, sometimes workplace/city), and an approximate location — useful for confirming a persona, adding recent imagery for reverse-search, or placing someone in a region. Best treated as one dating-platform check among several.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install the Skout app (or use app.skout.com) and sign in with a dedicated sock-puppet account; set/limit your location deliberately.
2. Search or browse for the subject by `username`/`name`; if you have a photo, watch for a matching face in nearby results.
3. Read a matching profile: photos, bio, stated age/location, and any linked handles.
4. Pivot: profile photos feed `[[reverse-image-search]]` and face tools; a stated city/handle feeds people- and username-OSINT.

## Inputs → Outputs
- **In:** `username`/`name`, or an `image`/face to match.
- **Out:** dating `social-profile` — photos (`image`), bio, approximate `geolocation`.
- **Empty/negative result looks like:** no matching profile — the subject isn't on Skout, uses a different handle, or is outside your searchable radius. Absence is not proof they use no dating apps.

## Gotchas & OpSec
- Active and exposing: it's proximity-based and surfaces profile viewers — your puppet may be seen by the target. Spoof/limit location and never use a real account.
- Human-in-the-loop: requires app install and login.
- Profiles are unverified and location is user-set/approximate; corroborate before relying on any detail.

## Overlaps ("do both")
- Cross-check other dating/social platforms and run any profile photo through reverse-image and face-search tools; a face reused across apps is a strong link.

## Trust & verifiability
`trust: community` — a legitimate commercial app, but profile content is self-declared and unverified. Use it to locate a persona and imagery, then verify identity through independent means.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skout |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name, image → social-profile, image, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
