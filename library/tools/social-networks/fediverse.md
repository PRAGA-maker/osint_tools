---
id: fediverse
name: Fediverse
description: Use when a subject may be on decentralized social networks and you need to know which platforms/instances exist — a guide to the Fediverse (Mastodon, Lemmy, PeerTube…) that routes your username search.
url: https://fediverse.party
category: social-networks
path:
- social-networks
bestFor: Learning the Fediverse landscape (which apps/instances exist) so you know where to search for a subject's decentralized profiles.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free educational portal; no account. It is a directory/guide, not itself a data source.
opsec: passive
opsecNote: Browsing the guide is passive and anonymous. The actual searching happens on individual instances afterward — where viewing a profile is typically also passive, but interacting (following, messaging) is attributable, so use a sock puppet for that.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A community-run introductory guide/directory to federated networks; accurate as orientation, but it points elsewhere and does not itself hold or verify user data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- fediverse.party
- Mastodon / Fediverse guide
tags:
- toddington
- curated-directory
- social-media
- fediverse
- mastodon
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# Fediverse

> A map of the decentralized social web — fediverse.party catalogues the platforms (Mastodon, Lemmy, PeerTube, Pixelfed, Friendica…) so you know *where* to hunt for a subject who left mainstream networks.

## When to use
Your subject isn't on the big platforms, or you have a `username`/`name` and suspect a presence on decentralized/federated networks. Because the Fediverse is a patchwork of independent instances with no single search box, the first problem is *knowing the terrain* — which apps exist and how they federate. This guide solves that orientation step, after which you search the relevant instances directly. It's a starting map, not a people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://fediverse.party and browse the catalogue of Fediverse apps to identify which platforms fit your subject's interests (microblogging → Mastodon; video → PeerTube; link-aggregation → Lemmy; photos → Pixelfed).
2. Note the major instances and how each platform works.
3. Move to the actual search: use a Fediverse user-search tool or an instance's own search for the `username`; a handle like `@name@instance.social` is your key selector.
4. Pivot: a found profile yields posts, follows (`associate`) and often links back to mainstream accounts.

## Inputs → Outputs
- **In:** `name` / `username` (used to decide where to look)
- **Out:** orientation to the right platforms/instances → `social-profile` (found on those instances, not here)
- **Empty/negative result looks like:** the site simply won't "return" a person — it's a guide. Treat it as the step that tells you which instance search to run next; the real hit/miss happens there.

## Gotchas & OpSec
- **Guide, not search:** don't expect user results from fediverse.party itself — its value is knowing where to search.
- The same `username` can exist independently on many instances (and be impersonated) — verify the specific `@user@instance` handle, not just the name.
- OpSec: browsing and most profile-viewing are passive; following/DMing on an instance is attributable — use a sock puppet.

## Overlaps ("do both")
- Pairs with dedicated Fediverse/Mastodon user-search engines and cross-platform username tools — this tells you which networks exist; those actually locate the handle across them.

## Trust & verifiability
`trust: unverified` — a helpful community orientation directory, not a records source. Everything actionable is verified on the destination instance the guide leads you to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fediverse |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
