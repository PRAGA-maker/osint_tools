---
id: onionsearch
name: OnionSearch
description: Use when you have a keyword, `name`, or `username` and want to search many Tor .onion search engines at once — returns aggregated .onion URLs matching the term as a CSV.
url: https://pypi.org/project/onionsearch/
category: dark-web
path:
- dark-web
bestFor: Bulk-querying 15+ darknet search engines from one command to collect .onion links matching a term.
selectorsIn:
- name
- username
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (megadose/OnionSearch); install via pip. Runs against public darknet search engines at no cost.
opsec: active
opsecNote: Scraping .onion search engines is active reconnaissance on the darknet. Run it through Tor from an isolated/VM environment, never from an attributable IP. It only queries search engines (not the listed hidden services), but visiting any returned .onion still requires Tor and caution — treat results as untrusted/possibly illegal content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A well-known open-source tool by megadose (author of holehe/toutatis); widely used, but a community scraper dependent on volatile darknet engines.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- ahmia
- torch
aliases:
- OnionSearch
- megadose OnionSearch
tags:
- dark-web
- tor
- darknet-search
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# OnionSearch

> One command that fans a keyword out across 15+ darknet search engines and aggregates the .onion hits into a CSV — the fast first sweep of Tor for a term, name, or handle.

## When to use
You need to know whether a keyword, `name`, `username`, brand, or leaked identifier surfaces anywhere the darknet indexes — marketplaces, forums, leak sites. Rather than querying Ahmia, Torch, Haystak, etc. one by one, OnionSearch scrapes many at once and gives you a deduped list of matching `.onion` URLs to triage.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install onionsearch` (or clone https://github.com/megadose/OnionSearch). You need Tor/`torsocks` for actually visiting results.
2. Run: `onionsearch "search term" --output results.csv` (add `--engines ahmia darksearchio ...` to limit engines, `--limit` to cap pages).
3. It queries each supported engine (ahmia, tordex, tor66, haystack, onionland, phobos, and more) and writes matching `.onion` URLs to CSV.
4. Triage the CSV: prioritise engines/hits relevant to your term; the tool returns links, not content.
5. Pivot: open promising `.onion`s **only** over Tor in an isolated VM (e.g. via `[[ahmia]]` for clearnet-safe previews); feed clearnet crossovers into standard OSINT.

## Inputs → Outputs
- **In:** a keyword / `name` / `username`
- **Out:** aggregated `.onion` `domain`s (URLs) matching the term, as CSV
- **Empty/negative result looks like:** few or no rows — the term isn't indexed by these engines, or engines were down/blocking (darknet search engines are flaky); retry later or with different engines.

## Gotchas & OpSec
- Darknet search engines change addresses and go offline constantly; some engine modules break over time — expect partial coverage and update the tool.
- OpSec: **active** and sensitive. Always run over Tor from a non-attributable, isolated environment. Returned services may host illegal content — collecting links is fine; do not download or interact beyond your authority.
- Results are unranked leads, not verified facts — every .onion needs manual, careful review.

## Overlaps ("do both")
- Pairs with `[[ahmia]]` and `[[torch]]` — OnionSearch aggregates across many engines for breadth; Ahmia offers a safer clearnet-accessible front end for reviewing hits.

## Trust & verifiability
`trust: community` — a popular, open-source tool by a respected OSINT developer; the code is auditable, but it depends on third-party darknet engines whose results are unvetted and volatile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onionsearch |
| category | dark-web |
| selectorsIn → selectorsOut | name, username → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
