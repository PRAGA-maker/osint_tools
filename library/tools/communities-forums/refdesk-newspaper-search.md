---
id: refdesk-newspaper-search
name: RefDesk Newspaper Search
description: Use when you have a subject's `name` and a `geolocation` and want the right local newspaper to search for coverage of them — returns links to regional news outlets.
url: http://www.refdesk.com/paper.html
category: communities-forums
path:
- communities-forums
bestFor: Finding the local/regional newspaper(s) covering a given US or world location so you can search them for a person.
selectorsIn:
- name
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free directory of external newspaper links; RefDesk hosts no content and requires no account.
opsec: passive
opsecNote: RefDesk itself is a passive link directory. OpSec depends on the newspaper sites you then visit — use a sock-puppet browser, since a local paper's site could log or paywall-track you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, well-known reference-desk site ("Fact Checker for the Internet"); it curates links to primary news sources rather than hosting claims itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- refdesk
aliases:
- refdesk.com newspapers
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# RefDesk Newspaper Search

> A curated directory of newspaper links organized by US state and by world region — the fast way to identify *which* local paper to search when you know where a subject lived.

## When to use
You have a `name` and a `geolocation` (a town, county, state, or country) and want to check local press for coverage of the person: obituaries, arrest/court reports, wedding/graduation notices, community stories, or local business mentions. National search engines miss much small-town journalism, so the first step is finding the actual regional outlet — this directory maps locations to their newspapers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.refdesk.com/paper.html.
2. Scroll to the subject's region — all 50 US states, plus world newspapers grouped by continent, and top-100 US papers / archive links.
3. Click through to the relevant local paper(s).
4. On each paper's own site, search the subject's `name` (and known associates/addresses); many carry searchable archives.
5. Pivot: a local-news hit can yield `associate` names, an `employer-org`, an `address`, a `dob` (from an obituary), or event dates — feed those into records and people-search tools.

## Inputs → Outputs
- **In:** `name` + `geolocation`
- **Out:** links to the region's newspaper sites (then, on those sites, articles mentioning the subject)
- **Empty/negative result looks like:** the directory always returns papers; the "miss" happens on the newspaper site itself when a name search yields nothing — try alternate spellings, nearby towns, and archive date ranges before concluding.

## Gotchas & OpSec
- RefDesk is only the *index* — the actual searching happens on each newspaper's site, whose archives, paywalls, and search quality vary widely.
- Link rot: some listed papers have merged, moved, or gone paywalled; verify the link before relying on it.
- OpSec: passive at RefDesk; individual paper sites may track or paywall — browse via a sock puppet.

## Overlaps ("do both")
- Pairs with `[[refdesk]]` (same provider's broader reference tools) and with general news-archive search engines — this pinpoints the *local* outlet a broad search would overlook.

## Trust & verifiability
`trust: trusted` — an established reference directory that points to primary news sources; verify any specific claim in the underlying article itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | refdesk-newspaper-search |
| category | communities-forums |
| selectorsIn → selectorsOut | name, geolocation → (local news links) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
