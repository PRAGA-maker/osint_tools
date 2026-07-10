---
id: renren-com
name: Renren (人人网)
description: Use when you have a Chinese subject's `name` or `username` and want to check for a Renren social-network profile (esp. older student-era accounts) — returns `social-profile` and `name`, if any survives.
url: http://www.renren.com/
category: social-networks
path:
- social-networks
bestFor: Finding legacy Chinese social-network profiles — Renren was China's dominant student/"Facebook-style" network in the 2010s; useful for historical presence of a Chinese subject.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free to use, but registration and a working (often Chinese) phone-based login are effectively required to search or view profiles. The platform is in a prolonged "upgrade"/decline state.
opsec: active
opsecNote: Viewing profiles requires logging in, tying activity to whatever account you use — use a sock-puppet Chinese-registered account, not your own. The site is Chinese-jurisdiction and may log foreign access.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Renren is a genuine, once-major Chinese social network, now much diminished and repeatedly "upgrading." Profile availability and search are unreliable; treat any find as a lead.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- renren.com
- 人人网
- Chinese Facebook
tags:
- gsocialmedia
- general-social-media-sites
- china
- social-networks
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Renren (人人网)

> China's once-dominant student social network — a Facebook-era relic now in permanent decline, but still worth checking for a Chinese subject's legacy profile.

## When to use
You have a Chinese subject (or someone who studied in China in the 2010s) identified by `name` or `username` and want to find historical social presence. Renren was *the* Chinese campus social network in its heyday, so older accounts can carry real names, universities, hometowns, photos, and classmate networks — valuable for a Chinese-nexus missing-person or identity case where Western platforms yield nothing. Manage expectations: the platform is degraded and much content has aged out or moved.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.renren.com/ (Chinese-language interface; a translation layer helps).
2. Expect a login/registration wall and an ongoing "upgrade" notice — searching or viewing profiles generally needs a logged-in account, ideally a Chinese-registered **sock puppet**.
3. Search by `name` (Chinese characters greatly improve results) or a known `username`.
4. Read any profile hit: real name, university/school, hometown, photos, friends/classmates (`associate`s).
5. Pivot: university/hometown → localized Chinese records and Weibo; classmate list → `associate` mapping; photos → reverse-image/face.

## Inputs → Outputs
- **In:** `name` (Chinese script best) or `username`
- **Out:** `social-profile`, `name`, plus school/hometown/photos where the profile survives
- **Empty/negative result looks like:** login wall, "upgrade in progress," or no search hits — the account may be deleted/dormant, or (very likely) you're blocked without a Chinese login. Empty here is weak evidence of absence given the platform's state.

## Gotchas & OpSec
- **Login-gated and Chinese-only:** without a Chinese-registered account and some Chinese-language ability, you'll mostly hit walls.
- The platform has been "upgrading"/declining for years; historical data is patchy and may vanish.
- OpSec: **active** — viewing requires login on a Chinese-jurisdiction site; use a puppet account and assume access is logged.

## Overlaps ("do both")
- Pairs with Weibo search and other Chinese platform tools — for a Chinese subject, run all of them, since coverage is fragmented and Renren is often thin now.

## Trust & verifiability
`trust: unverified` — a real but heavily degraded platform; any profile you find is a genuine lead but may be outdated. Corroborate school/hometown/name against other Chinese sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | renren-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
