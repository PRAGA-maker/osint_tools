---
id: bluesky
name: Bluesky
description: Use when you have a `username` or `name` and want to find and read a subject's Bluesky account and social graph — returns social-profile, posts, and associate links.
url: https://bsky.app
category: social-networks
path:
- social-networks
bestFor: Finding and enumerating a subject on Bluesky, whose open AT Protocol makes the full public graph queryable.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- image
- associate
status: live
pricing: free
costNote: Free to browse. The public AT Protocol API and firehose are open and free; no key required for public data.
opsec: passive
opsecNote: Reading public posts/graph via the web app or the public API is passive and unauthenticated — the subject isn't notified. Following, liking, or messaging from an account is active; use a sock-puppet handle if you interact. Note Bluesky's data is unusually open, so your own account's activity is likewise public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Major open social network; profile/post content is user-generated and unverified, but the AT Protocol makes the public graph directly and reliably queryable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- Bluesky
- bsky
- bsky.app
- AT Protocol
tags:
- major-social-networks
- decentralized-social
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Bluesky

> A major Twitter-style network built on the open AT Protocol — meaning the entire public social graph (followers, follows, posts, likes) is queryable without login.

## When to use
You have a `username`/handle or a `name` and want to find the subject on Bluesky and map their public activity: posts, timeline, who they follow and who follows them (`associate` network), profile photo, and any linked identity. Because the AT Protocol exposes public data openly, Bluesky is unusually rich for graph and timeline analysis compared to walled-garden networks.

## How to use it (`bestInteractionPattern`: web-manual)
1. On `https://bsky.app`, search the handle or name, or go directly to `bsky.app/profile/<handle>`.
2. Read the profile: display name, `@handle.domain`, bio, avatar/banner, join date, follower/following counts.
3. Scroll posts and replies for content, timing, and location/context clues; open the followers/following lists to map associates.
4. For bulk/repeatable work, hit the public API (`public.api.bsky.app`, e.g. `getProfile`, `getFollows`, `getAuthorFeed`) or the firehose — no auth needed for public records.
5. Pivot: a custom-domain handle (e.g. `alice.example.com`) ties the account to a `domain` you can WHOIS; the avatar feeds reverse-image; associates feed graph analysis.

## Inputs → Outputs
- **In:** `username`/handle, `name`
- **Out:** `social-profile`, `name`, `image`, `associate` (follow graph); posts as free-text context
- **Empty/negative result looks like:** search returns no account for the handle, or a profile with zero posts/follows — no usable presence. Handles can be squatted/renamed; verify by content, not name alone.

## Gotchas & OpSec
- Handles are mutable and can use custom domains; the stable identifier is the account's DID, not the handle — record the DID when it matters.
- OpSec: read-only browsing and the public API are **passive**; following/liking from an account is visible. Use a sock puppet to interact.
- Content is user-generated and can be impersonation; corroborate identity claims.

## Overlaps ("do both")
- Pairs with cross-platform username tools like `[[nexfil]]` — those flag that the handle exists on Bluesky; here you extract the actual graph, posts, and any custom-domain link to pivot on.

## Trust & verifiability
`trust: community` — a real, major network with an open, reliably-queryable graph; the data is authentic to the account but self-published, so treat claims within posts as unverified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bluesky |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, image, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
