---
id: overseas-weibo-com
name: overseas.weibo.com
description: Use when you have a `name`/`username` and want to reach Sina Weibo to search for a Chinese-language social profile — returns social-profile, name. The overseas portal now just redirects to weibo.com.
url: http://overseas.weibo.com/
category: social-networks
path:
- social-networks
bestFor: Entry point to Sina Weibo profile/keyword search (overseas portal now folds into weibo.com).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free to browse; overseas.weibo.com now 301-redirects to the main weibo.com. Deeper viewing/search on Weibo increasingly requires a registered (often China-mobile-verified) account.
opsec: active
opsecNote: Weibo is a Chinese-operated platform with real-name policies and heavy logging; searching and especially registering ties activity to you. Use a sock-puppet account and browser, and assume queries are logged. Do not use a personal identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: The genuine Sina Weibo platform, but the dedicated "overseas" portal is effectively deprecated (redirects to weibo.com); search depth is gated behind login and Chinese-language handling.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- Weibo overseas
- Sina Weibo international
tags:
- gsocialmedia
- General Social Media Sites
- weibo
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- sina-weibo-chinese
- weibo-china
- weibo-com
---

# overseas.weibo.com

> The (now-redirecting) overseas gateway to Sina Weibo — China's largest microblog — for finding a subject's Chinese-language social profile, though search depth is login-gated.

## When to use
You have a `name` or `username` and reason to think the subject has a Chinese/Chinese-diaspora footprint, so you want to search Sina Weibo. The dedicated overseas portal is effectively gone (it redirects to weibo.com), so treat this as a pointer into mainstream Weibo search rather than a distinct tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://overseas.weibo.com/ — it now 301-redirects to weibo.com.
2. Use Weibo's search for the subject's `name`/`username` (try Chinese characters and pinyin/transliterations).
3. For anything beyond surface results, Weibo will prompt for a registered account — use a **sock-puppet** account only (registration often needs a Chinese mobile number; a burner/virtual number may be required).
4. Review candidate profiles: display name, bio, posts, followers — confirm against known identifiers.
5. Pivot: a confirmed Weibo `social-profile` feeds Chinese-platform OSINT and image/relationship analysis; posted photos feed reverse-image/face tools.

## Inputs → Outputs
- **In:** `name` or `username` (try Chinese + transliterated forms)
- **Out:** `social-profile` (Weibo profile), `name`, posts/photos
- **Empty/negative result looks like:** no matches or a login wall blocking results — often the login gate or a wrong-script query, not proof the person isn't on Weibo; retry with Chinese characters when possible.

## Gotchas & OpSec
- The overseas portal is deprecated — you're effectively on weibo.com; search depth requires login.
- OpSec (active): Chinese-operated, real-name, heavily logged — use a sock-puppet account/number and never a personal identity.
- Language: results hinge on correct Chinese-character spelling; transliteration alone often misses the account.

## Overlaps ("do both")
- Pairs with other Weibo entries ([[weibo-com]], [[weibo-china]]) and Chinese-platform search tools — run the same name in Chinese script across them and reconcile.

## Trust & verifiability
`trust: community` — the real Weibo platform (authentic profiles), but the overseas portal is deprecated and search is login-gated; verify any match against multiple identifiers.
