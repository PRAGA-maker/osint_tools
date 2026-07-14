---
id: qzone-china
name: Qzone (China)
description: Use when you have a QQ number/`username` or `name` and want to find a subject's Tencent Qzone social profile — returns social-profile, image, and associate leads.
url: https://qzone.qq.com
category: social-networks
path:
- social-networks
bestFor: Locating and viewing a Chinese subject's Qzone (QQ Zone) profile, photos, and friend network, tied to their QQ number.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- associate
status: live
pricing: free
costNote: Free Tencent consumer service; viewing most content requires a QQ account and, for many profiles, being an approved friend.
opsec: passive
opsecNote: Viewing a Qzone requires logging in with a QQ account, and visiting some profiles leaves a "visitor" footprint the owner can see. Use a sock-puppet QQ account and be aware Tencent operates under Chinese data/censorship regimes.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A genuine, massive Tencent platform tied to QQ; authoritative as the subject's own posts, but heavily access-controlled and privacy-gated for outsiders.
missingPersonsRelevance: high
coverage:
- cn
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- wechatsogou
- weibo-com
aliases:
- QQ Zone
- QQ空间
- Qzone
tags:
- major-social-networks
- china
- qq
- tencent
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Qzone (China)

> Tencent's long-running social network, bound to the QQ ecosystem — one of the primary places a Chinese subject's photos, diary, and friends live.

## When to use
Your subject is Chinese or QQ-connected and you have their QQ number (used as a `username`) or a `name`/nickname. Qzone (QQ空间) is where QQ users post photos, blog entries, and status updates and connect with friends. A found Qzone can yield images (`image`), a friend network (`associate` leads), and lifestyle content — valuable in China-linked cases where Western platforms are absent.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in to https://qzone.qq.com with a sock-puppet QQ account (viewing requires login).
2. If you have the QQ number, go directly to `https://user.qzone.qq.com/<QQnumber>`; otherwise search by nickname within QQ/Qzone.
3. Read what's public: profile, photo albums (`image`), mood/diary posts, and visible friends.
4. Respect the walls: many Qzones are friends-only; don't send friend requests from a traceable account.
5. Pivot: the QQ number links to WeChat/other Tencent services; photos feed reverse-image/face tools; friends feed associate mapping.

## Inputs → Outputs
- **In:** QQ number (`username`) or `name`/nickname
- **Out:** `social-profile` (Qzone), `image` (albums), `associate` (friends), posts
- **Empty/negative result looks like:** a friends-only/private Qzone showing only a profile shell, or no match — privacy settings hide most content from non-friends; absence of visible data isn't absence of activity.

## Gotchas & OpSec
- Human-in-the-loop: a **QQ account login** is required to view anything meaningful — use a burner.
- Visiting a profile can leave a visible "recent visitor" trace — be cautious.
- Tencent operates under Chinese jurisdiction; weigh data-handling and censorship for sensitive cases.

## Overlaps ("do both")
- Pairs with `[[wechatsogou]]` (WeChat public-account discovery, same Tencent ecosystem) and `[[weibo-com]]` (China's microblog) — run all three to cover a Chinese subject's likely platforms.

## Trust & verifiability
`trust: community` — a real, enormous Tencent platform; the subject's own posts are authoritative, but heavy privacy gating means outsiders see little without access. Confirm identity via the QQ number linkage across Tencent services.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | qzone-china |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
