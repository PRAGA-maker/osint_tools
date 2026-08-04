---
id: osint-dojo
name: OSINT Dojo
description: Use when you need a vetted, category-organised starting directory of OSINT tools and learning material — returns pointers to specific tools/methods, not person data itself.
url: https://www.osintdojo.com/resources/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A curated, actively-maintained meta-directory of OSINT tools grouped by task (social media, geolocation, email, crypto, people search).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public resource page; no account. Some linked third-party tools are themselves paid, but the directory is free.
opsec: passive
opsecNote: Browsing the directory is passive — you are only reading OSINT Dojo's own pages, not touching a target. OpSec discipline applies once you leave for a linked tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by the OSINT Dojo educational project (active YouTube/Mastodon/X presence); a well-known community reference rather than a first-party data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osintdojo-com
aliases:
- OSINT Dojo Resources
- osintdojo.com/resources
tags:
- other-resources
- curated-directory
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# OSINT Dojo

> A curated, category-organised directory of OSINT tools and training material — the place to discover which tool fits the task in front of you.

## When to use
You are at the start of an investigation and want a shortlist of vetted tools for a specific task (e.g. "reverse image search", "email breach check", "geolocation"), or you want structured learning material on OSINT technique. This is a discovery/reference layer, not a lookup: it points you at the right tool rather than returning data about a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.osintdojo.com/resources/.
2. Scan the category headings (social media, technical/infrastructure, geolocation, crypto, person search, email, collection/automation) and pick the one matching your current pivot.
3. Follow the linked tool out to its own site — that tool, not this page, is where you enter a selector.
4. For methodology, pair the resources list with the site's `[[osintdojo-com]]` flow diagrams, which show how to pivot from one selector to the next on a given platform.

## Inputs → Outputs
- **In:** none (a task/category, not a selector)
- **Out:** links to specific tools and guides
- **Empty/negative result looks like:** the category exists but no linked tool covers your exact need — treat as "look elsewhere", the directory does not itself hold subject data.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; the linked tools may each carry captchas/logins.
- OpSec: passive here; re-assess for each downstream tool you launch.
- Some links inevitably rot — cross-check anything that looks stale against the tool's live site.

## Overlaps ("do both")
- Pairs with `[[osintdojo-com]]` — the diagrams page gives platform-specific pivot flowcharts, while this resources page is the flat tool index; use the diagram to decide the pivot, this list to find the tool.

## Trust & verifiability
`trust: community` — a respected educational project, but a third-party curator: verify that any linked tool is still live and that its data quality suits your case.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-dojo |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
