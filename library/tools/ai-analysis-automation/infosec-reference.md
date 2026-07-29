---
id: infosec-reference
name: Infosec Reference
description: Use when you need a curated knowledge base to point you to the right infosec/OSINT technique, tool, or reading — returns reference material.
url: https://github.com/rmusser01/Infosec_Reference
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A large curated infosec/security knowledge base and reading list to find methods and tools.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source knowledge base hosted on GitHub (also rendered as a web book).
opsec: passive
opsecNote: Passive — reading reference material; nothing touches any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained reference by rmusser01; a curated index/reading list, so treat specifics as pointers and verify against the primary sources it links.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Infosec_Reference
- rmusser01 Infosec Reference
tags:
- related-awesome-lists
- reference
- knowledge-base
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Infosec Reference

> A sprawling, curated infosec knowledge base — when you're not sure *how* to approach a security or OSINT problem, it points you to the techniques, tools, and reading that cover it.

## When to use
You're stuck on method rather than data: which technique applies, what tool exists for a task, where to read up on an attack/recon/analysis area. Infosec Reference is a large, categorised index (recon, OSINT, forensics, network, web, etc.) that surfaces the relevant tools and writeups so you can pick the right next step instead of guessing. It's a meta-resource — a map to other tools, not a data source itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo at https://github.com/rmusser01/Infosec_Reference (or its rendered web-book form).
2. Browse to the relevant section (e.g. OSINT, Network Attacks, Forensics) or search the repo for a keyword.
3. Follow the curated links to specific tools, papers, and tutorials.
4. Pivot: the tool/technique you find here becomes the actual step in your workflow — this resource just gets you to it faster.

## Inputs → Outputs
- **In:** a topic/technique you want references for (no personal selectors)
- **Out:** curated links to tools, writeups, and reading on that topic
- **Empty/negative result looks like:** a thin or dated section — the reference is broad but not uniformly deep, so some niches are sparse; that's a gap in the index, not the field.

## Gotchas & OpSec
- It's an **index, not authority** — links can be stale, and inclusion isn't endorsement; verify each tool/source itself.
- Large and unevenly maintained; use search rather than reading top-to-bottom.
- Passive; reading it touches no subject.

## Overlaps ("do both")
- Complements curated OSINT tool collections and this very library — Infosec Reference is broader security-wide, so use it to discover approaches, then come back to a focused OSINT toolset to execute.

## Trust & verifiability
`trust: community` — a well-known community reference; treat its entries as leads and confirm each linked tool/source on its own merits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infosec-reference |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
