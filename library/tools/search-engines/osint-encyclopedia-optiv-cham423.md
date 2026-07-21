---
id: osint-encyclopedia-optiv-cham423
name: OSINT Encyclopedia (optiv / cham423)
description: Use when you have a selector but not a method and want a reference catalogue of OSINT techniques and tools to consult — returns methodology and tool pointers, not target data.
url: https://github.com/optiv/OSINT_Encyclopedia
category: search-engines
path:
- search-engines
bestFor: A reference encyclopedia of OSINT methods, resources and tooling to plan an investigation or find the right technique for a given selector.
selectorsIn:
- name
- email
- username
- domain
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source GitHub repository; clone or read online at no cost.
opsec: passive
opsecNote: Reading or cloning the repo is invisible to any target. Techniques it describes vary from passive to active — apply the opsec judgment of whichever specific method you enact, not of the encyclopedia itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Optiv (an established security firm) and maintained by cham423 on GitHub; a curated reference, not a data source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINT_Encyclopedia
- optiv OSINT encyclopedia
- cham423 encyclopedia
tags:
- tool-collection
- encyclopedia
- github
- methodology
source: ultimate-osint
lastVerified: '2026-07-21'
enrichment: full
---

# OSINT Encyclopedia (optiv / cham423)

> An Optiv-published reference wiki of OSINT techniques, resources and tooling — a methodology handbook, not a lookup service.

## When to use
You hold a selector (`name`, `email`, `username`, `domain`) but aren't sure of the best technique or which tool covers that pivot. This encyclopedia catalogues methods and resources across the OSINT lifecycle — infrastructure, people, social, breach data — so you can plan an approach or discover a tool you didn't know existed. Reach for it to level up a workflow, not to query a target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/optiv/OSINT_Encyclopedia (or clone it for offline reference).
2. Browse the README/sections by the discipline you need (e.g. email, domain, social, geolocation).
3. Read the technique write-up and note the specific tools it recommends for your selector.
4. Jump to that tool and execute the actual lookup there.
5. Pivot: use the encyclopedia to sequence multiple techniques into a coherent investigation plan.

## Inputs → Outputs
- **In:** a selector type you want techniques for (`name`, `email`, `username`, `domain`)
- **Out:** methodology write-ups and tool recommendations that lead toward `social-profile` and other findings once executed elsewhere
- **Empty/negative result looks like:** the topic isn't covered in the repo — supplement with a broader "awesome-osint" index or the tool's own docs.

## Gotchas & OpSec
- It is a knowledge base, not a scanner — it returns no data about a person; you still run the tools it names.
- Repos age: confirm any linked tool is still live before relying on it.
- OpSec: reading is passive; the opsec footprint is entirely a property of the technique you subsequently perform.

## Overlaps ("do both")
- Pairs with broad tool-directory lists (awesome-osint style) — those enumerate tools, while this explains the methodology and when to use each.

## Trust & verifiability
`trust: trusted` — authored/published under Optiv, a recognised security firm, and maintained on GitHub by cham423; reliable as guidance, though (like any reference) verify that individually linked tools remain current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-encyclopedia-optiv-cham423 |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, username, domain → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
