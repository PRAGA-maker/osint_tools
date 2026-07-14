---
id: ameba
name: Ameba
description: Use when you have a `username` or `name` and want to find a Japanese subject's Ameba blog/social profile — returns social-profile and image (posted photos) leads.
url: https://www.ameba.jp
category: social-networks
path:
- social-networks
bestFor: Finding a Japanese subject's Ameba blog and profile, and mining posts for photos and personal detail.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free consumer blogging platform; reading public blogs needs no account, commenting/following does.
opsec: passive
opsecNote: Reading a public Ameba blog is passive and leaves no trace. Following or commenting requires an account and is visible — use a sock-puppet account and stay read-only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A large, genuine Japanese blogging platform (CyberAgent); the subject's own posts are authoritative, but username matches need corroboration and content is Japanese-language.
missingPersonsRelevance: high
coverage:
- jp
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mixi
- line-play
aliases:
- Ameblo
- アメーバ
- Ameba Blog
tags:
- japan
- blogging
- social-media
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Ameba

> One of Japan's largest blogging/social platforms (CyberAgent's Ameblo) — a primary place a Japanese subject may keep a public diary, photos, and follower network.

## When to use
Your subject is Japanese or Japan-connected and you have a `username` or `name`/nickname. Ameba (Ameblo) hosts millions of personal blogs — celebrities and ordinary users alike — often rich with photos, daily detail, and location cues. If a handle from elsewhere resolves to an Ameba blog, it can corroborate a persona and open a trove of first-person content. Especially useful where Western platforms are thin for a Japanese subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ameba.jp and search by `username`/nickname, or try `ameblo.jp/<username>` directly.
2. Also run a search-engine dork: `site:ameblo.jp "<name/handle>"` to surface blogs by content.
3. Read the public blog: posts (photos = `image`), profile, and commenter/follower handles (`associate` leads). Machine-translate the Japanese.
4. Stay read-only — don't comment or follow from a traceable account.
5. Pivot: photos feed reverse-image/face tools; a reused handle feeds username enumeration; post content feeds location leads.

## Inputs → Outputs
- **In:** `username`/nickname or `name`
- **Out:** `social-profile` (Ameba blog), `image` (post photos), posts, follower/commenter handles
- **Empty/negative result looks like:** no blog by that handle, or a dormant/empty blog — the handle may be unused on Ameba or the person blogs elsewhere (e.g. Note, Livedoor). Absence isn't proof.

## Gotchas & OpSec
- Content is Japanese-language — use translation and be careful with name transliteration (kanji vs romaji).
- Handles aren't unique to a person across the web; corroborate a match before attributing.
- Reading is passive; only interaction exposes you — stay read-only.

## Overlaps ("do both")
- Pairs with `[[mixi]]` (Japanese social network) and `[[line-play]]` (LINE ecosystem) — run these together to cover a Japanese subject's likely platforms.

## Trust & verifiability
`trust: unverified` — a legitimate major platform; the subject's own posts are authoritative, but the username→person link is a lead that needs corroborating detail from the content itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ameba |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
