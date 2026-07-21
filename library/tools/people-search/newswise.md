---
id: newswise
name: Newswise
description: Use when you have a topic or expert `name` and want the researchers/spokespeople and institutions behind news — returns expert `name`s, their `employer-org` (university/institution) and contact routes from research press releases.
url: https://www.newswise.com
category: people-search
path:
- people-search
bestFor: Finding named academic/research experts and their institutions via a research-news and expert-source wire.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free to read; press-release distribution and full journalist features may require a free registration.
opsec: passive
opsecNote: Reading and searching is passive and anonymous. Contacting an expert or listed PIO reveals an identity — use a sock-puppet journalist persona, not your real one, and never approach a subject's colleagues from a traceable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established research-news wire aggregating university and institutional press releases and an expert directory; content is issued by the institutions, so it's authentic but promotional.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- newswise.com
tags:
- expert-search
- research-news
- press-releases
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Newswise

> A research-news wire and expert directory — the fastest way to connect a `name` or topic to the named academics, institutions and press contacts behind a piece of research.

## When to use
You want to identify or corroborate an academic/research subject, or find the humans behind a study or institution. Newswise carries university and research-institution press releases (which name principal investigators, spokespeople, and public-information officers with contact routes) and an expert-source directory. Use it to confirm a person's affiliation and role, or to enumerate the named experts at an `employer-org`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.newswise.com.
2. Search by `name`, topic, or institution across news releases and the expert directory.
3. Open matching releases and read for OSINT signals: named researchers and titles, their institution, and the media-contact/PIO block (name, email, phone).
4. Use the expert directory to map named specialists to their `employer-org`.
5. Pivot: a confirmed affiliation feeds institutional directories and LinkedIn; a media-contact detail feeds email/phone-OSINT; a co-author surfaces an `associate`.

## Inputs → Outputs
- **In:** `name`, topic, or `employer-org`
- **Out:** expert `name`s, their `employer-org` (institution), roles, and press-contact routes
- **Empty/negative result looks like:** no releases or expert entries — the person/topic isn't covered here (Newswise skews academic/scientific and US-centric). Try a general press wire or the institution's own newsroom before concluding nothing exists.

## Gotchas & OpSec
- Content is **institution-issued** — names, titles and affiliations are usually accurate, but framing is promotional; verify factual claims independently.
- Coverage is biased toward universities, medical centers and research bodies; non-academic subjects won't appear.
- OpSec: **passive** to read; **active** the moment you contact an expert or PIO — use a sock-puppet identity.

## Overlaps ("do both")
- Pairs with `[[prnewswire]]` and institutional directories — Newswise leans academic/research while PR Newswire leans corporate, so run both to cover a subject who spans industry and academia.

## Trust & verifiability
`trust: community` — an established research-news aggregator. The affiliations and contacts are authentic institutional data; just treat the surrounding narrative as promotional and confirm identity through the institution directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | newswise |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
