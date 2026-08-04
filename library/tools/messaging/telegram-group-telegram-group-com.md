---
id: telegram-group-telegram-group-com
name: Telegram Group (telegram-group.com)
description: Use when you have a topic/keyword and want relevant Telegram communities — a directory that returns public groups/channels/bots as `social-profile` join links.
url: https://www.telegram-group.com
category: messaging
path:
- messaging
bestFor: Discovering public Telegram groups, channels and bots by topic or keyword.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free directory; browsing and join links require no account (joining a group needs a Telegram account).
opsec: passive
opsecNote: Browsing the directory is passive. Actually JOINING a group is active and exposes your Telegram account/username to that group's members and admins — use a sock-puppet Telegram account (separate number), never your real one, when entering a subject's community.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run listing (heavily Israel/Hebrew-oriented but multi-language); coverage is partial and self-submitted, so it's a discovery aid, not a complete index of Telegram.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- telegram-group-find-telegram-channels-bots-and-groups
aliases:
- telegram-group.com
tags:
- telegram
- groups
- directory
source: osintambition-social
lastVerified: '2026-08-04'
enrichment: full
---

# Telegram Group (telegram-group.com)

> A searchable directory of public Telegram groups, channels and bots — a way in when you know a topic or community keyword but not the specific chat.

## When to use
You want to find Telegram communities relevant to a subject, location, or interest — e.g. a local group, a topic channel, or bots tied to a theme — and need a starting list of join links. Useful for community-mapping and for locating where a subject's interest-group discussions happen before you monitor or (carefully) join.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.telegram-group.com.
2. Search by keyword or browse the topic categories; results show group name, description, member count, creation date and a join link.
3. Note candidate groups/channels — read metrics and descriptions to judge relevance.
4. To go inside, join from a **sock-puppet** Telegram account, not your own.
5. Pivot: a discovered channel/handle feeds Telegram-specific OSINT tools (member/message analysis); group topics feed further community mapping.

## Inputs → Outputs
- **In:** a topic/keyword (`name` of a subject, place, or interest)
- **Out:** public Telegram groups/channels/bots as `social-profile` join links, with member counts and descriptions
- **Empty/negative result looks like:** few/no results for your keyword — the directory is partial and skewed regionally, so a blank result means "not listed here," not "no such Telegram community."

## Gotchas & OpSec
- **Joining is active and identity-exposing** — your Telegram username/number becomes visible to the group; always use a dedicated sock puppet.
- Coverage is self-submitted and regionally skewed (strong Israeli/Hebrew presence); combine with native Telegram search and other directories for completeness.
- Listings can be stale (dead groups, changed links); verify a group is live before relying on it.

## Overlaps ("do both")
- Pairs with [[telegram-group-find-telegram-channels-bots-and-groups]] and native Telegram search — different directories index different communities, so query more than one.

## Trust & verifiability
`trust: community` — a self-submitted community directory; treat listings as leads and verify each group directly in Telegram.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-group-telegram-group-com |
| category | messaging |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
