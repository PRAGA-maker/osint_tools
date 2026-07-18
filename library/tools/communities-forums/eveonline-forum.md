---
id: eveonline-forum
name: EVE Online Forums
description: Use when you have a gaming `username`/handle and want to tie it to EVE Online activity and posts — returns social-profile and associate.
url: https://forums.eveonline.com
category: communities-forums
path:
- communities-forums
bestFor: Searching the official EVE Online player forums for a handle's posts, corporation/alliance ties and history.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- username
status: live
pricing: free
costNote: Free to read/search; posting requires an EVE Online account.
opsec: passive
opsecNote: Reading and searching public forum posts is passive. Do not register or post from an account tied to your identity; use a sock-puppet if interaction is ever needed (it usually isn't).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Official CCP Games community forum; posts are genuine player content, but in-game personas are pseudonymous and not identity-verified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- EVE Online forums
- forums.eveonline.com
tags:
- gaming
- forums
- socmint
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# EVE Online Forums

> The official player forum for EVE Online — a place to run down a gaming handle, its post history, and the corporations/alliances (and thus other players) it associates with.

## When to use
You have a `username`/gamertag and suspect the subject plays EVE Online, or you are trying to attribute a reused handle across platforms. The forums are public and searchable: a handle's post history can reveal timezone/activity patterns, in-game corporation and alliance affiliations, disputes, and links to Discord/other accounts players share. In-game "corporations" and "alliances" are effectively social groups — the other members are `associate` leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://forums.eveonline.com and search the `username`, or use `site:forums.eveonline.com "handle"` on a search engine.
2. Read the handle's posts and profile for corporation/alliance names, activity timing, and any off-platform links.
3. Note co-posters, corp-mates, and named allies/rivals as association leads.
4. Cross-reference the same handle on other platforms (a reused gamertag is a strong cross-platform pivot).
5. Pivot: corporation/alliance members → `associate` mapping; shared Discord/social links → `social-profile`/`username` OSINT; posting times → timezone/lifestyle inference.

## Inputs → Outputs
- **In:** `username` (in-game handle / gamertag)
- **Out:** `social-profile` (forum profile/posts), `associate` (corp/alliance/co-posters), `username` (linked handles)
- **Empty/negative result looks like:** no posts under the handle — the subject may play without forum activity, use a different in-game name, or not play EVE at all; try in-game/third-party player trackers.

## Gotchas & OpSec
- EVE identities are pseudonymous — a handle links to a *character/player persona*, not a verified real identity; treat cross-platform handle reuse as a lead to corroborate, not proof.
- Coverage is only the subset of players who post on the forums.
- OpSec: passive read; never engage from an identifiable account.

## Overlaps ("do both")
- Pairs with cross-platform username-search tools (Sherlock/WhatsMyName-style) and gaming-profile lookups — the forum gives context and associations, those confirm the same handle's spread across other services.

## Trust & verifiability
`trust: community` — official-forum content is genuine, but the personas are pseudonymous; any real-world attribution must be corroborated with independent evidence beyond the game handle.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eveonline-forum |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, associate, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
