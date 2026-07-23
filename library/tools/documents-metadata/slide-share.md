---
id: slide-share
name: SlideShare
description: Use when you have a `name`/`username` or topic and want a subject's uploaded presentations/documents — returns social-profile, employer-org context, and document leads with metadata.
url: https://www.slideshare.net/
category: documents-metadata
path:
- documents-metadata
bestFor: Finding a person's uploaded slide decks/documents and the professional context (and metadata) they reveal.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
- metadata-exif
status: live
pricing: free
opsec: passive
opsecNote: Browsing public SlideShare content and profiles is passive and doesn't notify the uploader. SlideShare is a LinkedIn/Scribd property, so a viewing account links to that identity — browse logged-out or with a sock puppet. Downloaded decks may carry document metadata (author, software, timestamps) worth extracting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A mainstream slide/document-sharing platform (now under Scribd); content is user-uploaded, useful as leads and for the metadata it carries.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SlideShare
- slideshare.net
tags:
- presentations
- document-search
- toddington
- curated-directory
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# SlideShare

> A slide/document-sharing platform whose public uploads and profiles expose a subject's presentations, professional context, and the document metadata baked into their files.

## When to use
You have a `name`/`username` or a topic tied to a subject (often a professional, academic, or speaker) and want their uploaded decks/documents. A SlideShare profile reveals employer/role context, event participation, areas of expertise, and links to a wider professional identity — and downloaded files frequently carry `metadata-exif`-style document metadata (author name, organization, software, timestamps) that can leak more than the slides themselves.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.slideshare.net/ and search by `name`, `username`, organization, or topic keywords.
2. Match a profile/upload to your subject via name, avatar, employer, or topic.
3. Read the profile and decks for professional context and links (`selectorsOut`); download a deck and inspect its embedded document metadata.
4. Pivot: the profile handle/name cross-checks to LinkedIn and other sites; document metadata (author/org) can confirm identity or surface a real name.

## Inputs → Outputs
- **In:** `name` or `username` (or topic keywords)
- **Out:** `social-profile` (SlideShare profile + linked identity), `employer-org` (role/organization context), `metadata-exif` (document metadata in downloaded files)
- **Empty/negative result looks like:** no matching profile/uploads — the subject may not use SlideShare or posts under a different name; try Scribd, academia.edu, or LinkedIn.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing.
- OpSec: passive; a logged-in view ties to your LinkedIn/Scribd account — browse logged-out or with a puppet.
- Content is self-published and can be outdated or self-promotional; use decks as leads, but the embedded document metadata is often the higher-value find.

## Overlaps ("do both")
- Pairs with Scribd, academia.edu, and LinkedIn (same professional subject, different platforms) and with document-metadata extractors — SlideShare surfaces the files; a metadata tool mines what's embedded in them.

## Trust & verifiability
`trust: unverified` — a legitimate mainstream platform, but uploads are user-generated. Treat the professional context as leads to corroborate, and lean on the extractable document metadata for harder identity signals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slide-share |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
