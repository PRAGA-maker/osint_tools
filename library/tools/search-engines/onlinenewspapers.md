---
id: onlinenewspapers
name: OnlineNewspapers
description: Use when you need to find local/regional newspapers for a specific country or city to search for a subject or event — a directory of thousands of newspapers worldwide.
url: http://www.onlinenewspapers.com
category: search-engines
path:
- search-engines
bestFor: Locating local and national newspaper websites by country/region to find hyperlocal coverage of a person or event.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free directory; no account.
opsec: passive
opsecNote: Browsing a directory and reading published news is passive — nothing is sent to any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing directory of newspaper websites; it's a link index, so the authority of any story is the individual outlet's, and some listed links may be stale.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Online Newspapers
- onlinenewspapers.com
tags:
- news
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# OnlineNewspapers

> A worldwide directory of newspaper websites organized by country and region — the fastest way to find the *local* outlet that would have covered a person or event.

## When to use
Hyperlocal coverage often holds the details national media and Google miss — an obituary, a court notice, a small-town incident, a school or club mention. When your subject or event is tied to a specific place, OnlineNewspapers helps you find that town/region's papers so you can search each one directly, especially outside the well-indexed English-language web.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.onlinenewspapers.com and drill down by continent → country → region/city.
2. Open the relevant local paper(s) from the list.
3. Use each paper's own search (or a site-scoped Google `site:` query) for the subject's `name`, event, or address.
4. Repeat across neighboring towns/regions for fuller coverage.
5. Pivot: names, dates and places in local stories feed people-search, public-records and mapping tools; archive any story you rely on.

## Inputs → Outputs
- **In:** a country/region/city (to find outlets) — you then search each paper
- **Out:** a list of local/national newspaper websites for that place
- **Empty/negative result looks like:** a region with few listed papers, or dead links — the directory is a link index that can go stale; supplement with a search-engine `site:`/news query for that locale.

## Gotchas & OpSec
- It points you to papers; it doesn't search their content — you search each outlet yourself.
- Some listings are outdated (papers close or move) — expect broken links.
- Paywalls/local-language content are common; pair with a translator and archive tools.

## Overlaps ("do both")
- Pairs with Google News/`site:` searches and news archives — the directory finds the *right local outlet*, then search engines and archives retrieve and preserve the specific story.

## Trust & verifiability
`trust: community` — a useful link directory; trust the *outlet* you land on, not the directory, and verify any story against the paper's own page (and an archive copy).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onlinenewspapers |
