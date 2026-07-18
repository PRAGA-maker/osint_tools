---
id: ravelry
name: Ravelry
description: Use when you have a username or name and suspect the subject is a knitter/crocheter — returns a member social-profile, project photos, and location/associate leads.
url: https://www.ravelry.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a fiber-arts hobbyist's member profile, project history, forum activity, and stated location.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
- geolocation
- image
status: live
pricing: free
costNote: Free to join and use; a free account is required to search members and view most profiles and forum content.
opsec: passive
opsecNote: Viewing profiles is passive, but you must be logged in — so use a sock-puppet account, not a personal one. Ravelry does not tell a member who viewed them, though favoriting/messaging/friending would expose your account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established, well-run niche community (millions of members); profile content is user-supplied, so treat stated details as self-reported.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- ravelry.com
tags:
- communities-forums
- hobby
- username-search
- knitting
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Ravelry

> A large, tight-knit community for knitters, crocheters, and fiber artists — a niche username/name search that can place a hobbyist subject with photos, projects, and a stated location.

## When to use
You have a `username` or `name` and reason to think the subject is into fiber crafts (a hobby mentioned in a bio, a reused handle, a craft-related lead). Ravelry members build detailed profiles — project galleries with photos, favourites, groups, and a self-entered location — so a hit gives you a `social-profile`, corroborating `image`s, and often a `geolocation`, plus `associate` links through friends and group membership. Reused handles make it a useful stop in username enumeration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create/sign in with a free sock-puppet account at https://www.ravelry.com (search and profiles require login).
2. Use People search for the username or name; refine by location or group if the name is common.
3. Open the profile: read the bio/location, browse the project and stash photos, note groups joined and friends listed, and skim forum post history.
4. Pivot: a reused `username` extends your enumeration to other platforms; a stated city is a `geolocation` lead; project photos may carry `metadata-exif` if downloadable; friends/groups give `associate` leads.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile`, `username`, `geolocation` (self-stated location), `image` (project/stash photos)
- **Empty/negative result looks like:** no member matches the handle/name, or a profile that exists but is sparse/private with no projects or location — the subject may not use Ravelry or keeps a minimal profile.

## Gotchas & OpSec
- Human-in-the-loop: a free account login is required even to search; keep it a dedicated sock puppet.
- OpSec: passive viewing is not shown to the member, but any interaction (favorite, message, friend request, forum reply) exposes your account — don't interact.
- User-supplied data: locations and names are self-reported and may be pseudonymous; corroborate before trusting.

## Overlaps ("do both")
- Pairs with cross-platform username tools (e.g. Sherlock/WhatsMyName-style checkers) — those tell you the handle exists on Ravelry, while visiting the profile here yields the photos, location, and social graph a checker can't.

## Trust & verifiability
`trust: community` — Ravelry is a reputable, long-standing community, but profile fields are user-entered, so treat location and identity details as leads to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ravelry |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username, geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
