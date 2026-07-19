---
id: okcupid
name: OkCupid
description: Use when you have a `name`, `username` or photo and want to check for a dating profile — returns `social-profile`, `image` and self-reported `physical-description`.
url: https://www.okcupid.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding and reading a subject's OkCupid dating profile (photos, bio, location, self-reported details) once you have a likely handle or are searching a local area.
selectorsIn:
- name
- username
- image
selectorsOut:
- social-profile
- image
- physical-description
status: live
pricing: freemium
costNote: Free to register and browse; premium tiers add filters and incognito. You must create an account to view profiles at all.
opsec: active
opsecNote: OkCupid is interaction-visible. Viewing a profile can appear in the target's "visitors" list, and likes/messages are obviously visible. Always use a dedicated sock-puppet account (fresh email, no real photos, plausible location) and never interact from a real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A major mainstream dating platform (Match Group). Profiles are self-authored, so content is real-but-unverified; identity, age and location are whatever the user chose to claim.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- okcupid.com
tags:
- dating
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# OkCupid

> A mainstream dating platform whose profiles carry photos, self-described traits and a coarse location — searchable, but only from behind a logged-in account.

## When to use
You suspect a subject uses online dating, or you have a likely OkCupid `username`, a `name`, or a profile photo to reverse-match, and you want the dating `social-profile`: recent photos, self-reported age/height/location, orientation, and free-text bio that may leak habits, workplace or nearby landmarks. Useful for corroborating that someone is active, in a given city, and for gathering fresh imagery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log in with a **sock-puppet** OkCupid account (create one if needed — you cannot browse without an account). Set its location near the target's suspected area, since discovery is distance-based.
2. Use Search/Discovery and filter by age, location and any distinguishing traits; scan photo results for your subject.
3. If you have a photo, compare against results, or run the image through a face/reverse-image tool ([[pimeyes]]) to confirm identity independently.
4. Read the `social-profile`: photos (`image`), self-reported `physical-description`, location, and bio text for pivotable detail.
5. Pivot: cross-check the photos and bio claims against other social accounts; feed a distinctive handle to a username search.

## Inputs → Outputs
- **In:** `name`, `username`, or `image` (for visual matching)
- **Out:** `social-profile`, `image`, self-reported `physical-description` (age/height/body, location)
- **Empty/negative result looks like:** no profile surfaces within your search radius/filters. Because discovery is distance- and preference-gated, absence is weak — the person may exist but be outside your account's search parameters or have paused their profile.

## Gotchas & OpSec
- **Active and visible:** profile views can show up in the target's visitor list; there is no truly passive way to browse without a paid incognito tier. Assume you may be seen — use a clean sock puppet.
- Discovery is location- and preference-scoped, so you often must set a sock-puppet location and demographics to even see the target.
- Everything is self-reported: treat age, location and even photos as claims to verify, not facts.

## Overlaps ("do both")
- Pairs with [[pimeyes]] and reverse-image search to confirm that the dating photos match your subject rather than a catfish, and with username-search tools to link the handle to other platforms.

## Trust & verifiability
`trust: community` — a legitimate major platform, but the *content* is user-authored and unverified. Confirm identity through independent photo matching and cross-referenced details before relying on anything in the profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | okcupid |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username, image → social-profile, image, physical-description |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
