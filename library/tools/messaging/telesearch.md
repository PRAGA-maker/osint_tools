---
id: telesearch
name: TeleSearch (telesearch.me)
description: Use when you have a `name`/keyword and want to find public Telegram channels, groups, and bots about it — returns social-profile leads with subscriber counts and join links.
url: https://telesearch.me/
category: messaging
path:
- messaging
bestFor: Discovering public Telegram channels/groups/bots by keyword or topic.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free web directory of Telegram communities; no account needed to search.
opsec: passive
opsecNote: You search a website, not from your Telegram account, so this discovery step doesn't expose your Telegram identity to channel owners. Opening/joining a found channel from your Telegram client is a separate, active step — use a sock-puppet account for that.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A user-submitted Telegram directory ("registered by users") with a disclaimer that it doesn't vet content. Good for discovery; listings are self-submitted, so coverage is partial and quality varies.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- telesearch.me
tags:
- telegram
- channel-search
- directory
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# TeleSearch (telesearch.me)

> A web directory for finding public Telegram channels, groups, and bots by keyword — searchable without a Telegram account.

## When to use
You want to find where a topic, community, or handle lives on Telegram, and you'd rather search a website than message a bot from your account. Enter a `name`/keyword and get listed channels/groups/bots with subscriber counts and join links — a low-exposure way to scope Telegram before you touch it with a sock-puppet client.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open telesearch.me.
2. Search by keyword/`name`/`username`, or browse categories (channels, groups, bots).
3. Review results: community name, subscriber count, language, and a join/open link.
4. Pivot: open promising channels in a **sock-puppet** Telegram client to verify, read history, and enumerate members/links.

## Inputs → Outputs
- **In:** `name` / keyword / `username`
- **Out:** `social-profile` listings — Telegram channels/groups/bots with subscriber counts and join links
- **Empty/negative result looks like:** no or only loosely-related listings — the community isn't self-submitted to this directory (it indexes submissions, not all of Telegram). A blank here doesn't mean nothing exists on Telegram; try a bot-based search too.

## Gotchas & OpSec
- Coverage is submission-based, so it misses channels that never registered — treat it as one discovery angle, not exhaustive.
- OpSec: searching the site is passive; joining/opening a channel from Telegram is active — do that only from a burner account.
- No content vetting: results can include scam/illegal channels; approach with caution.

## Overlaps ("do both")
- Pairs with in-Telegram search bots (like `[[oksearch]]`) and other Telegram indexes — a web directory and a bot index cover different submissions, so run both when scoping a subject's Telegram footprint.

## Trust & verifiability
`trust: community` — a self-submission directory with no content vetting. Reliable as a discovery pointer; verify any hit by opening the actual channel and corroborating it's your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telesearch |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
