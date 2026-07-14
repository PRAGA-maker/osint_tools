---
id: wechatsogou
name: WechatSogou
description: Use when you have a WeChat public-account `name`/`username` or keyword and want to discover the account and its articles via Sogou's WeChat search — returns social-profile (account metadata) and image (QR/avatar).
url: https://github.com/chyroc/WechatSogou
category: messaging
path:
- messaging
- wechat-line
bestFor: Programmatically discovering WeChat public (official) accounts and their recent articles by scraping Sogou's WeChat search.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free and open-source Python library; no fees. Cost is operational — Sogou throttles and serves CAPTCHAs heavily.
opsec: passive
opsecNote: Queries Sogou's public WeChat search, not WeChat itself, and never contacts the target account. Sogou aggressively rate-limits and CAPTCHA-gates scraping, so run from a disposable IP; the tool historically needed proxy/CAPTCHA handling.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: python-lib
trust: community
trustNote: Well-known open-source project (chyroc/WechatSogou) with a large following, but WeChat/Sogou anti-crawling has degraded reliability; the code is public and inspectable.
missingPersonsRelevance: high
coverage:
- cn
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- wechat-id-search
aliases:
- WeChatSogou
- 微信公众号爬虫
tags:
- wechat
- open-source
- scraper
- china
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# WechatSogou

> A Python library that scrapes Sogou's WeChat search to discover WeChat public (official) accounts and their articles — the OSINT back-door into a walled-garden messenger dominant in China.

## When to use
Your subject or the organisation around them runs a WeChat public account, and you have its `name`/`username` or a topical keyword. WeChat itself is closed to outside search, but Sogou indexes public accounts and their articles — WechatSogou automates that. Use it to confirm an account exists, pull its profile metadata (WeChat ID, intro, QR/avatar), and enumerate recent articles for content leads.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install wechatsogou` (or clone https://github.com/chyroc/WechatSogou) into a Python environment.
2. Instantiate the API and search: e.g. `ws_api.get_gzh_info('<account name>')` for account metadata, or `get_gzh_article_by_history` / search functions for articles.
3. Read the structured output: profile URL, avatar image, WeChat name, WeChat ID, post/view permissions, QR code, introduction, authentication status.
4. Handle the friction: Sogou will throw CAPTCHAs and rate-limits — supply a CAPTCHA-solving callback and/or proxies as the library documents.
5. Pivot: the WeChat ID and QR feed identity confirmation; article content feeds location/associate leads.

## Inputs → Outputs
- **In:** `username` / `name` (account name or WeChat ID) or keyword
- **Out:** `social-profile` (account metadata: WeChat ID, intro, auth status), `image` (avatar / QR code), article listings
- **Empty/negative result looks like:** a CAPTCHA wall or empty result set — usually Sogou blocking the scrape, not proof the account doesn't exist. Retry with a fresh IP / solved CAPTCHA.

## Gotchas & OpSec
- **Degraded:** Sogou's anti-crawling (CAPTCHAs, IP bans) has made this flaky; budget for CAPTCHA solving and proxies, and expect maintenance drift.
- Coverage is effectively China-centric and limited to *public* accounts — private WeChat user data is not reachable here.
- Passive against the target, but hammering Sogou from one IP gets you blocked fast.

## Overlaps ("do both")
- Pairs with a direct WeChat-ID lookup (`[[wechat-id-search]]`) — WechatSogou discovers the public account and its content; an ID search corroborates the underlying identifier.

## Trust & verifiability
`trust: community` — a widely-used, inspectable open-source project, but reliability is at the mercy of Sogou's defenses. Treat article/metadata results as leads and verify against the live Sogou WeChat page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wechatsogou |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | yes (captcha) |
