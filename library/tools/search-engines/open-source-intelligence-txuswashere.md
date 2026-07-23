---
id: open-source-intelligence-txuswashere
name: Open-Source-INTelligence (txuswashere)
description: Use when you need to discover OSINT tools and methodologies for a given selector or task — returns a curated reference index of tools/techniques to branch from, not data on a subject.
url: https://github.com/txuswashere/Open-Source-INTelligence
category: search-engines
path:
- search-engines
bestFor: A curated GitHub reference list of OSINT tools and methodologies to find the right tool for a task.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public GitHub repository; no account needed to read (a GitHub login only to star/fork).
opsec: passive
opsecNote: Reading a public repo is passive and reveals nothing about a subject — it's a directory, not a lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained "awesome"-style list on GitHub; useful as a pointer, but each linked tool must be vetted individually.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- txuswashere OSINT
- Open-Source-INTelligence
tags:
- directory
- awesome-list
- reference
source: gh-topic-osint-framework
lastVerified: '2026-07-23'
enrichment: full
---

# Open-Source-INTelligence (txuswashere)

> A curated GitHub index of OSINT tools and methodologies — a map to branch from when you're not sure which tool fits a task.

## When to use
You're stuck on which technique or tool applies to a selector or objective (username enumeration, breach data, geolocation, infrastructure recon) and want a curated menu of options and methods. This is a meta/reference resource: it points you at tools and workflows; it holds no data about any individual. Use it to broaden your toolkit, then switch to the actual tools it lists.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo at https://github.com/txuswashere/Open-Source-INTelligence.
2. Read the README/sections; use the browser's find (Ctrl-F) or GitHub search to jump to a topic (e.g. "email", "phone", "geoint").
3. Follow links to individual tools — then vet each one for whether it's live, free, and reputable before relying on it.
4. Treat it as a discovery layer that feeds your actual investigation with candidate tools/methods.
5. Pivot: a listed tool that fits your selector becomes the next concrete step.

## Inputs → Outputs
- **In:** a task/topic you want tools for (no personal selectors).
- **Out:** a curated list of OSINT tools, links, and methodologies to investigate further.
- **Empty/negative result looks like:** a topic the list doesn't cover, or links that have since died — being a static list, some entries go stale; cross-check with other awesome-OSINT lists.

## Gotchas & OpSec
- It's a pointer, not a vetted registry — individual linked tools may be dead, paid, or sketchy; verify each before use.
- "Awesome" lists drift out of date; check the repo's last commit and corroborate with fresher directories.
- No investigative data here — don't mistake presence on the list for a tool's quality.

## Overlaps ("do both")
- Overlaps with other OSINT directories/awesome-lists and this very library: use several indexes together, since each surfaces tools the others miss.

## Trust & verifiability
`trust: community` — a personal curated list; valuable as a starting map, but every tool it points to needs independent verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-source-intelligence-txuswashere |
