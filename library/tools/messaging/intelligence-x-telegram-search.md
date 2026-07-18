---
id: intelligence-x-telegram-search
name: Intelligence X Telegram Search
description: Use when you have a keyword or `username` and want to search public Telegram content — returns channels/posts via Google CSEs and Telegago.
url: https://intelx.io/tools?tab=telegram
category: messaging
path:
- messaging
bestFor: A one-page launcher for multiple Google-based public Telegram searches (two CSEs plus Telegago).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: The Telegram search launchers on the tools page are free to use; Intelligence X's own paid breach-search product is separate and not required here.
opsec: passive
opsecNote: Passive — the launchers run Google searches over public t.me pages; you don't touch Telegram or join channels, and no channel owner is alerted. IntelX notes it isn't responsible for third-party results.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Intelligence X is a reputable OSINT vendor, but these Telegram launchers are thin wrappers over third-party Google CSEs and Telegago, so coverage/quality is inherited from those and can drift.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- telegago
- telegram-search
- facebook-graph-searcher-intelligencex
- intelligence-x
- intelligence-x-2
- intelligence-x-person-tools
- intelligencex
- intelligencex-linkedin-search
- intelx-io
aliases:
- IntelX Telegram tools
- intelx.io telegram
tags:
- bellingcat-toolkit
- telegram
- custom-search-engine
source: bellingcat-toolkit
lastVerified: '2026-07-18'
enrichment: full
---

# Intelligence X Telegram Search

> Intelligence X's free tools page for Telegram — a launcher bundling two Google Custom Search Engines and Telegago to search public channels.

## When to use
You have a keyword, phrase, or `username`/`name` and want to search public Telegram from the outside without an account. This IntelX tools tab gathers several Google-based Telegram searches (CSE 1, CSE 2, and the well-known Telegago) in one place, so you can run the same term through multiple indexes quickly. Useful for finding a subject's public channels/handles or the communities discussing a topic, and for comparing coverage across engines.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://intelx.io/tools?tab=telegram.
2. Enter your term in one of the Telegram search boxes (CSE 1, CSE 2, or Telegago) and run it.
3. Review the Google-indexed public t.me results: channel pages, group pages, and post previews.
4. Re-run the same term in the other launchers — each CSE is configured differently and surfaces different channels.
5. Pivot: open promising t.me links in a browser to view previews; feed discovered handles into cross-platform username enumeration.

## Inputs → Outputs
- **In:** keyword, phrase, or `username`/`name`
- **Out:** `social-profile` (public Telegram channels/posts), `username` (channel handles)
- **Empty/negative result looks like:** no results across the launchers — the content isn't Google-indexed (private channels and most in-channel messages aren't), so absence here is a coverage limit, not proof of no Telegram presence.

## Gotchas & OpSec
- These are wrappers over third-party Google CSEs/Telegago — IntelX explicitly disclaims responsibility for their results, and a CSE can silently degrade.
- Only public, Google-indexed t.me pages are searchable; the bulk of Telegram traffic is invisible.
- Don't confuse this free Telegram launcher with IntelX's paid breach-data search — different product.
- OpSec: passive; you query Google, never Telegram directly.

## Overlaps ("do both")
- Pairs with `[[telegago]]` (the same engine, standalone) and `[[telegram-search]]` (another t.me CSE) — running a term across all of them maximizes the public channels you surface, since each index differs.

## Trust & verifiability
`trust: community` — hosted by a reputable vendor but functionally dependent on third-party Google CSEs; results are real indexed pages, yet coverage is partial and inherited, so treat it as one discovery angle among several.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelligence-x-telegram-search |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
