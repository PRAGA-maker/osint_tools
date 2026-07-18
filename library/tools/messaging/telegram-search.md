---
id: telegram-search
name: Telegram Search
description: Use when you have a `username`, `name`, or keyword and want to find public Telegram channels/groups/posts — returns social profiles and channel links.
url: https://cse.google.com/cse?cx=004805129374225513871:p8lhfo0g3hg
category: messaging
path:
- messaging
bestFor: Google-powered keyword search restricted to public Telegram channel/group web pages (t.me links).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: degraded
pricing: free
costNote: Free Google Custom Search Engine; no account. Coverage is whatever Google has indexed of public t.me pages, filtered by the CSE config.
opsec: passive
opsecNote: Passive — you query Google's index, not Telegram itself, so no channel owner is alerted and you don't join anything. Nothing about your search reaches the target's Telegram.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Google CSE curated by an unknown maintainer; it only surfaces what Google indexes of public Telegram web previews, and the CSE config can silently drift or break over time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- telegram-search-engine
- telegago
aliases:
- Telegram CSE
- Telegram Google Custom Search
tags:
- telegram
- messaging
- custom-search-engine
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Telegram Search

> A Google Custom Search Engine scoped to public Telegram (t.me) pages — keyword-search channels, groups, and posts without joining anything.

## When to use
You have a `username`, a `name`, or a keyword/phrase and want to find where it appears on public Telegram — a channel handle, a group, or an indexed post preview. Because Telegram's own in-app search is limited and requires an account, this CSE is a useful passive way to discover public channels/groups tied to a subject or topic from the outside. Good for locating a subject's public Telegram presence or the communities discussing a topic.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL (cse.google.com/cse?cx=…).
2. Enter the `username`, `name`, or keyword; use quotes for exact phrases.
3. Read the results: links to public t.me channel/group pages and post previews Google has indexed.
4. Open a promising t.me link in a browser (not necessarily the app) to view the public preview before deciding whether to engage.
5. Pivot: a discovered channel/handle feeds Telegram-specific tools; a username can be enumerated across other platforms.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword
- **Out:** `social-profile` (public Telegram channel/group pages), `username` (channel handles)
- **Empty/negative result looks like:** no results — the content isn't indexed by Google (private channels and most in-channel messages aren't), the CSE config has drifted, or the term is too rare; absence here does NOT mean the subject has no Telegram presence.

## Gotchas & OpSec
- **Index-limited:** only public t.me web previews Google has crawled are searchable — the vast majority of Telegram messages are invisible to it.
- Google CSEs decay: the underlying `cx` config or Google's indexing can change, degrading results without notice (status: degraded).
- It finds channels/pages, not message-level content inside groups — use a dedicated Telegram message search for that.
- OpSec: fully passive; you never touch Telegram or join a channel by searching.

## Overlaps ("do both")
- Pairs with `[[telegram-search-engine]]` and `[[telegago]]` — different indexes/approaches to public Telegram; run the same term through each, since coverage barely overlaps and each surfaces channels the others miss.

## Trust & verifiability
`trust: community` — an unofficial Google CSE of unknown curation; results are real Google-indexed pages, but coverage is partial and the config can break, so treat it as one discovery angle, not a complete search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-search |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
