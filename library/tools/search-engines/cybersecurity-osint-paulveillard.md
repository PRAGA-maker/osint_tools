---
id: cybersecurity-osint-paulveillard
name: cybersecurity-osint (paulveillard)
description: Use when you want to discover OSINT tools by category — a GitHub "awesome" list returning tool leads and methodology references, not subject data.
url: https://github.com/paulveillard/cybersecurity-osint
category: search-engines
path:
- search-engines
bestFor: Browsing a categorized directory of OSINT tools, frameworks and resources to find the right tool for a task.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source on GitHub; no account needed to read (a GitHub login only helps if you want to star/fork).
opsec: passive
opsecNote: Reading a public GitHub list touches no investigation target and leaks nothing about your case. The only footprint is a normal GitHub page view; browse logged-out if you'd rather not tie the read to your account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-maintainer community "awesome list" (modest star count); a useful index but not curated or vetted for tool quality — treat entries as leads to evaluate.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- paulveillard cybersecurity-osint
- awesome cybersecurity OSINT
tags:
- directory
- awesome-list
- reference
source: gh-topic-osint-framework
lastVerified: '2026-07-29'
enrichment: full
---

# cybersecurity-osint (paulveillard)

> A community-maintained "awesome list" on GitHub: a categorized index of OSINT tools, frameworks and resources. A discovery/reference resource, not a data source you query.

## When to use
You're deciding *which tool* to use for a task — search engines, social-media recon, image analysis, domain/infra research, threat intel — and want a categorized menu of options in one place. Reach for it when scoping a workflow or when your usual tool fails and you need alternatives. It returns no subject data; it points you at tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/paulveillard/cybersecurity-osint.
2. Use the README's table of contents (50+ categories) to jump to your area of interest.
3. Scan the linked tools; open the ones relevant to your case.
4. **Vet before trusting** — the list is an index, not a quality bar; check each tool is live and reputable (many entries here already have dedicated skills in this library).
5. Pivot: take a named tool and look it up in this library or add it to your workflow.

## Inputs → Outputs
- **In:** none (a topic/task, not a selector)
- **Out:** OSINT tool and resource links by category — no subject `selectorsOut`
- **Empty/negative result looks like:** the category you need isn't covered or links are stale; fall back to another OSINT directory.

## Gotchas & OpSec
- No target interaction — nothing leaks.
- Single-maintainer lists drift; some links rot and inclusion isn't an endorsement — verify each tool independently.
- Overlaps heavily with other awesome-osint collections; use it as one index among several.

## Overlaps ("do both")
- Complements the other curated OSINT directories/awesome-lists in the library — cross-reference several to catch tools any single list misses.

## Trust & verifiability
`trust: community` — a genuine community index with public history, but uncurated for quality and maintained by one person; treat every entry as a lead to verify, not a vetted recommendation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cybersecurity-osint-paulveillard |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
