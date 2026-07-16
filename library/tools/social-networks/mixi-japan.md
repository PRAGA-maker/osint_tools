---
id: mixi-japan
name: Mixi (Japan)
description: Use when you have a Japanese `name`/`username` and want a Mixi social-networking profile — returns profile, community memberships and diary/activity for this Japan-centric network.
url: https://mixi.jp
category: social-networks
path:
- social-networks
bestFor: Investigating a subject's presence on Mixi, a long-running Japan-focused social network.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to use; viewing most member content requires a (free) Mixi account, and Japanese phone/registration may be needed to sign up.
opsec: active
opsecNote: Mixi is a login-gated, relationship-oriented Japanese network — much content needs an account, and viewing profiles from a logged-in account can leave "footprints" (ashiato) visible to the member. Use a dedicated sock-puppet account, and be aware footprint-visibility can alert the subject. Never use a real/attributable account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A major, long-established Japanese social network (Mixi, Inc.); authentic platform, but access is gated and Japanese-language, and its user base has declined from its peak.
missingPersonsRelevance: high
coverage:
- jp
auth: account
api: false
localInstall: false
registration: true
aliases:
- Mixi
- mixi.jp
- ミクシィ
tags:
- major-social-networks
- japan
- japanese-web
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- mixi
---

# Mixi (Japan)

> Japan's veteran social network — a login-gated, Japanese-language platform where a subject may keep a profile, communities, and a diary not visible on Western networks.

## When to use
Your subject is Japanese or connected to Japan and you're looking for social presence Western networks won't show. Mixi, once Japan's dominant SNS, still hosts profiles, interest communities, and diary (日記) content. Search it when a Japanese `name` or `username` needs coverage beyond Twitter/Facebook, especially for older accounts from Mixi's peak years.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mixi.jp with a **dedicated sock-puppet Mixi account** (registration is Japanese-language and may require a Japanese phone/verification).
2. Search by `name`/`username` in Japanese where possible; browse communities (コミュニティ) tied to the subject's interests/location.
3. Open profiles and diaries you can access; note community memberships as `associate`/interest signals.
4. **Mind footprints (足あと):** viewing a profile can record your (sock-puppet) account as a visitor — never browse from a real account.
5. Pivot: a profile/handle feeds `[[user-searcher]]` and Japanese search (`[[naver-com]]`-style, Yahoo! Japan); images feed `[[reverse-image-search]]`.

## Inputs → Outputs
- **In:** Japanese `name` / `username`
- **Out:** Mixi `social-profile`, display `name`, community memberships, diary/activity (access-gated)
- **Empty/negative result looks like:** no findable profile — the person isn't on Mixi, the profile is friends-only, or you searched in romaji not Japanese. Mixi's decline means many have moved on; absence is common and not conclusive.

## Gotchas & OpSec
- **Login-gated and Japanese-language:** most content needs an account and Japanese search terms; registration itself can be a hurdle (phone verification).
- **Footprints (ashiato):** profile visits may be visible to the member — a real risk of tipping off the subject. Sock puppet only.
- OpSec: **active** — you must log in and may leave visible traces.

## Overlaps ("do both")
- Pairs with Yahoo! Japan / Japanese search engines and `[[user-searcher]]` — Mixi covers the gated SNS layer; Japanese search engines cover the open web (blogs, news). Run both for a subject with a Japan footprint.

## Trust & verifiability
`trust: community` — an authentic major Japanese platform, but access-gated and declining in use. Content is user-generated; verify identity by cross-referencing profile detail, communities, and other Japanese sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mixi-japan |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
