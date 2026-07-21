---
id: osint-toolkit-cybersight-security
name: OSINT-Toolkit (Cybersight-Security)
description: Use when you have a selector but need the right tool and want a categorized catalog of OSINT tools/websites to pick from — returns tool pointers across breach, forensics, and platform investigation, not target data.
url: https://github.com/Cybersight-Security/OSINT-Toolkit
category: search-engines
path:
- search-engines
bestFor: A categorized reference catalog of OSINT tools/websites to find the right resource for a given selector or task.
selectorsIn:
- name
- email
- username
- domain
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source (GPL-3.0) GitHub repo with a hosted web catalog; no account or payment.
opsec: passive
opsecNote: Reading or cloning the catalog is invisible to any target. The opsec footprint belongs entirely to whichever tool you pick from it — apply that tool's own guidance.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained (GPL-3.0, ~53 stars, actively committed) catalog of OSINT tools/websites; a curated index whose quality tracks the maintainers' upkeep and the linked tools.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Cybersight OSINT-Toolkit
- OSINT-Toolkit
tags:
- tool-collection
- catalog
- toolkit
- github
source: gh-topic-osint-resources
lastVerified: '2026-07-21'
enrichment: full
---

# OSINT-Toolkit (Cybersight-Security)

> A categorized, community-maintained catalog of 100+ OSINT tools and websites (with a hosted web UI) — a resource picker organized by investigation type.

## When to use
You hold a selector (`name`, `email`, `username`, `domain`) or face a task (breach search, Discord investigation, URL/file safety analysis, digital forensics) and want to find the right tool rather than reinvent a workflow. This toolkit groups tools into ~11 categories so you can jump to the relevant set and pick one. Use it to discover tooling and structure an approach; it returns no data about a subject itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the catalog at https://github.com/Cybersight-Security/OSINT-Toolkit (or its GitHub Pages site).
2. Browse to the category matching your task (data breach, forensics, Discord, URL analysis, etc.).
3. Pick a tool suited to your selector and open it.
4. Run the actual lookup in that destination tool.
5. Chain categories to sequence a fuller investigation.

## Inputs → Outputs
- **In:** a selector type / task you need tooling for (`name`, `email`, `username`, `domain`)
- **Out:** categorized tool pointers that lead toward `social-profile` and other findings once executed elsewhere
- **Empty/negative result looks like:** no tool listed for your niche need — supplement with a broader "awesome-osint" index or another catalog.

## Gotchas & OpSec
- It's a catalog, not a scanner — it produces no data; you run the tools it names.
- Community-maintained: verify a linked tool is still live and reputable before relying on it.
- OpSec: reading is passive; footprint lives in the downstream tools.

## Overlaps ("do both")
- Pairs with other tool directories ([[osint-encyclopedia-optiv-cham423]], awesome-osint lists) — cross-reference catalogs, since each curator covers different tools.

## Trust & verifiability
`trust: community` — an open-source, actively-committed catalog; trustworthy as an index, but vet each linked tool individually and confirm findings at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-toolkit-cybersight-security |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, username, domain → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
