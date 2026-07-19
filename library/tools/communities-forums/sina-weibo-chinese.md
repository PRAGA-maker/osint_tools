---
id: sina-weibo-chinese
name: Sina Weibo
description: Use when you have a `username`/`name` tied to China and want their Weibo profile — returns social-profile, posts, photos, and location/associate signals.
url: http://weibo.com/login.php
category: communities-forums
path:
- communities-forums
bestFor: Finding and reading a subject's Sina Weibo (Chinese microblog) profile — posts, photos, followers, and self-disclosed location.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free to use; viewing most content increasingly requires a (free) logged-in account, and some features require a Chinese phone number to register.
opsec: active
opsecNote: Weibo increasingly gates viewing behind login, and it is a heavily-monitored PRC platform — accounts, IPs, and activity are logged, and registration may need a Chinese mobile number. Use a dedicated sock-puppet account and VPN; do not follow/interact, as that can notify the subject.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A major, genuine PRC social platform; profiles are self-created and unverified (aliases common), and platform censorship/deletion means absence of content is not proof of anything.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- overseas-weibo-com
- weibo-china
- weibo-com
aliases:
- Weibo
- 微博
- weibo.com
tags:
- china
- microblog
- social-networking
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Sina Weibo

> China's dominant microblogging platform — the primary place to find a China-connected subject's social profile, posts, photos, and network.

## When to use
Your subject is Chinese or China-connected and you need their social footprint. Weibo is where hundreds of millions post publicly — a `username`/handle or real `name` can lead to a profile with posts, photos (feed to reverse-image/face tools), follower/following network (`associate` leads), and self-disclosed `geolocation` (Weibo often shows a posting region). It's often the single richest source on a mainland-China individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a dedicated sock-puppet account at weibo.com (viewing increasingly requires login; registration may need a Chinese mobile number).
2. Search the handle/name (Chinese-character names work best); open the profile.
3. Read posts, photos, bio, follower/following lists, and the shown IP/region label.
4. Pivot: photos → reverse-image/face search; followers/mentions → `associate` mapping; the region label and post content → `geolocation`; reused handle → cross-platform enumeration.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (posts, photos, network), self-disclosed/region `geolocation`
- **Empty/negative result looks like:** no profile, or a locked/deleted account — Weibo censors and deletes; absence may reflect takedown, not that the person was never there. Names are ambiguous at scale.

## Gotchas & OpSec
- ACTIVE and monitored: login gating, IP logging, and possible Chinese-phone registration; use a sock-puppet + VPN and never interact (follows/likes can alert the subject).
- Content is censored/removable — treat gaps and deletions as expected, not as evidence.
- Chinese-language search is far more effective than romanized names.

## Overlaps ("do both")
- Pairs with reverse-image/face search and Chinese people-search tools — Weibo yields the photos and network; those confirm the person and extend the map.

## Trust & verifiability
`trust: community` — a real, huge platform, but user-generated and censored; every field is a claim to corroborate, and absence is never proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sina-weibo-chinese |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
