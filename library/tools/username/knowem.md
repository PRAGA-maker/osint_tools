---
id: knowem
name: KnowEm
description: Use when you have a `username` and want to see, across 500+ networks, where it is already taken — returns per-platform availability implying existing `social-profile`s.
url: https://knowem.com/
category: username
path:
- username
bestFor: Broad web check of a username/brand's availability across 500+ social and business networks.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to check a username across the major networks; KnowEm monetises a paid brand/username registration and protection service you can ignore for OSINT.
opsec: passive
opsecNote: Passive — KnowEm checks the platforms server-side and shows you availability; you don't touch the target sites and the subject isn't notified. KnowEm's servers log the handles you submit; use a clean browser if the handle is sensitive.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running commercial username/brand checker; a fast triage signal (taken vs free), not proof of account ownership, and its per-site accuracy can lag reality.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- KnowEm
- knowem.com
tags:
- username
- availability
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# KnowEm

> A web checker that flags a username as taken or free across 500+ networks — even broader than Namechk, useful as a wide triage before deeper enumeration.

## When to use
You have a `username` and want a fast, no-install view of everywhere it's registered (each "taken" hit implies a `social-profile` to inspect). Its breadth — hundreds of social, business, and niche platforms — makes it a good second opinion alongside Sherlock/Namechk, catching sites the others don't cover.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://knowem.com/ and enter the `username`.
2. KnowEm shows availability across major networks first, with an option to check hundreds more by category.
3. Treat each **taken** social platform as a lead — open that platform's `/username` URL to confirm it's your subject.
4. Ignore the paid brand-registration upsell.
5. Pivot: confirmed handles feed `[[sherlock]]`; profile photos feed reverse-image/face tools.

## Inputs → Outputs
- **In:** `username`
- **Out:** per-platform availability; "taken" ⇒ an existing `social-profile` to inspect
- **Empty/negative result looks like:** everything "available" — the handle is unused, or KnowEm's checks for those sites are stale. Verify important hits by hand.

## Gotchas & OpSec
- Human-in-the-loop: expect **rate-limiting**/slow batch checks on the long-tail networks; space out queries.
- OpSec: **passive** — server-side checks; KnowEm logs your queries.
- "Taken" ≠ your subject owns it, and availability logic drifts. Always open the actual profile URL to confirm.

## Overlaps ("do both")
- Pairs with `[[namechk]]` and `[[sherlock]]` — KnowEm's breadth catches niche/business networks the others miss; run more than one enumerator.

## Trust & verifiability
`trust: community` — a convenient commercial triage tool, not an authority. Confirm any meaningful "taken" result on the live platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | knowem |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
