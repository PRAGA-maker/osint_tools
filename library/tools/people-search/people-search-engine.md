---
id: people-search-engine
name: People Search Engine
description: Use when you have a `name` or `username` and want a Google-powered search pre-scoped to people-finder and social sites — returns web links and social-profile leads from a curated custom search engine.
url: https://cse.google.com/cse?cx=14db36e158cd791c0
category: people-search
path:
- people-search
bestFor: Running a name/handle through a Google Custom Search Engine tuned to people-search and social sources in one query.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
- domain
status: degraded
pricing: free
costNote: Free — it's a Google Custom Search Engine (CSE). No account; results are Google-backed but limited to the sites the CSE creator configured.
opsec: passive
opsecNote: Passive — a Google-backed search that never contacts the subject. Your query goes to Google (and is subject to Google logging/personalization); use a sock-puppet browser/logged-out session to reduce attribution and filter-bubble effects.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built Google Custom Search Engine; its usefulness depends entirely on an unknown creator's site list, which can drift or degrade over time and is not maintained by a vendor.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- People Search CSE
- Google Custom Search people
tags:
- peoplesearch
- custom-search-engine
- google-cse
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# People Search Engine

> A Google Custom Search Engine (CSE) pre-scoped to people-finder and social sources — you get Google's index power but filtered to the sites most likely to hold a person's footprint.

## When to use
You have a `name` or `username` and want a people-focused search without hand-building a long `site:` dork. Because the CSE is restricted to a curated set of people-search and social sites, its results are denser with relevant profiles than a raw web search — a good quick pass early in a workup, or a second opinion alongside a general engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cse.google.com/cse?cx=14db36e158cd791c0 in a browser (logged-out/sock-puppet session recommended).
2. Enter the `name` in quotes, or a `username`, optionally with a city/employer disambiguator.
3. Read the results — they come from Google but are restricted to the CSE's configured people/social sites, so expect profile pages, directory listings, and social links.
4. Open and confirm each `social-profile`/directory hit against a second selector.
5. Pivot: feed profiles into username tools (`[[gaddr]]`, `[[360username-com]]`), and confirm directory/people-search hits against an authoritative source.

## Inputs → Outputs
- **In:** `name` / `username` (+ optional disambiguator)
- **Out:** `social-profile` links, `name` matches, personal/directory `domain`s
- **Empty/negative result looks like:** few or no hits — but because coverage is limited to the CSE's site list, a blank result mainly means "not on those sites," not "no footprint." Fall back to a broad engine like `[[webcrawler-com]]` or native Google dorking.

## Gotchas & OpSec
- It's only as good as the (unknown) creator's site list, which can go stale — sites drop out, the CSE can even stop returning results. Treat coverage as opaque and possibly degraded; that's why status is `degraded`.
- Results are still Google-ranked and personalized to your session — use logged-out to avoid your own filter bubble.
- Passive; nothing reaches the subject. Your query is logged by Google.
- No advanced-operator guarantees; the CSE may ignore some Google dork syntax.

## Overlaps ("do both")
- Pairs with `[[webcrawler-com]]` — the CSE gives a curated people-focused slice; metasearch gives broad blended coverage. Run both.
- Feed hits onward to `[[searchpeoplefree]]` / `[[canada411-advanced-search-whitepages-ca]]` for structured contact/address data.

## Trust & verifiability
`trust: community` — a useful but unmaintained community CSE whose value hinges on an unknown creator's configuration. Use it for lead generation; verify every hit against the primary source, and don't assume its coverage is current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | people-search-engine |
| category | people-search |
| selectorsIn → selectorsOut | name, username → social-profile, name, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
