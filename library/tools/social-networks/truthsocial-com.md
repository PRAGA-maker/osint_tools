---
id: truthsocial-com
name: truthsocial.com
url: https://truthsocial.com/
category: social-networks
path:
- social-networks
description: Use when you have a `username` or `name` and want to check for a Truth Social presence — returns a `social-profile` with posts, bio, and connected accounts.
bestFor: Finding and reading a subject's Truth Social profile and posts, especially US right-leaning users absent from mainstream networks.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to use; reading most public profiles/posts works without an account, though some views and all interaction require free registration.
opsec: active
opsecNote: Logged-out browsing of public profiles is passive. Creating an account to see more or to follow/reply is active and can expose a sock-puppet identity; the platform requires registration (historically email/phone) and interactions are visible. Keep read-only and logged out where possible.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Trump Media & Technology Group; the platform is authentic (a Mastodon-derived network), though individual accounts may be impersonators or parody.
missingPersonsRelevance: medium
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Truth Social
- truthsocial
tags:
- rightwingsocialmediasites
- Right Wing Social Media Sites
- alt-social
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# truthsocial.com

> Truth Social, the Mastodon-derived US social network — the place to look for a subject's posts and connections when they've left or been banned from mainstream platforms.

## When to use
You have a `username` or `name` and want to know whether the subject is active on Truth Social and what they post there. It disproportionately hosts US right-leaning users who may have migrated from X/Facebook, so it is a useful non-mainstream network to check when a person's mainstream presence is thin. A profile yields bio, posting history, followers/following and reposted accounts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://truthsocial.com/ (try logged out first for passive reading).
2. Try the handle directly at `truthsocial.com/@<username>`, or use in-app search for the `name`/handle.
3. Read the profile: bio, join date, post history, media, and who they follow/repost.
4. If a view is gated, register a sock-puppet account to see more — but keep to reading; following/replying is visible.
5. Pivot: reused `username` feeds cross-platform enumeration; posted media feeds reverse-image/geolocation; followed accounts feed `associate` mapping.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (bio, posts, follows), real `name` where disclosed
- **Empty/negative result looks like:** no account for the handle, or a lookalike impersonator/parody — verify by cross-checking linked accounts and posting style before attributing.

## Gotchas & OpSec
- Impersonation and parody accounts are common; confirm identity via cross-links, not the handle alone.
- Some views and all interactions require a free account; registration historically needs an email/phone — use a sock puppet.
- OpSec: reading logged out is passive; logging in and any follow/reply is active and can burn a puppet identity.

## Overlaps ("do both")
- Pairs with `[[masto]]` (Mastodon/fediverse) since Truth Social is Mastodon-derived, and with `[[username-search-tool]]` to see if the handle is reused on X/Gab/other networks.

## Trust & verifiability
`trust: trusted` — the platform itself is a genuine, operating network; treat the *contents* of any single account as self-published and potentially impersonated until corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | truthsocial-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
