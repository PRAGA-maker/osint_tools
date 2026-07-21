---
id: computerworld
name: Computerworld
description: Use when you have a `name` or `employer-org` in enterprise IT and want long-run coverage — returns `employer-org`, `associate` and professional-timeline context from articles.
url: https://www.computerworld.com
category: communities-forums
path:
- communities-forums
bestFor: Enterprise-IT press coverage — tracing IT leaders, vendors, and long-standing tech-industry figures.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free to read and search; ad-supported.
opsec: passive
opsecNote: Searching and reading a public news site transmits nothing about your subject. Fully passive; a private window avoids personalisation cookies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-established enterprise-IT publication (Foundry/IDG). Reliable secondary source with a decades-long archive, subject to the usual journalistic caveats.
missingPersonsRelevance: low
coverage:
- global
aliases:
- ComputerWorld
- computerworld.com
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Computerworld

> A veteran enterprise-IT publication with a deep archive — useful for tracing IT executives, analysts, vendors, and long-standing industry figures over time.

## When to use
Your subject is an enterprise-IT professional, CIO/CISO, analyst, or vendor spokesperson. Computerworld's long history and enterprise focus make it good for people whose careers span decades of tech coverage — confirming an `employer-org`, quoted roles, conference appearances, and professional `associate`s across many years.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.computerworld.com and use site search, or run: `site:computerworld.com "Full Name"` / `"Company"`.
2. Read matching articles for the person's title, employer, quotes, and dates — note the long archive may hold older roles.
3. If the subject is an author/columnist, open their contributor page to enumerate their work.
4. Note co-quoted people and organisations as pivots.
5. Pivot: a confirmed title/employer feeds LinkedIn and registry lookups; older articles help reconstruct a career timeline.

## Inputs → Outputs
- **In:** `name` / `employer-org` (enterprise IT)
- **Out:** `employer-org`, `associate` (colleagues, co-quoted figures), professional timeline
- **Empty/negative result looks like:** no article matches — the person wasn't covered here; try sister IDG/Foundry titles (CIO, InfoWorld, Network World) and broader tech press.

## Gotchas & OpSec
- Enterprise-IT focus — narrow; a non-IT subject won't appear.
- Secondary source: confirm titles/quotes against a primary source where it matters.
- Fully passive — searching leaks nothing.

## Overlaps ("do both")
- Pairs with sister publications (CIO, InfoWorld, Network World) and LinkedIn — the IDG/Foundry family often covers the same people; run several to build a full professional picture.

## Trust & verifiability
`trust: trusted` — an established outlet with a long archive; reliable secondary sourcing, with specifics worth confirming against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | computerworld |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
