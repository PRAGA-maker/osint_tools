---
id: memeorandum-political-web
name: Memeorandum
description: Use when you want to see which US political stories and commentary are being discussed right now — returns clustered news articles, the blogs/pundits reacting to them, and links to `social-profile`s.
url: http://www.memeorandum.com
category: communities-forums
path:
- communities-forums
bestFor: Tracking the current US political news conversation and who (bloggers/pundits) is reacting to a story.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to read; no account.
opsec: passive
opsecNote: Reading an auto-generated news aggregator is passive and reveals nothing about your target. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running automated political news aggregator (Techmeme's sister site); it curates links algorithmically — the linked outlets vary in reliability, so judge each source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- memeorandum.com
tags:
- news-aggregator
- politics
- us
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Memeorandum

> An automated US-politics news aggregator: it clusters the day's top political stories and, under each, the blogs and commentators reacting — a live map of who is saying what.

## When to use
You want to understand the current US political news conversation around an event or figure, or to find which bloggers/pundits are commenting on a story (and thus their `social-profile`s to follow). Memeorandum surfaces stories algorithmically and shows the surrounding commentary cluster, which is useful for media-landscape mapping, source discovery, and seeing how a topic is being framed across outlets in real time. Its value is contextual, not people-finding.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.memeorandum.com — the front page is the current clustered political headlines.
2. For each lead story, read the indented list of blogs/outlets reacting to it; click through to the commentators.
3. Use the archive (dated URLs) to see what was prominent on a given past date.
4. Pivot: commentator links lead to blogs and `social-profile`s worth monitoring; a story cluster shows the spread and framing of a topic.

## Inputs → Outputs
- **In:** a current topic/event, or a `name` you want to see discussed.
- **Out:** clustered news links, the reacting blogs/pundits, and their `social-profile`s.
- **Empty/negative result looks like:** your topic isn't in today's clusters — Memeorandum only shows what's currently prominent; use its archive or a general search for anything niche or dated.

## Gotchas & OpSec
- US-politics-only and algorithmic — it reflects what's trending, not a searchable database of people.
- Linked outlets range from mainstream to fringe; assess each source's reliability yourself.
- Not a search tool: you browse clusters, you don't query for a person.

## Overlaps ("do both")
- Pair with general news search and social monitoring; use Memeorandum to discover commentators, then track them on their own platforms.

## Trust & verifiability
`trust: community` — a reputable automated aggregator, but it only curates links. Trust flows from the underlying outlet, not from Memeorandum — evaluate each linked source on its own merits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | memeorandum-political-web |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
