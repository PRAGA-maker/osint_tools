---
id: registry-finder
name: Registry Finder
description: Use when you have a `name` and want to find their gift registries (wedding/baby) across major US retailers — returns registry links revealing `associate` (partner/family), event dates, and `address` (event/city) hints.
url: https://registryfinder.com/
category: people-search
path:
- people-search
- registries
bestFor: Locating a person's wedding/baby gift registries to surface partner names, dates, and location clues.
selectorsIn:
- name
selectorsOut:
- associate
- name
- address
status: live
pricing: free
costNote: Free to search; no account required (revenue comes from retailer affiliate links).
opsec: passive
opsecNote: You query a registry aggregator, not the subject, and no notice is sent to them. Viewing a registry does not alert the registrant. Safe to run from a clean browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party aggregator that federates searches to Amazon, Target, and other retailers; results depend on those retailers' registry search and are only as current as they are.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- RegistryFinder.com
tags:
- registries
- people-search
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Registry Finder

> A cross-retailer gift-registry search — one query checks Amazon, Target, and other stores for a person's wedding or baby registry, which often leaks partner names, dates, and locations.

## When to use
You have a subject's `name` and want the surprisingly rich context a gift registry exposes: a wedding registry names the couple (a strong `associate` link) and often an event date/city; a baby registry implies a due date and a household. Useful for confirming relationships, life events, and approximate location, especially for US subjects who have recently married or had a child.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://registryfinder.com/ and enter the registrant's first and last `name` (optionally the co-registrant/partner name).
2. Submit — it federates the search across supported retailers and returns matching registries.
3. Open a match: note the co-registrant (`associate`), the event type and date, and any shipping city/region or event location (`address` hints).
4. Confirm identity via the partner name + timing before trusting a match (common names collide).
5. Pivot: the partner name feeds people-search and social; the event date/city narrows other searches; the registry items themselves can corroborate a household.

## Inputs → Outputs
- **In:** `name` (registrant first + last; optionally partner name)
- **Out:** registry links revealing `associate` (partner/family), event date, and `address`/city hints
- **Empty/negative result looks like:** no registries — most people have none, and privacy settings or retailer opt-outs hide many; absence is expected and not informative. Common-name matches must be disambiguated.

## Gotchas & OpSec
- Coverage depends on the retailers it federates to; a registry on an unsupported store won't show.
- Registries are frequently set private or expire after the event — a past wedding may no longer be findable.
- US-centric.

## Overlaps ("do both")
- Pairs with general people-search (`[[truepeoplesearch]]`) and wedding-site/social searches — the registry gives the relationship + date, while people-search resolves the current address and the partner's identity.

## Trust & verifiability
`trust: unverified` — a third-party aggregator relaying retailer data; treat a hit as a strong lead (partner + event) but confirm identity and details against another source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | registry-finder |
| category | people-search |
| selectorsIn → selectorsOut | name → associate, name, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
