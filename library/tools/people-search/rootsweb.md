---
id: rootsweb
name: RootsWeb
description: Use when you have a `name`/surname and want historic genealogy data — user-submitted family trees, surname lists, and archived mailing lists — returns ancestors, relatives, dates, and places from a now read-only archive.
url: https://www.rootsweb.com
category: people-search
path:
- people-search
bestFor: Searching legacy user-submitted genealogy (WorldConnect trees, surname lists, mailing-list archives) by name.
selectorsIn:
- name
selectorsOut:
- name
- associate
- address
- dob
status: degraded
pricing: free
costNote: Free to search. Owned by Ancestry; the community-contributed data here is free, though Ancestry's paid records are separate.
opsec: passive
opsecNote: Passive reading of an archived, largely read-only site — nobody is contacted or notified. Ordinary browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Legacy user-submitted genealogy owned by Ancestry. Content is hobbyist-contributed (often unsourced) and, since 2020-2024, made largely read-only — accurate as leads, not as verified records.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- RootsWeb WorldConnect
- home.rootsweb.ancestry.com
tags:
- people-search
- genealogy
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# RootsWeb

> The "granddaddy" of free genealogy sites — a vast archive of user-submitted family trees, surname lists, and mailing-list posts, now largely frozen as a read-only reference.

## When to use
You have a `name`/surname and want historic family-tree data: ancestors, relatives (`associate`s), birth/death dates, and places others have compiled. Valuable in long-lost-relative and next-of-kin work for reconstructing a family across generations — but treat it as a lead source, since entries are hobbyist-contributed and the site is no longer actively updated.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.rootsweb.com and use the WorldConnect tree search (or browse surname resources).
2. Search by surname/`name`; add dates or a place to narrow.
3. Read matching trees: named individuals with dates, places, and linked relatives; note the submitter for provenance.
4. For older mailing-list discussions, follow the migrated archives (many now on the Internet Archive).
5. Pivot: named relatives become `associate` leads; historic `address`es/places feed records; a submitter may be a living relative to contact via other channels.

## Inputs → Outputs
- **In:** `name`/surname (+ dates/place)
- **Out:** family-tree entries with `name`s, `associate`s (relatives), `dob`/death dates, historic places/`address`
- **Empty/negative result looks like:** no matching tree — the family was never submitted; absence proves nothing, especially for common or non-Western surnames.

## Gotchas & OpSec
- Read-only/archived: Ancestry retired the surname list (2017), mailing lists (2020), and made the site largely read-only by 2024 — data is frozen, so recent events won't appear.
- Unsourced: user-submitted trees frequently contain errors and copied mistakes; verify every date against a primary record.
- OpSec: passive; nothing reaches any living subject.

## Overlaps ("do both")
- Pairs with `[[curious-fox-united-kingdom]]` and `[[myfamilyannouncements-co-uk]]` — RootsWeb gives the historic tree, Curious Fox connects you to living researchers, and family notices confirm recent events.

## Trust & verifiability
`trust: community` — hobbyist-contributed genealogy owned by Ancestry; useful for leads and structure but unsourced, so corroborate against vital records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rootsweb |
| category | people-search |
| selectorsIn → selectorsOut | name → name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
