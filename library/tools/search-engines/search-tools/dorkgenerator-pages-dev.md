---
id: dorkgenerator-pages-dev
name: Dork Generator
description: Use when you have a `name`, `username`, `email` or `domain` and want ready-made Google dork queries to hunt it — returns advanced search-operator strings.
url: https://dorkgenerator.pages.dev/
category: search-engines
path:
- search-engines
- search-tools
bestFor: Quickly building advanced Google dork queries (site:, intext:, filetype:, etc.) to surface a selector across the open web.
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- social-profile
- document-id
status: live
pricing: free
costNote: Free static web app; no login. It only builds query strings — the searching happens on your chosen engine.
opsec: passive
opsecNote: The generator itself just assembles text and reveals nothing. The OpSec cost is in RUNNING the queries: those searches hit Google/Bing from your IP, and clicking through visits the target's assets. Run generated dorks from a sock-puppet/VPN session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small community front-end that assembles standard search operators; it invents nothing and stores nothing, so its output is only as good as the operators you feed it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Google Dork Generator
tags:
- dorking
- google
- search-operators
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Dork Generator

> A free helper that builds advanced Google dork queries from your selectors — a query-construction aid, not a search engine itself.

## When to use
You have a `name`, `username`, `email`, or `domain` and want to squeeze more out of Google/Bing than a plain search: find documents mentioning the person (`filetype:pdf`), pages on a specific site (`site:`), exact-phrase matches (`intext:`/quotes), or exposed files. The generator assembles the correct operator syntax so you don't have to remember it — useful for quickly producing a battery of targeted queries to run.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dorkgenerator.pages.dev/.
2. Enter your selector(s) and pick operators/filters (site, filetype, intext, intitle, date, etc.).
3. Copy the generated dork string(s).
4. Run them in a search engine (from a sock-puppet session) and work the results; a hit like a leaked `document-id` or a profile page feeds the next tool.

## Inputs → Outputs
- **In:** `name` / `username` / `email` / `domain`
- **Out:** advanced query strings that surface `social-profile` pages, `document-id`/files, and mentions
- **Empty/negative result looks like:** the generator always returns a query — "empty" is when the query itself yields no search results, meaning that operator combination found nothing; broaden or vary operators.

## Gotchas & OpSec
- It only builds queries; it does not search. Judgement about which operators fit the target is still on you.
- Aggressive dorking (many rapid queries, exposed-file hunting) can trip Google's bot detection and, if you click through, touch the target's servers — throttle and use a VPN.
- OpSec: the generator is passive; running the dorks is where exposure happens.

## Overlaps ("do both")
- Complements general search engines and other dork cheat-sheets — generate the query here, then run and iterate; pair with people/username tools to act on the hits.

## Trust & verifiability
`trust: community` — a simple, transparent query builder; it fabricates nothing, but the value comes entirely from the operators and results, which you must judge yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dorkgenerator-pages-dev |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, domain → social-profile, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
