---
id: wordpress-content-snatcher
name: WordPress Content Snatcher
description: Use when you have a name, handle, or keyword and want to search across WordPress-hosted blogs specifically — returns matching blog posts/pages (a scoped Google Custom Search).
url: https://cse.google.com/cse/publicurl?cx=011081986282915606282:w8bndhohpi0
category: search-engines
path:
- search-engines
bestFor: Running a keyword/name search restricted to WordPress blog content via a prebuilt Google Custom Search Engine.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free — a public Google Custom Search Engine; no account required.
opsec: passive
opsecNote: This is a Google search scoped to WordPress sites; your query goes to Google, not to any subject. Nothing here contacts a target. Use a sock-puppet browser if the query terms are sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Custom Search Engine; its scope depends on the (opaque) CSE config and can drift over time, so treat coverage as approximate.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WordPress CSE
tags:
- google-cse
- blog-search
- content-search
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# WordPress Content Snatcher

> A prebuilt Google Custom Search Engine narrowed to WordPress-hosted content — the same Google index, filtered so blog posts and pages surface without the rest of the web drowning them out.

## When to use
You suspect a subject blogs, comments, or is written about on WordPress sites, and a plain web search buries those results. This CSE restricts the query to WordPress content so bios, author pages, and posts rise to the top. It is a scoped search lens; hits are pages to open and read, and any subject data comes from those pages, not the tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL (a public Google Custom Search page).
2. Enter a name, `username`, email fragment, or topic keyword.
3. Read the results — WordPress blog posts/pages matching the query. Open promising hits to read author bios, post content, and comment threads.
4. Pivot: an author page or handle feeds username- and people-search; a self-hosted WordPress domain feeds domain/WHOIS OSINT.

## Inputs → Outputs
- **In:** a `name`, `username`, keyword, or phrase
- **Out:** matching WordPress blog posts/pages (leading to `social-profile`/author info on those pages)
- **Empty/negative result looks like:** few or no hits — the subject may not use WordPress, or the CSE's scope may exclude the relevant sites; fall back to a general search before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — a Google-backed search; it leaks nothing to the subject.
- The CSE's configuration is opaque and may narrow or drift over time, so its "WordPress-only" scope is approximate — cross-check with a general search using `site:` operators for reliability.

## Overlaps ("do both")
- Pairs with general [[google-dorking]] (`site:wordpress.com`, `inurl:/wp-content/`) — the CSE is a quick prebuilt lens, hand-crafted dorks give precise, controllable scope; run both when blog presence matters.

## Trust & verifiability
`trust: community` — a user-built CSE over Google's index. The underlying results are Google's, but the filtering is third-party and unauditable, so verify coverage against manual `site:` searches before trusting a null result.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wordpress-content-snatcher |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
