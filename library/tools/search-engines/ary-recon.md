---
id: ary-recon
name: Ary-Recon
description: Use when you want a single-page launcher of passive-recon links organised by task — a directory (not a scanner) that points you to 30+ subdomain/email/IP/breach tools.
url: https://github.com/giriaryan694-a11y/Ary-Recon
category: search-engines
path:
- search-engines
bestFor: Browsing passive-reconnaissance tools by category from one HTML page.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source single-page HTML directory; no account, no install beyond opening a file.
opsec: passive
opsecNote: The directory itself does nothing but link out — it's passive. OpSec depends entirely on whichever linked tool you then use; each destination has its own exposure profile, so vet the target tool before running it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small single-author GitHub project (0 stars, ~11 commits, last updated 2025); a convenience index, not a vetted authority — judge each linked tool on its own merits.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- ARY Recon
tags:
- directory
- passive-recon
source: gh-topic-footprinting
lastVerified: '2026-07-29'
enrichment: full
---

# Ary-Recon

> A lightweight one-page index of passive-recon tools, grouped by task — a jump list, not something that finds data itself.

## When to use
You want a quick, categorised menu of passive reconnaissance tools (subdomain discovery, tech fingerprinting, email finding, IP intelligence, breach checking, malware analysis) without maintaining your own bookmark list. It is a meta-resource: it accelerates *finding the right tool*, then you leave to that tool. It never processes a selector itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the project's `index.html` — directly in a browser, via its GitHub Pages deployment, or self-hosted.
2. Browse the ~11 categories and pick a tool matching your current pivot (e.g. "IP intelligence").
3. Click through to the external tool and do the actual work there.
4. Pivot: nothing to pivot *within* Ary-Recon; it hands you off to the chosen tool.

## Inputs → Outputs
- **In:** none (you browse categories)
- **Out:** curated links to third-party recon tools (no data)
- **Empty/negative result looks like:** a category with no tool that fits your need — fall back to a broader OSINT framework/directory.

## Gotchas & OpSec
- It's just links — every real risk lives in the tool you click through to; vet each destination.
- Minimal maintenance (single author, low adoption) means links may rot; confirm a tool is still live before relying on it.
- Not exhaustive — treat it as one convenience index among many, not a definitive catalogue.

## Overlaps ("do both")
- Overlaps with any broader OSINT-framework directory; use Ary-Recon for a fast task-grouped menu and a fuller framework when you need breadth.

## Trust & verifiability
`trust: unverified` — a small personal directory; it vouches for nothing, so evaluate each linked tool independently before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ary-recon |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
