---
id: awesome-threat-intelligence
name: awesome-threat-intelligence
description: Use when you need to discover threat-intelligence sources, feeds and tools — a curated GitHub directory; returns pointers to other tools rather than selectors on a subject.
url: https://github.com/hslatman/awesome-threat-intelligence
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Finding vetted threat-intel feeds, frameworks and tools to pull into an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open, community-curated GitHub "awesome" list; no account.
opsec: passive
opsecNote: Reading a GitHub list is inert and touches no subject. OpSec only becomes relevant when you go on to use the tools/feeds it points to — evaluate each of those on its own terms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing, widely-referenced curated list (maintainer hslatman + contributors); entries are community-submitted, so vet each linked resource independently.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- hslatman/awesome-threat-intelligence
tags:
- threat-intelligence
- resource-list
- awesome-list
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# awesome-threat-intelligence

> A curated, community-maintained catalogue of threat-intelligence sources, feeds, frameworks and tools — a map to the ecosystem, not a lookup itself.

## When to use
This is a discovery resource. Reach for it when you need a threat-intel capability you don't already have — an IOC feed, a sharing framework (STIX/TAXII, MISP), a research blog, or a specific analysis tool — and want a vetted starting point rather than a raw web search. It returns no selectors on a subject; it points you to the tools that do. Useful when scoping how to investigate a domain, IP, or malware sample and deciding which downstream sources to pull in.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/hslatman/awesome-threat-intelligence.
2. Use the README's table of contents to jump to the relevant section (Sources, Formats & Standards, Frameworks & Platforms, Tools, Research, etc.).
3. Skim the annotated entries and pick candidate feeds/tools for your task.
4. Open the linked resource and evaluate it directly (freshness, coverage, cost, access) before relying on it.
5. Pivot: adopt the chosen feed/tool into your actual workflow — this list's job ends at pointing you there.

## Inputs → Outputs
- **In:** none (a browsable catalogue, not a query)
- **Out:** none directly — curated links to threat-intel feeds, frameworks, and tools
- **Empty/negative result looks like:** not applicable; it's a static list. The real "miss" is a linked resource that has since gone dead — always confirm the target still exists.

## Gotchas & OpSec
- Human-in-the-loop: none for the list; judgement is needed to evaluate each linked tool.
- OpSec: **passive** to browse. The OpSec profile of anything you then use is a property of that tool, not of this list.
- As with any "awesome" list, some entries drift out of date; treat it as a directory, not a guarantee of quality or availability.

## Overlaps ("do both")
- Complements the individual threat-intel and IOC tools already in this library — use the list to find gaps, then wire the specific feeds/tools into your process.

## Trust & verifiability
`trust: community` — a reputable, heavily-referenced curated list, but entries are community-submitted. Verify each linked resource's provenance and status yourself before operational use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-threat-intelligence |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
