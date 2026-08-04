---
id: digital-privacy-ffffffff0x
name: Digital-Privacy (ffffffff0x)
description: Use when you want a broad reference index of OSINT and privacy tools/techniques — a curated (now archived) directory pointing to search engines, social-media investigation, people-tracking and geolocation resources.
url: https://github.com/ffffffff0x/Digital-Privacy
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A one-stop bilingual (EN/中文) reference list of OSINT and privacy-protection resources to discover other tools.
selectorsIn:
- name
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free public GitHub repository; the list itself costs nothing (some linked destinations are paid).
opsec: passive
opsecNote: Reading the list is passive and reveals nothing about your target. OpSec depends entirely on which linked destination you then use — evaluate each tool's exposure before submitting selectors to it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A popular community awesome-list (ffffffff0x, ~4.9k stars) but ARCHIVED/read-only since Jan 2023 — links are curated but no longer updated, so expect some dead entries.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ffffffff0x digital privacy
tags:
- github
- resource-collection
- awesome-list
- privacy
source: osintambition-social
lastVerified: '2026-08-04'
enrichment: full
---

# Digital-Privacy (ffffffff0x)

> A large, bilingual curated index of privacy-protection and OSINT resources — a menu of hundreds of tools grouped by function, useful for discovering the right instrument for a task.

## When to use
You want to browse the landscape rather than run a single lookup: you have a task (find social-media investigation tools, flight/ship tracking, IP geolocation, breach-checking) and want a curated jumping-off point to the specific tools that do it. Treat it as a directory that helps you find a tool, not a tool that returns data itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/ffffffff0x/Digital-Privacy and read the README/table of contents.
2. Jump to the relevant section (OSINT search engines, social-media investigation, people/asset tracking, geolocation, privacy hardening).
3. Follow a linked tool to its own site and use it there with your selector (e.g. a `name`).
4. Because the repo is archived, sanity-check links — use a web archive if a destination has moved or closed.
5. Pivot: the destination tool is what actually returns `social-profile`/other data; this index only routes you to it.

## Inputs → Outputs
- **In:** a task/topic (and, at the destination tool, a selector such as `name`).
- **Out:** links to categorised OSINT/privacy tools; the eventual `social-profile` or other data comes from whichever destination you open.
- **Empty/negative result looks like:** a section whose links are stale/dead — an artefact of the archive freeze, not a signal about any subject.

## Gotchas & OpSec
- **Archived (read-only since Jan 2023):** curation stopped, so some links are dead or point to changed tools — verify before relying on them.
- It's an index, not an analyser — it returns no data on its own.
- Bilingual (English + Simplified Chinese); some entries are China-region-focused.

## Overlaps ("do both")
- A directory rather than a competitor to specific tools — use it to find instruments, then run something like `[[recon-ng]]`, `[[slash]]`, or `[[dns-twist]]` for the actual collection.

## Trust & verifiability
`trust: community` — a well-known but frozen community list; its value is curation, and because it's no longer maintained you should treat every link as needing a freshness check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | digital-privacy-ffffffff0x |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
