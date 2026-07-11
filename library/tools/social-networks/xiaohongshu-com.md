---
id: xiaohongshu-com
name: xiaohongshu.com
description: Use when you have a `username` or `name` and want to find a subject on Xiaohongshu (RED / Little Red Book), China's major lifestyle social platform — returns profiles, posts, and location/lifestyle context.
url: https://www.xiaohongshu.com/explore
category: social-networks
path:
- social-networks
bestFor: Finding a subject's profile and lifestyle/location posts on Xiaohongshu (RED), a major Chinese social network.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- geolocation
status: live
pricing: free
costNote: Free to view; deep browsing, search, and most content require the mobile app and a logged-in account (often a Chinese phone number to register).
opsec: active
opsecNote: The platform aggressively gates content behind login and app use; a logged-in session ties viewing to your account and the platform is Chinese-jurisdiction. Use a dedicated sock-puppet account and device/browser, avoid your real phone number, and assume viewing/following can be surfaced to the target and logged by the platform.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Genuine, very large Chinese social platform (RED); profiles are self-authored and the walled-garden UX makes systematic OSINT hard, so treat findings as leads.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Xiaohongshu
- RED
- Little Red Book
- 小红书
tags:
- gsocialmedia
- General Social Media Sites
- chinese-social-media
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# xiaohongshu.com

> Xiaohongshu ("RED" / Little Red Book) — one of China's largest lifestyle/social platforms — use it to locate a Chinese-speaking subject's profile and the location-and-lifestyle-rich posts they share there.

## When to use
You have a `username` or `name` (often Chinese-language) and think the subject is active in Chinese social media, especially younger, urban, or lifestyle-focused users. RED posts are heavy on real-world context — cafes, travel, purchases, neighborhoods — which can leak `geolocation` and routine. Reach for it when Western platforms are empty and the subject's footprint is likely on Chinese apps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.xiaohongshu.com/explore. For anything beyond the front page you will hit a login/app wall.
2. From a sock-puppet account (dedicated device/browser), search the subject's `name`/`username`; the mobile app gives the fullest search.
3. Open candidate profiles; read the bio, post grid, tagged locations, and comments.
4. Extract location tags, recurring places, and linked handles as `geolocation` and pivot leads.
5. Pivot: cross-reference tagged places on maps; match photos with reverse-image/face tools; reuse handles on WeChat/Weibo/Douyin.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** `social-profile`, `name`, `geolocation` (post/location tags), plus lifestyle/routine context
- **Empty/negative result looks like:** login wall blocks the search, or no matching handle — absence here is weak evidence given the strict gating; retry in the app with a valid account and try Chinese-character name variants.

## Gotchas & OpSec
- Human-in-the-loop: **login/app-gated** — most OSINT value needs a logged-in (ideally app) session; registration often wants a Chinese phone number.
- OpSec: **active** — logged-in viewing/following can surface to the target and is logged under Chinese jurisdiction. Sock-puppet account and device only; never your real phone/identity.
- Names are often in Chinese; transliteration mismatches are common — search characters, not just pinyin.

## Overlaps ("do both")
- Pairs with Weibo, WeChat, and Douyin OSINT — Chinese users spread across these apps, so run the set and match handles/photos; RED is strongest for lifestyle/location leakage.

## Trust & verifiability
`trust: community` — a real, massive platform, but a walled garden with self-authored profiles; treat everything as a lead and corroborate identity and location independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xiaohongshu-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
