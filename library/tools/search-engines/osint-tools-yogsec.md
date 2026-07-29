---
id: osint-tools-yogsec
name: OSINT-Tools (yogsec)
description: Use when you have a selector and don't know which tool fits — returns a categorised directory of OSINT tools and methods to pick from.
url: https://github.com/yogsec/OSINT-Tools
category: search-engines
path:
- search-engines
bestFor: Discovering the right OSINT tool or method for a given selector, organised across 26 investigation categories.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open GitHub repository; browse in the README or clone.
opsec: passive
opsecNote: A static reference list on GitHub — reading it touches no target. OpSec applies only to the individual tools you then choose to run; the directory itself leaks nothing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained tool/method collection (~67 stars) by the yogsec project; actively organised but link quality varies — treat listed tools as leads to verify, not endorsements.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- one-liner-osint
- yogsec
- bellingcat-online-investigation-toolkit
aliases:
- yogsec OSINT-Tools
tags:
- directory
- reference
- methods
source: gh-topic-osint-framework
lastVerified: '2026-07-29'
enrichment: full
---

# OSINT-Tools (yogsec)

> A categorised GitHub directory of OSINT tools and methods — a "which tool do I use for this?" index spanning 26 investigation categories.

## When to use
You hold a selector (username, email, domain, image, phone, geolocation) but aren't sure which tool covers it, or you want to broaden beyond the tools you already know. This repo groups resources by category — username/email investigation, domain/IP, image/video/document, social networks, people search, geolocation, threat intel, malware analysis, OpSec — with direct links, so you can quickly find candidate tools for the case in front of you.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/yogsec/OSINT-Tools and read the README (or clone for offline browsing).
2. Jump to the category matching your selector (e.g. "Username", "Geolocation").
3. Scan the listed tools and their links; pick candidates that fit your input/output need.
4. Verify each candidate is live and free before committing — this is a curated list, not a maintained status board.
5. Pivot: many listed tools have dedicated skills in this library; use this directory to find the name, then use the fuller skill entry for how-to and OpSec.

## Inputs → Outputs
- **In:** none (a discovery directory, not a selector-driven lookup)
- **Out:** categorised lists of candidate OSINT tools and methods with links
- **Empty/negative result looks like:** the category you need is thin or the links are stale — cross-reference a second directory rather than assuming no tool exists.

## Gotchas & OpSec
- It is a reference, not a data source — it returns tool suggestions, not investigation results.
- Link rot: community lists accumulate dead entries. Confirm any tool is still live before relying on it.
- Overlaps heavily with other OSINT directories; use it alongside one or two others to fill category gaps.

## Overlaps ("do both")
- Pairs with `[[bellingcat-online-investigation-toolkit]]` and `[[one-liner-osint]]` — cross-referencing two or three directories beats trusting one, since each curates a different slice and ages differently.

## Trust & verifiability
`trust: community` — a useful, actively organised community index, but inclusion is not vetting. Every tool it names must be verified for status, cost, and safety before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-tools-yogsec |
