---
id: site-dorks
name: Site Dorks
description: Use when you have a search term (a `name`, email, or keyword) and want to dork it across many curated OSINT sites and multiple engines at once — returns candidate `social-profile`/`document-id` hits.
url: https://github.com/Zarcolio/sitedorks
category: documents-metadata
path:
- documents-metadata
bestFor: Fanning a single search term across hundreds of site-scoped dorks and several search engines.
selectorsIn:
- name
selectorsOut:
- social-profile
- document-id
status: live
pricing: free
costNote: Free and open-source Python script; run locally.
opsec: passive
opsecNote: It builds and opens search-engine queries, so the engines (Google/Bing/Yandex/etc.) see your searches — not the targets. Run behind a VPN/sock-puppet browser; a burst of many dorks can trip engine rate limits/CAPTCHAs, so pace it.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by Zarcolio; it only constructs and launches queries against public engines, so no independent data claims.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- sitedorks
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- google-dorking
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Site Dorks

> A dork multiplexer — takes one search term and runs it as site-scoped queries across a large curated list of websites and multiple search engines (Google, Bing, Ecosia, Yahoo, Yandex).

## When to use
You have a `name`, email, username, or keyword and want to cast a wide net: search it specifically across hundreds of relevant sites (social networks, paste sites, code hosts, document stores) and several engines, without hand-typing `site:` dorks one by one.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/Zarcolio/sitedorks.git` and install its Python requirements.
2. Run with your term, e.g. `python3 sitedorks.py -s "target term"`; choose the engine and the site category to scope.
3. It opens/emits the constructed queries; work through the results per site.
4. Solve any CAPTCHAs the engines throw when you fire many queries quickly — pace the run to avoid blocks.
5. Pivot: `social-profile` and `document-id` hits feed the relevant per-selector tools (profile enrichment, document metadata).

## Inputs → Outputs
- **In:** `name`/email/username/keyword
- **Out:** search-result links to `social-profile`s, `document-id`s, and mentions across many sites
- **Empty/negative result looks like:** engines return nothing for a term across sites — try variant spellings/handles; a blocked/CAPTCHA state is a rate-limit, not a true negative.

## Gotchas & OpSec
- Human-in-the-loop: heavy dorking triggers CAPTCHAs/rate limits (`captcha`) — throttle and rotate.
- Its value is breadth; expect noise and dedupe/verify hits manually.
- OpSec: **passive** to targets, but your queries are visible to the engines — use a VPN.

## Overlaps ("do both")
- Complements manual Google dorking and single-site search tools; sitedorks is for breadth, then drill into the best hits with focused tools.

## Trust & verifiability
`trust: community` — open-source query builder; every hit is a real engine result you open and verify yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | site-dorks |
| category | documents-metadata |
| selectorsIn → selectorsOut | name → social-profile, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (captcha) |
