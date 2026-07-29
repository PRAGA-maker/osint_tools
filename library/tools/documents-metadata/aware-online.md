---
id: aware-online
name: Aware Online (OSINT Tools)
description: Use when you have a `username`, `name`, or keyword and want quick pre-built search queries across social/media platforms — returns direct search links into Facebook, Reddit, Vimeo, YouTube, etc.
url: https://www.aware-online.com/osint-tools/
category: documents-metadata
path:
- documents-metadata
bestFor: A free hub of custom search-query tools that turn a username/keyword into ready-made platform searches (Facebook, Reddit, Vimeo, YouTube, image search, and more).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: The OSINT tools page is free to use (Aware Online also sells paid OSINT training separately). No account needed for the search tools.
opsec: passive
opsecNote: The tools just build query URLs; the actual searching happens on the destination platform, so treat each pivot with normal platform OpSec (sock-puppet browser, don't log in as yourself). Aware Online itself sees only that you loaded its tool page.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by Aware Online, a known Dutch OSINT training company; the tools are convenience query-builders over public platform search, reliable as pivots but not a data source themselves.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osint-industries
- whatsmyname
- sherlock
aliases:
- Aware Online OSINT tools
- aware-online.com
tags:
- osint-toolkit
- social-search
- query-builder
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Aware Online (OSINT Tools)

> A free collection of custom search-query builders from a Dutch OSINT trainer: type a username or keyword and get ready-made searches fired into specific platforms.

## When to use
You have a `username`, `name`, or keyword and want to sweep it across specific platforms fast without hand-crafting each query. Aware Online's tools page bundles builders for Facebook, Reddit, Vimeo, YouTube, image search, and other sites — you enter your term and it constructs the right search URL for that platform. It's a convenience layer of pivots, useful early in a workup to spread a selector wide.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.aware-online.com/osint-tools/ and pick the platform tool you need (e.g. Facebook search, Reddit search, image search).
2. Enter your `username`/`name`/keyword into that tool's fields.
3. It builds and opens the platform-specific search; review results on the destination site.
4. Work through several platform tools with the same selector to map where a handle/name appears.
5. Pivot: profiles you find feed dedicated enrichment — run usernames through `[[whatsmyname]]`/`[[sherlock]]`, and confirmed profiles through your social-network tools.

## Inputs → Outputs
- **In:** `username` / `name` / keyword.
- **Out:** `social-profile` leads — direct platform search results (not data Aware Online holds itself).
- **Empty/negative result looks like:** the platform search returns nothing — the term isn't on that platform, or the platform has changed its search and the pre-built query is stale.

## Gotchas & OpSec
- Human-in-the-loop: none for the query builders.
- OpSec: **passive** at Aware Online (it only makes URLs), but the real searching happens on each platform — apply platform OpSec (sock-puppet browser, no personal login) as you follow the links.
- Query-builders rot: platforms change their search endpoints, so a tool may occasionally produce a broken/outdated query — sanity-check results.
- It's a pivot hub, not a source: it surfaces where to look, then hands off to the platform.

## Overlaps ("do both")
- Overlaps with `[[whatsmyname]]` / `[[sherlock]]` — those enumerate a username across hundreds of sites systematically; use Aware Online for quick per-platform searches and those for exhaustive username sweeps.

## Trust & verifiability
`trust: community` — from a reputable OSINT-training company, but the tools are thin query-builders over public search, so trust the destination platforms' results, not Aware Online as a data source. Verify each hit on the platform itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aware-online |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
