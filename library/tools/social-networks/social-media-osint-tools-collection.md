---
id: social-media-osint-tools-collection
name: Social-Media-OSINT-Tools-Collection
description: Use when you have a `username`, `name`, `email`, or `phone` and want to find the right platform-specific SOCMINT tool — returns a curated catalog pointing to social-profile discovery tools across 16+ platforms.
url: https://github.com/osintambition/Social-Media-OSINT-Tools-Collection
category: social-networks
path:
- social-networks
bestFor: Finding the current best tool for a specific platform (Facebook, Instagram, X, Telegram, TikTok, LinkedIn, etc.) before starting collection.
selectorsIn:
- username
- name
- email
- phone
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open GitHub repository (curated list). No account; clone or browse in-page.
opsec: passive
opsecNote: Reading a GitHub list is passive and reveals nothing about your target. The tools it links to have their own, varying OpSec profiles — assess each individually before running it.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Well-referenced community SOCMINT catalog (1.8k+ GitHub stars); a directory, not a vetted tool — link quality and freshness vary.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- osintambition Social Media OSINT Tools
- SOCMINT tools collection
tags:
- awesome-list
- socint
- catalog
source: gh-topic-osint-resources
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- awesome-browser-extensions-for-osint
---

# Social-Media-OSINT-Tools-Collection

> A platform-organized index of social-media OSINT tools — the map you consult to pick the right tool for the network you're working.

## When to use
You know which platform your subject lives on (or you have a `username`/`name`/`email`/`phone` and a target network) and you want the current best-of-breed tool for it, rather than guessing. This is a meta-resource: it doesn't find people itself — it routes you to the ~290+ discrete tools that do, grouped by the 16+ platforms they target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/osintambition/Social-Media-OSINT-Tools-Collection.
2. Jump to the section for your platform (Facebook, Instagram, X/Twitter, Telegram, TikTok, LinkedIn, Reddit, etc.).
3. Scan the listed tools; pick one matching your selector (username lookup, profile scraper, media downloader, geo tool).
4. **Verify before trusting:** open the tool, confirm it's still live and safe, and check its own OpSec profile.
5. Pivot: run the chosen tool on your selector; return to the list for a second tool to cross-check results.

## Inputs → Outputs
- **In:** the platform + a selector you already hold (`username`/`name`/`email`/`phone`)
- **Out:** pointers to `social-profile`-discovery tools — leads, not data
- **Empty/negative result looks like:** a section that's sparse or full of dead links. Curated lists rot; a tool listed here may be offline or superseded — treat entries as candidates to verify, not endorsements.

## Gotchas & OpSec
- This is a directory, not a tool — its value is orientation and discovery, and you still do the real work in whatever it points you to.
- Link rot: verify each tool is current before relying on it; cross-check with other awesome-lists.
- OpSec: reading the list is passive, but the linked tools range from passive viewers to active scrapers — vet each one.

## Overlaps ("do both")
- Pairs with other catalogs like the OSINT Framework and `[[awesome-osint]]`-style lists — different curators surface different tools, so mine two or three lists when scoping a platform.

## Trust & verifiability
`trust: community` — a popular, frequently-referenced community catalog, but inclusion is not vetting; confirm any tool's legitimacy and current status yourself before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-media-osint-tools-collection |
| category | social-networks |
| selectorsIn → selectorsOut | username, name, email, phone → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
