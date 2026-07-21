---
id: commentgram-cse
name: Commentgram CSE
description: Use when you have a `username`, `name` or keyword and want to search across indexed Telegram channel comments/discussion for it — returns matching Telegram posts and commenter `social-profile` links.
url: https://cse.google.com/cse?cx=006368593537057042503:ig4r3rz35qi#gsc.tab=0
category: messaging
path:
- messaging
bestFor: Keyword/username search over Google-indexed Telegram comment and discussion pages via a purpose-built Custom Search Engine.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account or key. Results limited to what Google has indexed.
opsec: passive
opsecNote: Passive — you query Google's index, not Telegram directly, so the target's channel is not touched and gets no signal. Heavy repeated querying can trigger a Google CAPTCHA; solve it and continue.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party Google CSE (creator-defined site list); its coverage scope is opaque and can silently drift, so absence of results is not proof of absence.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Commentgram
- Telegram comments CSE
tags:
- Messengers
- Telegram
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Commentgram CSE

> A Google Custom Search Engine scoped to Telegram comment/discussion pages — a passive way to find where a handle or phrase shows up in Telegram threads that Google has indexed.

## When to use
You have a `username`, `name`, or distinctive phrase and want to see if it appears in **Telegram channel comments and discussion groups** without querying Telegram itself. Useful for tying a handle to conversations, surfacing a commenter's other posts, or finding the channel context around a keyword.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL and enter the `username` (with and without `@`), `name`, or phrase.
2. Use quotes for exact handles and standard Google operators to narrow.
3. Open results to the underlying Telegram post/comment; read the commenter's handle and surrounding thread.
4. Cross-check the handle directly on Telegram (or another Telegram-search tool) to confirm it's live and current.
5. Pivot: a confirmed handle feeds cross-platform username checks; a channel feeds channel-level Telegram OSINT.

## Inputs → Outputs
- **In:** `username` / `name` / keyword
- **Out:** Telegram post/comment links and commenter `social-profile` (handle)
- **Empty/negative result looks like:** no hits — meaning Google hasn't indexed matching Telegram pages (indexing of Telegram is patchy), *not* that the handle is absent from Telegram; verify with a native Telegram search.

## Gotchas & OpSec
- Coverage is limited to Google's index of Telegram web pages, which is incomplete and time-lagged — a null result is weak evidence.
- The CSE's included-site scope is defined by its creator and can change without notice.
- Heavy use may throw a Google CAPTCHA (solve manually).
- OpSec: passive — the target's Telegram channel receives no visit from you.

## Overlaps ("do both")
- Pairs with `[[intelligence-x-telegram-search]]`, `[[find-telegram-channels-bots-groups]]` and `[[lyzem-blog]]` — each indexes Telegram differently, so run several; where this CSE misses a handle, a native Telegram search engine may catch it.

## Trust & verifiability
`trust: unverified` — a community-built Google CSE with an opaque, mutable site list; treat hits as leads and confirm the handle/thread on Telegram directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | commentgram-cse |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
