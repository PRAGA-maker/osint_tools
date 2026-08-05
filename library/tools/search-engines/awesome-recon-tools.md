---
id: awesome-recon-tools
name: awesome-recon-tools
description: Use when you're stuck for the right tool and want a categorized menu of recon/footprinting options — returns a curated directory pointing to tools for `domain`, `email`, and personal recon.
url: https://github.com/nateahess/awesome-recon-tools
category: search-engines
path:
- search-engines
bestFor: A curated, categorized index of reconnaissance and footprinting tools to pick the right one for a given lead.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public GitHub repository; some tools it links to are commercial (Shodan, Maltego), most are open-source.
opsec: passive
opsecNote: Reading a GitHub list leaks nothing about a subject. OpSec depends entirely on which linked tool you then use — evaluate each one's exposure before running it against a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained "awesome" list (100+ stars); it is a signpost, not a vetted toolkit — assess each linked tool's freshness and safety yourself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- awesome recon tools
- nateahess/awesome-recon-tools
tags:
- curated-list
- reconnaissance
- footprinting
source: gh-topic-footprinting
lastVerified: '2026-08-05'
enrichment: full
---

# awesome-recon-tools

> A categorized menu of reconnaissance and footprinting tools — the page you open when you know the lead but not the tool.

## When to use
You have a lead (a `domain`, an `email`, a person to footprint) and want to see the field of tools that address it, grouped by purpose, rather than guessing. This curated GitHub list organizes tools into **Domain & Network Recon**, **Personal Info & Email Footprinting**, and **Hacking with Google** (dorks), spanning big platforms (Shodan, Maltego) to open-source staples (recon-ng, theHarvester). Use it to broaden your options or find a specialized tool you didn't know existed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/nateahess/awesome-recon-tools.
2. Jump to the section matching your lead: domain/network, personal/email, or Google dorking.
3. Scan the entries and pick candidate tools; open each tool's own page to check it's still maintained and free/affordable.
4. Cross-check any tool you're unsure about against this library's own entry (if present) for OpSec and trust notes before running it.

## Inputs → Outputs
- **In:** none (a meta-resource; you bring the lead, it suggests tools)
- **Out:** a shortlist of recon tools to try for `domain` / `email` / personal footprinting
- **Empty/negative result looks like:** the category you need isn't well covered, or listed tools are stale/dead. As with any awesome-list, entries age — verify each before relying on it.

## Gotchas & OpSec
- It's a signpost, not a guarantee — linked tools vary wildly in freshness, cost, and safety; vet each.
- Some entries are commercial or attack-oriented; confirm a tool fits a lawful missing-persons/OSINT purpose before use.
- OpSec: reading the list is passive; the risk is in the tools you subsequently run.

## Overlaps ("do both")
- Complements this library itself: use the list to *discover* a tool, then look it up here for the vetted how-to, OpSec, and trust rating before you point it at a subject.

## Trust & verifiability
`trust: community` — a volunteer-curated index; treat it as a discovery aid and independently verify each linked tool's current status and reputation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-recon-tools |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
