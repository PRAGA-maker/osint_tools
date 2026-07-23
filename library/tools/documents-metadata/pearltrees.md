---
id: pearltrees
name: Pearltrees
description: Use when you have a `name` or `username` and want a subject's curated web collections (bookmarks, files, notes, photos) — returns `social-profile` and interest/associate leads.
url: http://www.pearltrees.com
category: documents-metadata
path:
- documents-metadata
bestFor: Finding a person's public Pearltrees collections to map their interests, saved documents, and network.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Free to browse and to hold a basic account; larger storage/premium features are paid, but public collections are viewable without paying.
opsec: passive
opsecNote: Browsing public collections is passive, but Pearltrees can show "who viewed"/activity to logged-in users — browse logged-out or from a sock-puppet account, never your real one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Established consumer bookmarking service; content is user-generated, so any "fact" in a collection is the subject's claim, not verified data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- pearltrees.com
tags:
- bookmarking
- social-curation
- curated-directory
source: toddington-resources
lastVerified: '2026-07-23'
---

# Pearltrees

> A visual social-bookmarking platform: users organise web pages, files, photos, and notes into shareable "trees" — public ones reveal a subject's interests, sources, and collaborators.

## When to use
You have a `name` or `username` and want a window into what a subject reads, saves, and cares about. A public Pearltrees profile exposes curated collections (research topics, saved documents/images, notes) and often collaborators — useful for building an interest/associate map, confirming a professional or hobby focus, or recovering documents a person chose to file publicly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search Pearltrees (and Google `site:pearltrees.com "<name/username>"`) for the subject's profile or collections.
2. Open a public profile and browse its trees, sub-collections, and uploaded files/notes.
3. Note collaborators and "team" members on shared trees — these are `associate` leads.
4. Pivot: recurring topics feed interest/employment hypotheses; a reused username feeds cross-platform search; uploaded files may carry `metadata-exif` worth extracting.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (interests, saved content), `associate` (collaborators on shared trees)
- **Empty/negative result looks like:** no matching profile, or a profile whose trees are private/empty — absence just means nothing public here, not that the person doesn't use it.

## Gotchas & OpSec
- Everything is user-curated: a saved article reflects interest, not endorsement or fact; treat collection contents as leads.
- Some content is private or team-only and won't show when logged out.
- OpSec: **passive**, but avoid browsing while logged into a real account — use a sock puppet or stay logged out.

## Overlaps ("do both")
- Pairs with other social-bookmarking/curation sites and username search — Pearltrees shows one facet of a person's interests; cross-checking sources builds a fuller picture.

## Trust & verifiability
`trust: unverified` — a legitimate consumer service, but the intelligence value is entirely user-generated content that must be corroborated elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pearltrees |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, username → social-profile, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
