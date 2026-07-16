---
id: people-search
name: People Search (iTools)
description: Use when you have a `name` and want a curated jump-off directory of people-search engines to run it through — returns links to address, phone, email and social-profile lookup tools.
url: http://itools.com/search/people-search
category: people-search
path:
- people-search
bestFor: A hand-picked launchpad of people-finder services (Spokeo, Wink, reverse phone/address, etc.) to run one name across several engines.
selectorsIn:
- name
selectorsOut:
- address
- phone
- email
- social-profile
status: live
pricing: freemium
costNote: The iTools directory is free to browse. The individual tools it links to are a mix of free and paywalled (Spokeo and similar background-check services charge for full reports).
opsec: passive
opsecNote: Browsing the iTools directory is passive and leaks nothing about the target. OpSec risk begins only when you follow a link and submit the target's name to a downstream engine — assess each destination separately and use a sock-puppet where the destination logs queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: iTools is a long-running independent tools portal; it is a link directory, not a data broker, so trust concerns attach to the downstream services it points at rather than to iTools itself.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- itools people search
tags:
- people-search
- directory
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- wink
---

# People Search (iTools)

> A curated directory page, not a search engine — it collects the better people-finding services in one place so you can fan a single name out across several of them.

## When to use
You have a `name` (optionally with a city/state) and want a vetted list of people-search engines to try, rather than guessing which broker to use. Good as a first "where do I even look" step when you don't already have a preferred stack of people-finders.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://itools.com/search/people-search.
2. Scan the listed tools (Spokeo, Wink People Search, Yahoo/reverse lookups, background-check services) — each entry describes what it does.
3. Click through to a destination engine and enter the target `name` there.
4. Read the destination's output — most give a teaser (city, age range, relatives) free and gate full contact data behind payment.
5. Pivot: run the same name through 2–3 different engines from the list; overlap between them is your confidence signal. Feed confirmed hits into a full people-search like `[[peoplelooker-us]]` or public records.

## Inputs → Outputs
- **In:** `name` (best with a location qualifier)
- **Out:** links leading to `address`, `phone`, `email`, `social-profile`, relatives/associates — via the downstream tools, not iTools itself
- **Empty/negative result looks like:** iTools always renders its directory (it doesn't "search"), so an empty result only happens at the downstream engine — treat each destination's "no records" independently.

## Gotchas & OpSec
- iTools returns nothing about a person by itself — it is a menu. Don't record it as a source of a fact; record the downstream engine that produced the fact.
- Some linked entries are stale or now paywalled; verify each destination is still live before trusting it.
- OpSec: passive at the directory layer; the real exposure is whatever you type into the downstream broker. Use a sock-puppet browser session for engines that log queries.

## Overlaps ("do both")
- Pairs with any concrete people-finder such as `[[peoplelooker-us]]` — iTools tells you which engines exist; those engines actually return the data.

## Trust & verifiability
`trust: community` — an independent, well-established link portal. Because it only aggregates links, its reliability is really the reliability of whatever service you click into; validate each one on its own merits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | people-search |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, email, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
