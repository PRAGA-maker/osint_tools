---
id: tviv
name: The TV IV
description: Use when you have a name or clue about a TV programme and want to identify the show, its network, air dates, and cast — returns name and associate leads (cast/crew) for corroborating a media reference.
url: http://tviv.org/Main_Page
category: search-engines
path:
- search-engines
bestFor: Identifying a television programme and its cast/air history from a partial clue.
selectorsIn:
- name
selectorsOut:
- name
- associate
status: live
pricing: free
costNote: Free, open, community-editable wiki. No account needed to read.
opsec: passive
opsecNote: Ordinary anonymous browsing of a public wiki; reading leaks nothing about your subject. Editing would require an account and expose activity, but this is a read-only reference use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A crowdsourced, anyone-can-edit TV encyclopedia; useful for orientation but, like any open wiki, individual facts should be confirmed against a primary source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- tviv.org
- The TV IV
tags:
- toddington
- curated-directory
- specialty-search
- television
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# The TV IV

> Crowdsourced television encyclopedia (tviv.org) — a reference for identifying shows, networks, air dates, and cast, useful for pinning down a media reference in an investigation.

## When to use
You have a fragment of a television reference — a show `name`, a network, an approximate era, or a description a subject gave — and you need to identify the programme and the people attached to it. This is a supporting/context tool, not a people-locator: it corroborates a claim ("they appeared on / worked on show X"), resolves a partial title, or gives you cast and crew `name`/`associate` leads to pivot into people-search elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://tviv.org/Main_Page.
2. Use the wiki search (or a site-scoped web search: `site:tviv.org <term>`) for the show title, network, or keyword you have.
3. Open the programme page: read network, run dates, episode/season structure, and any cast/crew listed.
4. Take the cast/crew names and pivot them into a proper people-search or IMDb-style tool — tviv is the orientation step, not the endpoint.

## Inputs → Outputs
- **In:** `name` (show title / partial clue / network).
- **Out:** identified programme with air history, plus cast/crew `name` and `associate` leads.
- **Empty/negative result looks like:** no matching page, or a thin stub with no cast — common for obscure, non-US, or very recent shows. Absence here means the wiki hasn't covered it, not that the show doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none for reading.
- OpSec: **passive** — anonymous public-wiki browsing; nothing reaches your subject.
- It is an open wiki: coverage is uneven and any single fact can be wrong or outdated. Treat it as a lead source and confirm against a primary/authoritative TV database.

## Overlaps ("do both")
- Pairs with mainstream TV/film databases (e.g. IMDb-style tools) — tviv is quick for identifying a show, while an authoritative database confirms cast, dates, and credits.

## Trust & verifiability
`trust: unverified` — a hobbyist, community-editable wiki with no editorial guarantee. Fine for orientation; verify anything decision-critical elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tviv |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
