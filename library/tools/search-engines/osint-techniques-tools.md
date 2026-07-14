---
id: osint-techniques-tools
name: OSINT Techniques Tools
description: Use when you have a `name`, `username`, `email`, `phone`, or `image` and want a practitioner-vetted list of the right tool for it — a curated index that routes you to `social-profile`/people-search resources.
url: https://www.osinttechniques.com/osint-tools.html
category: search-engines
path:
- search-engines
bestFor: A clean, practitioner-curated categorized index of people, username, email, phone, and image tools.
selectorsIn:
- username
- email
- phone
- name
- image
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse; the index itself needs no account (individual linked tools may charge).
opsec: passive
opsecNote: Reading the index is passive. OpSec exposure belongs to the tools it links to — evaluate each before use and route active lookups through a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Michael Bazzell-adjacent practitioner "OSINT Techniques" (a well-known investigator/author); curation is deliberate and kept reasonably current.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- osinttechniques.com tools
tags:
- tool-collection
- people-search
- username
- image
source: ultimate-osint
lastVerified: '2026-07-14'
enrichment: full
---

# OSINT Techniques Tools

> A practitioner-curated, categorized tools index — a fast, trustworthy way to pick the right tool for the selector you're holding.

## When to use
You have a specific selector — a `name`, `username`, `email`, `phone`, or `image` — and want a short, vetted shortlist of tools for it rather than wading through a sprawling framework. This page is maintained by a practising investigator, so it favours tools that actually work, making it a good first stop when you need to choose a downstream resource quickly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.osinttechniques.com/osint-tools.html.
2. Jump to the category matching your selector (people search, username, email, phone, images).
3. Pick a listed tool and follow through to run the actual lookup there.
4. Verify the destination tool still functions (indexes lag reality) and cross-check against this library's entry for it.
5. Pivot: use it purely as a router — capture findings against the specific tools you use.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, `phone`, or `image` (to choose a category)
- **Out:** routes to tools that produce `social-profile`s and other identifiers — this page is an index, not a lookup engine
- **Empty/negative result looks like:** a category with only tools that don't fit your exact case, or an occasional dead link — move to another curated index.

## Gotchas & OpSec
- It performs no searches itself; all data quality and OpSec risk sit with the tools it links to.
- More curated (smaller, higher-signal) than mega-frameworks — that means it may omit niche tools; combine with a broader directory when coverage matters.

## Overlaps ("do both")
- Pairs with `[[socmint]]` and OSINT Framework — cross-referencing a curated shortlist against a broad framework balances quality and coverage.

## Trust & verifiability
`trust: trusted` — maintained by a recognised practitioner, so the *selection* is reliable; each linked tool still warrants its own verification before you act on its output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-techniques-tools |
| category | search-engines |
| selectorsIn → selectorsOut | username, email, phone, name, image → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
