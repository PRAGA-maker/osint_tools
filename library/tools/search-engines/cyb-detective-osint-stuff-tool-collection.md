---
id: cyb-detective-osint-stuff-tool-collection
name: cyb_detective OSINT stuff tool collection
description: Use when you have a selector class (username, email, phone, image, domain…) and want to discover niche tools for it — returns pointers to 1000+ categorized OSINT tools, not subject data.
url: https://cipher387.github.io/osint_stuff_tool_collection/
category: search-engines
path:
- search-engines
bestFor: Browsing an enormous, deeply categorized index of niche OSINT tools and services to find the right instrument for a selector.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public index on GitHub Pages (with a companion GitHub repo); no account or payment.
opsec: passive
opsecNote: Browsing the collection is passive — it's a directory of tools, not a query against a subject. Each listed tool has its own OpSec profile; evaluate that before running any of them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by cipher387 (cyb_detective), a prolific and well-regarded OSINT tool curator; the curation is reputable, though individual listed tools vary in quality and liveness.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- cipher387 osint_stuff_tool_collection
- cyb_detective
tags:
- tool-collection
- directory
- username
- email
- phone
- image
source: ultimate-osint
lastVerified: '2026-07-14'
enrichment: full
---

# cyb_detective OSINT stuff tool collection

> cipher387's sprawling, meticulously categorized index of 1000+ niche OSINT tools — the place to find the obscure, purpose-built instrument no mainstream list covers.

## When to use
You have a specific selector — a `username`, `email`, `phone`, `image`, `domain`, crypto wallet, etc. — and the common tools have run dry. This collection's strength is depth of niche coverage: unusual dorks, single-country registries, format-specific parsers, and tools you didn't know existed. Use it to expand your toolkit for a hard selector rather than to look up a person directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the index at cipher387.github.io/osint_stuff_tool_collection (or the companion GitHub repo).
2. Navigate to the category matching your selector (username, email, phone, images, maps, crypto, etc.).
3. Scan the entries — each is a short pointer to a niche tool; pick candidates that fit your exact need.
4. Open the chosen tool and run your actual query there; vet its trust/OpSec first.
5. Pivot: whatever the picked tool returns feeds your workflow. Return here for the next hard selector.

## Inputs → Outputs
- **In:** none (a directory — you bring a need, not a selector value)
- **Out:** categorized pointers to niche OSINT tools and services
- **Empty/negative result looks like:** a category with only tools you already have, or listed tools that have since died — cross-check with other directories and confirm liveness before relying on a listing.

## Gotchas & OpSec
- Returns *tools*, never subject data — a listing is a lead to a tool, not a result.
- With 1000+ entries harvested over time, some links are dead or the tools defunct; verify each is live before use.
- Listed tools span first-party to sketchy; vet trust, pricing, and OpSec per tool.

## Overlaps ("do both")
- Pairs with `[[osint-stash]]` and other OSINT directories — cross-referencing multiple indexes surfaces tools any single list misses. cyb_detective skews toward niche/technical tools; combine with broader people-focused directories.

## Trust & verifiability
`trust: trusted` — an authoritative, actively maintained curation by a respected OSINT figure. Its value is breadth of curation; judge each *linked* tool independently and confirm it still works before acting on its output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyb-detective-osint-stuff-tool-collection |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
