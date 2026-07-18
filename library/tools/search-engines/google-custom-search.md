---
id: google-custom-search
name: Google Custom Search
description: Use when you have a set of sites (or a whole search vertical) and want a reusable Google-powered search box scoped to just them — returns Google web results restricted to your chosen `domain` set.
url: https://programmablesearchengine.google.com/about/
category: search-engines
path:
- search-engines
bestFor: Building a reusable search engine that queries Google but only over a hand-picked list of sites (or a topic), for repeatable scoped OSINT sweeps.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free tier searches your defined sites with AdSense ads; the JSON API is free up to 100 queries/day then paid. The hosted search UI itself is free to build and use.
opsec: passive
opsecNote: Queries run on Google's infrastructure, not against the target, so nothing reaches the subject. Building an engine requires a Google account, which ties the CSE (and any API key) to that identity — use a dedicated investigative Google account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google product (Programmable Search Engine, formerly Custom Search); results are genuine Google index results scoped by your configuration.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- Google Programmable Search Engine
- Google CSE
- Programmable Search
tags:
- speciality-search-engines
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Google Custom Search

> Google's Programmable Search Engine — roll your own Google-backed search box scoped to a curated list of sites, so a scoped OSINT query is one click instead of a page of `site:` operators.

## When to use
You repeatedly search the same universe of sites — say a dozen regional forums, a set of social platforms, or all local-newspaper domains — and want a saved, reusable engine rather than retyping `site:` filters. Point a Programmable Search Engine at those domains, then query a `name` or `username` and get Google-quality results confined to exactly that set. It is also scriptable: the JSON Custom Search API lets you automate the same scoped query from code.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in with an investigative Google account at https://programmablesearchengine.google.com and click **Add** / **Create**.
2. List the sites to search (specific `domain`s), or choose "Search the entire web but emphasize included sites."
3. Save — you get a hosted search page (and an embeddable widget) plus a **Search engine ID (cx)**.
4. Query your selectors (`name`, `username`, phrases) in that engine; results are Google hits limited to your configured sites.
5. To automate: create an API key, then call the Custom Search JSON API with your `cx` — free up to 100 queries/day.
6. Pivot: results feed straight into `social-profile`/`domain` follow-up; save several engines for different investigation verticals.

## Inputs → Outputs
- **In:** `name`, `username`, keywords — plus, at setup, the list of `domain`s to scope to
- **Out:** Google web results confined to your site set → `social-profile`, `domain`, page mentions
- **Empty/negative result looks like:** no results within the scoped sites — the subject isn't on those specific domains; widen the site list or drop back to open Google before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** — you must be signed into a Google account to build and manage an engine. Use a sock-puppet/investigative account.
- OpSec: **passive** toward the target (Google runs the query), but the engine and any API key are bound to your Google identity — keep that identity segregated.
- Scope is a double-edged sword: results are only as complete as your site list, so a blank means "not in these sites," not "not online."
- The free JSON API cap (100/day) is easy to hit when scripting; batch queries or upgrade.

## Overlaps ("do both")
- Complements open-web engines like `[[swisscows]]` and mainstream Google `site:` searches — the CSE is for *repeatable, scoped* sweeps, the open engines for breadth.

## Trust & verifiability
`trust: trusted` — it is a first-party Google product returning real Google index results; the only variability is the site scope you configure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-custom-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
