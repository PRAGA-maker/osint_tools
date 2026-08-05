---
id: taylor-and-francis-online
name: Taylor & Francis Online
description: Use when you have a `name` who may be an academic and want their scholarship — returns papers exposing affiliation (`employer-org`) and co-authors (`associate`).
url: https://www.tandfonline.com
category: search-engines
path:
- search-engines
bestFor: Finding an author's journal articles across Taylor & Francis titles and reading the affiliations/co-authors they reveal.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free to search and read article metadata (title, authors, affiliation, abstract); full text is often paywalled unless the article is open-access.
opsec: passive
opsecNote: Searching a public publisher database is passive; the author is not notified. Nothing you query reaches the subject. Standard browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official platform of Taylor & Francis, a major academic publisher; author/affiliation metadata is authoritative, though full text may be paywalled.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- oa-mg
- crossref
- base
- core
aliases:
- tandfonline
- Taylor and Francis Online
tags:
- academic-search
- journals
- news
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Taylor & Francis Online

> The journal platform of a major academic publisher — a place to pin down an academic subject's publications, their institution, and the people they publish with.

## When to use
Your subject may be an academic or researcher and you want their scholarly record from one of the big publishers. Even behind a paywall, the *metadata* is free and valuable: article titles, the full author list, each author's stated `employer-org` affiliation, publication dates, and abstracts. That confirms an identity, a current/past institution, a research area, and a network of co-authors (`associate`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tandfonline.com and search the author `name` (quote it; add a field or institution to disambiguate common names).
2. For breadth, also run `site:tandfonline.com "Full Name"` in a general engine.
3. Open matching articles and read the free metadata: authors, affiliations, dates, abstract. Open-access articles give full text.
4. Pivot: affiliation → `employer-org`; co-authors → `associate` leads; corresponding-author email (when shown) → an `email` selector.

## Inputs → Outputs
- **In:** `name` (optionally + field/institution)
- **Out:** journal articles → `employer-org` (affiliation), `associate` (co-authors), dates
- **Empty/negative result looks like:** no articles, or only same-name strangers. Absence means the subject hasn't published in T&F titles — not that they aren't an academic; check other publishers/indexes.

## Gotchas & OpSec
- Full text is frequently paywalled — you can still use the free metadata, which is what matters here; find open copies via `[[oa-mg]]`/`[[core]]`.
- Common-name collisions are frequent; confirm via affiliation and co-author overlap.
- OpSec: passive; searching reveals nothing to the subject.

## Overlaps ("do both")
- Run the same name through `[[oa-mg]]`, `[[crossref]]`, `[[base]]`, and `[[core]]` — those aggregate across publishers and often surface a free full-text copy of a T&F paywalled paper, and cross-index co-author overlap confirms identity.

## Trust & verifiability
`trust: trusted` — it's the publisher's own authoritative platform, so author/affiliation metadata is reliable; still corroborate identity (name+affiliation) before attributing work to your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | taylor-and-francis-online |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
