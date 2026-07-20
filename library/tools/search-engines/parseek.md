---
id: parseek
name: Parseek
description: Use when you have a `name`, `employer-org`, or event tied to Iran and want Persian-language news coverage — returns aggregated Iranian news headlines and links providing `social-profile`/context.
url: https://www.parseek.com
category: search-engines
path:
- search-engines
bestFor: Finding Persian-language Iranian news coverage of a person, company, or event across dozens of Iranian outlets.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free Persian news aggregator; no account required.
opsec: passive
opsecNote: Reading aggregated headlines is passive and leaks nothing about the subject. Results redirect to original Iranian news sites — those third-party outlets may log your visit, so use a sock-puppet/logged-out session when clicking through.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Parseek is an established Iranian news reader (khabarkhan) that aggregates headlines from many Persian outlets; it does no original reporting, so trust flows from the underlying sources.
missingPersonsRelevance: low
coverage:
- ir
auth: none
api: false
localInstall: false
registration: false
aliases:
- parseek.com
- پارسیک
tags:
- search
- international
- iran
- persian-news
source: metaosint
lastVerified: '2026-07-20'
relatedTools:
- parseek-iran
---

# Parseek

> Iran's long-running news aggregator (khabarkhan) — a fast way to sweep Persian-language coverage of a subject across dozens of Iranian outlets at once.

## When to use
You have a `name`, `employer-org`, or event with an Iranian nexus and want Persian-language news coverage that Western search engines index poorly. Parseek is a خبرخوان (news reader) that pulls current headlines from many Iranian news sources and organizes them by category (Iran, world, economics, society, science/tech, culture, sports). It is not a people-search engine; its value is surfacing Persian news mentions, which can corroborate roles, `associate` links, and timelines for a subject in the Iranian media sphere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.parseek.com (Persian interface; use a translator if needed).
2. Use its search / browse by category to find recent headlines; enter the subject `name` or company in Persian script for best recall.
3. Because it aggregates, dork the underlying outlets too: `<name in Persian> site:*.ir news` in Google to complement it.
4. Click through to the original outlet for full articles (from a sock-puppet session).
5. Pivot: named companies/associates feed registry and people-search; Persian spelling of a name helps further Persian-language searches.

## Inputs → Outputs
- **In:** `name` or `employer-org` (ideally in Persian script), or a topic
- **Out:** aggregated Iranian news headlines/links → article context, roles, `associate` mentions, `social-profile` links
- **Empty/negative result looks like:** no headline matches — expected for private individuals; aggregators only index news, not people, so absence is weak evidence.

## Gotchas & OpSec
- Persian-language and aggregation-only — you must transliterate the subject's name into Persian for good recall, and follow links for full text.
- It reflects the Iranian media landscape (state and semi-state outlets); weigh source bias when reading.
- OpSec: aggregator is passive, but clicking through to outlets exposes your referrer — use a clean session.

## Overlaps ("do both")
- Pairs with `[[parseek-iran]]` and general web-news search — Parseek gives the Persian-news breadth; general engines and registries confirm the facts it surfaces.

## Trust & verifiability
`trust: community` — Parseek itself is a reliable, established aggregator, but it does no reporting; judge each hit by its underlying outlet and corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | parseek |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
