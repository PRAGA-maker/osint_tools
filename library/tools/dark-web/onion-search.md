---
id: onion-search
name: OnionSearch
description: Use when you have a keyword, `name`, `username`, or `email` and want to search across many dark-web (.onion) search engines at once — returns onion result links (`domain`).
url: https://github.com/megadose/OnionSearch
category: dark-web
path:
- dark-web
bestFor: Scraping results for a query across dozens of dark-web search engines in a single command.
selectorsIn:
- name
- username
- email
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source Python CLI (pip installable); requires a local Tor proxy.
opsec: passive
opsecNote: You query dark-web search engines through Tor — this doesn't contact your subject, so it's passive toward them. But dark-web work is high-risk: run it only inside a hardened, isolated environment ([[whonix]]/Tails), never on your main machine, and never open a result .onion casually.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by megadose (author of holehe/toutatis); it aggregates third-party onion search engines whose index quality, uptime, and result legality vary widely.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- holehe
- palenath
- toutatis
aliases:
- OnionSearch
tags:
- Search engines
- Darknet/deepweb search tools
- dark-web
- tor
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# OnionSearch

> One command that fans a query out across many dark-web search engines and collects the .onion result links — a breadth-first entry point to the Tor network.

## When to use
You have a selector — a `name`, `username`, `email`, brand, or keyword — and want to see whether it surfaces anywhere indexed by dark-web search engines (marketplaces, forums, leak/paste sites). Instead of querying each onion search engine by hand, OnionSearch scrapes many of them at once and aggregates the hits, giving you a fast map of where to look next. Relevant when an investigation reaches into leaked data or dark-web activity.

## How to use it (`bestInteractionPattern`: cli)
1. Inside an isolated Tor-capable environment ([[whonix]] / Tails / a dedicated VM), install: `pip3 install onionsearch` (or clone `https://github.com/megadose/OnionSearch`).
2. Ensure a local Tor SOCKS proxy is running (the tool routes engine queries through it).
3. Run: `onionsearch "<query>" --output results.txt` (flags let you pick engines, limit pages, set output format).
4. Review the aggregated `.onion` result links and their source engines.
5. Pivot: treat each result as a lead to examine **safely** — record the onion address, but only visit anything from a hardened, disposable environment; correlate usernames/emails with clearnet tools like [[holehe]] / [[toutatis]].

## Inputs → Outputs
- **In:** a query — `name`, `username`, `email`, or keyword
- **Out:** aggregated `.onion` result links (`domain`) with their source search engine
- **Empty/negative result looks like:** few or no results — many onion search engines are down, rate-limited, or have thin indexes at any given time; re-run later and don't read emptiness as "nothing exists on Tor".

## Gotchas & OpSec
- Onion search engines are **unreliable** — some in the tool's list will be offline; expect partial coverage every run.
- Results can point to illegal/harmful content; treat addresses as leads to assess carefully and lawfully, not destinations to browse freely.
- OpSec: mandatory isolation. Use [[whonix]]/Tails, never your real IP/host, and never log into anything that identifies you.

## Overlaps ("do both")
- Pair with clearnet identity tools ([[holehe]], [[toutatis]]) to correlate any username/email you find, and run it from within [[whonix]] for the required network isolation.

## Trust & verifiability
`trust: community` — a reputable open-source aggregator, but it only relays third-party onion engines; verify any lead independently and assume result quality is uneven.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onion-search |
| category | dark-web |
| selectorsIn → selectorsOut | name, username, email → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
