---
id: mastodon
name: Mastodon
description: Use when you have a `name` or `username` and want to find a subject's profile on the decentralised Mastodon/fediverse network — returns a social-profile handle and their public posts.
url: https://mastodon.social
category: social-networks
path:
- social-networks
bestFor: Locating a person's Mastodon (fediverse) profile and reading their public posts across federated instances.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source; searching public posts/profiles needs no account, though a (puppet) account improves full-text search on some instances.
opsec: passive
opsecNote: Reading public profiles and posts is passive. Mastodon is privacy-conscious and federated — following, boosting or replying from a real account exposes you to the target and their instance admins. Use a sock-puppet account on a large public instance if you need to interact or use logged-in search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Legitimate open-source federated network; there is no central authority verifying identities, and anyone can run an instance, so treat handles and claims as self-asserted.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Mastodon
- fediverse
- mastodon.social
tags:
- toddington
- curated-directory
- social-media
- fediverse
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Mastodon

> The largest Twitter-like decentralised social network (the fediverse) — check here for a subject's alternative or primary social presence, especially if they left mainstream platforms.

## When to use
You're enumerating a person's social footprint and want to cover Mastodon, where privacy-minded, tech-leaning, journalist and activist users often migrated from Twitter/X. Start from a `name` or a reused `username` and look for a matching `social-profile` (`user@instance.tld`). Mastodon handles frequently mirror handles used elsewhere, so it's a strong cross-platform pivot even when the person's mainstream accounts are locked.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try a fediverse-wide search engine or a large instance's search for the `username`/`name` (e.g. search on mastodon.social or via a fediverse directory).
2. A Mastodon ID is `user@instance.tld` — note the full federated handle when you find a match, including the home instance.
3. Read the public posts, bio links, and followers/following where visible.
4. Cross-reference the handle and bio links against the subject's other accounts to confirm identity.
5. Pivot: a reused username feeds cross-platform enumeration; bio links often expose a personal site/other socials; the home instance hints at community/location.

## Inputs → Outputs
- **In:** `name`, `username`
- **Out:** `social-profile` (a `user@instance` handle + public posts/bio)
- **Empty/negative result looks like:** no match in the instances/directories you search — because Mastodon is federated with no complete global index, absence on one search surface is NOT proof the person isn't on the fediverse elsewhere.

## Gotchas & OpSec
- **No universal search:** full-text and cross-instance search are limited by design; you may need to search several instances or use a fediverse aggregator.
- Handles are self-asserted and instances can vanish; confirm identity via bio links and cross-platform username matches.
- Interacting (follow/boost/reply) exposes you — browse from a puppet.

## Overlaps ("do both")
- Pairs with `[[diaspora]]` and username-enumeration tools — a `username` on Mastodon commonly reappears across the fediverse and beyond, so run a cross-platform sweep alongside it.

## Trust & verifiability
`trust: community` — a legitimate network, but identities are unverified and instance-dependent; corroborate any match against other selectors before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mastodon |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
