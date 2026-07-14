---
id: the-bump
name: The Bump Baby Registry Finder
description: Use when you have a parent's name and want to find their baby registry — returns registry links, expected item lists and sometimes an event date or general location.
url: https://registry.thebump.com/babyregistrysearch
category: people-search
path:
- people-search
- registries
bestFor: Locating an expectant/new parent's baby registry by name to confirm identity, timing and associates.
selectorsIn:
- name
selectorsOut:
- name
- associate
- address
status: live
pricing: free
costNote: Free to search; no account or payment required to look up a registry by parent name.
opsec: passive
opsecNote: You search The Bump's public registry index, not the parent's account — the target is not notified. The Bump logs your search; use a VPN for sensitive work. Registries are self-published, so treat what you find as information the person chose to make public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A mainstream consumer parenting site (part of The Knot Worldwide); the registry index is reliable but user-submitted, so detail depends on what each parent published.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- The Bump registry search
- thebump baby registry finder
tags:
- people-search
- registries
- baby-registry
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# The Bump Baby Registry Finder

> A public baby-registry search — enter a parent's name and find their registry, a surprisingly rich confirmation of identity, timeline (a due date) and social circle.

## When to use
You have a `name` for someone who may be an expectant or recent parent. A baby registry is a small OSINT goldmine: it confirms the parent's name (and often a partner's), implies a rough timeframe (registries cluster around a due date), can leak a shipping city/area, and — through gift activity and co-hosts — hints at family and friends. The Bump is one of the two big US registry indexes (alongside Babylist), so it's a first stop when the subject's life stage fits.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://registry.thebump.com/babyregistrysearch.
2. Enter the parent's **first and last name** and search.
3. Open a matching registry: read the couple/parent names, the item list, and any event/shower details or general location shown.
4. Cross-check the name(s) and timing against what you already know; note a partner name as an `associate`.
5. Pivot: partner/family names feed people-search and social lookups; a due-date window anchors a timeline; a shipping city feeds address/location work.

## Inputs → Outputs
- **In:** a parent's `name` (first + last)
- **Out:** registry link, parent/partner `name`s (`associate`), item list, and sometimes an event date or general `address`/city
- **Empty/negative result looks like:** no registry for that name — the person may have used Babylist/Amazon/Target instead, kept it private, or not be a parent. A miss here is weak evidence; check other registry sites.

## Gotchas & OpSec
- Registries are self-published and often use a nickname or only a first name — try variations, and the partner's name too.
- US-centric; parents elsewhere are unlikely to appear.
- Passive and non-alerting, but the data is only as complete as the parent chose to make public.
- Multiple people share common names — confirm with a second data point (city, partner) before attributing.

## Overlaps ("do both")
- Pairs with Babylist / Amazon / Target registry searches — parents pick one platform, so run several to find the right one.
- Feeds general people-search once a partner or family name emerges from the registry.

## Trust & verifiability
`trust: community` — a mainstream, reliable consumer platform, but the registry contents are user-submitted; corroborate names, dates and locations against an independent source before acting on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-bump |
| category | people-search |
| selectorsIn → selectorsOut | name → name, associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
