---
id: wordpress-custom-search
name: WordPress Custom Search (Google Programmable Search)
description: Use when you have a `name`/`username`/keyword and want to search across WordPress-hosted blogs specifically — a scoped Google Programmable Search, no personal selectors out.
url: https://cse.google.com/cse?cx=011081986282915606282:w8bndhohpi0
category: search-engines
path:
- search-engines
bestFor: Keyword/name searching restricted to WordPress-hosted blog content via a prebuilt Google CSE.
selectorsIn:
- name
- username
selectorsOut: []
status: degraded
pricing: free
costNote: Free to use (Google Programmable Search / Custom Search Engine). No account needed to run a query.
opsec: passive
opsecNote: Queries go to Google's Programmable Search, not to any target site, so this is passive against your subject. Google logs the search against your session/IP as with any Google query; use a clean browser profile if you don't want it tied to your other research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Custom Search Engine; its site list and freshness are controlled by whoever built the CSE and are opaque. Coverage can silently degrade over time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- WordPress CSE
- WordPress blog search
tags:
- custom-search-engine
- blogs
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# WordPress Custom Search (Google Programmable Search)

> A prebuilt Google Custom Search Engine scoped to WordPress-hosted blogs — narrows a query to blog content instead of the whole web.

## When to use
You're hunting for a subject's blogging footprint, comments, or mentions and want to bias results toward WordPress-hosted sites rather than sifting the entire web. Enter a `name`, `username`, handle, or distinctive phrase. It returns web results (page links), not personal selectors directly — you read those off the pages you find.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE link (cse.google.com with the WordPress `cx`).
2. Enter your search terms — a name in quotes, a username, an email fragment, or a signature phrase.
3. Scan the results, which are constrained to the sites the CSE indexes (WordPress-oriented blogs).
4. Open promising pages and extract `name`/`username`/bio/contact details from the content.
5. Pivot: an author profile or handle → username-search tools; a phrase → a broader web search to find reposts.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword/phrase
- **Out:** web page links to WordPress-hosted blog content (selectors read from the pages, not returned structured)
- **Empty/negative result looks like:** no hits — which, for a scoped CSE, may mean the content isn't on an indexed site rather than that it doesn't exist. Re-run on a general search engine before concluding.

## Gotchas & OpSec
- **Opaque, possibly stale coverage:** you don't control which sites this CSE indexes, and third-party CSEs decay; treat empties as inconclusive and confirm with `site:` operators on a general engine.
- Not limited to `wordpress.com` alone — it targets WordPress-*powered* sites per its config, which is broad and imprecise.
- Passive; standard Google query logging applies to you.

## Overlaps ("do both")
- Reproduce and extend this with a general engine using `site:wordpress.com` or platform-specific dorks, which you fully control — use the CSE for convenience, the manual dork for completeness.

## Trust & verifiability
`trust: community` — a third-party-built search config with no transparency into its index. Handy as a quick scoped pass, but never treat its coverage as complete; verify on a controllable general search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wordpress-custom-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → (web results) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
