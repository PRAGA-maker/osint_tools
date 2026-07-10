---
id: switchboard
name: Switchboard
url: http://www.switchboard.com
category: people-search
path:
- people-search
description: Use when you have a US `name` (or phone/address) and want a white-pages record — returns `address`, `phone` and relatives; now resolves to the Whitepages directory.
bestFor: A quick US white-pages lookup by name, phone or address that surfaces current address, landline and household relatives.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- associate
- name
status: live
pricing: freemium
costNote: Free to see basic listing matches (name, city, partial address/phone); full reports, historical addresses and relatives are behind Whitepages' paid tier.
opsec: passive
opsecNote: A passive query against a consumer data-broker index; the subject is not notified. The site profiles you as a visitor (ads/tracking) but reveals nothing to the target. Use a clean browser and expect upsell funnels.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing US directory brand that now redirects to Whitepages; data is aggregated broker records, so treat matches as leads and confirm current address/phone elsewhere.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- switchboard.com
- Switchboard White Pages
tags:
- people-search
- white-pages
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Switchboard

> A classic US white-pages brand (now served by Whitepages) — enter a name, phone or address and get a current address, landline and household relatives.

## When to use
You have a US `name` (optionally a city, or a `phone`/`address` to reverse) and want a fast directory-grade record: current/associated address, listed phone, and other people at the household. Good as an early, free-ish corroboration step for a US subject before spending on a full people-search report.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open switchboard.com (it resolves to the Whitepages directory).
2. Choose the search type — person by name, reverse phone, or reverse address — and enter the selector, narrowing by state/city for common names.
3. Read the free preview: matched name(s), approximate address, partial phone, and listed relatives/associates.
4. Decide whether the paid full report (history, full numbers) is worth it, or pivot the free leads elsewhere.
5. Pivot: an `address` feeds property/electoral records and `[[411-ca]]`-style directories (for cross-border), relatives feed `associate` mapping.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address`
- **Out:** `address`, `phone`, `associate` (household/relatives), confirmed `name`
- **Empty/negative result looks like:** no listing or only unrelated same-name records — common for people who are unlisted, mobile-only, or young. Absence here does not mean the person doesn't exist; landline directories skew older.

## Gotchas & OpSec
- Data is broker-aggregated and can be stale or conflated between same-name individuals; confirm before acting.
- The valuable detail (history, full numbers, all relatives) is paywalled via Whitepages.
- OpSec: passive to the subject; just avoid the "is this you?" upsell traps and use a clean browser.

## Overlaps ("do both")
- Pairs with `[[411-ca]]` (Canada) and other national directories, and with `[[melissa-com]]` for verified US contact data — different brokers hold different records.

## Trust & verifiability
`trust: community` — a reputable directory brand backed by Whitepages data, but aggregated broker records carry conflation/staleness risk, so treat any single match as a lead to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | switchboard |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
