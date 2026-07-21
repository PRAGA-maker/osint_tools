---
id: wikimedia-meta-wiki
name: Wikimedia Meta-Wiki
description: Use when you have a Wikimedia editor `username` and want their cross-project (SUL) global account and coordination activity — returns linked project accounts and `associate` collaboration leads.
url: https://meta.wikimedia.org/wiki/Main_Page
category: search-engines
path:
- search-engines
bestFor: Resolving a Wikimedia editor's global (cross-wiki) account and coordination-space activity from a username.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
- associate
status: live
pricing: free
costNote: Free and open; no account needed to read pages or global account info.
opsec: passive
opsecNote: Viewing public wiki pages and global-account tools is passive and invisible to the editor. Note that editing/logging any action from an account is itself a public, attributable edit — stay in read-only mode.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Meta-Wiki is the official Wikimedia Foundation coordination wiki; account and log data is authoritative, though user-supplied page content is self-reported.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- meta.wikimedia.org
- Meta-Wiki
tags:
- toddington
- curated-directory
- specialty-search
- wikimedia
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- wikispecies
---

# Wikimedia Meta-Wiki

> The Wikimedia movement's coordination wiki and home of global (SUL) account tools — the hub for pivoting one editor username across all Wikimedia projects.

## When to use
You have a Wikimedia `username` (a Wikipedia/Commons/Wiktionary editor) and want to see everywhere that single global account is active. Wikimedia's unified login (SUL) ties one username to all projects, and Meta-Wiki hosts the global-account and cross-wiki tools plus a public user page the editor may fill with self-disclosed detail. Use it to expand from one wiki to an editor's full footprint and the people they coordinate with.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to Special:CentralAuth on Meta-Wiki (`meta.wikimedia.org/wiki/Special:CentralAuth/<username>`) to list every project where that global account exists, with edit counts and registration dates.
2. Read the editor's Meta and per-project user pages for self-disclosed identity, languages, and affiliations.
3. Check their contributions and talk-page interactions for collaborators.
4. Note recurring co-editors as `associate` leads.
5. Pivot: reused usernames feed cross-platform username-search; self-disclosed real names/languages/locations feed people-search and geolocation.

## Inputs → Outputs
- **In:** a Wikimedia `username`
- **Out:** global-account map across projects (`social-profile`/`username`), user-page self-disclosures, co-editor `associate`s
- **Empty/negative result looks like:** CentralAuth shows no global account for the name — the handle isn't a Wikimedia editor (or is spelled differently); absence isn't proof of no wiki activity under another name.

## Gotchas & OpSec
- Handle ≠ identity: editors are pseudonymous — treat a username match as a lead unless the user page self-discloses.
- User-page content is self-reported: verify claims independently.
- Read-only: any logged action from an account is a public, permanent, attributable edit — never edit while investigating.
- OpSec: passive when reading.

## Overlaps ("do both")
- Pairs with cross-platform username-search and Wikipedia contribution tools — Meta-Wiki maps the cross-project account, while those extend the handle beyond Wikimedia and analyze edit patterns.

## Trust & verifiability
`trust: trusted` — official Wikimedia infrastructure, so account/log data is authoritative; the caveat is that free-text user-page content is self-reported and needs corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikimedia-meta-wiki |
| category | search-engines |
| selectorsIn → selectorsOut | username → social-profile, username, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
