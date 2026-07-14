---
id: osint-stash
name: OSINT STASH
description: Use when you have a case type or selector class (username, email, image…) and want to discover which tool to reach for next — returns pointers to categorized OSINT tools, not subject data.
url: https://osint.best/
category: search-engines
path:
- search-engines
bestFor: Browsing a clean, modern, categorized directory of OSINT tools to pick the right instrument for a selector.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public directory (osint.best); no account or payment.
opsec: passive
opsecNote: You are browsing a tool index, not querying a target — fully passive and safe. (Any tool you then launch from it has its own OpSec profile; evaluate that separately.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-curated directory. Useful as a jump-off point; individual listed tools vary widely in trust and must be judged on their own.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- osint.best
tags:
- tool-collection
- directory
- username
- email
- image
source: ultimate-osint
lastVerified: '2026-07-14'
enrichment: full
---

# OSINT STASH

> A tidy, modern directory (osint.best) that groups OSINT tools by category — a "what do I use for this selector?" launchpad, not a data source itself.

## When to use
You're mid-investigation and hold a selector class — a `username`, `email`, `image`, `name`, phone, or a case type — but you don't know the best tool for the next step. OSINT STASH lets you browse curated categories to pick an instrument. Use it to expand coverage (find a tool you don't have) rather than to look up a person directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.best/.
2. Browse or filter by category (people, username, email, image, social, etc.).
3. Read each entry's short description and pick a tool matching your current selector.
4. Open the chosen tool and run your actual query there.
5. Pivot: whatever the picked tool returns feeds the rest of your workflow. Come back here when you hit another dead-end selector.

## Inputs → Outputs
- **In:** none (this is a directory — you bring a *need*, not a selector value)
- **Out:** categorized pointers to OSINT tools
- **Empty/negative result looks like:** a category that's sparse or lists tools you already have — cross-check against other directories rather than assuming no tool exists.

## Gotchas & OpSec
- This never returns subject data — do not treat a directory listing as a result. It only tells you *where to look next*.
- Listed tools range from first-party to sketchy scrapers; vet each one (trust, OpSec, pricing) before use.
- Directories drift out of date; a listed tool may be dead. Confirm the tool is live before relying on it.

## Overlaps ("do both")
- Pairs with other OSINT tool directories and framework indexes — cross-referencing directories surfaces tools any single list misses. Use several to build coverage.

## Trust & verifiability
`trust: community` — a well-organized but community-maintained index; its value is curation, not authority. Judge each linked tool independently before acting on its output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-stash |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
