---
id: trace-labs-blog
name: Trace Labs Blog
description: Use when you want missing-persons OSINT methodology, tooling and training — returns Trace Labs' articles, geolocation guides, VM releases and Search Party CTF write-ups.
url: https://www.tracelabs.org/blog/rss.xml
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Learning missing-persons OSINT tradecraft, methodology and tooling from the Trace Labs team.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free blog / RSS feed; no account required.
opsec: passive
opsecNote: Reading the blog is passive and reveals nothing about any subject. The techniques it teaches, however, are for real missing-persons cases — apply them ethically and within Trace Labs' rules of engagement (no contact with the subject or family, no illegal access).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official blog of Trace Labs, a well-known nonprofit that runs the Global OSINT Search Party CTF crowdsourcing OSINT for real missing-persons cases in partnership with law enforcement.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- trace-labs-osint-vm
aliases:
- trace labs
- tracelabs blog
tags:
- missing-persons
- methodology
- training
- awesome-osint
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Trace Labs Blog

> The official Trace Labs blog: the missing-persons OSINT organisation's own methodology, geolocation tutorials, tooling and Search Party CTF debriefs — a primary training source for this whole discipline.

## When to use
You want to sharpen missing-persons OSINT tradecraft directly from the people who built the field's largest crowdsourced effort. The blog publishes methodology guides, geolocation and verification techniques, releases of the Trace Labs OSINT VM, and recaps of the Global OSINT Search Party CTF (where teams find OSINT on real missing individuals for law enforcement). It's a learning/reference resource, not a lookup tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tracelabs.org/blog (or subscribe to the RSS feed at https://www.tracelabs.org/blog/rss.xml).
2. Browse by theme: OSINT methodology/training series, geolocation how-tos, VM release notes, and CTF operations posts.
3. For hands-on tooling, follow the posts to the Trace Labs OSINT VM (a curated Linux distro of missing-persons OSINT tools).
4. Apply the techniques within Trace Labs' rules of engagement when working a case.
5. Pivot: methodology here informs which selector tools to reach for; the OSINT VM bundles many of them.

## Inputs → Outputs
- **In:** none (a reading/training resource)
- **Out:** methodology, tutorials, tooling pointers, and community/CTF context for missing-persons OSINT
- **Empty/negative result looks like:** not applicable — it's a content feed; if a specific technique isn't covered, check the Trace Labs Discord/community or the OSINT VM docs.

## Gotchas & OpSec
- This teaches technique; it does not itself return data on a person.
- Ethics gate: Trace Labs enforces strict rules of engagement (no contact with the missing person or their family, no unlawful access) — follow them on any real case.
- Passive to read; the OpSec responsibility is in how you apply what you learn.

## Overlaps ("do both")
- Pairs with the Trace Labs OSINT VM and general OSINT framework guides — the blog explains the *how*, the VM ships the *tools*; use both when working missing-persons cases.

## Trust & verifiability
`trust: trusted` — a reputable nonprofit that partners with law enforcement on live missing-persons cases; its published methodology is authoritative for this domain.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trace-labs-blog |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
