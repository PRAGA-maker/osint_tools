---
id: osint-cli-tool-skeleton
name: osint-cli-tool-skeleton
description: Use when you are building your own OSINT lookup tool and want a ready-made CLI scaffold — a developer template, not an investigative lookup itself.
url: https://pypi.org/project/osint-cli-tool-skeleton/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A boilerplate/scaffold for developers writing a new OSINT CLI tool in Python.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (by soxoj, author of Maigret). Installed from PyPI; no account or key.
opsec: passive
opsecNote: The skeleton itself performs no lookups and contacts nothing — it is inert scaffolding. OpSec depends entirely on whatever tool you build on top of it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: A small utility template from a reputable OSINT developer (soxoj). It is a code skeleton, so it has no data of its own to trust or distrust; judge the tools built from it individually.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- soxoj osint-cli-tool-skeleton
- osint cli skeleton
tags:
- developer-template
- Tools collections/toolkits
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# osint-cli-tool-skeleton

> A developer scaffold, not a lookup tool: a Python boilerplate that gives a new OSINT CLI tool its argument parsing, output formatting (table/JSON/CSV), and cookie/session plumbing out of the box.

## When to use
You are *writing* an OSINT tool and don't want to reinvent the CLI plumbing. This skeleton (from soxoj, the author of Maigret) provides the standard shape — input handling, structured output, proxy/cookie support — so you can drop in your own data-collection logic. Reach for it at build time; it is **not** something you run to look up a person, domain, or account.

## How to use it (`bestInteractionPattern`: python-lib)
1. `pip install osint-cli-tool-skeleton` (or clone the repo) to get the template.
2. Copy/fork the skeleton and rename it to your tool.
3. Implement your collection logic in the provided module hooks; the skeleton already wires up argument parsing and multi-format output.
4. Ship your finished tool — the skeleton's value is entirely in what you build on it.
5. Pivot: none for investigators — this is upstream of investigation. If you just need results, use a finished tool (e.g. Maigret) instead.

## Inputs → Outputs
- **In:** none (it's source code you extend)
- **Out:** none directly — it produces the *framework* for a tool that will have its own selectors
- **Empty/negative result looks like:** N/A — running the bare skeleton does nothing useful until you add collection logic.

## Gotchas & OpSec
- This is developer infrastructure; if you were expecting a ready-to-run investigative tool, this isn't one.
- Any OpSec, rate-limit, or trust concerns come from the code *you* add, not the skeleton.

## Overlaps ("do both")
- Pairs conceptually with finished soxoj tooling like Maigret — the skeleton is the mould, those are the cast products. Investigators should use the products.

## Trust & verifiability
`trust: community` — a legitimate, small open-source template from a well-known OSINT developer. It carries no data, so trust attaches to the tools you build with it, not to this package.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-cli-tool-skeleton |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
