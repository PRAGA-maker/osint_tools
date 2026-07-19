---
id: gijn-online-research-tools
name: GIJN Online Research Tools
description: Use when you need a vetted OSINT/verification tool for a task and want a journalist-grade curated list — returns pointers to tools for records, people, images and verification.
url: https://gijn.org/online-research-tools/
category: search-engines
path:
- search-engines
bestFor: A journalism-grade, curated directory of research and verification tools, organized by investigative task.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free resource directory maintained by a nonprofit journalism network; no account needed.
opsec: passive
opsecNote: Reading a curated tool list is passive. OpSec applies only to the individual tools it points you to, each of which you should assess separately.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Global Investigative Journalism Network (GIJN), a respected nonprofit; its recommendations are vetted for professional investigative use.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- gijn-org
- gijn-org-3
- gijn-org-4
tags:
- tool-collection
- journalism
- verification
- meta-resource
source: ultimate-osint
lastVerified: '2026-07-19'
enrichment: full
---

# GIJN Online Research Tools

> The Global Investigative Journalism Network's curated resource hub — a vetted, task-organized directory of the tools professional investigators actually use for records, people-tracing, imagery, and verification.

## When to use
You're stuck on a task ("how do I verify this video?", "where do I find company records in country X?", "what image-search tools exist?") and want a trustworthy shortlist rather than a random Google result. GIJN's curation is journalist-grade, so it's a reliable meta-resource for discovering the right tool and technique for a specific investigative need, including people-tracing and public-records work relevant to missing-persons cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to GIJN's Resource Center / online research tools section (start at https://gijn.org/ and open the research-tools resources).
2. Browse by category or task — verification, social media, images/video, public records, people, mapping, data.
3. Read GIJN's short write-up for each recommended tool to understand what it does and when to use it.
4. Follow through to the actual tool and assess it on its own (cost, coverage, OpSec) before relying on it.
5. Pivot: the specific tool you pick becomes the next step; return to GIJN when you hit the next unknown.

## Inputs → Outputs
- **In:** an investigative need/task (no data selector)
- **Out:** curated pointers to vetted research and verification tools, grouped by task
- **Empty/negative result looks like:** the category you need isn't well covered, or a listed tool has since died — a directory reflects its last update, so verify that a recommended tool is still live before committing to it.

## Gotchas & OpSec
- It's a directory, not a tool: it points you onward. Evaluate each recommended tool's freshness, cost, and OpSec separately.
- Curated lists lag; some entries may be outdated or discontinued.
- The GIJN site can be behind a bot-filter; open it in a normal browser if a scripted fetch is blocked.
- OpSec: reading is passive.

## Overlaps ("do both")
- Complements other curated OSINT directories (e.g. OSINT Framework, awesome-lists) — GIJN adds professional editorial vetting and task context that raw link-lists lack.

## Trust & verifiability
`trust: trusted` — GIJN is a leading nonprofit investigative-journalism network; its tool recommendations are vetted and reputable, though (as with any directory) you should confirm a given tool is still operational before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gijn-online-research-tools |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
