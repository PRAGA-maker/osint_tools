---
id: tgram-io
name: Tgram.io
description: Use when you have a `username`, name or topic keyword and want to find public Telegram channels, groups or bots — returns matching Telegram `social-profile`s to join or monitor.
url: https://tgram.io
category: messaging
path:
- messaging
bestFor: Discovering public Telegram channels/groups/bots by keyword, topic or handle.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse and search; no account. It only indexes public channels/groups that opt into directories.
opsec: passive
opsecNote: Searching the tgram.io directory is passive — the target's channel doesn't see you. Opening/joining a Telegram channel from the results IS visible to that channel's admins and exposes your Telegram account, so use a sock-puppet Telegram identity for anything sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Telegram directory; it aggregates public listings and is not affiliated with Telegram, so coverage is partial and freshness varies.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- tgram.io
tags:
- telegram
- search
- directory
source: osintambition-social
lastVerified: '2026-08-04'
enrichment: full
---

# Tgram.io

> A public directory and search for Telegram — look up channels, groups and bots by keyword, topic, language or handle.

## When to use
You have a `username`, a name, or just a subject/topic and want to find associated public Telegram communities — a channel a subject runs, groups around a locale or interest, or bots tied to a service. Useful for scoping where a person or community congregates on Telegram before you monitor or join.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tgram.io.
2. Use the search bar for a handle/keyword, or browse the category and language filters (IT, Culture, Science, etc.).
3. Read the listings — each shows the channel/group name, `@handle`, description and a direct Telegram link.
4. Note candidate `social-profile`s; open promising ones in Telegram to review membership, pinned posts and activity.
5. Pivot: cross-check a discovered `@handle` with other Telegram search/analytics tools and with username-OSINT to tie the handle to a person.

## Inputs → Outputs
- **In:** `username` / name / topic keyword
- **Out:** Telegram channel/group/bot `social-profile`s (handles + links)
- **Empty/negative result looks like:** no listings for your term — meaning nothing matching is in this directory, not that no such channel exists (private/undirectoried channels won't appear). Try another Telegram search index before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none for search; joining a channel is a manual, identity-exposing step.
- OpSec: browsing tgram.io is **passive**, but the moment you open or join a channel in Telegram your account is exposed to its admins — always use a puppet Telegram account for sensitive work.
- Directory coverage is partial and can be stale; absence from tgram.io proves nothing.

## Overlaps ("do both")
- Pair with other Telegram search/analytics indexes and with username-OSINT — different directories index different channels, and username lookups tie a discovered handle back to a real identity.

## Trust & verifiability
`trust: community` — an unofficial aggregator of public Telegram listings; treat hits as leads and verify each channel directly in Telegram.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tgram-io |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
