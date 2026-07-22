---
id: the-osint-rack-mario-santella
name: The OSINT Rack
description: Use when you need to discover an OSINT tool for a given selector/task — returns a filterable directory of 500+ vetted OSINT resources by category, type and pricing.
url: https://www.mariosantella.com/the-osint-rack/
category: search-engines
path:
- search-engines
bestFor: Finding the right OSINT tool for a task by filtering a large curated directory by category, type and cost.
selectorsIn:
- domain
- email
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse and filter; it is a directory that links out to the actual tools (which have their own pricing).
opsec: passive
opsecNote: Browsing a tool directory is passive and reveals nothing about a target — you run no query against a subject here, you only pick tools to use elsewhere.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A curated OSINT resource directory (now at osintrack.com) maintained by practitioner Mario Santella; a helpful meta-resource, but inclusion is curation, not endorsement of each linked tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINT Rack
- osintrack.com
- Mario Santella OSINT Rack
tags:
- osint-directory
- tool-index
- meta-resource
source: ultimate-osint
lastVerified: '2026-07-22'
enrichment: full
---

# The OSINT Rack

> A large, filterable directory of vetted OSINT tools — a meta-resource for *finding the right tool* for a selector or task, not a lookup you run against a person.

## When to use
You're mid-investigation and need a tool for a specific job — reverse-image a `face`, pivot a `domain`, enumerate a `username`, check breach data — and want a curated shortlist rather than a raw awesome-list. The OSINT Rack indexes 500+ resources across SOCMINT, GEOINT, image analysis, breach/credential data, people/username search, domain/email intel, dark web and visualization, filterable by category, tool type (platform, CLI, browser extension, etc.) and pricing (free/freemium/paid/invite).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site (mariosantella.com/the-osint-rack, which now redirects to osintrack.com).
2. Filter by category (e.g. "username search"), tool type (e.g. CLI, browser extension) and pricing to match your constraints.
3. Open the shortlisted tools and evaluate for your selector/task.
4. Pivot: pick a tool and run your actual selector there; use the Rack again as the task shifts to a new selector.

## Inputs → Outputs
- **In:** the *kind* of selector/task you have (`domain`, `email`, `username`, `name`, image, etc.)
- **Out:** a filtered list of candidate OSINT tools/resources (each linking out) — indirectly, `social-profile`/data once you use them
- **Empty/negative result looks like:** a sparse filter combination (e.g. a very specific selector + "free" + "CLI") returning few tools — broaden the filters.

## Gotchas & OpSec
- It's an index, not a data source — it finds tools; the intelligence comes from the tools you then use.
- Curation ≠ endorsement; still vet each linked tool for freshness, trust and OpSec before use.
- Passive; you query no subject here.

## Overlaps ("do both")
- Pairs with other OSINT meta-resources (OSINT Framework, awesome-osint) and this very library — cross-reference to catch tools any single index misses.

## Trust & verifiability
`trust: community` — a practitioner-curated directory; a reliable discovery aid, but assess each linked tool independently before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-osint-rack-mario-santella |
| category | search-engines |
| selectorsIn → selectorsOut | domain, email, username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
