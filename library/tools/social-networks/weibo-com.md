---
id: weibo-com
name: Sina Weibo
description: Use when you have a username or name and want to find a subject's Chinese-language social presence — returns social profiles, posts, photos and network links.
url: http://www.weibo.com/signup/mobile.php?lang=en-us
category: social-networks
path:
- social-networks
bestFor: Finding and reading a subject's activity on China's dominant microblogging platform.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- image
- associate
status: live
pricing: free
costNote: Free to search and read, but Weibo increasingly gates full post history, follower lists and search behind a logged-in account, and many actions require a Chinese mobile number to register.
opsec: passive
opsecNote: Public profile viewing is passive, but Weibo aggressively fingerprints and rate-limits anonymous visitors and often forces a login wall after a few page views. Use a sock-puppet account (ideally registered on a burner number) and a clean browser; do not follow, like or message the target from an attributable account.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Sina Corporation; this is the genuine first-party platform, though content authenticity of individual posts is only as reliable as the poster.
missingPersonsRelevance: high
coverage:
- global
- cn
auth: account
api: false
localInstall: false
registration: true
aliases:
- Weibo
- 微博
- Sina Weibo
- weibo.com
tags:
- gsocialmedia
- General Social Media Sites
- china
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- overseas-weibo-com
- sina-weibo-chinese
- weibo-china
---

# Sina Weibo

> China's largest microblogging network — the primary place to find a Chinese subject's public posts, photos and social graph.

## When to use
You have a `username` (a Weibo handle or nickname) or a `name`, and the subject is Chinese, based in China, or part of a Chinese diaspora community. Weibo is where much of that activity lives that never surfaces on Western platforms — public posts, geotagged photos, follower/following links and comment threads that place a person in time, location and social context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet Weibo account (registration usually needs a Chinese mobile number; without login you will hit a wall after a few views).
2. Use the search bar (magnifier icon) to search a `name`/`username`, or go directly to `weibo.com/<uid>` if you already have a numeric user ID.
3. Filter results to **用户 (users)** to find the profile, or **实时 (real-time)** to read posts mentioning your term.
4. On a profile, read the bio, pinned/recent posts, photo grid, and follower/following lists for `associate` links. Note the numeric UID — it is stable even if the display name changes.
5. Pivot: geotagged posts feed geolocation work; the profile photo feeds reverse-image/face search; associates feed further Weibo or cross-platform lookups.

## Inputs → Outputs
- **In:** `username` or `name` (Chinese characters usually work far better than romanised spellings)
- **Out:** `social-profile`, real `name`/nickname, `image` (avatar + posted photos), `associate` (followers/following)
- **Empty/negative result looks like:** no user match, or a profile with posts hidden behind "关注后可见" (visible only to followers) / a locked account. Try the Chinese-character form of the name and the numeric UID before concluding nothing exists.

## Gotchas & OpSec
- Human-in-the-loop: expect a login wall and rate-limiting; a Chinese phone number is often required to create a usable account.
- Names romanise many ways — search the native characters; a single English spelling will miss most results.
- Content is subject to platform censorship and deletion; a gap in a timeline may be removed content, not inactivity.
- Never interact (follow/like/DM) from the investigating account — Weibo surfaces "who viewed" and follow signals.

## Overlaps ("do both")
- Pairs with reverse-image and face-search tools — run the avatar and posted photos to link the same person on other networks.
- Complements Chinese search engines (e.g. `[[monstercrawler-com]]`-style broad search plus Baidu) to find profile links and mentions Weibo's own search hides behind login.

## Trust & verifiability
`trust: trusted` — Weibo is the authentic first-party Sina platform, so a confirmed account is a genuine presence; individual post content, however, carries the usual social-media reliability caveats and may be edited or deleted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | weibo-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, image, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, rate-limit) |
