---
id: google-cse-instances-search-engine
name: Google CSE instances Search Engine
description: Use when you have a `name`/`username`/`domain` and want to search a curated OSINT-focused Google Programmable Search Engine that queries only a hand-picked set of sources — returns web results (`social-profile`, `domain`).
url: https://cse.google.com/cse?cx=009462381166450434430:vggeu3dhhgg#gsc.tab=0
category: search-engines
path:
- search-engines
bestFor: Running a keyword/name query against a pre-built OSINT Google CSE that restricts results to a curated source list, cutting general-web noise.
selectorsIn:
- name
- username
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free Google Programmable Search Engine (formerly Custom Search Engine); no account needed to run queries.
opsec: passive
opsecNote: You submit a query string to Google's CSE infrastructure — passive with respect to the target (no site of theirs is touched). Google logs the search against your session/IP; use a sock-puppet/clean browser if the query itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Programmable Search Engine; Google runs the search, but the source list is curated by an unnamed maintainer and its exact scope is not independently documented.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Google Programmable Search Engine
- OSINT CSE
tags:
- search-engine
- google-cse
- programmable-search
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Google CSE instances Search Engine

> A pre-built Google Programmable Search Engine curated for OSINT — a name/keyword query restricted to a fixed set of sources instead of the whole web.

## When to use
You want the reach of Google search but scoped to a curated source list (a Programmable Search Engine narrows results to specific sites/domains chosen by its maintainer, reducing noise and personalization). Use it as one lens alongside a plain Google/Yandex search when hunting a `name`, `username`, or `domain`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL in a clean/sock-puppet browser.
2. Enter your query — a `name`, `username`, handle, or `domain`. Standard Google operators (quotes, `site:`, `-`) work.
3. Read the output: ranked web results drawn only from the CSE's configured sources; each links to a live page.
4. Pivot: follow promising hits to profiles/pages, then feed extracted selectors into dedicated enrichment tools. Re-run the same query on general Google to catch anything the CSE's narrow scope excluded.

## Inputs → Outputs
- **In:** `name` / `username` / `domain` (free-text query)
- **Out:** web results — links to `social-profile`s, `domain`s, articles within the curated scope
- **Empty/negative result looks like:** no hits can mean the term is absent *or* simply outside this CSE's configured sites — always corroborate with an unrestricted search before concluding nothing exists.

## Gotchas & OpSec
- The exact list of sites this CSE searches is defined by its config (`cx`) and is not publicly documented here — its scope may drift or the maintainer may retire it over time; treat coverage as unknown-but-curated.
- Human-in-the-loop: occasional Google CAPTCHA on heavy use.
- OpSec: passive toward the target; Google logs the query to your session.

## Overlaps ("do both")
- Do both with a plain Google `site:` search and Yandex — the CSE trades recall for a cleaner, curated slice, so run it alongside broad search rather than instead of it.

## Trust & verifiability
`trust: community` — Google executes the search reliably, but a third party chose the sources; verify each hit on its live page and never assume the curated scope is exhaustive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-cse-instances-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, domain → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
