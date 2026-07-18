---
id: i-intelligence-osint-handbook-2025
name: i-intelligence OSINT Handbook (2025)
description: Use when you need a curated reference of OSINT tools and methods — returns a categorized compendium of resources to pick the right tool for a task.
url: https://www.osinthandbook.com/
category: search-engines
path:
- search-engines
bestFor: A broad, categorized reference compendium of OSINT tools and techniques to consult when planning an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to download; the maintainer (i-intelligence) typically asks for an email address to send the PDF, so it's free-with-registration.
opsec: passive
opsecNote: Passive — it's reference material, not a live query tool; reading it exposes nothing about a subject. Downloading may require giving an email to the publisher, so use a research address.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-standing, well-regarded OSINT reference maintained by i-intelligence and updated periodically; it's a curated directory, so individual linked tools still need their own verification.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
relatedTools:
- osint-framework
- bellingcat-s-online-investigation-toolkit
aliases:
- OSINT Tools and Resources Handbook
- i-intelligence handbook
- osinthandbook.com
tags:
- handbook
- tool-collection
- reference
source: ultimate-osint
lastVerified: '2026-07-18'
enrichment: full
---

# i-intelligence OSINT Handbook (2025)

> A periodically-updated, categorized compendium of OSINT tools and methods — the reference you skim to find the right tool for a given selector or task.

## When to use
You're planning an investigation and want a curated map of what's available — search engines, social-media tools, people/company search, geolocation, image/video analysis, and technique write-ups — organized by category. It's not a live lookup tool; it's the "which tool should I reach for" reference. Useful early in a case to enumerate approaches you might otherwise miss, and to discover specialized resources for a particular data type.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.osinthandbook.com/ and download the handbook (you'll likely need to provide an email to receive the PDF).
2. Open the PDF and use its table of contents / categories to jump to the data type you're working (e.g. usernames, images, domains).
3. Read the entries for each listed tool and the accompanying technique notes.
4. Pick candidate tools and verify each independently before relying on it (directories date quickly).
5. Pivot: use the handbook to broaden your toolset, then run the actual selectors through the specific tools it points you to.

## Inputs → Outputs
- **In:** none (a reference document, not a query interface)
- **Out:** a categorized list of OSINT tools and methods to consult
- **Empty/negative result looks like:** not applicable — it always "returns" the compendium; the failure mode is stale or dead links inside it, which is why each listed tool needs its own check.

## Gotchas & OpSec
- It's a directory: some listed tools will be outdated, moved, or dead by the time you read it — verify before trusting any single entry.
- Download typically requires an email; use a research identity, not your personal address.
- It informs strategy but performs no lookups itself — don't cite "the handbook" as evidence, cite the underlying tool/source.

## Overlaps ("do both")
- Pairs with `[[osint-framework]]` and `[[bellingcat-s-online-investigation-toolkit]]` — other curated OSINT directories; cross-reference them, since each lists tools and techniques the others omit.

## Trust & verifiability
`trust: trusted` — a reputable, well-maintained OSINT reference; the compendium itself is reliable guidance, but it is a pointer to third-party tools that each carry their own trust level and must be verified in use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | i-intelligence-osint-handbook-2025 |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
