---
id: line-play
name: LINE Play
description: Use when you have a `username` or `name` and want to check for a presence on LINE Play (an avatar-based social app popular in Asia) — returns social-profile and image (avatar) leads.
url: https://play.game.line.me
category: social-networks
path:
- social-networks
bestFor: Checking whether a subject has a LINE Play avatar profile and pulling their avatar, nickname, and social connections.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free consumer app; no fee to view profiles, though full interaction needs the LINE Play app and a LINE account.
opsec: passive
opsecNote: Viewing a public LINE Play profile is passive, but following/messaging or adding the user is active and visible. Use a sock-puppet LINE account and stop at read-only viewing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: unverified
trustNote: An official LINE consumer product, but its OSINT use (finding and reading a target's avatar profile) is community practice, not a documented investigative feature; profile matching by nickname is unreliable.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- line-app
- linecorp-com
aliases:
- LinePlay
- LINE Play avatar
tags:
- line
- avatar
- social-media
- asia
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# LINE Play

> LINE's avatar-based social world — a niche corner to check when a subject is active in the LINE ecosystem, especially in Japan, Taiwan, and Thailand.

## When to use
Your subject uses LINE (dominant in parts of East/Southeast Asia) and you're chasing their secondary/leisure identities. LINE Play is an avatar app where users chat, keep diaries, and connect with friends. If you have a `username`/nickname or `name`, checking LINE Play can surface an avatar profile, a nickname, posted content, and friend connections — a pivot when mainstream platforms are dry. It's a supplement, not a primary locator.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install LINE Play and sign in with a sock-puppet LINE account (the full experience is app-based).
2. Use in-app search for the subject's `username`/nickname (LINE Play IDs and display names).
3. View the profile read-only: avatar (`image`), nickname, diary/posts, and friends (`associate` leads).
4. Do NOT follow, gift, or message — those actions are visible to the user.
5. Pivot: a confirmed nickname feeds username enumeration elsewhere; the LINE ecosystem link corroborates other LINE findings.

## Inputs → Outputs
- **In:** `username`/nickname or `name`
- **Out:** `social-profile` (LINE Play profile), `image` (avatar), nickname, friends
- **Empty/negative result looks like:** no matching nickname, or many similar avatars — nicknames aren't unique, so a hit is a weak identity signal until corroborated.

## Gotchas & OpSec
- Human-in-the-loop: needs the LINE Play **app and a LINE account** — use a burner.
- Avatars and nicknames are freely chosen and non-unique; do not attribute on a nickname match alone.
- Interaction (follow/gift/message) is visible — stay read-only.

## Overlaps ("do both")
- Pairs with the core `[[line-app]]` (LINE add-by-ID/QR) and `[[linecorp-com]]` (what LINE data exists and the legal channel) — LINE Play adds a leisure-identity angle within the same ecosystem.

## Trust & verifiability
`trust: unverified` — a legitimate LINE product, but using it for investigation relies on weak nickname matching and community practice. Treat any match as a lead requiring corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | line-play |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | yes (account-login) |
