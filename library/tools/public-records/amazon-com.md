---
id: amazon-com
name: Amazon Registry Search
description: Use when you have a `name` and want to find a person's public Amazon wedding/baby registry — returns the registrant `name`, an approximate city/state `address` and their listed items.
url: https://www.amazon.com/gp/registry/search
category: public-records
path:
- public-records
bestFor: Locating a person's public Amazon wedding/baby gift registry by name to confirm identity, location and life events.
selectorsIn:
- name
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Free; no Amazon account required to search public gift registries.
opsec: passive
opsecNote: Searching public registries is passive and anonymous to the target. Do NOT purchase items or contact the registrant — that reveals you and is intrusive. Registries are self-published, so treat the data as volunteered public info.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Amazon's own first-party registry search; the data is exactly what registrants chose to make public, so it is authentic but self-reported.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- amazon-registry-search
- amazon-pay
- amazon-rekognition
- amazon-sns
- aws-public-datasets
- us-east-1-console-aws-amazon-com
aliases:
- Amazon.com registry search
- Amazon wedding/baby registry finder
tags:
- registry
- amazon
- wishlist
source: metaosint
lastVerified: '2026-07-21'
enrichment: full
---

# Amazon Registry Search

> Amazon's public gift-registry finder — search a name and pull the wedding/baby registries people intentionally made discoverable, exposing name, rough location and life-event timing.

## When to use
You have a `name` and want to confirm identity, place a person in a city/state, or corroborate a life event (an upcoming wedding, a new baby). Public wedding and baby registries are designed to be found by name, and they typically show the registrant's name, an approximate city/state, an event date, and a wishlist — all volunteered by the subject. Useful for narrowing which "John Smith" you have and building a life-timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.amazon.com/gp/registry/search (or the Wedding / Baby Registry "Find a Registry" pages).
2. Enter the person's first and last `name`.
3. Use the **city/state filter** to disambiguate common names — this is essential given how many people share a name.
4. Read the results: registrant name, city/state, event date, and the registry's item list.
5. Pivot: the city/state narrows geolocation and corroborates residence; the event date builds a timeline; a co-registrant name surfaces a spouse/partner `associate`.

## Inputs → Outputs
- **In:** `name` (+ optional city/state filter)
- **Out:** registrant `name`, approximate `address` (city/state), event date, and wishlist items
- **Empty/negative result looks like:** no registry found — the person never made one, kept it private, or it's a **personal wishlist** (Amazon no longer lets you search personal wishlists by name; only wedding/baby registries remain searchable). Absence proves nothing about the person.

## Gotchas & OpSec
- **Only wedding/baby registries are searchable now** — Amazon removed public personal-wishlist and email search, so this is narrower than older guides claim.
- Location is self-entered city/state, not a street address; treat it as a region, not a home.
- OpSec: **passive** — never buy an item or message the registrant; that unmasks you.

## Overlaps ("do both")
- Pairs with general people-search and social-profile tools — the registry gives a confirmed name + city + partner + timing that those tools can then expand into full identity and contact detail.

## Trust & verifiability
`trust: trusted` — first-party Amazon data showing exactly what the registrant published. Authentic but self-reported, so verify identity against an independent source before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-com |
| category | public-records |
| selectorsIn → selectorsOut | name → name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
