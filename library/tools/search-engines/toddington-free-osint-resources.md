---
id: toddington-free-osint-resources
name: Toddington Free OSINT Resources
description: Use when you have any starting selector and want a vetted, professionally-maintained index of free OSINT tools to pick the right one — returns pointers to specialized tools, not data itself.
url: https://www.toddington.com/resources/free-osint-resources-open-source-intelligence-search-tools-research-tools-online-investigation/
category: search-engines
path:
- search-engines
bestFor: A vetted, professionally-curated directory of free OSINT search and research tools.
selectorsIn:
- name
- username
- email
- phone
- image
selectorsOut:
- social-profile
- address
status: live
pricing: free
costNote: The resource list is free to browse. Toddington International (TII) is a paid training/services firm, but this tools directory is public and free.
opsec: passive
opsecNote: Browsing the directory is passive; the OpSec profile of anything you launch from it depends on that individual tool, so read each tool's own footprint before use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Toddington International, a long-established professional online-investigation training firm; the list is curated and periodically pruned, unlike raw scraped seed lists.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Toddington International resources
- TII free OSINT resources
tags:
- tool-collection
- people-search
- public-records
source: ultimate-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- toddington-online-research-cheat-sheets
---

# Toddington Free OSINT Resources

> A professionally-curated directory of free OSINT tools — the place to decide *which* tool to reach for, spanning people search, public records, social, and imagery.

## When to use
You have a starting selector (`name`, `username`, `email`, `phone`, or `image`) and want a trustworthy, human-vetted menu of free tools rather than a raw scraped list. Use it as a jumping-off index when you're unsure which specialized tool fits your current pivot, or to discover categories you hadn't considered.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the resources page on toddington.com.
2. Browse by category (people search, public records, social media, images, etc.) to find candidate tools matching your selector.
3. Launch a chosen tool in a separate sock-puppet session — and check *that tool's* own OpSec/pricing before submitting any target data.
4. Pivot: this is an index; the actual data comes from the specialized tools it links to.

## Inputs → Outputs
- **In:** any selector you're trying to work (`name`/`username`/`email`/`phone`/`image`)
- **Out:** curated pointers to specialized tools (which then yield `social-profile`, `address`, etc.) — the directory itself returns no personal data
- **Empty/negative result looks like:** no listed tool fits your niche need — expected for very specialized tasks; fall back to this library's own category indexes or a broader framework.

## Gotchas & OpSec
- It's an index, not a lookup: it confirms nothing about a person; value is curation quality and coverage breadth.
- Links can age; a listed tool may have changed pricing or gone offline since curation — verify before relying.

## Overlaps ("do both")
- Complements this library and other curated frameworks: use Toddington to discover a tool, then this library's enriched entry (where it exists) for the OpSec/how-to detail before running it.

## Trust & verifiability
`trust: trusted` — curated by an established professional-investigation firm; still verify each linked tool's current status yourself, as directories inevitably lag reality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | toddington-free-osint-resources |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, phone, image → social-profile, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
