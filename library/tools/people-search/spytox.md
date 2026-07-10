---
id: spytox
name: SpyTox
description: Use when you have a `name`, `phone` or `address` in the US and want a free reverse-lookup — returns `address`, `phone`, age and relatives (`associate`).
url: https://www.spytox.com/
category: people-search
path:
- people-search
bestFor: Free US people-search and reverse phone/address lookup returning current/prior addresses, phone numbers, approximate age, and relatives.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- associate
status: live
pricing: freemium
costNote: Core name/phone/address lookups are free; some deeper details push toward paid partner reports. No account needed for basic search.
opsec: passive
opsecNote: A public-records aggregator search; the subject is not notified. You disclose the query to a commercial data broker that may log it — use a puppet browser/IP for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial US people-search aggregator drawing on public records and marketing data; records are frequently stale or conflate namesakes, so verify before relying.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- spytox.com
tags:
- people-search
- us-records
- reverse-lookup
- relatives
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# SpyTox

> A free US people-search aggregator: put in a name, phone, or address and get back addresses, phone numbers, age, and relatives.

## When to use
You have a US-based `name` (or a `phone`/`address` to reverse) and want a quick, free read of associated addresses, phones, approximate age, and family/relatives. Relatives are the high-value output — they open `associate` pivots and help disambiguate a common name. Reach for it as one of several free people-search aggregators to triangulate, since any single one is patchy.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.spytox.com/ in a clean/puppet browser.
2. Pick the search type — by name, reverse phone, or reverse address — and enter the selector.
3. Read the free result: current/prior `address`es, `phone` numbers, approximate age, and listed relatives (`associate`).
4. Note where it nudges to a paid partner report; the free fields are usually enough for leads.
5. Pivot: relatives → build a family graph and locate the subject through them; address → property/voter records; phone → carrier/other reverse tools.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address` (US)
- **Out:** `address` (current/prior), `phone`, `associate` (relatives), approximate age
- **Empty/negative result looks like:** "no results" or a sparse card — the person may have a thin US public-records footprint, be younger/renting, or the name is too common/misspelled. Aggregators disagree, so a miss here isn't definitive; try another (`[[peoplesearchnow]]`).

## Gotchas & OpSec
- **Stale / conflated data:** these brokers mix records and namesakes; treat everything as a lead and cross-verify with a second source before attributing.
- Free tier funnels toward paid reports — the free fields are the useful, non-committal part.
- US-only coverage.
- OpSec: **passive** — no subject notification; a data broker logs your query.

## Overlaps ("do both")
- Pairs with `[[peoplesearchnow]]`, TruePeopleSearch, FastPeopleSearch and similar — run several free aggregators and reconcile; each has different records.

## Trust & verifiability
`trust: community` — a commercial aggregator with the usual staleness/namesake risks. Confirm addresses/relatives against a second people-search or primary records before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spytox |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
