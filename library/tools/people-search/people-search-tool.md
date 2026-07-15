---
id: people-search-tool
name: People Search Tool (Aware Online)
description: Use when you have a `name`, `username`, `email`, or `phone` and want ready-made search-engine queries across Google/Bing/Yandex/Baidu — returns social-profile, name, and address leads.
url: https://www.aware-online.com/en/osint-tools/people-search-tool/
category: people-search
path:
- people-search
bestFor: One-click query-builder that fires a person's identifier at multiple search engines with OSINT-optimised dorks.
selectorsIn:
- name
- username
- email
- phone
selectorsOut:
- social-profile
- name
- address
- associate
status: live
pricing: free
costNote: Free browser-based query generator from Aware Online Academy; no account, no payment. It does not host data itself — it redirects your query to third-party search engines.
opsec: passive
opsecNote: The tool builds and launches searches from YOUR browser against Google/Bing/Yandex/Baidu, so those engines log the queries under your IP; nothing is sent to or seen by the target. Run it behind a sock-puppet browser/VPN if you don't want the queries tied to you. Note Yandex/Baidu are Russian/Chinese-jurisdiction engines.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published by Aware Online Academy, an established Dutch OSINT training provider. It is a query builder, not a data source, so there is no scraped-data quality risk — only the quality of the underlying engines.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- google-dorks
aliases:
- Aware Online people search
- aware-online person search tool
tags:
- people-search
- search-engine-dorks
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# People Search Tool (Aware Online)

> A free query-builder that turns one identifier (name/username/email/phone) into optimised searches across four major search engines in one click.

## When to use
You have a single selector for a person — a `name`, `username`, `email`, or `phone` — and you want to sweep the general web quickly without hand-writing dorks. This is a good first, wide pass at the start of a person investigation: it surfaces `social-profile`, `name`, and `address` mentions from Google, Bing, Yandex, and Baidu so you can decide where to dig deeper.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.aware-online.com/en/osint-tools/people-search-tool/ in a sock-puppet browser.
2. Type the identifier you hold into the relevant field (full name, first + surname, username, email, or phone).
3. Click the engine button (Google / Bing / Yandex / Baidu). A new tab opens with the pre-built query already run.
4. Read the results in each engine — Yandex often surfaces different (especially RU/CIS) hits than Google for the same name.
5. Pivot: promising profiles feed username tools like `[[whatsmyname]]`, and address/associate hits feed people-aggregators.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, or `phone`
- **Out:** `social-profile`, `name`, `address`, `associate` leads (as ordinary search-engine results)
- **Empty/negative result looks like:** the engine returns unrelated or zero hits — this only means the plain-text query missed, not that the person is absent; try a different engine or add a location term.

## Gotchas & OpSec
- Human-in-the-loop: none for the tool itself, though the engines it opens may throw their own CAPTCHAs under heavy use.
- It only wraps public search engines — it invents nothing and stores nothing, so treat output exactly as you would raw Google/Yandex results (verify before trusting).
- OpSec: passive but your queries hit Yandex/Baidu (RU/CN jurisdiction). Use a VPN + throwaway browser if attribution matters.

## Overlaps ("do both")
- Pairs with dedicated username-enumeration tools because this casts a broad search-engine net while those confirm exact account existence across sites.
- Run alongside a paid people-aggregator when you already have a US name — this finds the free-web footprint the aggregator misses.

## Trust & verifiability
`trust: community` — maintained by a reputable OSINT academy and transparent about being a redirector to third-party engines, so accuracy equals whatever the underlying engine returns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | people-search-tool |
| category | people-search |
| selectorsIn → selectorsOut | name, username, email, phone → social-profile, name, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
