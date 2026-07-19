---
id: lyzem-blog
name: Lyzem
description: Use when you have a `username`/keyword and want public Telegram channels, groups, and messages — returns matching Telegram content and channel social-profiles.
url: https://lyzem.com/
category: messaging
path:
- messaging
bestFor: Searching public Telegram channels, groups, and messages by keyword or username without joining anything.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Telegram search engine; no account needed to search public content.
opsec: passive
opsecNote: Searches an external index of already-public Telegram content, so you do not join channels or reveal a Telegram account — passive. If you then open a channel inside Telegram to verify, use a sock-puppet Telegram account, since viewing/joining there can be observable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Telegram search index; coverage is limited to public channels it has crawled, and results can be stale — treat as a discovery layer, then verify in Telegram.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Lyzem search
- lyzem.com Telegram search
tags:
- telegram
- messaging-osint
- channel-search
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Lyzem

> A web search engine for public Telegram — find channels, groups, and messages by keyword or username without joining anything or exposing a Telegram account.

## When to use
You have a `username`/handle, `name`, org, or distinctive keyword and want to know where it appears across public Telegram: which channels/groups mention it, whether the subject runs or posts in a channel, and what's been said. Because Telegram is largely invisible to Google, a dedicated index like Lyzem is the practical entry point — and searching from the web keeps you off the platform.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://lyzem.com/ and enter a username, name, or keyword.
2. Review results: channels/groups and message hits, with links to the public Telegram content.
3. Read for the channel `@handle`, description, message context, and dates.
4. Pivot: a found `@handle` feeds username enumeration and Telegram profile tools; message content anchors a timeline; to verify, open the channel in a sock-puppet Telegram client.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword
- **Out:** matching Telegram channels/groups/messages → channel `social-profile`s and `@handles`
- **Empty/negative result looks like:** no hits — the content may be in private channels (uncrawlable), too new, or not indexed; cross-check with other Telegram search tools before concluding absence.

## Gotchas & OpSec
- Only PUBLIC channels/messages the index has crawled are searchable; private/invite-only content is invisible.
- Results can lag; verify anything important directly in Telegram (via a sock-puppet account).
- OpSec: passive from the web; joining/viewing inside Telegram is the observable step — protect it.

## Overlaps ("do both")
- Pairs with `[[telegcrack-com]]` (Telegra.ph articles) and other Telegram channel/username tools — each indexes a different slice of the Telegram ecosystem; run several.

## Trust & verifiability
`trust: community` — a third-party index of public Telegram; discovery is genuine but coverage is partial and possibly stale, so confirm in-platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lyzem-blog |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
