---
id: telegram-search-engine
name: Telegram Search Engine
description: Use when you have a keyword, link, or `username` and want to find which public Telegram channels posted it — returns channel names and posts mentioning the term.
url: https://clickbee.me/Telegram-Search-Engine.html
category: messaging
path:
- messaging
bestFor: Checking whether a keyword, referral link, or handle has been posted recently in public Telegram channels.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free web search tool; no account needed to run a query. The parent site (ClickBee) also runs unrelated crypto "earn" bots.
opsec: passive
opsecNote: Passive — you search ClickBee's index of public channel posts, not Telegram directly, so no channel is alerted. Note the operator's reputation is questionable; avoid its bots and don't enter credentials or wallet info anywhere on the site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Operated by ClickBee, whose main business is crypto-reward bots of dubious reputation; the channel-search feature works but the operator is untrusted, so corroborate any hit directly in Telegram.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- telegram-search
- telegago
aliases:
- ClickBee Telegram Search
- clickbee.me telegram search
tags:
- telegram
- messaging
- keyword-search
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Telegram Search Engine

> A keyword search over public Telegram channel posts — enter a phrase, link, or handle and see which channels recently posted it.

## When to use
You have a keyword, a referral/URL, or a `username`/`name` and want to know whether and where it surfaced in public Telegram channels. It is aimed at content discovery: tracing where a link, phrase, or handle spread across channels. In an investigation this can locate the channels discussing a subject or amplifying a specific message/link — a different angle from handle/channel-name discovery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://clickbee.me/Telegram-Search-Engine.html.
2. Enter the keyword, link, or handle you want to trace.
3. Review the returned channels/posts that recently contained the term.
4. Verify each hit by opening the channel/post directly in Telegram (the tool's index can be stale or incomplete).
5. Pivot: a channel that posted the term feeds channel-analysis tools; a recurring handle feeds cross-platform username enumeration.

## Inputs → Outputs
- **In:** keyword, link, or `username`/`name`
- **Out:** `social-profile` (public channels/posts containing the term), `username` (channel handles)
- **Empty/negative result looks like:** no matches — the term wasn't in ClickBee's recent public-channel index (which is partial and recency-biased), not proof it never appeared on Telegram.

## Gotchas & OpSec
- **Operator caution:** ClickBee's primary product is crypto "earn" bots with a poor reputation; use only the search page, avoid its bots, and never enter credentials or wallet details.
- Coverage is partial and skewed to recent public-channel posts; private channels and older content are invisible.
- Always confirm a hit inside Telegram before relying on it — treat the tool as a pointer, not evidence.
- OpSec: passive; no channel is notified by your search.

## Overlaps ("do both")
- Pairs with `[[telegram-search]]` (a Google CSE over t.me pages) and `[[telegago]]` — each indexes public Telegram differently, so running the same term through all three catches channels any single one misses.

## Trust & verifiability
`trust: unverified` — a feature of a low-reputation operator; the search results are real but the source is untrusted, so every finding must be corroborated directly in Telegram.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-search-engine |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
