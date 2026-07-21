---
id: passion-com
name: Passion.com
description: Use when you have a `username` or `name`/location and want to check for an adult-dating presence on Passion.com (a FriendFinder-network site) — returns social-profile leads.
url: https://passion.com
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a handle or persona has a profile on the Passion.com adult dating/social network.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to register and browse basic profiles; messaging and full features are paywalled. No payment needed to check for a profile's existence.
opsec: active
opsecNote: Meaningful browsing requires a logged-in account, and profile views/likes/messages can notify the member. Adult platforms also fingerprint and may show you as a "recent visitor." Use a fully sandboxed sock-puppet account with a burner email and no real photos; never interact from an attributable identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A FriendFinder Networks adult-dating property; profiles are self-created and unverified, and the network is known for fake/bot profiles, so treat any match cautiously.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools: []
aliases:
- Passion
- passion.com
tags:
- toddington
- curated-directory
- online-communities-blogs
- dating
- adult
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Passion.com

> An adult dating/social network in the FriendFinder family — useful narrowly for checking whether a subject's handle or persona has a profile here.

## When to use
You are tracing a `username` across platforms, or you have a `name` + location and reason to think a subject uses adult-dating sites, and you want to check Passion.com for a matching profile. Its OSINT value is confirming presence and reading a self-authored profile (photos, stated location/age, interests) — corroboration and image leads, not a reliable locator, since profiles are self-reported and the network carries many fake accounts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a fully sandboxed sock-puppet account (burner email, no real photos) — meaningful search/browse requires login.
2. Use the member search to query the `username` or filter by location/age/gender to narrow toward a suspected persona.
3. Read any matching profile for reused handles, photos (feed reverse-image search), and self-stated location/interests. Do not like, favorite, or message.
4. Pivot: a reused `username` or profile photo links to other platforms via username/reverse-image search; stated details are corroboration leads to verify elsewhere.

## Inputs → Outputs
- **In:** `username` or `name`/location
- **Out:** `social-profile` (Passion.com profile, photos, self-stated attributes)
- **Empty/negative result looks like:** no matching profile in search — the persona isn't here (or uses a different handle). Given heavy fake-profile volume, a "match" on a common handle is weak until corroborated by photo/detail overlap.

## Gotchas & OpSec
- Human-in-the-loop: account-login required; account creation may involve email/phone verification.
- The FriendFinder network is notorious for bot and fake profiles — do not treat a handle match alone as identification.
- OpSec: **active.** Profile views and any interaction can surface you to the member and to the platform's "visitors" features; stay strictly passive from a burner identity.

## Overlaps ("do both")
- Run the same `username` and profile photos through a cross-platform username enumerator and reverse-image search — those establish whether the same persona appears elsewhere, which is what turns a weak Passion.com match into a corroborated one.

## Trust & verifiability
`trust: unverified` — a real, live platform, but every profile is self-created and unverified, and fake accounts are common. Any identification must rest on corroborating photos/handles/details across independent sources, not a single profile here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | passion-com |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
