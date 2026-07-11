---
id: weibo-china
name: Weibo (China)
description: Use when you have a Chinese-context `name`/`username` and want their microblog presence — returns the `social-profile`, posts, photos (`image`) and self-disclosed `geolocation` on China's dominant Twitter-equivalent.
url: http://weibo.com
category: social-networks
path:
- social-networks
bestFor: Finding and reading a subject's activity on China's largest microblogging platform.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
- geolocation
status: live
pricing: free
costNote: Free to use. Meaningful search/browsing now generally requires a (free) Weibo account login, and creating one usually needs a Chinese mobile number or a workaround.
opsec: active
opsecNote: Viewing profiles while logged in ties your (sock-puppet) account to the target; Weibo shows some visitor/interaction signals and the platform operates under Chinese data jurisdiction. Never use a real identity — register a dedicated sock-puppet account, browse via VPN, and avoid following/liking/messaging the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Weibo (Sina Weibo) is a first-party, real platform — the dominant Chinese microblog. Content is authentic user data; the caveats are access friction (login/geo) and heavy platform censorship, not authenticity.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- baidu
aliases:
- Sina Weibo
- 微博
- weibo.com
tags:
- major-social-networks
- china
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Weibo (China)

> China's dominant Twitter-equivalent microblog — the primary place to find and read a Chinese-context subject's public posts, photos, and social graph.

## When to use
Your subject has a China nexus (Chinese national, diaspora, business, travel) and you need their social footprint where Western platforms are absent. You have a `name` (Chinese or romanized) or a `username` and want the person's `social-profile`: posts, uploaded photos (`image`), check-ins and stated locations (`geolocation`), followers/following, and interests. Often the richest — sometimes only — social source for a subject inside the Chinese internet.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in with a **sock-puppet Weibo account** (search/browse is heavily gated for logged-out users) at https://weibo.com, ideally over a VPN.
2. Search the target `name`/`username` in the user search; also try known nicknames and pinyin variants.
3. Open candidate profiles and read posts, images, geotags/check-ins, and the follow graph.
4. Note self-disclosed location, workplace, school, and connected accounts; save/screenshot key posts (content is frequently deleted or censored).
5. Pivot: images feed reverse-image/face search; a real name feeds `[[baidu]]` and Chinese people-search; geotags feed mapping.

## Inputs → Outputs
- **In:** `name` or `username` (Chinese characters or pinyin)
- **Out:** `social-profile` (posts, follow graph), `image` (uploaded photos), `geolocation` (check-ins/stated location)
- **Empty/negative result looks like:** no matching user, or a profile with posts hidden/removed — could mean the person isn't on Weibo, uses a different handle, or content was censored/deleted. Absence here is weak evidence given the platform's churn.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** is effectively required; registration typically wants a Chinese mobile number, so plan the sock puppet in advance.
- OpSec: **active** — logged-in viewing associates your account with the target and runs inside Chinese data jurisdiction. Use a dedicated identity + VPN, never engage (no follow/like/DM), and assume visitor signals may be visible.
- Censorship and deletion are constant; capture evidence immediately and expect gaps.

## Overlaps ("do both")
- Pairs with `[[baidu]]` — Weibo is the social/behavioural layer, Baidu the general Chinese-web search layer. A name found on Weibo should be run through Baidu (and Chinese people-search) to corroborate identity and surface off-platform mentions.

## Trust & verifiability
`trust: trusted` — Weibo is a genuine first-party platform, so the content is authentic user data. Treat the access friction (login/geo gating) and pervasive censorship as the real limitations, and preserve findings before they're removed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | weibo-china |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, image, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
