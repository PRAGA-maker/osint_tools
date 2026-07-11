---
id: cybersecstu-osint-for-finding-people
name: CyberSecStu - OSINT for Finding People
description: Use when you have a `name`/`username`/`email`/`phone` and want a curated list of which tools to try next for locating a person — returns pointers to social-profile, address, and phone tools.
url: https://docs.google.com/spreadsheets/d/1JxBbMt4JvGr--G0Pkl3jP9VDTBunR2uD3_faZXDvhxc/edit
category: people-search
path:
- people-search
bestFor: A people-finding-specific tool index in spreadsheet form — a "what do I try next" menu, not a lookup itself.
selectorsIn:
- name
- username
- email
- phone
selectorsOut:
- social-profile
- address
- phone
status: live
pricing: free
costNote: Free public Google Sheet; read-only, no account needed. Individual tools it links to may have their own costs.
opsec: passive
opsecNote: Reading the sheet is inert — it's a static Google Doc and nothing is queried about your subject. OpSec risk lives entirely in the downstream tools you pick from it; vet each one before running it against a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-curated Google Sheet attributed to CyberSecStu; a directory, so link quality varies and entries can go stale. Verify any tool it points to independently.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CyberSecStu people OSINT sheet
tags:
- people-search
- spreadsheet
- missing-persons
- directory
source: ultimate-osint
lastVerified: '2026-07-11'
enrichment: full
---

# CyberSecStu - OSINT for Finding People

> A public Google Sheet themed specifically around finding people — use it as a curated menu of downstream tools, not as a lookup you run.

## When to use
You have a starting selector (`name`, `username`, `email`, or `phone`) and you're deciding *which* tool to reach for next in a person-location workflow. This sheet is organised around finding people specifically, so it's a fast way to remember an option you'd otherwise forget. It returns nothing about your subject itself — it points you at the tools that do.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the sheet URL (read-only Google Sheets view).
2. Scan tabs/sections for the selector you hold (people search, social, phone, etc.).
3. Pick a candidate tool, then leave the sheet and run that tool against your subject.
4. Pivot: treat each linked tool as its own node — cross-check whether this library already has an enriched skill for it and prefer that.

## Inputs → Outputs
- **In:** a `name` / `username` / `email` / `phone` you want to research (used to decide which listed tool fits)
- **Out:** pointers to tools that themselves return `social-profile`, `address`, `phone`
- **Empty/negative result looks like:** a section with dead links or no tool matching your selector — fall back to the broader indexes in this library.

## Gotchas & OpSec
- Human-in-the-loop: none to read; judgement is required to pick a sound tool from it.
- Staleness: community directories rot — links may 404 or point to tools that shut down. Confirm a tool is live before relying on it.
- OpSec: reading is passive; the real exposure is in whatever downstream tool you launch.

## Overlaps ("do both")
- Complements other harvested tool directories in this library — sheets like this catch niche people-finders that a general awesome-list misses, so cross-reference both when scoping a search.

## Trust & verifiability
`trust: community` — an individually maintained public Sheet (CyberSecStu). Useful as a prompt for options, but every tool it lists must be verified on its own merits before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cybersecstu-osint-for-finding-people |
| category | people-search |
| selectorsIn → selectorsOut | name, username, email, phone → social-profile, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
