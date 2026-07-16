---
id: telegramchannels-me
name: Telegramchannels.me
description: Use when you have a `username`, `name`, or keyword and want to discover public Telegram channels — returns `social-profile` links to matching/ranked channels.
url: https://telegramchannels.me/list/biggest?language=en
category: messaging
path:
- messaging
bestFor: Browsing and searching a directory of public Telegram channels, ranked by subscriber count and language.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse and search the public channel directory; no account required.
opsec: passive
opsecNote: Browsing a public web directory of already-public Telegram channels leaks nothing to any subject and needs no Telegram login. Standard web hygiene (clean session) is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party Telegram channel directory/rating site; listings are crawled from public channels, coverage is partial, and the operator is anonymous.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- telegram-channels
aliases:
- telegramchannels.me
tags:
- Messengers
- Telegram
- channel-directory
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Telegramchannels.me

> A searchable web directory of public Telegram channels, ranked by size and language — a way to find and contextualize channels a subject runs or follows without opening Telegram.

## When to use
You have a channel `username`, a subject `name`/handle, or a topic keyword and want to locate the associated public Telegram channel(s), gauge their size, and read the description/category — from a browser, without a Telegram account. Useful for placing a subject in a community, finding a channel they administer, or scoping a channel before joining from a sock puppet.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://telegramchannels.me in a clean browser.
2. Use the site search or category/language lists to look up a channel name, handle, or keyword.
3. Read the listing: channel title, `@username`, subscriber count, category, and description (`social-profile`).
4. Follow the link to the channel's public preview (t.me) to review content passively.
5. Pivot: a channel a subject admins/posts in reveals topics and associates; feed the `@username` into Telegram-specific search bots.

## Inputs → Outputs
- **In:** channel `username`, subject `name`/handle, or keyword
- **Out:** matching channel listings — title, `@username`, subscriber count, category (`social-profile`)
- **Empty/negative result looks like:** no directory matches — the channel is small, private, or simply not indexed here (the directory favors larger public channels), which is not proof it doesn't exist.

## Gotchas & OpSec
- Coverage skews to big, public channels; small or niche channels tied to an individual may be absent.
- Directory metadata (subscriber counts, categories) can be stale — confirm on the live t.me preview.
- It indexes channels, not individual users' private chats; don't expect person-level results.

## Overlaps ("do both")
- Pairs with `[[telegram-channels]]` and Telegram search bots (e.g. `[[surftg-bot]]`) — this is discovery/ranking; those search message content inside channels.

## Trust & verifiability
`trust: unverified` — an anonymous third-party directory; listings point to real public channels, but treat counts/categories as approximate and verify on Telegram itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegramchannels-me |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
