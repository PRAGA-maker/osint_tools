---
id: advanced-search-operators-list
name: Advanced Search Operators List
description: Use when you need the correct advanced-search / dork syntax for a specific service (Google, Gmail, Twitter, GitHub, Shodan…) — returns links to each platform's official operator docs.
url: https://github.com/cipher387/Advanced-search-operators-list
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Quickly finding the official advanced-search operator documentation for 100+ services.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public GitHub repository; no account needed to read it.
opsec: passive
opsecNote: A static reference list on GitHub — reading it leaks nothing about your target. OpSec applies only when you subsequently run the operators against a live service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated by cipher387 (a well-known OSINT author); a link directory, so its value is the quality of the pointers rather than any data of its own.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- cipher387 advanced search operators
tags:
- ai-analysis-automation
- dorks
- reference
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- apis-for-osint
- awesome-grep
- code-understanding-tools-list
- dorks-collections-list
- grep-for-osint
- maltego-transforms-list
- python-osint-automation-examples
---

# Advanced Search Operators List

> A curated index of links to the official advanced-search / dork syntax docs for 100+ services — the fast way to look up the exact operator you need.

## When to use
You want to craft a precise query on a specific platform (Google, Bing, DuckDuckGo, Yandex, Gmail, Outlook, Discord, Twitter/X, LinkedIn, Reddit, YouTube, GitHub, GitLab, Slack, Shodan, Censys, FOFA and more) and need the authoritative operator reference rather than half-remembered syntax. It points you to each service's own documentation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/cipher387/Advanced-search-operators-list.
2. Scan the categorised README (search engines, communication tools, social platforms, dev platforms, IoT search engines, helper tools) for your target service.
3. Follow the link to that service's official operator documentation.
4. Build your query with the correct syntax, then run it in the actual service (or via a dork-collection tool).

## Inputs → Outputs
- **In:** none (you browse it by service name)
- **Out:** none as a selector — it returns documentation links, not data
- **Empty/negative result looks like:** the service you want isn't listed, or an upstream doc link has rotted — fall back to the service's own help pages.

## Gotchas & OpSec
- It is a directory of links, not a query engine — it never returns results, only tells you how to phrase them.
- Upstream operator docs change; a service may deprecate operators the list still references.
- OpSec is entirely about where you *run* the resulting query, not about reading the list.

## Overlaps ("do both")
- Pairs with `[[dorks-collections-list]]` — that gives ready-made dork queries, while this explains the operator syntax so you can write your own; use together to both learn and reuse.

## Trust & verifiability
`trust: community` — maintained by a recognised OSINT author, but it only aggregates links, so verify each operator against the linked official docs before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | advanced-search-operators-list |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
