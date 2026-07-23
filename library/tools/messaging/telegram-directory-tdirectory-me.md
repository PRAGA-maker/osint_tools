---
id: telegram-directory-tdirectory-me
name: Telegram Directory (tdirectory.me)
description: Use when you have a `name`, keyword, or topic and want to discover public Telegram channels/groups/bots tied to a person or interest — returns matching `social-profile` links plus channel analytics.
url: https://tdirectory.me
category: messaging
path:
- messaging
bestFor: Discovering public Telegram channels, groups, and bots by name or keyword.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to search and browse; no account required. Listings are owner-submitted plus indexed.
opsec: passive
opsecNote: Searching the directory is passive — you query tdirectory.me, not Telegram itself, so the channel owner is not notified. Only when you click through and JOIN a Telegram channel do you become visible to it; browse the directory first, and join from a sock-puppet Telegram account if you must.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party, largely owner-submitted directory; entries are self-listed and rated by users, so coverage is partial and metadata unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- tdirectory
- tdirectory.me
- Telegram Directory
tags:
- telegram
- directory
source: osintambition-social
lastVerified: '2026-07-23'
enrichment: full
---

# Telegram Directory (tdirectory.me)

> A searchable, owner-submitted index of public Telegram channels, groups, and bots — a discovery layer over Telegram, since Telegram's own search is weak.

## When to use
You have a `name`, brand, handle, or topic and want to find associated public Telegram presences — a person's channel, a community group, or a bot they run. Reach for this when Telegram's in-app search isn't surfacing what you need, or when you want channel metadata (subscriber counts, category, reviews) without joining. It indexes only public, listed entities, so it won't reveal private groups or membership.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tdirectory.me and search by `name`, `username`, or keyword.
2. Browse results by category or popularity; open a listing to see its description, subscriber/member counts, category, and user reviews.
3. Note the direct `t.me/...` link — that is the pivot into Telegram itself.
4. To view the actual channel content, open the `t.me` link; only JOIN from a sock-puppet Telegram account if you need to read a members-only group.
5. Pivot: a discovered channel/handle feeds Telegram-specific OSINT (member analysis, message search) and username lookups elsewhere.

## Inputs → Outputs
- **In:** `name`, `username`, or topic keyword
- **Out:** `social-profile` links (`t.me/...`) plus directory metadata (category, subscriber counts, reviews)
- **Empty/negative result looks like:** no listings match — the entity may simply be unlisted (directory is opt-in/partial), not that it doesn't exist on Telegram.

## Gotchas & OpSec
- Coverage is partial: it indexes only channels/groups/bots that were submitted or crawled, so absence is not proof.
- Listings are self-submitted and user-rated — treat descriptions and stats as unverified leads.
- OpSec: passive while browsing; joining a Telegram channel exposes your account — use a sock puppet.

## Overlaps ("do both")
- Complements in-app Telegram search and dedicated Telegram-analytics tools — use tdirectory to *find* the channel, then those tools to analyse members and messages. Cross-check with other Telegram directories, since each indexes a different subset.

## Trust & verifiability
`trust: unverified` — a third-party, opt-in directory; the `t.me` link it gives you is the ground truth, so always click through and confirm the channel on Telegram itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-directory-tdirectory-me |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
