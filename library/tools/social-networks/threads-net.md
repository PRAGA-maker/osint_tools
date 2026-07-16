---
id: threads-net
name: Threads
description: Use when you have a `username` (usually the subject's Instagram handle) and want their Threads posts, bio and network — returns `social-profile`, `name`, post content.
url: https://www.threads.net/login
category: social-networks
path:
- social-networks
bestFor: Reading a subject's Threads posts and confirming the Instagram-linked identity behind a handle.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free to view; public profiles/posts are partly readable logged-out, but full browsing (scrolling, replies, followers) increasingly prompts a login.
opsec: passive
opsecNote: Viewing public posts is passive, but Threads is a Meta property tightly coupled to Instagram — logging in to see more ties your (sock-puppet) account to the viewing and can surface you in suggestions. Use a dedicated puppet, never a personal Meta account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Meta/Instagram platform; profile data is authoritative for that account, though anyone can create a handle.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Threads by Instagram
- threads.com
tags:
- threads
- Threads Related Sites
- instagram
- meta
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- threads
---

# Threads

> Meta's text-based social app, tightly bound to Instagram: a Threads `@handle` is (almost always) the same account as the subject's Instagram, making it a direct identity and activity pivot.

## When to use
You have a `username` — typically the subject's Instagram handle, since Threads accounts are created from Instagram — and want their text posts, bio, and follower/following signals. Because the handle is shared with Instagram, confirming a Threads profile both surfaces fresh posts and corroborates the Instagram identity. High value: people who've gone quiet on other platforms often still post here.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://www.threads.com/@<username>` (threads.net now redirects to threads.com). Public posts are partly viewable logged-out.
2. Read the bio, pinned/recent posts, and linked Instagram account.
3. To scroll the full timeline, replies and follower lists you'll usually be prompted to log in — use a sock-puppet Meta account.
4. Capture post timestamps, media, mentioned locations/people, and the linked Instagram handle.
5. Pivot: jump to the linked Instagram profile, reverse-image any media, and enumerate the handle on other platforms.

## Inputs → Outputs
- **In:** `username` (Instagram/Threads handle) or `name`
- **Out:** `social-profile` (posts, bio, linked Instagram), `name`
- **Empty/negative result looks like:** "user not found" or a private account showing only a bio — the handle has no Threads presence or is locked; a private account still confirms the identity exists.

## Gotchas & OpSec
- Threads and Instagram share the handle and login — a Threads find is also an Instagram lead, and vice versa.
- Logged-out viewing is increasingly limited; deeper browsing needs a puppet login, which couples your account to the target's ecosystem.
- Anyone can register a handle — confirm identity via linked Instagram/content, not the name alone.

## Overlaps ("do both")
- Pairs with Instagram tooling — the accounts are linked, so always check both; posts, followers and media often differ between the two surfaces.

## Trust & verifiability
`trust: trusted` — first-party Meta platform, so the account data is authoritative; identity attribution still needs corroboration since handles are self-chosen.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threads-net |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
