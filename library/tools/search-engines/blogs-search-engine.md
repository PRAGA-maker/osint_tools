---
id: blogs-search-engine
name: Blogs Search Engine
description: Use when you have a `name`/`username`/keyword and want a person's blog posts — returns matching blog articles and author `social-profile`s.
url: https://cse.google.com/cse?cx=013991603413798772546:8c1g6f0frp8#gsc.tab=0
category: search-engines
path:
- search-engines
bestFor: Searching across blogging platforms at once for a person's posts or a topic.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free Google Custom Search Engine; no account.
opsec: passive
opsecNote: Passive — results come from Google's index, so you never hit the blog hosts directly and the author gets no signal. Standard Google-query hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Google Custom Search Engine scoped to blogging sites; coverage is defined by the CSE's creator and can drift or break over time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- blog search CSE
tags:
- google-cse
- blogs
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Blogs Search Engine

> A Google Custom Search Engine scoped to blogging platforms — find where a `name`, handle, or topic has been written about across blogs.

## When to use
Blogs are a durable, self-authored source: people write under their own names, reveal opinions, locations, employers, and life events, and link their other profiles. When you have a `name`/`username` and want their blogging footprint (or want to research a topic across many blogs at once), this CSE narrows Google to blog content.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL (a Google Custom Search Engine over blogging sites).
2. Search a `name`, `username`, or distinctive phrase; use quotes for exact matches.
3. Read the hits: post titles, author bylines, dates, and the blog's own about/contact pages.
4. Pivot: an author byline/handle feeds username enumeration; an "about me" page often leaks employer, location, and linked `social-profile`s.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** blog posts and author `social-profile`s / bylines
- **Empty/negative result looks like:** no hits — the person may not blog, or their blog isn't in this CSE's scope; fall back to a broad Google search or platform-specific search.

## Gotchas & OpSec
- CSE scope is fixed by its creator and opaque — coverage is partial and can silently degrade; gaps mean "not covered," not "doesn't exist."
- Blog content can be old or abandoned; corroborate that it's the same person before relying on details.
- Self-authored ≠ true — treat claims in posts as leads.

## Overlaps ("do both")
- Pairs with general Google dorking and the [[mailing-list-archives-search-engine]] — different self-authored corpora (blogs vs list posts) surface different facets of the same person.

## Trust & verifiability
`trust: community` — a third-party Google CSE; the underlying blog posts are as trustworthy as their authors, while the search scope is curator-defined and unverifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blogs-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
