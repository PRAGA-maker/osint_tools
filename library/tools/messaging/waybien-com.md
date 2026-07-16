---
id: waybien-com
name: waybien.com
description: Use when you have a topic, name, or handle and want public groups/channels a subject may belong to across Telegram, WhatsApp, Discord, Signal, Slack and Facebook — returns social-profile (group/channel links).
url: https://waybien.com/en
category: messaging
path:
- messaging
bestFor: Discovering public messaging groups and channels by keyword across multiple platforms.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free keyword search of the public group/channel index; the site also runs a paid ads/promotion product, but discovery search itself is free.
opsec: passive
opsecNote: You search Waybien's index, not the platforms directly, so joining/target-facing actions don't happen here. Do not click through and JOIN a group from a personal account — use a sock-puppet Telegram/Discord identity if you intend to enter a discovered community.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent third-party aggregator; coverage depends on what its crawler has indexed and on channels self-listing, so absence is not proof and listings can be stale or promotional.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Waybien group search
- Waybien channel finder
tags:
- telegram
- Telegram
- group-search
- channel-discovery
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# waybien.com

> A cross-platform search engine for public groups and channels — Telegram, WhatsApp, Discord, Signal, Slack, Facebook and more.

## When to use
You want to find the communities a subject participates in or the venues where a topic/name/handle is discussed. Search a person's known username, an alias, an organisation name, a hometown, or a niche interest, and Waybien returns public group/channel links you can then scope. Useful for building a subject's affiliation map and for finding local/community channels around a missing-persons search area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://waybien.com/en.
2. Enter a keyword — a username/handle, name, place, or topic — into the search box.
3. Browse the returned groups/channels; note platform, name, member count, and link.
4. Assess before entering: read the public preview first; to actually join, switch to a sock-puppet identity, never a personal account.
5. Pivot: a discovered Telegram channel feeds channel/user OSINT tools; a WhatsApp/Discord invite feeds membership analysis.

## Inputs → Outputs
- **In:** `username` (also works as a general keyword: name, place, topic, org)
- **Out:** `social-profile` (links to public groups/channels across multiple messaging platforms)
- **Empty/negative result looks like:** no listings for the term — meaning nothing matching is in Waybien's index, not that no such group exists; try synonyms, the local-language term, or a broader keyword.

## Gotchas & OpSec
- Human-in-the-loop: none for search itself.
- OpSec: passive at the search stage. The risk is downstream — joining a discovered group is an active, identity-leaking act; use a research persona.
- Listings can be promotional or dead (channels self-list for ads via Waybien's paid product); verify a group is live and relevant before relying on it.

## Overlaps ("do both")
- Pairs with dedicated Telegram search bots such as `[[getchatlist]]` and `[[searchforchats]]` — Waybien spans several platforms, those go deeper on Telegram specifically, so run both to widen coverage.

## Trust & verifiability
`trust: unverified` — a third-party aggregator with no transparency into crawl completeness. Good for lead generation; confirm each group directly on its native platform before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | waybien-com |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
