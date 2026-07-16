---
id: yogsec
name: Yogsec
description: Use when you want a curated, categorised catalogue of pentest/OSINT tools to draw from — this security researcher's GitHub returns organised tool lists (notably the 1.8k-star "Hacking-Tools" collection), not a lookup on any person.
url: https://github.com/yogsec/
category: search-engines
path:
- search-engines
bestFor: Discovering and shortlisting OSINT/pentest tools from a maintained, categorised GitHub collection.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open on GitHub; no account needed to browse (a GitHub login only helps for starring/forking).
opsec: passive
opsecNote: Browsing a public GitHub profile is passive and touches no target. Vet any tool you pull from the list before running it against real subjects — a curated link is not an endorsement of a tool's safety or legality in your context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Abhinav Singwal (yogsec), an active security researcher with a followed, well-starred set of repos. It is a community reference list; individual linked tools vary in quality and must be judged on their own.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- one-liner-osint
- osint-tools-yogsec
aliases:
- yogsec
- Abhinav Singwal
- Hacking-Tools
tags:
- searchengines
- Search Engines
- curated-directory
- tool-list
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Yogsec

> A security researcher's GitHub — a jumping-off directory of categorised pentest/OSINT tools (the "Hacking-Tools" repo is the headline), not a search engine that returns data on a person.

## When to use
You are assembling or refreshing your toolkit and want a maintained, human-curated list of OSINT/reconnaissance tools organised by category, rather than a raw awesome-list. Yogsec's GitHub (especially the **Hacking-Tools** repo, ~1.8k stars) is a shortlist source: browse the categories, pick candidates, then evaluate each on its own merits. It answers "what tool exists for X?", never "who is this person?".

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/yogsec/ and review the pinned/popular repos — **Hacking-Tools** (curated pentest/OSINT list), plus topical repos (CORS checks, physical-pentest resources, XSS labs).
2. In Hacking-Tools, jump to the category matching your need (recon, social, phone, image, etc.).
3. Shortlist candidate tools; open each tool's own repo/site and vet it (maintenance, stars, issues, whether it's safe/legal for your use).
4. Pivot: bring the vetted tool into your actual workflow; use this library's authored entries where they exist for a specific tool instead of the raw link.

## Inputs → Outputs
- **In:** none (a reference resource — you browse, you don't query a subject)
- **Out:** categorised lists of tool names/links to evaluate
- **Empty/negative result looks like:** N/A — it is a static-ish catalogue. "Failure" is finding the list stale; check each linked tool's own repo for current status.

## Gotchas & OpSec
- It is a **directory, not a tool** — inclusion is not endorsement; vet every linked tool before use.
- Repo activity is modest, so some links may age; verify a tool is still maintained before relying on it.
- OpSec: **passive** browsing; the OpSec that matters is whatever the downstream tool you pick requires.

## Overlaps ("do both")
- Complements other curated sources in this library (awesome-osint, MetaOSINT, Toddington) — cross-reference lists to catch tools any single directory misses, then prefer a fully-authored entry here for operational guidance.

## Trust & verifiability
`trust: community` — a reputable, active researcher's public collection. The list itself is trustworthy as a starting point, but the tools it links are third-party and uneven; judge each independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yogsec |
| category | search-engines |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
