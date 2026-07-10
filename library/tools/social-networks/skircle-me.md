---
id: skircle-me
name: skircle.me
description: Use when you have a Bluesky `username`/handle and want to see who they interact with most — returns an interaction "circle" of their top ~49 most-engaged connections (`associate`/`social-profile`).
url: https://skircle.me/
category: social-networks
path:
- social-networks
bestFor: Mapping a Bluesky user's most-engaged connections from just their handle, no login.
selectorsIn:
- username
selectorsOut:
- associate
- social-profile
status: live
pricing: free
costNote: Free; generates a circle from any public Bluesky handle with no login required.
opsec: passive
opsecNote: Builds the circle from public Bluesky interaction data using only the handle you enter; the target is not notified and you do not need to log in. Bluesky is an open network, so this is inference from public activity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community "interaction circle" generator for Bluesky; the ranking is a heuristic over public engagement, so treat the circle as an indicator of interaction strength, not a definitive relationship map.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- tagsexplorer
aliases:
- Skircle
- Bluesky interaction circle
tags:
- bluesky
- BlueSky / BSky Related Sites
- network-analysis
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# skircle.me

> A Bluesky "interaction circle" generator — enter a handle and see the accounts that user engages with most, ranked by closeness.

## When to use
You have a Bluesky `username`/handle and want a quick map of the subject's closest online contacts. Skircle arranges their top ~49 connections in concentric rings, with the most-engaged accounts nearest the centre — a fast way to surface a person's frequent interlocutors (`associate`) on Bluesky without reading their whole timeline. Because it needs no login and only a public handle, it's a low-friction first pass on a subject's Bluesky social graph.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://skircle.me/.
2. Enter the subject's Bluesky handle (e.g. `name.bsky.social`) — no login needed.
3. Read the circle: inner ring = most-engaged connections, outer rings = weaker ties. Each node is an account (`social-profile`) the subject interacts with.
4. Screenshot the circle; re-run periodically to see how the network shifts over time.
5. Pivot: an inner-circle handle feeds cross-network username search and profile enrichment; compare against the subject's follows/followers.

## Inputs → Outputs
- **In:** Bluesky `username`/handle
- **Out:** interaction circle → `associate` (top ~49 engaged accounts), `social-profile` links, relative closeness
- **Empty/negative result looks like:** a sparse or empty circle — the account is new, low-activity, or the handle is wrong. Absence reflects low public engagement, not necessarily few real relationships.

## Gotchas & OpSec
- The ranking is a **heuristic** over public engagement (likes/replies/reposts) — closeness on the circle ≠ confirmed real-world relationship.
- Bluesky-only; says nothing about the subject's ties on other platforms.
- OpSec: **passive** — inference from public data, no login, no notification to the subject.

## Overlaps ("do both")
- Conceptually pairs with `[[tagsexplorer]]` (Twitter/X conversation networks) — each maps a subject's most-engaged contacts on its own platform; run per-platform and compare recurring names.

## Trust & verifiability
`trust: community` — a fun, useful community tool built on public Bluesky data; the circle is a strong indicator of interaction intensity but should be corroborated before asserting a relationship.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skircle-me |
| category | social-networks |
| selectorsIn → selectorsOut | username → associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
