---
id: mewe
name: MeWe
description: Use when you have a `name` or `username` and want to check for a MeWe profile (a privacy-focused social network that draws communities pushed off mainstream platforms) — returns `social-profile`.
url: https://mewe.com
category: social-networks
path:
- social-networks
bestFor: Checking a subject's presence on MeWe — an ad-free, privacy-branded network that attracted users (and groups) deplatformed elsewhere; useful when mainstream platforms come up empty.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to join. Meaningful search and profile/group viewing require a (free) account login; there is little useful anonymous public search.
opsec: active
opsecNote: Because you must log in to search/view, activity ties to your account and MeWe's privacy model limits what non-members see — use a sock-puppet MeWe account, not your own. Joining groups to view them can expose your puppet to group admins.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: MeWe is a real, operating social platform, but its privacy-by-design means limited public/OSINT visibility; presence is confirmable but content is often gated behind login and membership.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- mewe.com
- MeWe social
tags:
- toddington
- social-media
- social-networks
- alt-platform
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# MeWe

> A privacy-branded, ad-free social network that became a landing spot for communities pushed off mainstream platforms — worth checking when a subject has thin mainstream footprint.

## When to use
You have a `name` or `username` and mainstream platforms (Facebook, X, Instagram) yield little — MeWe is a plausible alternative home, especially for subjects in communities that migrated off larger networks (privacy-focused, alt-political, deplatformed groups). Reach for it to confirm a MeWe presence and, via a puppet account, read profile and group activity that can reveal interests, associates, and location clues.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a **sock-puppet** MeWe account (search/viewing is largely login-gated).
2. Log in and use MeWe's member/handle search for the subject's `name` or `username`.
3. Open a matching profile: bio, posts (privacy-permitting), and public groups/pages they belong to.
4. To see group content, you may need to join the group with your puppet — do this cautiously, as admins can see members.
5. Pivot: groups → interests/community/location; connections → `associate` mapping; reused username → cross-platform enumeration.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (MeWe profile), group/community memberships, posts where visible
- **Empty/negative result looks like:** no member match, or a profile with everything restricted. MeWe's privacy defaults mean an existing profile can show almost nothing to non-connections — "found but empty" is common and not a tool failure.

## Gotchas & OpSec
- **Login-gated:** little works anonymously; you need an account, so treat this as an active, account-bound task.
- Privacy-by-design limits visibility — even confirmed profiles may reveal little without a connection.
- OpSec: **active** — searching/viewing is tied to your (puppet) account; joining groups exposes it to admins.

## Overlaps ("do both")
- Pairs with cross-platform username enumeration (`[[lullar]]`, Sherlock/WhatsMyName) to spot a MeWe handle, and with other alt-platform checks (Gab, Parler archives, Telegram) when mapping a subject who left the mainstream.

## Trust & verifiability
`trust: unverified` — a genuine live platform, but its privacy model makes OSINT coverage shallow; confirm any profile match by details visible after login, and don't over-read an empty-but-present profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mewe |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
