---
id: qzone
name: QZone
description: Use when you have a QQ number/`username` or `name` for a Chinese subject and want their Tencent social profile — returns a `social-profile` with photos, diaries, and social connections.
url: https://qzone.qq.com
category: social-networks
path:
- social-networks
bestFor: Finding a Chinese subject's Tencent QZone profile (tied to their QQ number) — photos, posts, and friend network.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free, but a QQ/Tencent account (and usually login) is required to view most QZone content; many profiles are friends-only.
opsec: active
opsecNote: QZone is a logged-in Tencent platform; viewing profiles can leave visitor footprints and Tencent logs activity extensively (and is subject to Chinese jurisdiction). Use a dedicated sock-puppet QQ account on an isolated device; never your real identity, and assume the platform is monitored.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Tencent platform (one of China's largest social networks, tied to QQ); profile data is authentic, though heavy privacy settings and the Chinese-language interface limit access.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- wechat-com
- renren-com
aliases:
- Qzone
- QQ空间
- qzone.qq.com
tags:
- toddington
- curated-directory
- social-media
- china
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# QZone

> Tencent's QZone — one of China's largest social networks, bound to the QQ instant-messaging ecosystem: a QQ number often resolves to a QZone profile with photos, diaries, and a friend network.

## When to use
Your subject is Chinese or China-linked and you have (or can find) their QQ number or a candidate `username`/`name`. QZone is the "home page" of a QQ account, so it can reveal photos (`image`), posts/diaries, interests, and social connections (`associate`) — a primary social surface for Chinese subjects where Western platforms return nothing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log in with a **sock-puppet** QQ account (most content requires login).
2. Access a profile via its QQ number (QZone URLs are keyed to the QQ ID) or search within QQ/QZone by `name`/`username`.
3. View available content: profile photos, published photos/albums, diary posts, and visible friends.
4. Do not friend-request or interact with the target; browse only what's visible.
5. Pivot: photos feed reverse-image search; the QQ number cross-references `[[wechat-com]]`/other Tencent services; visible friends are `associate` leads.

## Inputs → Outputs
- **In:** QQ number/`username` or `name`
- **Out:** `social-profile` (photos, posts, connections), profile/album `image`s
- **Empty/negative result looks like:** a friends-only or restricted profile shows almost nothing to a non-friend; absence of visible content reflects privacy settings, not necessarily an inactive account.

## Gotchas & OpSec
- Human-in-the-loop: **QQ account login required**; the interface is Chinese-language.
- Heavy privacy controls mean many profiles are largely closed to non-friends.
- OpSec: **active** and jurisdiction-sensitive — Tencent logs extensively and operates under Chinese law. Use an isolated sock-puppet QQ account and device; never your real identity.

## Overlaps ("do both")
- Pairs with `[[wechat-com]]` (the other major Tencent platform) and `[[renren-com]]` — a Chinese subject may appear on several; check across them.

## Trust & verifiability
`trust: trusted` — a first-party Tencent platform, so visible profile data is authentic. The limits are access (privacy settings, login, language), not data authenticity; corroborate identity via photos/connections across Tencent services.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | qzone |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
