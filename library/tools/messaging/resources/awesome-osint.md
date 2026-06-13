---
id: awesome-osint
name: Awesome OSINT
description: Use when you need to discover OSINT tools or methods for a given selector/platform — a large curated index of tools and resources.
url: https://github.com/jivoi/awesome-osint
category: messaging
path:
- messaging
- resources
bestFor: Broad OSINT tool/resource discovery, organized into ~50+ categories from social media to phone/email/people research.
input: Manual browsing by topic/category
output: Categorized links to OSINT tools and learning resources
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source curated list on GitHub.
opsec: passive
opsecNote: A reference index only — reading it touches no target. OPSEC depends entirely on whichever linked tools you then use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, widely used community list (~26k+ stars) maintained by jivoi and contributors; reputable as a directory, though individual linked tools vary in quality and must be vetted.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- awesome-osint
- jivoi awesome-osint
tags:
- resource
- directory
- methodology
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# Awesome OSINT

> A large, community-curated GitHub directory of OSINT tools and resources, organized into ~50+ categories — a map for finding the right tool, not a tool itself.

## When to use
You don't yet know which tool fits a given `selector` or platform (a phone number, an email, a username, a Telegram channel, a vehicle, a region) and want a curated starting point. Use Awesome OSINT to browse categories — social media (Telegram, Facebook, Instagram, etc.), email/phone/people search, domain/IP, geospatial, threat intel — and shortlist candidate tools to then evaluate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/jivoi/awesome-osint.
2. Use the README's table of contents (or in-page find / GitHub search) to jump to the relevant category.
3. Read the curated links and one-line descriptions; open promising tools in new tabs.
4. Pivot: vet each shortlisted tool individually (it's an index, not a guarantee), then run the actual lookup in that tool with your selector.

## Inputs → Outputs
- **In:** a topic/category or platform of interest (no selector entered into the page itself)
- **Out:** a categorized list of candidate tools and reading resources
- **Empty/negative result looks like:** a category exists but its links are stale/dead — cross-check with other directories and the project's last-commit date.

## Gotchas & OpSec
- It's a directory: link rot is inevitable; some tools are dead, paid, or low quality despite being listed.
- No vetting per-link beyond inclusion — always assess each tool's trust/opsec before use.
- OpSec: passive (just reading GitHub); your real OPSEC exposure starts when you use a linked tool.

## Overlaps ("do both")
- Use alongside other OSINT framework indexes (e.g. OSINT Framework, Bellingcat's toolkit) to fill category gaps and catch tools one list misses.

## Trust & verifiability
`trust: trusted` — a long-standing, heavily-starred community list maintained by jivoi and contributors. Trust applies to the directory's curation, not to every linked tool; verify each tool independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-osint |
| category | messaging |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
