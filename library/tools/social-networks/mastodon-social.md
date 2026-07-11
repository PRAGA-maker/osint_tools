---
id: mastodon-social
name: mastodon.social
description: Use when you have a `username`/`name` and want to find someone on Mastodon/the fediverse — returns their profile, posts and connections (`social-profile`) on the flagship Mastodon instance and beyond.
url: https://mastodon.social/about
category: social-networks
path:
- social-networks
bestFor: Finding and reading a subject's presence on Mastodon and the wider fediverse.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to browse public profiles and posts without an account. A (free) account improves full-text/post search and lets you follow across instances.
opsec: passive
opsecNote: Reading public profiles/posts is passive and doesn't notify the target. Following, favouriting, or boosting from an account is active and visible. If you create an account to search, use a sock puppet — and note the fediverse is decentralised, so different instances see and expose different data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: mastodon.social is the flagship, first-party Mastodon instance run by the Mastodon project — genuine platform data. The caveat is federation: no single instance sees the whole network, so absence here isn't absence everywhere.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- fedidb
- streamscout
aliases:
- Mastodon
- mastodon.social
- fediverse search
tags:
- mastodon
- Mastodon Related Sites
- fediverse
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# mastodon.social

> The flagship Mastodon instance and a practical entry point to searching the decentralised fediverse for a subject's handle, posts, and connections.

## When to use
Your subject may use Mastodon or another fediverse platform (Pleroma, Misskey, etc.), and you have a `username`/handle or `name` to look for. Mastodon accounts often mirror handles used elsewhere, and public posts can reveal interests, location cues, and connections. mastodon.social is the largest instance and a convenient search hub, but remember a person's account may live on any of thousands of instances — the handle format is `@user@instance.tld`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mastodon.social and use the search bar for the `username`, full `@user@instance` handle, or `name`/keywords.
2. If you know the home instance, go directly to `https://<instance>/@username` to view the native profile.
3. Read the profile: bio, linked/verified websites, posts (toots), followers/following, and pinned content.
4. For fuller post/keyword search, sign in (sock puppet) — some search features require an account and depend on the instance's settings.
5. Pivot: linked websites and cross-used handles feed username/identity work; connections feed `associate` mapping; use fediverse directories/tools when the home instance is unknown.

## Inputs → Outputs
- **In:** `username`/handle or `name`
- **Out:** `social-profile` — bio, verified links, posts, follower/following graph, and `name`
- **Empty/negative result looks like:** no match on mastodon.social's search — the person may be on a different instance (search is federation-limited), uses a different handle, or isn't on the fediverse. Try the full handle or other instances; absence here isn't network-wide absence.

## Gotchas & OpSec
- Human-in-the-loop: none to read public profiles; only advanced search/following needs a login.
- OpSec: **passive** while reading; **active** if you follow/favourite/boost (visible to the user). Use a sock-puppet account for any interaction.
- Federation is the key gotcha: search coverage is limited to what an instance knows about, and post search is often opt-in per instance. Verified links (green check) are a reliable identity signal — use them.

## Overlaps ("do both")
- Pairs with fediverse discovery tools/directories (e.g. `[[fedidb]]`, `[[streamscout]]`) — the flagship instance is a starting point, but network-wide handle discovery needs tools that index across instances. Combine to avoid missing an account on a small instance.

## Trust & verifiability
`trust: trusted` — genuine first-party platform data. The reliability caveat is structural (decentralisation limits any one instance's view), so treat a negative as instance-scoped and confirm identity via verified profile links.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mastodon-social |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
