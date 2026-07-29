---
id: yeggi
name: Yeggi
description: Use when you have a `username`, keyword, or model name and want to find 3D-printable model listings across repositories — returns links to designer profiles on Thingiverse, Printables, etc.
url: https://www.yeggi.com/
category: search-engines
path:
- search-engines
bestFor: Meta-searching 3D model repositories to locate a design or a maker's uploads across many sites at once.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to search; no account needed. A free account adds saved lists and new-model alerts. Individual model downloads may be paid on the destination repository, not on Yeggi.
opsec: passive
opsecNote: A public meta-search engine; you query Yeggi, not the maker. Clicking through to a repository is a normal visit to that site. No target notification. Use a clean session for attribution hygiene as with any search engine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent aggregator run since 2013 by Sebastian Karpp; indexes 6M+ models across public 3D repositories. Reliable as a discovery layer; authority for any listing is the destination repo.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- yeggi.com
tags:
- Search engines
- 3d-printing
- hobbyist
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Yeggi

> A meta-search engine for 3D-printable models — one query fans out across Thingiverse, Printables, MyMiniFactory, Cults3D and more, indexing 6M+ designs.

## When to use
Niche but real for OSINT: when a subject is a maker/hobbyist and you have a `username` or handle they might reuse on 3D-printing sites, Yeggi lets you sweep many repositories at once to find their uploaded designs, linked profiles, and activity. Also useful to trace a specific model (by name or distinctive keyword) back to its original designer across mirrored uploads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.yeggi.com/.
2. Search a `username`/handle, a maker's name, or a distinctive model title/keyword.
3. Results are model thumbnails with the source repository badge and a link; open the destination listing to reach the designer's profile.
4. On the destination repo, read the uploader's `username`, profile, and other uploads — that is the pivot into their maker identity.
5. Pivot: a confirmed reused `username` feeds cross-platform username tools; a designer profile feeds social-profile enumeration.

## Inputs → Outputs
- **In:** `username` / handle / `name` / model keyword
- **Out:** links to model listings and, via them, designer `social-profile` / `username` on 3D repositories
- **Empty/negative result looks like:** "no results found" — the term matches no indexed model; the subject may not publish 3D designs, or uses a different handle there.

## Gotchas & OpSec
- Yeggi indexes models, not people directly — you reach identities by clicking through to a repository. Confirm the uploader on the destination site, not from Yeggi's thumbnail.
- The same model is often mirrored across sites; matching handles across repos is a stronger identity signal than a single listing.
- Coverage is limited to public 3D-printing repositories; irrelevant unless the subject is a maker.

## Overlaps ("do both")
- Complements general username-search tools: use those to establish a handle, then Yeggi to check the 3D-printing niche specifically, which broad username tools usually miss.

## Trust & verifiability
`trust: community` — a long-running independent aggregator. It reliably points to where a model lives; treat the destination repository as the authoritative source for any profile detail.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yeggi |
