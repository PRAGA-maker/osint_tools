---
id: appropedia
name: Appropedia
description: Use when you have a `name` or `username` active in sustainability/appropriate-technology and want their wiki contributions — returns authored project pages and edit history.
url: https://www.appropedia.org
category: search-engines
path:
- search-engines
bestFor: Searching the sustainability/appropriate-technology wiki for a contributor's project pages and edit trail.
selectorsIn:
- name
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free, open-licensed community wiki; no account needed to read or search. Editing requires a (free) account but is not needed for lookups.
opsec: passive
opsecNote: Reading and searching a public wiki — no login, nothing written, no subject notification. User contribution histories are public MediaWiki data. Do not create an account tied to your identity if you plan to view logged-in features.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running open community wiki (est. 2006) on sustainability; contributor identities are self-declared usernames, so treat authorship as a lead, not confirmed identity.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- the sustainability wiki
tags:
- toddington
- curated-directory
- specialty-search
- wiki
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Appropedia

> The open "sustainability wiki" — thousands of appropriate-technology and DIY project pages, searchable for a niche subject's contributions and a public MediaWiki edit trail.

## When to use
Your subject is active in sustainability, appropriate technology, off-grid living, humanitarian engineering, or academic project work, and you want to find what they've authored or a username tied to that world. Appropedia is a MediaWiki, so a `username` yields a full public contribution history (pages created, edits, timestamps), and a project page may name real people, institutions, or locations. It's a specialty source — high value only when the subject genuinely operates in this niche, near-zero otherwise.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.appropedia.org and search the subject's name, a known username, or a project/topic they'd be tied to.
2. For a candidate contributor, open `Special:Contributions/<username>` to see their full edit history and the pages they authored.
3. Read authored pages for real names, affiliated organizations, universities, or geographic project locations.
4. Pivot: a confirmed username feeds cross-platform username enumeration; a named institution or project location feeds people/organization lookups.

## Inputs → Outputs
- **In:** `name` or `username` (sustainability/appropriate-tech context)
- **Out:** authored project pages, public edit history, and a linkable `username` / `social-profile` handle
- **Empty/negative result looks like:** no page or contribution matches — meaning the subject isn't active on Appropedia, the norm for anyone outside this niche.

## Gotchas & OpSec
- Human-in-the-loop: none for reading; only create an account if you accept it's attributable.
- Usernames are self-declared — authorship is a lead toward identity, not proof of it.
- Very domain-specific; don't expect coverage of people outside sustainability/DIY-tech circles.

## Overlaps ("do both")
- Pairs with a cross-platform username checker — this confirms activity and content on Appropedia, that tests whether the same handle exists elsewhere.

## Trust & verifiability
`trust: community` — an established open community wiki; edit histories are verifiable MediaWiki records, but the identity behind a username is self-asserted, so corroborate before attributing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | appropedia |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
