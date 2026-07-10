---
id: snoopstation
name: SnoopStation
description: Use when you have a `name` (+ US state) and want a public-records/background search — returns `address`, `phone`, `associate`, and `dob` leads, gated into a paid Intelius-style report.
url: http://snoopstation.com
category: people-search
path:
- people-search
bestFor: A name-based US public-records search front-end (Intelius-powered) that teases addresses, phones, and relatives.
selectorsIn:
- name
selectorsOut:
- address
- phone
- associate
- dob
status: live
pricing: freemium
costNote: Free to run a search and see teaser results, but the full report is a paid Intelius-powered background check — SnoopStation is effectively an affiliate front-end that funnels to a paywall/subscription.
opsec: passive
opsecNote: You search an aggregator's records, not the target — the subject isn't notified. But purchasing a report ties your identity/payment to the search, and the site is explicitly not FCRA-compliant (no use for employment/housing/credit decisions). Use a research payment method and a lawful purpose.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A thin front-end over Intelius data; the underlying records are the usual aggregated public/marketing data — often stale or conflated, so treat hits as leads.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- SnoopStation
tags:
- people-search
- background-check
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# SnoopStation

> A name-based US people-search front-end powered by Intelius — free to search and tease, paid to see the full background report.

## When to use
You have a `name` (ideally with a US state) and want a quick people-search pass that may surface addresses, phone numbers, relatives, and approximate age. Useful as one of several aggregator checks to triangulate a US subject — but know it's a paywall funnel, so use the free teaser to decide whether the paid report (or a different aggregator) is worth it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://snoopstation.com in a clean/sock-puppet browser.
2. Enter the `name` and select the US state; run the search.
3. Read the free teaser (partial `address`/`associate`/age hints).
4. Decide whether to buy the full Intelius-powered report or pivot to another source — cross-check before paying.
5. Pivot: take teaser `address`/`phone`/`associate` leads into free tools (`[[thats-them]]`, `[[thatsthem-phone-search]]`) and reverse lookups to confirm without the paywall.

## Inputs → Outputs
- **In:** `name` (+ US state)
- **Out:** `address`, `phone`, `associate` (relatives/known associates), `dob`/age — teased free, full detail paywalled
- **Empty/negative result looks like:** no matches or an empty teaser — common for people with little US public-records footprint, or name/state mismatches. Absence isn't conclusive; try other aggregators and spelling variants.

## Gotchas & OpSec
- **Paywall funnel:** the useful detail is behind a paid Intelius report — verify with free tools before paying.
- Data is aggregated and often stale/conflated (wrong relatives, old addresses) — corroborate.
- Explicitly non-FCRA — not for employment/housing/credit; use lawfully.

## Overlaps ("do both")
- Pairs with `[[thats-them]]`, `[[thatsthem-phone-search]]`, and other US aggregators — each holds different records, so cross-check teasers across several rather than buying one report blind.

## Trust & verifiability
`trust: community` — a commercial affiliate front-end over aggregated data. Treat every result as an unverified lead and confirm at a primary or independent source.
