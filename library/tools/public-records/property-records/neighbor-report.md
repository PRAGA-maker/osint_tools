---
id: neighbor-report
name: Neighbor Report
description: Use when you have a `name`, `address` or `phone` and want a free US public-records aggregate — returns residents at an `address`, associated `phone`, and likely `associate` links plus neighborhood complaint posts.
url: https://neighbor.report/
category: public-records
path:
- public-records
- property-records
bestFor: Free reverse-address and reverse-phone lookup tying residents, numbers, and neighbors together across the US.
selectorsIn:
- name
- address
- phone
selectorsOut:
- address
- phone
- name
- associate
status: live
pricing: free
costNote: Free to browse and search; the site monetises via ads and "find more" hand-offs to paid people-search brokers — you never need to pay to see the base aggregate.
opsec: passive
opsecNote: Passive — it serves cached public-record aggregates and does not notify the person searched. It does log visitors like any site; use a sock-puppet browser/VPN for hygiene, and note the underlying data can be stale.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A US data-aggregator (BBB-listed) republishing public records; accuracy is uneven and entries can be outdated or conflate people with the same name.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- neighbor.report
tags:
- people-search
- reverse-address
- reverse-phone
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# Neighbor Report

> A free US people/address/phone aggregator (with a neighbor-complaint board bolted on) — a quick, no-login way to link a name to an address, a number, and the people around it.

## When to use
You have a US `name`, `address`, or `phone` and want a fast, free first pass before spending on a paid broker. It's most useful for **reverse-address** ("who lives / has lived here, and who are the neighbors") and **reverse-phone** ("who is behind this number") pivots, and for the occasional neighborhood complaint post that names a resident.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://neighbor.report/ in a sock-puppet browser.
2. Choose the lookup: name search, phone lookup, or address search (or browse the state/city directory at `/d/`).
3. Enter the selector and read the aggregate card: residents/associated names, phone(s), address history, and any neighbor-posted reports.
4. Treat "unlock full report / background check" buttons as ads — they hand off to paid brokers; the free card already shows the useful links.
5. Pivot: a co-resident name feeds `associate` mapping; a surfaced phone feeds carrier/phone OSINT; an address feeds property-record and voter tools.

## Inputs → Outputs
- **In:** `name`, `address`, or `phone`
- **Out:** residents at an `address`, associated `phone` numbers, other `name`s at that address (likely `associate`s), address history
- **Empty/negative result looks like:** a sparse page with "no records found" or a generic city page with no person data — the number/address isn't in their scrape, or it's too new.

## Gotchas & OpSec
- **Accuracy is uneven**: same-name people get conflated and records lag reality by months to years — corroborate every hit against a second source.
- The site pushes paid background-check upsells; nothing behind them is required to get the base aggregate.
- The neighbor-complaint posts are unverified user content — treat named accusations as leads, not fact.

## Overlaps ("do both")
- Pairs with other free US people aggregators and with property/voter records — cross-run the same name/address to separate a real match from a same-name collision.

## Trust & verifiability
`trust: unverified` — a commercial republisher of public records; a hit is a lead to verify against an authoritative source (county property, voter file), not proof on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | neighbor-report |
| category | public-records |
| selectorsIn → selectorsOut | name, address, phone → address, phone, name, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
