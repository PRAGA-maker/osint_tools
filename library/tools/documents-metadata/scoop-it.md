---
id: scoop-it
name: Scoop.it
description: Use when you have a `name`/`username` or a topic and want to find someone's publicly curated content pages — returns themed collections that reveal interests and linked sources.
url: https://www.scoop.it
category: documents-metadata
path:
- documents-metadata
bestFor: Finding a subject's public "topic" pages and the content they curate, exposing interests, sources, and linked profiles.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free tier lets you create and browse public topic pages; paid plans add analytics and private curation. Browsing existing public topics needs no account.
opsec: passive
opsecNote: Viewing a public Scoop.it topic page is passive and does not notify the curator. Creating/following requires an account tied to an identity — browse logged-out, or use a sock-puppet, to keep your interest in a subject private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Established commercial content-curation platform (~15 years, millions of users); the platform is legitimate, but topic pages are user-generated, so treat their curated links as leads to verify at source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Scoop.it content curation
tags:
- content-curation
- social-media
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Scoop.it

> A long-running content-curation platform where users build public "topic" pages — a place to surface what a subject collects, follows, and links to.

## When to use
You have a `name` or `username` and suspect the subject curates content publicly, or you want to see who is curating around a particular topic tied to your case. A person's Scoop.it topics are a window into their interests, the sources they trust, and the external links (blogs, articles, profiles) they gather — useful for building a profile or finding a fresh pivot when direct social accounts are thin.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.scoop.it (browse logged-out for passivity).
2. Use the site search — or a site-scoped Google query `site:scoop.it "<name or username>"` — to find the subject's topic pages or topics matching your subject area.
3. Open a topic page: read the curated posts, each linking to an external source with the curator's note.
4. Note the curator's profile, their other topics, and recurring linked domains/authors.
5. Pivot: linked articles/domains → source verification; the curator's other topics → interests and possible identity clues; linked social handles → cross-platform enumeration.

## Inputs → Outputs
- **In:** `name` / `username` or a topic keyword
- **Out:** public curated topic pages → the curator's `social-profile`, interests, and outbound source links
- **Empty/negative result looks like:** no matching topic pages or an inactive/empty profile — many people don't use Scoop.it, so a miss is expected and not informative; move to broader social search.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing public pages; account only needed to curate.
- Signal quality: curated links reflect what the subject chose to share, which is self-selected and can be aspirational or performative — corroborate before drawing conclusions.
- OpSec: passive; viewing public topics does not alert the curator.

## Overlaps ("do both")
- Pairs with broader username/social enumeration and bookmarking-platform searches (Pinterest, Flipboard) — Scoop.it captures one curation surface; the others catch where the same interests show up elsewhere.

## Trust & verifiability
`trust: unverified` — the platform is legitimate and stable, but every topic page is user-generated; use curated items as pointers and verify each linked source independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scoop-it |
