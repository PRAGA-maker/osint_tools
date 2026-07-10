---
id: diaspora
name: Diaspora*
description: Use when you have a `name` or `username` and want to check for a presence on the decentralised Diaspora* social network — returns a social-profile handle if the person is active on a pod.
url: https://diasporafoundation.org/
category: social-networks
path:
- social-networks
bestFor: Locating a person's profile on the decentralised, privacy-focused Diaspora* network (federated "pods").
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source; joining a pod is free. No cost to search public posts/profiles.
opsec: passive
opsecNote: Public post/tag search is passive. Diaspora* is privacy-focused and federated, so many profiles are limited to followers; interacting (following, messaging) from a real account would expose you — use a sock-puppet pod account if you need to see more than public content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Legitimate non-profit, open-source federated network; no central authority vouches for individual pods or user identities, so treat any profile as self-asserted.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- diaspora
- diaspora foundation
- diaspora pods
tags:
- toddington
- curated-directory
- social-media
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Diaspora*

> A decentralised, user-owned social network spread across independently run "pods" — an off-mainstream place to check for a subject's alternative social presence.

## When to use
You are enumerating a person's social footprint and want to cover the privacy-oriented, decentralised networks that mainstream people-search tools ignore. If your subject is privacy-minded, tech-leaning, or has migrated off big platforms, they may have a Diaspora* handle. You typically start from a `name` or a reused `username` and are looking for a matching `social-profile`. Because Diaspora* is federated with no single directory, treat it as a targeted check rather than a bulk search.

## How to use it (`bestInteractionPattern`: web-manual)
1. From https://diasporafoundation.org/, pick a pod (e.g. via the linked pod list / Fediverse Observer) or use a large public pod's search.
2. Search the pod for the subject's `username` or `name`; also search relevant `#hashtags` and interests they're known for, since discovery on Diaspora* is heavily tag-driven.
3. A Diaspora* ID looks like `user@pod.example.org` — note the full federated handle when you find a match.
4. Read the public posts/profile; much may be follower-only.
5. Pivot: a reused username here feeds cross-platform username search; a federated handle and its pod feed further fediverse checks (Mastodon, etc.).

## Inputs → Outputs
- **In:** `name`, `username`
- **Out:** `social-profile` (a `user@pod` federated handle and any public posts)
- **Empty/negative result looks like:** no matching handle on the pods you search — because there is no global index, absence on one pod is NOT proof the person isn't on Diaspora* elsewhere.

## Gotchas & OpSec
- No central search: you must search pod-by-pod (or via a tag/aggregator), so coverage is inherently partial.
- Privacy-first culture: many profiles restrict posts to contacts; you'll often see only the handle.
- OpSec: browsing public content is passive; following or messaging exposes your account — use a puppet pod account.

## Overlaps ("do both")
- Pairs with username-enumeration tools and Mastodon/fediverse search — a `username` that appears on Diaspora* frequently reappears across the fediverse, so run a cross-platform username sweep alongside it.

## Trust & verifiability
`trust: community` — a legitimate open-source network, but identities are self-asserted and unverified; confirm any match against other selectors before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | diaspora |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
