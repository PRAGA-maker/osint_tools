---
id: prezi
name: Prezi
description: Use when you have a `name` or `username` and want a subject's public presentations — searchable slide decks that expose work, affiliations, and embedded documents (`social-profile`, `document-id`).
url: https://prezi.com
category: documents-metadata
path:
- documents-metadata
bestFor: Finding a person's public Prezi presentations to surface professional work, affiliations, and embedded content.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Free to view public presentations and to hold a basic account; advanced authoring/privacy features are paid. Public prezis are viewable without paying.
opsec: passive
opsecNote: Viewing public presentations is passive and unlogged to the subject. Creating a Prezi account to follow a user's profile can expose you — browse logged-out or from a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Mainstream presentation platform; content is user-created, so anything in a deck is the author's claim, not verified fact.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- prezi.com
tags:
- presentations
- documents
- curated-directory
source: toddington-resources
lastVerified: '2026-07-23'
---

# Prezi

> A cloud presentation platform whose public decks are searchable — a place to find a subject's talks, coursework, pitches, and the affiliations and documents baked into them.

## When to use
You have a `name` or `username` and want professional or academic footprint: public Prezi presentations often reveal an employer or school, project details, co-presenters, contact slides, and embedded images/logos. Like SlideShare for slide decks, it's a source that generic people-search misses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search Prezi's Explore and Google `site:prezi.com "<name/username>"`.
2. Open matching public presentations and profiles.
3. Read the decks: title/author slides, "about me" slides, employer/school branding, co-presenter credits, and any contact details or embedded documents.
4. Pivot: an employer or school feeds directory/staff-page searches; co-presenters are `associate` leads; a contact slide may yield `email`/`phone`; branding/logos feed reverse-image search.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (Prezi profile/decks), `employer-org` and affiliation/contact leads from deck content
- **Empty/negative result looks like:** no public prezis, or a profile with only private decks — absence just means nothing public here.

## Gotchas & OpSec
- Content is self-authored: a claimed title, employer, or bio in a deck is a lead to verify, not a confirmed fact.
- Many prezis are private or unlisted and won't surface in search.
- OpSec: **passive** — view public decks logged-out or via sock puppet; don't follow the subject from a real account.

## Overlaps ("do both")
- Pairs with SlideShare/Scribd and other document-hosting searches — people scatter decks and files across platforms, so check several.

## Trust & verifiability
`trust: unverified` — a legitimate mainstream platform, but all intelligence value is user-generated presentation content requiring corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | prezi |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
