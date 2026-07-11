---
id: truepeoplesearch
name: TruePeopleSearch
description: Use when you have a US `name`, `phone`, or `address` and want current/past addresses, phone numbers, and relatives — returns address, phone, associate, and approximate dob.
url: https://www.truepeoplesearch.com/
category: people-search
path:
- people-search
bestFor: Free US person lookup that ties a name to address history, phones, and a relatives/associates web.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- associate
- dob
status: live
pricing: freemium
costNote: Core search and the main results (addresses, phones, relatives) are genuinely free. Some "full report"/background-check links hand off to paid third-party partners — you don't need those for the core data.
opsec: passive
opsecNote: Searching does not notify the subject. It is a data-broker aggregator, so treat results as leads, not proof, and be aware your own record is likely in it (an opt-out exists). Use a clean/sock-puppet browser; expect a bot-check.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A widely-used free US people-aggregator. Data is compiled from public records and commercial sources; coverage is strong but includes stale addresses and occasional wrong relative/associate links.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- True People Search
- TPS
tags:
- people-search
- data-broker
- reverse-phone
- reverse-address
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# TruePeopleSearch

> A free US people-search aggregator: name, phone, or address in — address history, phone numbers, age, and a relatives/associates network out.

## When to use
You have a US-based subject and one of `name` (ideally with a city/state), a `phone`, or an `address`, and you want to build out their footprint: where they've lived, what numbers trace to them, roughly how old they are, and who their relatives/associates are. One of the strongest free first-pass tools for US persons and a fast way to generate `associate` leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open truepeoplesearch.com in a clean browser (solve the bot-check if prompted).
2. Choose a search mode — Name (add city/state to narrow), Reverse Phone, or Reverse Address.
3. Enter the selector and open the best-matching person card.
4. Read: current & prior `address`es, associated `phone` numbers, approximate age/`dob` (often month/year), and listed relatives/`associate`s.
5. Pivot: each relative is a new subject; a prior address anchors a timeline; a phone feeds carrier/messaging-app checks.

## Inputs → Outputs
- **In:** `name` (+ city/state), `phone`, or `address`
- **Out:** current/historical `address`es, `phone` numbers, approximate `dob`/age, relatives & `associate`s, sometimes emails
- **Empty/negative result looks like:** no match or a thin card with no relatives/phones — common for young people, recent movers, those with common names (too many matches), or people who opted out. Absence isn't proof; try phone/address modes.

## Gotchas & OpSec
- Human-in-the-loop: a Cloudflare/bot-check (sometimes a CAPTCHA) frequently gates access — solve it manually.
- Data quality: aggregated public/commercial data. Old addresses and mistaken "relatives" appear; corroborate before asserting a link.
- OpSec: passive to the subject; but it's a broker — your queries aren't sent to them, yet the data itself is broker-sourced. Sock-puppet browser advised.

## Overlaps ("do both")
- Pairs with other free US aggregators (FastPeopleSearch, that-name-search family) — they share upstream data but each surfaces cards the others miss; cross-run a stubborn name. Feed phones into reverse-phone/messaging-app tools and relatives back into this same search.

## Trust & verifiability
`trust: community` — a popular free aggregator, not an authoritative record. Excellent for leads and network-building; verify any specific address/relationship against a second source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | truepeoplesearch |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
