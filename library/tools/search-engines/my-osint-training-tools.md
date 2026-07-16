---
id: my-osint-training-tools
name: My OSINT Training Tools
description: Use when you have any starting selector and want a curated, categorized launcher of vetted OSINT web tools to pick the right one — returns pointers to specialized tools, not data itself.
url: https://tools.myosint.training/
category: search-engines
path:
- search-engines
bestFor: Quickly launching vetted OSINT web tools by category.
selectorsIn:
- name
- username
- email
- phone
- image
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public tool board maintained by My OSINT Training; no account required.
opsec: passive
opsecNote: Browsing the board is passive; the OpSec footprint of anything you launch depends on that specific tool — check each one's own profile before submitting target data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Curated by Griffin Glynn (@hatless1der), a well-known OSINT trainer; a vetted, actively-maintained board rather than a raw scraped list.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- tools.myosint.training
- hatless1der tools board
tags:
- tool-collection
- launcher
- people-search
source: ultimate-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- myosint-training
- the-bitmoji-avatar-history-enumerator
---

# My OSINT Training Tools

> Griffin Glynn's categorized tool launcher — a fast, vetted menu for choosing the right OSINT web tool for the selector you're holding.

## When to use
You have a starting selector (`name`, `username`, `email`, `phone`, or `image`) and want a trusted, human-curated launcher rather than a sprawling scraped list. Use it to jump straight to a fit-for-purpose tool by category, or to discover approaches you hadn't considered. It's an index/launcher — the data comes from the tools it opens.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tools.myosint.training/.
2. Browse by category (people search, username, social media, images, etc.) to find candidate tools for your selector.
3. Launch a chosen tool in a separate sock-puppet session and check *that tool's* OpSec/pricing before entering target data.
4. Pivot: this board points you to the specialized tool; the actual leads come from there.

## Inputs → Outputs
- **In:** any selector you're working (`name`/`username`/`email`/`phone`/`image`)
- **Out:** curated pointers to specialized tools (which then yield `social-profile` and other data) — the board itself returns no personal data
- **Empty/negative result looks like:** no listed tool fits a very niche need — fall back to this library's category indexes or another curated framework.

## Gotchas & OpSec
- It's a launcher, not a lookup: it confirms nothing about a person.
- Even vetted boards lag reality — a listed tool may have changed pricing or gone offline; verify before relying.

## Overlaps ("do both")
- Complements `[[toddington-free-osint-resources]]` and this library: different curators cover different tools, so cross-check when hunting for the right instrument.

## Trust & verifiability
`trust: trusted` — maintained by a respected OSINT trainer; still verify each linked tool's current status yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | my-osint-training-tools |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, phone, image → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
