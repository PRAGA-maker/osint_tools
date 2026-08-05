---
id: slideshare-search-engine
name: SlideShare Search Engine
description: Use when you have a name, org, or topic and want presentations/documents about it on SlideShare specifically — returns matching decks and their author/company clues (a scoped Google Custom Search).
url: https://cse.google.com/cse?cx=465eeeb114c7f523f
category: search-engines
path:
- search-engines
bestFor: Searching SlideShare presentations for a person, company, or topic via a prebuilt Google Custom Search Engine.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- social-profile
status: live
pricing: free
costNote: Free — a public Google Custom Search Engine over SlideShare; no account required.
opsec: passive
opsecNote: This is a Google search scoped to SlideShare; your query goes to Google, not to any subject. Nothing here contacts a target. Use a sock-puppet browser if the query terms are sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google CSE; scope depends on the opaque CSE config and may drift, so treat coverage as approximate and cross-check with a plain site: search.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SlideShare CSE
tags:
- google-cse
- document-search
- presentations
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# SlideShare Search Engine

> A prebuilt Google Custom Search Engine narrowed to SlideShare — surfacing the presentations, pitch decks, and documents people and companies upload there, which often leak names, roles, org charts, and contact details.

## When to use
Presentations are an underused OSINT goldmine: conference decks, corporate slides, and training material routinely name employees, titles, projects, and email formats. When investigating a person or `employer-org`, this CSE restricts the search to SlideShare so those documents rise to the top instead of being buried in general results. Hits are documents to open; the intelligence is inside them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL (a public Google Custom Search page).
2. Enter a `name`, company, project, or topic.
3. Read the results — SlideShare decks matching the query. Open promising ones for author names, job titles, org structure, email patterns, and internal jargon.
4. Pivot: an author/uploader feeds people- and username-search; named colleagues feed org mapping; an email format feeds email-permutation tools.

## Inputs → Outputs
- **In:** a `name`, `employer-org`, project, or topic
- **Out:** matching SlideShare presentations (yielding `employer-org` detail, author `social-profile`s, contact patterns)
- **Empty/negative result looks like:** few or no decks — the subject/org may not publish on SlideShare, or the CSE scope may miss them; cross-check with a general `site:slideshare.net` search before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — a Google-backed search; it leaks nothing to the subject.
- The CSE config is opaque and may drift, so its scope is approximate — verify a null result with a manual `site:slideshare.net` query.

## Overlaps ("do both")
- Pairs with general [[google-dorking]] (`site:slideshare.net "Company Name"`) and other document-search engines — the CSE is a quick prebuilt lens, hand-crafted dorks give precise control; run both when documents matter.

## Trust & verifiability
`trust: community` — a user-built CSE over Google's index. The results are Google's, but the filtering is third-party and unauditable; the real evidence is the content of each deck, which you should read and corroborate directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slideshare-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
