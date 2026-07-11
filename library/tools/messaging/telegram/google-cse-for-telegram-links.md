---
id: google-cse-for-telegram-links
name: Google CSE for Telegram links
description: Use when you have a keyword, `name`, or `username` and want public Telegram channels/groups mentioning it — returns Google-indexed t.me links to public Telegram resources.
url: https://cse.google.com/cse?cx=006368593537057042503:efxu7xprihg
category: messaging
path:
- messaging
- telegram
bestFor: Finding public Telegram channels and groups by keyword via a pre-scoped Google Custom Search Engine.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- username
status: degraded
pricing: free
costNote: Free hosted Google Custom Search Engine; no account required.
opsec: passive
opsecNote: Queries go to Google CSE, not to Telegram, so you never touch the target's Telegram or the channels themselves during search — nobody is notified. Only join/view channels from a sock-puppet Telegram account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party Google Custom Search Engine over t.me and Telegram-directory pages; coverage is only what Google has indexed and decays as the CSE config ages.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Telegram links CSE
- Google CSE Telegram
tags:
- telegram
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Google CSE for Telegram links

> A pre-built Google Custom Search Engine scoped to Telegram — a keyword-to-`t.me` shortcut for discovering public channels and groups that Telegram's own search buries.

## When to use
You have a keyword, `name`, `username`, or topic and want to find public Telegram channels/groups connected to it — e.g. a subject's handle, a location-based group, or a community a person of interest frequents. Telegram's native search is weak for discovery, so leaning on Google's index via this CSE surfaces public `t.me` links you'd otherwise miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL in a sock-puppet browser.
2. Enter the keyword/`name`/`username` (add a location or distinctive term to reduce noise).
3. Read the results: Google-indexed links to public Telegram channels, groups, and profile/directory pages.
4. Open promising `t.me` links only from a sock-puppet Telegram account; do not join from your real identity.
5. Pivot: a channel/username feeds Telegram-specific tools and username enumeration; membership/context hints at a subject's networks.

## Inputs → Outputs
- **In:** keyword, `name`, or `username`
- **Out:** `t.me` links to public channels/groups, associated `username`/`social-profile` pages
- **Empty/negative result looks like:** few/no hits — the resource is private (not indexable), too new, or the CSE config is stale. A miss reflects Google's index, not proof the channel doesn't exist; try other Telegram search tools.

## Gotchas & OpSec
- Index-limited: only publicly Google-indexed Telegram pages appear; private/invite-only channels are invisible.
- Stale CSE: the engine is a fixed third-party config and may not reflect current indexing — coverage degrades over time.
- OpSec: search is passive (hits Google); the risk is on *access* — join/view channels only from a sock puppet.

## Overlaps ("do both")
- Pairs with dedicated Telegram search/scraping tools and with raw `site:t.me` Google dorks — the CSE is one pre-tuned lens; run others too, as each indexes different public channels.

## Trust & verifiability
`trust: unverified` — a third-party CSE whose coverage depends entirely on Google's Telegram index and the config's freshness; verify each channel by opening it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-cse-for-telegram-links |
| category | messaging |
| selectorsIn → selectorsOut | name → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
