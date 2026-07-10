---
id: sinwindie-osint
name: sinwindie/OSINT
description: Use when you have a `username`/`social-profile` and need a platform-specific investigation playbook — a curated GitHub repo of per-platform OSINT workflows and resource lists.
url: https://github.com/sinwindie/osint
category: social-networks
path:
- social-networks
bestFor: Platform-by-platform social-media investigation workflows and curated tool/resource lists for tracing people across networks.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open GitHub repository; no account needed to read (a GitHub login only helps to star/clone).
opsec: passive
opsecNote: Reading a methodology repo is passive and touches no target. The techniques it lists vary in OpSec risk — assess each linked tool/workflow on its own before running it against a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Sinwindie, a respected community contributor to social-media OSINT; it is curated guidance, so individual linked tools still need independent verification.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osint-framework-2
- whatsmyname-web
aliases:
- Sinwindie OSINT
- sinwindie/osint
tags:
- tool-collection
- social-networks
- username
- github
- methodology
source: ultimate-osint
lastVerified: '2026-07-10'
enrichment: full
---

# sinwindie/OSINT

> A curated GitHub repository of platform-specific social-media investigation workflows — the "how do I actually investigate someone on X platform" reference, organised network by network.

## When to use
You have a `username` or `social-profile` on a particular platform and want a structured methodology: which features to exploit, which tools apply, and what pivots exist for that specific network. Rather than a lookup tool, this is a playbook — reach for it when you know the platform but not the best technique, or want a checklist so you don't miss an angle when tracing a person across social media.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/sinwindie/osint and navigate to the section for the platform you're investigating.
2. Read the workflow: the platform-specific search tricks, data points to extract, and recommended tools/resources.
3. Apply the steps to your subject on the actual platform, using the linked tools.
4. Move platform-to-platform as you pivot a `username` across networks, consulting each section.
5. Pivot: it routes you to concrete tools — e.g. cross-platform checks via `[[whatsmyname-web]]` — and complements a broad directory like `[[osint-framework-2]]`.

## Inputs → Outputs
- **In:** a `username`/`social-profile` and the platform it's on (you bring these)
- **Out:** methodology and curated tool/resource pointers that lead to `social-profile` and related data
- **Empty/negative result looks like:** not applicable in the lookup sense — it always returns guidance; a "gap" is a platform the repo covers thinly, in which case supplement with other references.

## Gotchas & OpSec
- It holds **no data** — it's methodology and links; the actual investigating happens on the platforms and tools it points to.
- Curated content can age as platforms change features; sanity-check that a described trick still works.
- OpSec: passive to read; each linked technique carries its own footprint — assess before running against a subject.

## Overlaps ("do both")
- Complements `[[osint-framework-2]]` (a broad tool directory) with deeper per-platform workflow; use it to plan, then `[[whatsmyname-web]]` and platform tools to execute.

## Trust & verifiability
`trust: community` — well-regarded, community-maintained guidance. Trust it as a methodology reference; verify each linked tool and technique independently before relying on results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sinwindie-osint |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
