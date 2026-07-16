---
id: blackplanet-com-member-find
name: BlackPlanet.com - Member Find
description: Use when you have a `username` or `name` and want to find a profile on BlackPlanet, a large African-American social network — returns a `social-profile` with photos, location and connections.
url: https://www.blackplanet.com/user_search/index.html
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Finding a BlackPlanet member profile for a subject active in the African-American online community.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: 100% free to search, message and view profiles; a free account/login is required to run member search and see full results.
opsec: active
opsecNote: Member search and profile viewing generally require being logged in, so you act from an account and viewing may register as a "hit"/visitor on the target's profile. Use a sock-puppet account; never message or interact with the subject.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A genuine, long-running niche social network (20M+ members); all profile data is user-supplied and unverified.
missingPersonsRelevance: high
coverage:
- us
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- peekyou
- webmii
- blackplanet
- blackplanet-com
aliases:
- BlackPlanet
- BlackPlanet member search
tags:
- gsocialmedia
- General Social Media Sites
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# BlackPlanet.com - Member Find

> BlackPlanet's member search — the way into one of the largest African-American social networks (20M+ members) to find a subject's profile by name or username.

## When to use
You have a `username` or `name` and are looking for social footprints in a demographic-specific community that mainstream aggregators often miss. BlackPlanet has been active since 1999 and remains popular, so a subject may have a profile here — with photos, a stated location, age, interests, and friend connections — that does not surface on Facebook/Instagram sweeps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.blackplanet.com/user_search/index.html.
2. Register/login with a **sock-puppet** account — member search and full profile viewing are gated behind login.
3. Search by `username` or `name`; you can narrow by gender, age, and ZIP code (including ZIPs outside your own area).
4. Read the profile: photos (`image`), display `name`, stated location, and social connections. Screenshot before privacy can change.
5. Pivot: a reused `username` feeds cross-network username tools; photos feed reverse-image search; a stated location narrows people-search.

## Inputs → Outputs
- **In:** `username` or `name` (optionally filtered by gender/age/ZIP)
- **Out:** `social-profile`, display `name`, `image` (profile photos), location, connections
- **Empty/negative result looks like:** no member matches the search terms, or a sparse profile with no photos/details — common for dormant accounts.

## Gotchas & OpSec
- Human-in-the-loop: **account-login required** — you cannot search anonymously.
- OpSec: **active** — viewing a profile while logged in can appear as a visit/"hit" to the owner. Never contact the subject from the puppet account.
- Profiles skew toward dating/social personas; corroborate identity before relying on stated details.

## Overlaps ("do both")
- Pairs with `[[peekyou]]` and `[[webmii]]` — name aggregators may flag a BlackPlanet presence without a login, then you use member-find to open the actual profile.

## Trust & verifiability
`trust: community` — a real, long-lived niche network, but all content is user-supplied; treat profile claims as leads to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blackplanet-com-member-find |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
