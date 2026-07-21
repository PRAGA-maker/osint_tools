---
id: boingboing-bbs
name: BoingBoing BBS
description: Use when you have a `username` active in tech/geek/maker culture and want their post history on Boing Boing's community forum — returns posts, interests and `associate` interaction leads.
url: https://bbs.boingboing.net
category: communities-forums
path:
- communities-forums
bestFor: Searching Boing Boing's Discourse community for a handle's posts, interests, and interactions.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
- associate
status: live
pricing: free
costNote: Free to read and search public posts; a free account is only needed to post.
opsec: passive
opsecNote: Reading public forum threads is passive and invisible to the user. Register a sock puppet only if some content requires login; never reply from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: bbs.boingboing.net is the genuine Discourse forum of Boing Boing; posts are user-generated and pseudonymous, so content is real but unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Boing Boing BBS
- bbs.boingboing.net
tags:
- toddington
- curated-directory
- online-communities-blogs
- forum
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# BoingBoing BBS

> The Boing Boing community forum (a Discourse board) — a niche source for a handle active in tech, geek, maker, and internet-culture circles.

## When to use
Your subject moves in tech/geek/maker/internet-culture spaces and you have a `username` you think they use. Boing Boing's long-running forum accumulates users' opinions, interests, and interactions, so it can confirm a reused handle, reveal interests and views, and surface people they engage with. A supplementary community source — reach for it when the subject's culture fits Boing Boing's audience.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bbs.boingboing.net and use its Discourse search, or dork: `site:bbs.boingboing.net "<username>"`.
2. Find the user profile and browse their post/topic history.
3. Read for self-disclosed detail, interests, and views; note recurring topics.
4. Note frequently-interacting users as `associate` leads.
5. Pivot: a reused handle feeds cross-platform username-search; interests/opinions corroborate an identity profile.

## Inputs → Outputs
- **In:** `username`
- **Out:** post history → interests/views, linked `social-profile`, interacting `associate`s
- **Empty/negative result looks like:** no profile/posts — the subject may not use this forum or uses a different handle; absence isn't proof of no forum activity elsewhere.

## Gotchas & OpSec
- Pseudonymous: a handle match isn't automatic attribution — corroborate via reused handle/style/self-disclosure.
- Niche audience: high value only if the subject fits Boing Boing's tech/geek demographic.
- OpSec: passive for reading; never post/reply from an attributable identity.

## Overlaps ("do both")
- Pairs with cross-platform username-search ([[boards-ie]] and other forums) — this covers Boing Boing's community; username tools show where else the handle appears.

## Trust & verifiability
`trust: unverified` — a genuine, established forum, but content is user-generated and pseudonymous; treat posts as leads and confirm identity links independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | boingboing-bbs |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, username, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
