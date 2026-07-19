---
id: fravia-soxoj
name: FRAVIA (soxoj)
description: Use when your searches keep coming up empty and you want to level up search-engine craft — a curated methodology resource ("The Art of Searching") that improves how you query, not a lookup itself.
url: https://github.com/soxoj/FRAVIA
category: search-engines
path:
- search-engines
bestFor: Learning advanced search-engine querying technique (operators, source-finding, "searchlore") to locate hard-to-find references on a subject.
selectorsIn:
- name
selectorsOut:
- social-profile
- document-id
status: live
pricing: free
costNote: Free, open resource on GitHub; no account required (a GitHub login only helps if you want to star/fork).
opsec: passive
opsecNote: Reading a methodology repo is passive. The OpSec that matters happens when you run the searches it teaches — do those in a sock-puppet browser/search session if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by soxoj (author of Maigret and other respected OSINT tooling), preserving/extending the late Fravia's "searchlore"; a well-regarded, non-commercial methodology source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- maigret
- socid-extractor
- username-generation-guide
- 1c-database-converter
- awesome-osint-mcp-servers
- counter-osint-guide-for-russians
- gitcolombo
- maigret-via-socid-extractor-soxoj-ecosystem
- mailto-analyzer
- marple
- osint-namecheckers-list
aliases:
- The Art of Searching
- searchlore
- soxoj FRAVIA
tags:
- search
- methodology
- guide
source: gh-topic-osint-resources
lastVerified: '2026-07-19'
enrichment: full
---

# FRAVIA (soxoj)

> A curated methodology resource on advanced search-engine craft ("The Art of Searching" / searchlore) — it sharpens *how* you search so you can surface references other people can't, rather than looking anything up for you.

## When to use
Your searches on a `name`, handle, or topic keep returning noise or nothing, and you want to improve your technique: advanced operators, choosing the right engines, finding primary sources, and thinking like a skilled searcher. FRAVIA collects and extends the classic "searchlore" tradition. Reach for it to upgrade your search methodology — it complements the tools in this library rather than replacing any of them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo at https://github.com/soxoj/FRAVIA and read the guides/sections.
2. Study the querying techniques — operator combinations, engine selection, source-tracing methods.
3. Apply them immediately to your live case: reformulate your `name`/keyword searches using the taught patterns.
4. Combine with soxoj's tooling (`[[maigret]]`, `[[socid-extractor]]`) for username/profile work.
5. Pivot: better queries surface `social-profile`s, `document-id`s, and primary sources you then run through the rest of your workflow.

## Inputs → Outputs
- **In:** a `name`/keyword you're struggling to search effectively
- **Out:** improved search technique that yields `social-profile`s, documents, and hard-to-find references (indirect — the skill is the deliverable)
- **Empty/negative result looks like:** N/A — it's a guide, not a query interface; the "result" is your own improved searching. If a technique doesn't help on a given case, try another engine/approach it describes.

## Gotchas & OpSec
- It's a methodology/reference, not a tool that returns data — set expectations accordingly.
- Some searchlore is classic/older; adapt techniques to current engines.
- OpSec applies to the searches you run, not to reading the guide.

## Overlaps ("do both")
- Pairs with `[[maigret]]`, `[[socid-extractor]]`, and `[[username-generation-guide]]` — FRAVIA teaches the search mindset, while those execute username/profile discovery.

## Trust & verifiability
`trust: trusted` — authored/curated by a respected OSINT toolmaker (soxoj); it's a non-commercial educational resource, so "verifiability" is about applying its techniques and confirming what your improved searches return.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fravia-soxoj |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
