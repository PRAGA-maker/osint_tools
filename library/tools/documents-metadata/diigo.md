---
id: diigo
name: Diigo
description: Use when you need to collect, annotate, and archive web evidence during an investigation, or to mine a subject's public Diigo `username` for their bookmarks — returns saved links/notes.
url: https://www.diigo.com
category: documents-metadata
path:
- documents-metadata
bestFor: Bookmarking, highlighting, and archiving web pages as an investigator; also reading a target's public bookmarks.
selectorsIn:
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: freemium
costNote: Free tier with limits (bookmarks, highlights, cached copies); paid plans raise limits and add features.
opsec: passive
opsecNote: Two modes. As a research tool, use a sock-puppet Diigo account and keep your libraries PRIVATE — public libraries leak your entire research trail. As a lookup, viewing a target's *public* bookmarks is passive and doesn't alert them.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running mainstream bookmarking service; reliable as a tool. Any target-profile data is user-published and only as complete as what they chose to share publicly.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- diigo.com
tags:
- Useful Websites, Tools & Documents
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Diigo

> A social bookmarking and web-annotation service — an investigator's tool for collecting, highlighting, and archiving evidence, and occasionally a source when a subject's own bookmarks are public.

## When to use
Two uses. (1) **As a research tool:** save, tag, highlight, and cache web pages you find during a case so evidence is preserved and organized (pages get deleted; a cached copy protects your finding). (2) **As a source:** if a subject uses Diigo and made their library public, their saved links and tags reveal interests, affiliations, and research focus — a small footprint pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. **Research mode:** register a sock-puppet Diigo account; set your library to **private**. Install the extension/bookmarklet and save + annotate pages as you work; use Diigo's cached copy to preserve evidence.
2. **Lookup mode:** check `https://www.diigo.com/user/<username>` for a subject's public library; review their bookmarks, tags, and highlights.
3. Export your library (or theirs, if public) for your case file.
4. Pivot: a target's bookmarked `domain`s and tags suggest interests/affiliations; their profile is a `social-profile` to correlate elsewhere.

## Inputs → Outputs
- **In:** `username` (a subject's Diigo handle) — or your own content, in research mode
- **Out:** `social-profile` (the user's Diigo profile), `domain` (their public bookmarked links/tags)
- **Empty/negative result looks like:** a private or empty public library — most users keep bookmarks private, so absence tells you nothing about whether they use the service.

## Gotchas & OpSec
- **Don't leak your own research:** keep your investigator library private — a public Diigo library exposes your entire trail of sources.
- Human-in-the-loop: using it as a tool needs an account (use a sock puppet).
- Target data is limited to what they made public — usually little.

## Overlaps ("do both")
- As evidence capture, pairs with archive tools (Wayback, archive.today) — do both, since Diigo's cache preserves *your* view while public archives give an independent, citable snapshot.

## Trust & verifiability
`trust: community` — a mainstream, dependable bookmarking service; solid as a tool, while any subject-profile data is self-published and partial, so corroborate footprint leads elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | diigo |
| category | documents-metadata |
| selectorsIn → selectorsOut | username → social-profile, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
