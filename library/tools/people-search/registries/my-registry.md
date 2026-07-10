---
id: my-registry
name: My Registry
description: Use when you have a `name` and want to find their gift/wedding/baby registry — returns registrant name, event type/date, a partner or co-registrant and location/shipping hints.
url: https://www.myregistry.com/
category: people-search
path:
- people-search
- registries
bestFor: Finding a person's universal gift registry to surface life events, a partner's name and location clues.
selectorsIn:
- name
selectorsOut:
- name
- associate
- address
status: live
pricing: free
costNote: Free to search ("Find a Registry") and to create registries; only cash-gift funds carry a small transaction fee. No account needed to search.
opsec: passive
opsecNote: Searching the public registry directory is passive — you query MyRegistry, not the subject, and registrants who appear have opted to be findable. Do not contact a registry or buy items as a pretext; that is active and exposes you. Use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A legitimate commercial universal-registry service; data is self-submitted by registrants and only appears if they made the registry publicly searchable, so coverage is partial and self-reported.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- MyRegistry
- myregistry.com
tags:
- people-search
- registries
- gift-registry
- life-events
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# My Registry

> A universal gift-registry search: a found registry ties a name to a life event, often a partner, and a rough location.

## When to use
You have a `name` and want to discover life-event context — an upcoming wedding, a baby, a housewarming, a move — and the people and places around it. A public registry frequently names a partner/co-registrant (`associate`), signals a date and location, and confirms the person is active. Useful for building the relationship graph and timeline around a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.myregistry.com/ and use "Find a Registry."
2. Search by the registrant's `name` (add event type or location to narrow).
3. Open a matching registry.
4. Read it for: registrant `name`(s) — often a couple, so a `associate`/partner name; the event type and date; and location/shipping hints (city, sometimes a shipping area). The gift list itself can hint at circumstances (baby, new home).
5. Pivot: a partner's name feeds people-search (`[[radaris-people-and-business-search-north-america]]`); an event date anchors a timeline; a location clue narrows geography.

## Inputs → Outputs
- **In:** `name`
- **Out:** registrant `name`(s), partner/co-registrant `associate`, event type/date, and location/`address` hints
- **Empty/negative result looks like:** no matching public registry — the person has none, or set theirs private/unsearchable (registrants control discoverability). Absence is not proof of no life event.

## Gotchas & OpSec
- Coverage is **opt-in and self-reported** — only publicly searchable registries appear, and details are as the registrant entered them.
- MyRegistry is universal (aggregates many stores); a person may instead use a store-specific registry (Amazon, Target, Zola) not indexed here — check those too.
- OpSec: **passive** to search; do not "purchase" or message through a registry as a ruse — that is active contact.

## Overlaps ("do both")
- Pairs with store-specific registry searches (Amazon, Target, Zola/The Knot) and with social/life-event OSINT — different platforms host different registries, so search several. A wedding registry plus a wedding-site listing corroborates the partner and date.

## Trust & verifiability
`trust: unverified` — a legitimate service, but registry contents are self-submitted and optionally private; treat a found registry as a strong lead to corroborate (partner name, event, location) against other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | my-registry |
| category | people-search |
| selectorsIn → selectorsOut | name → name, associate, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
