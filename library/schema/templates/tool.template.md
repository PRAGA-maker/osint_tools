---
# --- Required ---
id: example-tool
name: Example Tool
description: Use when you need to <do X> from a <selector> — returns <selectorsOut>.
url: https://example.com
category: people-search
trust: unverified
pricing: free
missingPersonsRelevance: medium
bestInteractionPattern: web-manual
# --- Strongly encouraged ---
path: [people-search, general]
bestFor: One-line primary use case.
selectorsIn: [name]
selectorsOut: [address, phone, associate]
status: unknown
opsec: passive
opsecNote: ""
humanInLoop: false
humanInLoopReason: []
trustNote: ""
coverage: [us]
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases: []
tags: []
source: ""
lastVerified: ""
enrichment: full
---

# Example Tool

> One-sentence positioning: what this is and the single thing it's best at.

## When to use
Concretely, the case state in which an agent should reach for this. Tie to selectors:
"You have a `name` + approximate `geolocation` and want current `address` / `associate` links."

## How to use it (`bestInteractionPattern`: web-manual)
Step-by-step for the declared interaction pattern.
1. Go to the URL / run the command.
2. Enter the input (`selectorsIn`).
3. Read the output (`selectorsOut`) — what good vs empty looks like.
4. Pivot: where the output feeds next (link `[[other-tool-id]]` or a strategy).

## Inputs → Outputs
- **In:** `name`
- **Out:** `address`, `phone`, `associate`
- **Empty/negative result looks like:** describe so the agent doesn't false-positive.

## Gotchas & OpSec
- Human-in-the-loop: <captcha? login?> and how to handle.
- OpSec: passive/active, what it leaks, whether to use a sock puppet.

## Overlaps ("do both")
- Pairs with `[[related-tool-id]]` because <coverage differs / one finds what the other misses>.

## Trust & verifiability
`trust: unverified` — <one line on why this rating; who maintains it>.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | example-tool |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
