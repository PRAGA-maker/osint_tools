---
id: trunk
name: Trunk (Fediverse)
description: Use when you have a topic/interest and want curated lists of Mastodon/Fediverse accounts about it — returns `social-profile` handles to explore or follow.
url: https://communitywiki.org/trunk/
category: messaging
path:
- messaging
bestFor: Discovering topical Mastodon/Fediverse accounts via volunteer-curated thematic lists (200+ topics), optionally mass-followed with the Pytrunk tool.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open (community wiki project). No account needed to browse the lists; being added to a list is opt-in for account owners.
opsec: passive
opsecNote: Browsing the public lists reveals nothing about your subject. Passive. (Auto-following lists via Pytrunk requires your Fediverse login — use a sock-puppet account for that.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running volunteer-maintained directory (kensanata/CommunityWiki); lists are opt-in and human-curated, useful for discovery rather than as authoritative data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Trunk for Mastodon
- Trunk for the Fediverse
- communitywiki trunk
tags:
- Social Media
- Mastodon
- fediverse
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Trunk (Fediverse)

> A volunteer-curated set of 200+ thematic Mastodon/Fediverse account lists — the fastest way to find who is active on a given topic in the Fediverse.

## When to use
You are researching a community or subject area on Mastodon/the Fediverse and want a starting set of relevant accounts (`social-profile`) grouped by theme (Privacy, Linux, a language community, a hobby, etc.). It is a discovery/orientation tool for finding topical accounts and communities, not a person-lookup engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://communitywiki.org/trunk/ .
2. Browse the thematic lists (200+ topics), or pick a language-specific Trunk (e.g. French, Spanish, Dutch).
3. Open a list to see the volunteered accounts on that topic.
4. Read the output: Fediverse handles (`social-profile`) grouped by theme, which you can visit individually.
5. Pivot: open promising accounts on their home instance; to mass-follow a whole list, use the companion Pytrunk tool with a sock-puppet Fediverse login.

## Inputs → Outputs
- **In:** a topic/interest (browse by `name` of theme)
- **Out:** `social-profile` (curated Fediverse account handles)
- **Empty/negative result looks like:** a niche topic with no list, or a list with few accounts — Trunk only covers people who opted in, so absence means nothing about who is really active.

## Gotchas & OpSec
- Opt-in and curated: accounts appear only because owners volunteered, so it is a discovery aid, not a comprehensive index of a topic.
- Coverage skews toward established, English-first accounts (list inclusion has activity/language criteria).
- OpSec: browsing is passive; only the Pytrunk auto-follow step touches an account — use a throwaway for it.

## Overlaps ("do both")
- Complements Fediverse/Mastodon search and instance directories: Trunk gives human-curated topical starting points, while search tools let you query specific handles or keywords.

## Trust & verifiability
`trust: community` — a mature volunteer wiki project. Good for discovery; the listings are curated opinion, not authoritative data, so verify any specific account independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trunk |
| category | messaging |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
