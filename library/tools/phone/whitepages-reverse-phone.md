---
id: whitepages-reverse-phone
name: Whitepages Reverse Phone
description: Use when you have a US `phone` number and want to attribute an owner and address — returns owner name, city/address, line type and related contacts (full detail behind a paywall).
url: https://www.whitepages.com/reverse-phone
category: phone
path:
- phone
bestFor: US reverse-phone attribution — owner name and location from a landline, cell or business number.
selectorsIn:
- phone
- name
selectorsOut:
- name
- address
- associate
- phone
status: live
pricing: freemium
costNote: Free layer returns owner name and city for many landlines/business numbers; full address, relatives, and reliable mobile-number attribution require a paid Premium plan (~$5.99/mo and up). Trials often convert to recurring charges.
opsec: passive
opsecNote: The lookup runs against a commercial data broker, never the target — no alert reaches the subject. You do disclose the number (and your session/IP, or account if you subscribe) to Whitepages. Use a sock-puppet browser; avoid paying with an identity-linked card if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established US data broker (Whitepages) aggregating public records and phone directories; broad coverage but attribution can be stale or wrong, especially for reassigned mobile numbers.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- whitepages.com reverse phone
- Whitepages
tags:
- reverse-phone
- data-broker
- people-search
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Whitepages Reverse Phone

> The classic US reverse-phone directory: drop in a number, get a probable owner and location — with the good detail behind a subscription.

## When to use
You have a US `phone` number and need to know who it belongs to and roughly where they are — triaging a number from a missing person's contacts, a caller ID, a listing, or a message. Whitepages has some of the deepest US landline/business coverage, so it is a strong first stop for fixed-line and business numbers; mobiles usually need the paid tier.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.whitepages.com/reverse-phone in a sock-puppet browser.
2. Enter the `phone` number (US format) and search. (The site also supports name→phone/address; swap tabs if you have a `name` instead.)
3. Read the free layer: owner `name`, city, line type (landline/mobile/VoIP), carrier, and sometimes an approximate `address`.
4. Decide on Premium: full street `address`, `associate`/relatives, and dependable mobile attribution are paywalled. Only subscribe if the free teaser looks on-target — and watch for trial-to-recurring conversion.
5. Pivot: an owner name feeds a people-search (`[[radaris-people-and-business-search-north-america]]`); an address feeds property/voter records; relatives seed the associate graph.

## Inputs → Outputs
- **In:** `phone` (or `name` in reverse)
- **Out:** owner `name`, city/`address`, line type + carrier, `associate`/relatives (paywalled), linked `phone` numbers
- **Empty/negative result looks like:** "No results" or only a carrier/line-type with no name — common for prepaid, recently ported, or VoIP numbers. Absence is not proof the number is inactive.

## Gotchas & OpSec
- Human-in-the-loop: a partial paywall gates the useful detail; the free layer is intentionally thin for mobiles.
- Data can be stale — numbers get reassigned, so verify a hit against a second source before acting on it.
- OpSec: **passive** to the subject; but subscribing ties the search to your payment identity. Prefer the free layer plus cross-checks over paying with a real card.

## Overlaps ("do both")
- Pairs with `[[radaris-people-and-business-search-north-america]]` and `[[cell-revealer-telephone-number-lookup]]` — different brokers hold different phone records, so a number blank on Whitepages may resolve elsewhere. Cross-check the returned name across at least two before trusting it.

## Trust & verifiability
`trust: community` — a reputable, long-running US broker, but its output is aggregated public-record data with no per-record provenance; treat every attribution as a lead to corroborate, not a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whitepages-reverse-phone |
| category | phone |
| selectorsIn → selectorsOut | phone, name → name, address, associate, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
