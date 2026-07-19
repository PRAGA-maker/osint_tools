---
id: find-telegram-channels-bots-groups
name: Find Telegram Channels/Bots/Groups
description: Use when you have a topic, name, or keyword and want to discover related Telegram channels/groups/bots — returns channel links, descriptions and subscriber counts.
url: https://xtea.io/ts_en.html
category: messaging
path:
- messaging
bestFor: Keyword discovery of Telegram channels, groups, and bots without joining or logging in.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free unlimited searching; a paid Pro tier only removes ads. No account needed to search or open results.
opsec: passive
opsecNote: Searching XTEA's index is passive and does not touch Telegram or the target. Opening/joining a channel from the results IS an active step inside Telegram — use a sock-puppet Telegram account, never your real one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party search index (~50k channels across 143 countries); coverage is partial and it self-reports no query logging. Treat it as a discovery aid, not a complete map of Telegram.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- telegram
- telegago
tags:
- telegram
- messaging
- channel-search
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Find Telegram Channels/Bots/Groups

> XTEA's Telegram search engine — a keyword-driven index of ~50,000 channels, groups, and bots for finding Telegram communities tied to a topic, place, or handle.

## When to use
Telegram has no built-in global search across public channels, so when your subject or case points to a topic, a local community, a marketplace, or a specific `username`, use XTEA to discover the relevant Telegram spaces to review. Good for locating regional/interest communities a missing person or associate might frequent, and for turning a bare channel name into a joinable link.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://xtea.io/ts_en.html.
2. Enter a topic, channel name, place, or keyword in the search box.
3. Review the results: channel/group/bot titles, descriptions, subscriber counts, and category.
4. Note candidates worth reviewing; the "open in Telegram" links jump straight to the channel.
5. To actually read/join, switch to a sock-puppet Telegram account (see OpSec) rather than opening from a real identity.
6. Pivot: a discovered channel → review members/admins and pinned content in Telegram; a `username` → cross-platform username checks.

## Inputs → Outputs
- **In:** topic / `name` / `username` keyword
- **Out:** matching Telegram channels/groups/bots with `social-profile` links, descriptions, subscriber counts
- **Empty/negative result looks like:** no matches, or only loosely-related channels — the index covers ~50k channels, a small slice of Telegram, so absence here is weak evidence. Try alternate keywords, transliterations, or another Telegram search index.

## Gotchas & OpSec
- Coverage is partial: only indexed public channels appear; private/invite-only groups and the long tail are missing.
- Discovery is passive, but the moment you open or join a channel you are acting inside Telegram — that can expose your account to admins and bots. Always use a dedicated sock-puppet account and number.
- Result metadata (subscriber counts, descriptions) can be stale or self-declared.

## Overlaps ("do both")
- Pairs with `[[telegago]]` (Google-CSE-based Telegram search) and `[[telegram]]` itself — run the same keyword through more than one index, since each covers a different slice of public channels.

## Trust & verifiability
`trust: community` — an independent index of unknown completeness; use it to find leads, then verify anything substantive inside Telegram against the live channel.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-telegram-channels-bots-groups |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
