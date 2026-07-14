---
id: metaosint-intelscott
name: MetaOSINT (IntelScott)
description: Use when you have a selector type (name, username, email, phone, image) and need to pick the right tool — a searchable, sortable, data-ranked table of top OSINT tools and resources.
url: https://metaosint.github.io/table
category: search-engines
path:
- search-engines
bestFor: Systematically choosing the best-ranked OSINT tools for a given selector and task by filtering a curated table.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free static site; no account, no payment.
opsec: passive
opsecNote: A read-only reference table hosted on GitHub Pages; browsing it involves no target contact and leaks nothing about your case.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by IntelScott; the ranking is data-driven (tools scored by how many curated OSINT source lists recommend them), making it a reliable meta-index rather than a personal opinion list.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osint-framework
- start-me
aliases:
- MetaOSINT table
- metaosint.github.io
tags:
- tool-collection
- searchable-table
- meta-resource
source: ultimate-osint
lastVerified: '2026-07-14'
enrichment: full
---

# MetaOSINT (IntelScott)

> A searchable, sortable, data-ranked table of the top OSINT tools — the meta-tool you consult to decide which tool to reach for next.

## When to use
You know the selector you hold (a `name`, `username`, `email`, `phone`, `image`, etc.) and the kind of pivot you want, but not the best tool for it. MetaOSINT ranks tools by how frequently they appear across many curated OSINT source lists, so filtering its table by category/type gives you a shortlist of the most widely-endorsed options rather than a random blog roundup. Use it at the start of a task or when you're stuck and need alternatives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://metaosint.github.io/table.
2. Filter/sort by category (e.g. person search, username, phone, image) and type.
3. Read the ranking — higher-scored rows are recommended by more independent OSINT lists.
4. Click through to a tool's site, or use it to justify a coverage decision (why this tool, not that one).
5. Pivot: pick the top-ranked tool for your selector and run it; return to the table if it dead-ends.

## Inputs → Outputs
- **In:** a task/selector *type* (not a personal selector value)
- **Out:** a ranked shortlist of tools with links, categories, and endorsement counts
- **Empty/negative result looks like:** a filter with few/no rows — that niche has few widely-endorsed tools; broaden the filter or consult a strategy note.

## Gotchas & OpSec
- It's a **tool-selection index**, not a lookup — you don't put a person's data in here.
- Ranking reflects popularity/endorsement, not live status — a top-ranked tool may still be down; verify before relying.
- Fully passive; nothing about your investigation is transmitted.

## Overlaps ("do both")
- Pairs with `[[osint-framework]]` and `[[start-me]]` OSINT dashboards — MetaOSINT ranks by endorsement, the others organize by workflow; consult both when scoping which tools to try.

## Trust & verifiability
`trust: trusted` — a transparent, data-driven meta-index maintained by IntelScott. The ranking method is explicit, so its recommendations are reproducible rather than opinion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metaosint-intelscott |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
