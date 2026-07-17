---
id: justia-blawgsearch
name: Justia BlawgSearch
description: Use when you have a `name`, firm or legal topic and want law-blog coverage — returns legal blog posts and blawg authors that can surface an attorney's writing and affiliations.
url: https://blawgsearch.justia.com/
category: search-engines
path:
- search-engines
bestFor: Searching law blogs ("blawgs") for an attorney, firm, or legal topic.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free search, part of Justia's free legal-resource network; no account required.
opsec: passive
opsecNote: A public keyword search on Justia's index — nothing about the subject is exposed and no one is alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Justia, a long-established free legal-information provider; it indexes real, attributed law-blog content, so results are verifiable at the source blog.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- justia-us-supreme-court-center-united-states
aliases:
- BlawgSearch
- Justia blawg search
tags:
- toddington
- curated-directory
- specialty-search
- legal
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Justia BlawgSearch

> A search engine for law blogs — the niche way to find what a lawyer or firm has written, and who writes about a legal topic.

## When to use
Your subject is (or may be) an attorney, legal professional, or firm, or you're researching a legal topic tied to a case. BlawgSearch indexes "blawgs" (law blogs), so you can surface an individual's published legal writing, the firm/organisation they blog under, their areas of practice, and commentary connecting people to matters — useful for confirming a professional identity or mapping expertise and affiliations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://blawgsearch.justia.com/.
2. Search the subject's `name`, firm/`employer-org`, or a legal topic; you can also browse blawgs by category and popularity.
3. Read the results: matching blog posts with author and blog (firm) attribution.
4. Open the source blog for author bios, firm details, contact info, and further posts.
5. Pivot: an author bio → `employer-org`, practice area, and often a professional `social-profile`/website; a firm blog → colleagues and case commentary.

## Inputs → Outputs
- **In:** `name`, firm/`employer-org`, or legal topic
- **Out:** law-blog posts with author/firm attribution → `social-profile` (author/blog) and `employer-org` leads
- **Empty/negative result looks like:** no posts — the person doesn't blog (many practising lawyers don't), or writes elsewhere. Absence here says nothing about whether they're a lawyer; check bar directories and Justia's lawyer listings instead.

## Gotchas & OpSec
- Scope is narrow: only law-*blog* content, not case law, dockets, or bar records. Most attorneys won't appear.
- Passive and free — safe to search freely.
- A post attributed to a name is a lead to verify at the source; confirm identity via the blog's bio and an independent bar/firm listing.

## Overlaps ("do both")
- Do both with `[[justia-us-supreme-court-center-united-states]]` and other legal-records sources (CourtListener/RECAP, state bar directories): BlawgSearch finds a lawyer's *commentary and voice*, while dockets and bar records give the *authoritative professional record*.

## Trust & verifiability
`trust: trusted` — run by Justia, a reputable free legal-information service; indexed posts are real and attributed, so you can verify every hit directly at its source blog.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | justia-blawgsearch |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
