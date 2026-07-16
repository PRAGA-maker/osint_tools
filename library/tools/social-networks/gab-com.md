---
id: gab-com
name: gab.com
description: Use when you have a `username` or `name` and want to find/monitor a subject on the Gab social network — returns their `social-profile` and posts.
url: https://gab.com/auth/sign_in
category: social-networks
path:
- social-networks
bestFor: Locating and reading a subject's presence on Gab, a Mastodon-based platform popular with the far right.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to use; some browsing works logged-out but a free account is needed for full access, follower lists, and search depth.
opsec: passive
opsecNote: Reading public Gab posts is passive. To see more you must register — use a sock-puppet account, never a real identity, since Gab is a closed-community platform where accounts and interactions are visible. Do not follow/interact with the target. Assume Gab logs account activity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A real, active social platform (Mastodon-based), but all profile/post content is user-generated and unverified; treat it as primary-source social media, not vetted data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Gab
- gab.com
tags:
- rightwingsocialmediasites
- Right Wing Social Media Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- gab-social
---

# gab.com

> Gab — a Mastodon-based social network with a far-right user base. A place to find a subject who's been deplatformed elsewhere, and to read their unfiltered posting.

## When to use
You have a `username` or `name` and suspect the subject is active on Gab — often the case for people banned from mainstream platforms. Gab profiles reveal posts, follows, and network that can corroborate identity, location clues, associates, and intent. Useful in missing-persons, threat, and extremism-adjacent investigations where the subject migrated to alt-platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet browser, try the public profile at `gab.com/<username>`; some content is visible logged-out.
2. For full access (search, follower/following lists, older posts), register a **puppet** account and sign in at https://gab.com/auth/sign_in.
3. Read the profile and posts for identity, location, and `associate` signals; note reused avatars/handles.
4. Stay read-only — do not follow, react, or message the target.
5. Pivot: run the avatar through reverse-image/face tools; check the handle on `[[sherlock]]`/`[[namechk]]`; archive key posts.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (Gab profile), posts, follows, confirmed display `name`, avatar
- **Empty/negative result looks like:** no profile / no search match — the subject isn't on Gab under that handle, or content is login-gated. Not proof of absence elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** for full access — use a puppet account.
- OpSec: **passive** for reading; registering/interacting is attributable. Never use a real identity on a closed-community platform.
- Content is user-generated and unverified; corroborate any claimed fact independently.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`/`[[namechk]]` (handle reuse) and reverse-image tools (avatar) — Gab is one alt-platform; confirm the same person across others.

## Trust & verifiability
`trust: unverified` — a live platform, but everything on it is self-published. Treat posts as primary-source claims to be corroborated, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gab-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
