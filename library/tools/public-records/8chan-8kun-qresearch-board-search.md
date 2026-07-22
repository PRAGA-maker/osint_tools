---
id: 8chan-8kun-qresearch-board-search
name: 8chan/8kun QResearch Board Search
description: Use when you have a `username`, name, or keyword and want to search millions of archived 8chan/8kun QResearch posts and linked datasets — returns matching posts and context.
url: https://qresear.ch/
category: public-records
path:
- public-records
bestFor: Full-text searching archived 8chan/8kun QResearch board posts and associated Q/leak datasets by keyword or URL.
selectorsIn:
- username
- name
selectorsOut: []
status: live
pricing: free
costNote: Free with no advertising or tracking, per the site; no account required.
opsec: passive
opsecNote: You query a static archive, not the live boards, so nothing is sent to the original posters or 8kun. The content is extremist/conspiracy-linked — handle findings carefully and consider the reliability and legality issues of the underlying material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent archive/search over 8chan/8kun QResearch content; useful for retrieval, but the underlying posts are anonymous, unverified, and often conspiratorial — corroborate everything.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- qresear.ch
- QResearch board search
tags:
- imageboard-archive
- forums
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# 8chan/8kun QResearch Board Search

> A free full-text search over ~28M archived 8chan/8kun QResearch posts and linked datasets — retrieve what an anonymous handle or a name has been mentioned in, without touching the live boards.

## When to use
Your investigation intersects the QAnon/8kun ecosystem: you want to find posts referencing a `name`, a `username`/tripcode, a domain, or a keyword across the QResearch board archive and its bundled datasets (Q-posts, leaks, etc.). Because 8chan/8kun content is otherwise hard to search and much is deleted from the live sites, this archive is often the only way to retrieve it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://qresear.ch/.
2. Enter a keyword/keyphrase, a name, a tripcode/handle, or a URL and search.
3. Review the matching posts — each links to its board/thread context and timestamp.
4. Treat every hit as anonymous, unverified content; note the thread and date for your record.
5. Pivot: names, handles, links or claims found here become leads to verify through independent, authoritative sources — never cite the board post itself as fact.

## Inputs → Outputs
- **In:** a `username`/tripcode, `name`, keyword, or URL
- **Out:** matching archived posts with board/thread context and timestamps
- **Empty/negative result looks like:** no hits means the term doesn't appear in the archived corpus — not proof it was never posted (some content is deleted or outside the dataset).

## Gotchas & OpSec
- The material is anonymous, conspiratorial, and frequently false or harmful — retrieval ≠ verification; corroborate independently and handle sensitive/defamatory content responsibly.
- It's an archive snapshot; coverage and freshness are limited to what has been ingested.
- OpSec: passive against a static archive; you are not touching the live boards.

## Overlaps ("do both")
- Pairs with general imageboard archives and the Wayback Machine — this is QResearch-specific and dataset-rich, while broader archives cover other boards and deleted pages.

## Trust & verifiability
`trust: community` — a useful retrieval index over inherently unreliable source content; trust the *search*, not the *posts*, and verify every claim elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 8chan-8kun-qresearch-board-search |
