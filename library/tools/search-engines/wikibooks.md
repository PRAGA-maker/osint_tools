---
id: wikibooks
name: Wikibooks
description: Use when you have an author `name`/`username` or a subject-matter lead and want open textbooks/manuals and their contributor histories — returns book content plus editor usernames and edit trails.
url: https://en.wikibooks.org
category: search-engines
path:
- search-engines
bestFor: Open textbooks/manuals and the Wikimedia contributor trail behind them.
selectorsIn:
- username
- name
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free, ad-free Wikimedia project; editing needs an account but reading and viewing histories does not.
opsec: passive
opsecNote: Reading pages and public edit histories is passive; no subject is notified. If you create an account to interact, your username and (unless logged in) your IP are publicly logged with every edit — use a research account and never edit from an attributable identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Wikimedia Foundation project; content is crowd-sourced (verify facts) but the edit/contributor metadata is authoritative and publicly logged.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- en.wikibooks.org
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Wikibooks

> A Wikimedia project of free, collaboratively-written textbooks and manuals — occasionally useful for subject-matter content, and (like all Wikimedia sites) for the public contributor trail behind each page.

## When to use
Two angles. (1) Content: you need an open, freely-licensed textbook/how-to on a topic a case touches. (2) People: a subject uses a Wikimedia `username`, and you want to see their Wikibooks contributions — edit history, talk-page activity, and interests — as part of mapping a Wikimedia footprint. The contributor metadata (who edited what, when) is the OSINT-relevant layer.

## How to use it (`bestInteractionPattern`: web-manual)
1. For content, search the topic at https://en.wikibooks.org (or another language edition).
2. For a person, go to `https://en.wikibooks.org/wiki/Special:Contributions/<username>` to list that account's edits, or open a page's "View history" to see contributor usernames and timestamps.
3. Check the user page and talk page for self-disclosed details and cross-links to other Wikimedia projects.
4. Note the Wikimedia global account — the same username often spans Wikipedia, Wikibooks, Commons, etc.
5. Pivot: a username here feeds cross-wiki tools and general username searches; edit timestamps hint at timezone/activity patterns.

## Inputs → Outputs
- **In:** topic keyword, or a Wikimedia `username` / author `name`
- **Out:** textbook content, and contributor `username`s with public edit trails (a Wikimedia `social-profile` slice)
- **Empty/negative result looks like:** no book on the topic, or an account with no Wikibooks edits — the person may be active on other Wikimedia projects instead; check Wikipedia/Commons.

## Gotchas & OpSec
- Crowd-sourced content — verify any factual claim against a primary/authoritative source.
- Coverage is thin compared to Wikipedia; many topics simply aren't covered here.
- OpSec: reading is passive; editing publicly logs your username (and IP if not logged in) forever — never touch it from an attributable identity.

## Overlaps ("do both")
- Pairs with Wikipedia/Commons contribution analysis and Wikimedia cross-wiki tools — a username's Wikibooks edits are one slice; the global Wikimedia account ties the whole footprint together.

## Trust & verifiability
`trust: trusted` — an official Wikimedia project; the public edit/contributor logs are authoritative even though article content is user-written and needs corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikibooks |
| category | search-engines |
| selectorsIn → selectorsOut | username, name → username, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
