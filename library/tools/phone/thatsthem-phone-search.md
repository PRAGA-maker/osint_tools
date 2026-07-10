---
id: thatsthem-phone-search
name: ThatsThem Phone Search
description: Use when you have a US `phone` number and want the owner's name, address, and linked details — returns `name`, `address`, `email`, `social-profile`, `associate`.
url: https://thatsthem.com/reverse-phone-lookup
category: phone
path:
- phone
bestFor: Free US reverse-phone lookup that resolves a number to a name, address, carrier, and linked email.
selectorsIn:
- phone
selectorsOut:
- name
- address
- email
- social-profile
status: live
pricing: freemium
costNote: Core reverse-phone results (name, city/state, carrier) are shown free with no login; fuller address/email/associate detail and bulk/API use are gated behind paid tiers.
opsec: passive
opsecNote: You query ThatsThem's own aggregated database, not the target's devices or accounts, so nothing reaches the subject. Still run from a clean/sock-puppet browser — ThatsThem logs searches and may profile your IP for ad/data purposes.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established free US data aggregator; data comes from marketing/public-record compilations that are often stale or partially wrong, so treat hits as leads.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- ThatsThem reverse phone
tags:
- phone
- reverse-phone-lookup
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# ThatsThem Phone Search

> A free US reverse-phone lookup that turns a number into a name, address, carrier, and linked email/social leads.

## When to use
You have a US `phone` number and want to identify who it belongs to and where they are — a starting point to attach a name and address to a number, or to corroborate a number you already tie to a subject. Strong early-stage tool because the core result costs nothing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://thatsthem.com/reverse-phone-lookup in a clean/sock-puppet browser.
2. Enter the `phone` number in E.164 or plain US format and submit.
3. Read the free result: owner `name`, city/state, line type/carrier, and any linked `email`.
4. For deeper `address`/`associate` links, follow into ThatsThem's other free lookups (name, email) rather than paying if you can pivot laterally.
5. Pivot: take the returned `name`/`address` into `[[thats-them]]` name search or a people-search tool; take a linked `email` into email OSINT.

## Inputs → Outputs
- **In:** `phone` (US number)
- **Out:** `name`, `address`, `email`, `social-profile`, carrier/line type, `associate` leads
- **Empty/negative result looks like:** "no results" for that number — common for mobiles, VoIP, or recently ported numbers. Absence is not proof the number is invalid; try `[[thats-them]]` and carrier lookups too.

## Gotchas & OpSec
- Data is aggregated from marketing and public-record sources — often out of date; verify the name/address independently.
- US-focused; little value for non-US numbers.
- Passive toward the target; ThatsThem itself logs and profiles searchers.

## Overlaps ("do both")
- Pairs with `[[thats-them]]` (same provider, other selectors) and other reverse-phone tools — each aggregator holds different records, so run several to cross-confirm.

## Trust & verifiability
`trust: community` — a free commercial aggregator. Reliable enough to generate leads, but never treat a single unverified name/address as fact.
