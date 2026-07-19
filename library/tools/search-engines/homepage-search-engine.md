---
id: homepage-search-engine
name: Homepage Search Engine
description: Use when you have a `name`/`username` and want to search across a curated set of personal-homepage/website sources — returns web pages and `social-profile` links via a Google Programmable Search Engine.
url: https://cse.google.com/cse?cx=005797772976587943970:3tu7im1-rdg#gsc.tab=0
category: search-engines
path:
- search-engines
bestFor: Running a name/username query against a pre-scoped Google Custom Search Engine biased toward personal homepages and profile sites.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free to use; it is a hosted Google Programmable Search Engine with no account required.
opsec: passive
opsecNote: Queries go to Google's Programmable Search infrastructure like any Google search — passive toward the target. Use a sock-puppet Google session/IP if you don't want the query tied to you, and be aware Google logs the search.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google CSE; you cannot see its exact site list, and coverage depends entirely on whatever domains the (unknown) creator scoped it to and may drift over time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Homepage CSE
tags:
- google-cse
- search-engine
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Homepage Search Engine

> A hosted Google Programmable Search Engine pre-scoped toward personal homepages and profile sites — a quick way to run a name/username query against a curated slice of the web instead of all of Google.

## When to use
You have a `name` or `username` and want a search that leans toward personal websites, homepages, and profile pages rather than the whole open web. Because the CSE is restricted to a curated set of sources, it can surface a subject's own site or profile faster than a broad Google query — but the exact scope is opaque, so treat it as one lens among several.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE: https://cse.google.com/cse?cx=005797772976587943970:3tu7im1-rdg#gsc.tab=0
2. Enter the `name` (in quotes for exact match) or `username`; add a disambiguating term (city, employer) if results are noisy.
3. Review hits — this CSE biases toward homepage/profile-style pages; open promising results for a `social-profile` or personal `domain`.
4. Re-run with alternate name spellings/handles.
5. Pivot: a discovered personal domain feeds WHOIS/domain tooling; a social profile feeds username-enumeration tools.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** web pages, personal `domain`s, and `social-profile` links from the CSE's scoped sources
- **Empty/negative result looks like:** no results, or only generic/irrelevant hits — meaning the subject isn't within this CSE's curated scope, not that they have no web presence. Fall back to full-web search.

## Gotchas & OpSec
- The site list behind a third-party CSE is invisible to you and can silently change; never treat a null result as authoritative.
- Google may throw a CAPTCHA on repeated queries — solve it manually.
- OpSec: passive, but tied to your Google session — use a sock puppet if attribution matters.

## Overlaps ("do both")
- Pairs with a full-web engine and username-search tools — this narrows toward homepages while a broad engine catches everything the CSE's scope excludes.

## Trust & verifiability
`trust: community` — it is a genuine Google search product, but configured by an unknown third party; the underlying Google index is reliable, the *scope selection* is not verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | homepage-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
