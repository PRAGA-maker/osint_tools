---
id: alt-com
name: Alt.com
description: Use when you have a `username`, `email`, or location and want to check for an adult/BDSM dating profile — returns a member `social-profile` with photos, area, and stated details.
url: https://alt.com
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a handle/email maps to an Alt.com adult-dating profile and reading its public-facing details.
selectorsIn:
- username
- email
- geolocation
selectorsOut:
- social-profile
- image
- physical-description
status: live
pricing: freemium
costNote: Free to register and browse/search profiles; messaging and full photo access are gated behind a paid membership. Profile discovery works on the free tier.
opsec: active
opsecNote: Active — you must register to search, and the platform (an adult site) may show profile viewers or send activity signals. Use a dedicated sock-puppet account and a clean browser/IP; never register or view from an attributable identity, and be mindful this is sensitive-category data.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A real, long-established adult-dating site (FriendFinder Networks); profiles are self-created and often pseudonymous/aspirational, so treat any detail as claimed, not verified.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- alt.com
- Alt personals
tags:
- toddington
- curated-directory
- dating
- adult
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Alt.com

> A large adult/BDSM/alternative-lifestyle dating platform — worth checking when a subject may keep a pseudonymous personals profile, but everything on it is self-declared and the search itself requires an account.

## When to use
You are profiling a person and have a reusable `username`, an `email`, or a location, and you want to know whether they maintain an adult-dating presence here. Dating profiles frequently reuse a handle from elsewhere, carry photos (reverse-image-searchable), and state an age, body description, and city/region — all useful corroboration or new leads. Reach for it specifically when the case points toward dating/personals activity; it is a sensitive-category source, so use it purposefully.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a **sock-puppet account** (Alt.com requires a login to search) using a clean email, browser, and IP.
2. Search by username/handle, or filter members by location, age, and attributes to narrow to a candidate.
3. Open a candidate profile: note the display handle, stated age/location, `physical-description`, and photos.
4. Reverse-image-search the profile photos and cross-check the handle against other platforms to confirm it's the same person.
5. Pivot: a reused `username` feeds username enumeration; profile `image`s feed reverse-image/face search; a stated `geolocation` narrows location.

## Inputs → Outputs
- **In:** a `username`, `email`, or `geolocation` (area to filter)
- **Out:** a member `social-profile` — handle, `image`(s), `physical-description`, stated age/location
- **Empty/negative result looks like:** no matching profile means no account under that handle/filters (or the profile is set private) — absence is not proof, and a match is not confirmed identity until photos/handle are corroborated.

## Gotchas & OpSec
- **Login required = active.** Searching needs an account; the site is adult and may expose profile-view activity — only ever act from a sock puppet, never a real identity.
- **Sensitive category.** Treat any finding with discretion; sexual-lifestyle data carries real harm potential if mishandled.
- Profiles are pseudonymous and often aspirational (age/appearance/location can be false) — verify with photos and cross-platform handle matches before believing details.
- Messaging/full photos sit behind a paywall, but profile *discovery* works on the free tier.

## Overlaps ("do both")
- Pairs with username-enumeration and reverse-image tools — Alt.com surfaces the personals profile, and those confirm the handle/photo belongs to the same person across sites.

## Trust & verifiability
`trust: community` — a genuine, long-running platform, but its content is entirely user-generated and pseudonymous; the site is real while every profile detail must be independently corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alt-com |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email, geolocation → social-profile, image, physical-description |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
