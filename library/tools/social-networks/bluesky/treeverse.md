---
id: treeverse
name: Treeverse
description: Use when you have a Bluesky post or thread URL and want to see the full reply structure and participants — returns a hierarchical thread tree of associate/social-profile leads.
url: https://treeverse.app/
category: social-networks
path:
- social-networks
- bluesky
bestFor: Visualizing a Bluesky conversation's full reply tree to surface participants and context.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free web app; open-source (created by Paul Butler). No account or payment required.
opsec: passive
opsecNote: Reads public Bluesky content via the public API without interacting with the target's account — fully passive, no notification to participants.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source hobby tool by a known developer; it only re-renders public Bluesky data, so accuracy tracks the platform's public API.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- treeverse.app
- Bluesky thread visualizer
tags:
- bluesky
- thread-visualization
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Treeverse

> A free web app that renders a Bluesky conversation as a navigable tree — the fastest way to see everyone who replied and how a thread branched.

## When to use
You have a Bluesky post/thread (a `social-profile`'s post URL or an `at://` URI) and want the whole conversation structure at a glance: who replied to whom, which sub-threads exist, and which accounts are involved. Good for enumerating participants (`associate` leads) around a subject and for reconstructing context that the linear Bluesky UI buries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://treeverse.app/.
2. Paste a Bluesky post URL or `at://` URL for the thread you want to explore.
3. Read the generated tree: each node is a post, branches are replies; click through to expand context and identify participating accounts.
4. Pivot: participant handles feed `[[social-profiles-finder]]` and username enumeration; the reply graph highlights an `associate` cluster around your subject.

## Inputs → Outputs
- **In:** Bluesky post/thread URL or `at://` URI (a `social-profile`'s content)
- **Out:** hierarchical thread tree, participating accounts (`social-profile`/`associate` leads)
- **Empty/negative result looks like:** a thread with no replies renders as a single node; deleted posts or a bad URL yield nothing — absence of replies is not absence of the account.

## Gotchas & OpSec
- Bluesky-only — it does not visualize Twitter/X (the older Treeverse browser extension for Twitter is separate and largely broken by X API changes).
- Only public data; private/blocked content won't appear.

## Overlaps ("do both")
- Pairs with `[[social-profiles-finder]]`: Treeverse maps the conversation participants on Bluesky, then a profile finder expands each participant across other networks.

## Trust & verifiability
`trust: community` — an open-source visualizer that only re-presents public Bluesky API data; verify any participant by opening their actual Bluesky profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | treeverse |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
