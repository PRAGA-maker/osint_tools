---
id: fbi-tools
name: FBI-tools
description: Use when you have a case type but not the right tool and want a categorised index of OSINT/forensics utilities to mine — returns pointers to other tools, not data on a person.
url: https://github.com/danieldurnea/FBI-tools
category: search-engines
path:
- search-engines
bestFor: Discovering additional OSINT/forensics tools organised by investigation type.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open GitHub README; no account, install, or payment. (Despite the name, it has no connection to the FBI — it is a community-maintained "awesome" list.)
opsec: passive
opsecNote: Browsing a public GitHub README leaks nothing about your subject. The tools it links to have their own OpSec profiles — read each tool's own page before pointing it at a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained awesome-style aggregator (danieldurnea/FBI-tools); it is a directory of links, not a vetted or first-party toolset, and inclusion is not endorsement.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- danieldurnea/FBI-tools
tags:
- awesome-list
- osint-collection
- forensics
source: gh-topic-reconnaissance
lastVerified: '2026-07-17'
enrichment: full
---

# FBI-tools

> A community "awesome list" on GitHub cataloguing OSINT and digital-forensics tools by category — a frontier to mine for tooling, not a lookup itself.

## When to use
You have hit a wall on a particular selector (a username, an email, a device image, a dark-web lead) and want to see what tools exist for that class of problem. FBI-tools is a curated README that groups hundreds of OSINT/forensics utilities — social-media recon, mobile forensics, geolocation, metadata, dark-web, email/username verification — so you can scan a category and find candidates you don't already have.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/danieldurnea/FBI-tools and read the README (or use the anchor/table-of-contents links to jump to a category).
2. Browse the section matching your need (e.g. "Email", "Phone Number", "Image forensics", "Dark Web").
3. Follow the link to a candidate tool's own repo/site and evaluate it there — check whether it is live, free, and safe to use before running it.
4. Pivot: treat each linked tool as a lead to enrich into your own workflow; nothing here queries a subject directly.

## Inputs → Outputs
- **In:** none — you bring an investigation type, not a selector
- **Out:** none — pointers to other tools; no data about any person
- **Empty/negative result looks like:** the category you need has no relevant entries, or the linked tool is dead/abandoned — verify each link, as awesome-lists rot over time.

## Gotchas & OpSec
- The "FBI" name is decorative marketing; there is no government affiliation. Do not represent it as an official source.
- Link rot and quality drift: entries are not continuously vetted, so a listed tool may be defunct, renamed, or now paid.
- OpSec: reading the list is passive; the risk lives in the tools it points you to — assess each one's footprint separately.

## Overlaps ("do both")
- Use alongside your existing library: this is a discovery index for finding *new* tools, complementary to any specific enriched tool rather than overlapping with one.

## Trust & verifiability
`trust: community` — it is a single maintainer's curated link collection; useful as a map, but every destination needs independent verification before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fbi-tools |
| category | search-engines |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
