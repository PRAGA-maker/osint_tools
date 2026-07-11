---
id: graphtreon-com
name: Graphtreon.com
description: Use when you have a Patreon creator `username`/page and want their patron counts, earnings estimates, and growth history — returns financial and audience metrics over time.
url: https://graphtreon.com/
category: social-networks
path:
- social-networks
bestFor: Estimating a Patreon creator's income, patron count, and growth trajectory, and ranking them against peers.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Core creator stats, rankings, and graphs are free; deeper/historical analytics and some features sit behind a paid tier.
opsec: passive
opsecNote: Reads Graphtreon's aggregated public metrics about a creator's page — it does not touch the creator or their patrons and sends no signal to the target. Purely observational; no sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running third-party Patreon analytics site; patron counts are observed but earnings are estimates (Patreon hides exact figures and creators can opt out), so treat income numbers as approximate.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Graphtreon
tags:
- patreon
- creator-analytics
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Graphtreon.com

> A third-party analytics tracker for Patreon: type a creator and get their patron counts, estimated monthly earnings, growth curves, and where they rank — useful for sizing a subject's creator business.

## When to use
Your subject is (or is linked to) a Patreon creator and you want to understand the scale and trajectory of that presence: how many patrons, roughly how much money, and whether it's growing or fading. This contextualizes a subject's finances, audience, and activity timeline, and the creator page itself (linked from Graphtreon) is a pivot into their content, other social links, and community. Reach for it when a Patreon handle surfaces and you want more than the paywalled front page reveals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://graphtreon.com/.
2. Search the creator's `name`/`username`, or browse rankings/filters (by paid members, earnings, growth, category) to locate them.
3. Read the creator profile: patron count (paid + free), estimated monthly payout, membership/revenue changes over 3/6/12 months, and category rank.
4. Follow the link to the actual Patreon page for bio, tiers, posts, and external links.
5. Pivot: the Patreon page → other `social-profile`s and content; growth spikes → timeline of notable events.

## Inputs → Outputs
- **In:** `username` / `name` (Patreon creator)
- **Out:** `social-profile` (Patreon page + metrics: patrons, estimated earnings, growth, rank)
- **Empty/negative result looks like:** creator not found, or earnings shown as hidden — the creator may have no Patreon, be too small/new to index, or have **opted out** of estimated earnings. Absence isn't proof; check Patreon directly.

## Gotchas & OpSec
- Human-in-the-loop: none; browsing only.
- **Earnings are estimates**, not disclosed figures, and creators can opt out — never report Graphtreon income as exact.
- Patron *counts* are more reliable than the dollar estimates.
- OpSec: passive; the creator is not notified.

## Overlaps ("do both")
- Pairs with the creator's actual Patreon page and cross-platform username tools — Graphtreon sizes and trends the account; the page and enumeration reveal identity, links, and content.

## Trust & verifiability
`trust: community` — a reputable long-running tracker, but its headline income numbers are modeled estimates; verify creator existence and links on Patreon itself and treat earnings as approximate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | graphtreon-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
