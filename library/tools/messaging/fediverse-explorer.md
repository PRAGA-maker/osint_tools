---
id: fediverse-explorer
name: Fediverse Explorer
description: Use when you have an interest, `name` or `username` and want to find matching Mastodon/fediverse accounts — returns `social-profile`s.
url: https://fediverse.info/explore/people
category: messaging
path:
- messaging
bestFor: Discovering Mastodon and other fediverse accounts by topic/interest or handle when a subject may have left mainstream networks for the fediverse.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free directory; no account required to browse. Listings are opt-in profiles that have chosen to be discoverable.
opsec: passive
opsecNote: Browsing the directory is read-only and does not notify anyone. Note that actually following or interacting with an account from your own fediverse instance is active and visible — stop at viewing unless you use a sock-puppet account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run fediverse onboarding/discovery portal; it only indexes accounts that opted into discovery, so coverage is partial and self-selected.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- followgraph-for-mastodon
aliases:
- fediverse.info
- Fedi explore people
tags:
- Social Media
- Mastodon
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Fediverse Explorer

> A discovery directory for the fediverse (Mastodon and friends) that lets you browse opted-in accounts by interest, name or handle.

## When to use
Your subject isn't on the big centralised networks but may run a Mastodon/fediverse presence, or you have a `username`/`name`/interest and want to find their decentralised-social account. Use it to surface fediverse `social-profile`s you can then read for posts, connections and cross-links back to other identities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://fediverse.info/explore/people.
2. Browse by interest/topic, or search by a handle or display `name`.
3. Scan the returned account cards; open a promising one to view its home instance profile, bio, links and public posts.
4. Pivot: note the account's **instance domain** (the part after the `@`) and any linked websites; feed the handle to [[followgraph-for-mastodon]] to map who they follow, and check bio links for other identities.

## Inputs → Outputs
- **In:** `username`, `name`, or interest keyword
- **Out:** `social-profile` and `username` (`@user@instance.tld`)
- **Empty/negative result looks like:** no matches — remember the directory only lists accounts that opted into discovery, so absence here is weak evidence; the person may still exist on an instance that isn't indexed.

## Gotchas & OpSec
- Coverage is self-selected and partial: many fediverse users disable discovery, so this misses them. For those, search individual instances or a dedicated fediverse search engine instead.
- OpSec: browsing is passive, but **following/replying** from your own account is public and traceable — use a sock-puppet instance account if you need to interact.

## Overlaps ("do both")
- Pairs with [[followgraph-for-mastodon]] because this finds the account and Followgraph maps its social graph to reveal associates.

## Trust & verifiability
`trust: community` — a community discovery portal indexing opt-in accounts. Good for finding a presence, but treat it as a lead source; verify identity from the account's own posts and linked profiles, not from its mere listing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fediverse-explorer |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
