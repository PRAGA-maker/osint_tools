---
id: awesome-honeypots
name: awesome-honeypots
description: Use when you need to stand up a honeypot or understand deception tooling — returns a curated, categorized index of free/open-source honeypots and related components (no selectors).
url: https://github.com/paralax/awesome-honeypots
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A comprehensive, maintained catalog of open-source honeypots and deception components by category.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Public GitHub "awesome list"; free to read, the listed tools are themselves free/open source.
opsec: passive
opsecNote: Reading the list is passive. The tools it catalogs are defensive/deception software — deploying a honeypot is an infrastructure decision with its own exposure and legal considerations; scope and authorize any deployment properly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known, heavily-starred (~10k) community awesome-list with hundreds of commits and active maintenance; a reference index, not a single tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- awesome honeypots
- paralax/awesome-honeypots
tags:
- related-awesome-lists
- honeypots
- defensive-security
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# awesome-honeypots

> The canonical curated index of open-source honeypots and deception tooling — where to look when you need to deploy, study, or recognize a honeypot rather than find a person.

## When to use
This is a defensive/infrastructure reference, not a subject-lookup tool. Reach for it when your investigation crosses into deception technology: you want to stand up a honeypot to observe an attacker, you are cataloging what a target's server might be running, or you need to recognize honeypot software in someone else's stack. It groups tools by type (web, database, service, ICS, malware-collection, network analysis) with a bias toward free/open source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/paralax/awesome-honeypots and read the category table of contents.
2. Jump to the category you need (e.g. "Web honeypots" or "Database honeypots").
3. Follow a project's link to its own repo/docs to evaluate and deploy it.
4. Pivot: use it as a checklist when profiling a server (does this fingerprint match a known honeypot?) or when building your own observation infrastructure.

## Inputs → Outputs
- **In:** none — you bring the need (deploy/identify a honeypot)
- **Out:** none directly — a categorized list of tools and links, no data about a subject
- **Empty/negative result looks like:** the niche you need is not listed (rare given its breadth) — fall back to the broader awesome-security lists it cross-references.

## Gotchas & OpSec
- Human-in-the-loop: none to read; each linked tool has its own setup.
- OpSec: passive to browse. Deploying deception infrastructure has real exposure and legal/authorization requirements — this list points to tools, it does not sanction any deployment.
- It is an index; tool quality varies and some entries may be stale despite active list maintenance.

## Overlaps ("do both")
- Pairs with `[[recon-ng-paralax-fork]]` and other awesome-security lists — same maintainer ecosystem; honeypots for observing adversaries complement recon tooling for investigating them.

## Trust & verifiability
`trust: community` — a large, actively-maintained, widely-cited awesome-list; reliable as a directory, but verify any individual tool against its own repo before deploying.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-honeypots |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
