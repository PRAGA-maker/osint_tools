---
id: thatsthem-people-search
name: ThatsThem People Search
description: Use when you have a `name` (or a phone/email/address to reverse) and want a US person's contact record — returns addresses, phones, emails, associates, and demographic hints, free.
url: https://thatsthem.com/people-search
category: people-search
path:
- people-search
bestFor: Free US people-search that reverses a name, phone, email, or address into contact and household details.
selectorsIn:
- name
- phone
- email
- address
selectorsOut:
- address
- phone
- email
- associate
- social-profile
- dob
status: live
pricing: freemium
costNote: Core name/phone/email/address lookups are free and unlimited; the site monetizes via ads and upsells to paid partner background reports for deeper data.
opsec: passive
opsecNote: A third-party data-broker query that does not notify the subject. It reflects aggregated broker data, not authoritative records — the site itself warns results need independent verification. Search from a clean browser; do not act on a single unconfirmed hit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, widely-used US people-search aggregator; data is broker-sourced and self-admittedly non-authoritative, so treat every field as a lead to confirm.
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
- ThatsThem
tags:
- people-search
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# ThatsThem People Search

> A free US people-search aggregator that runs in four directions — name, phone, email, or address — and returns a household contact record with associates and demographic hints.

## When to use
You have any one of a `name`, `phone`, `email`, or `address` and want to expand it into a fuller picture: current/prior addresses, phone numbers, email addresses, likely relatives/associates, and rough demographics (age, income band). Its free unlimited reverse lookups make it a fast first-pass enrichment step in a US locate case — especially to turn a single phone or email into a name and address, or to pull an associate list to work outward from.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://thatsthem.com/people-search.
2. Pick the search axis: name (+ optional city/state to narrow), or use the reverse tabs for phone, email, or address.
3. Enter the selector and submit — no login.
4. Read the result cards: addresses, phones, emails, associated people, and demographic estimates. Cross-reference multiple cards to pick the right individual.
5. Pivot: feed an `associate` back in as a new name; take a phone/email into other reverse tools; confirm the `address` against authoritative records.

## Inputs → Outputs
- **In:** `name` / `phone` / `email` / `address`
- **Out:** `address`, `phone`, `email`, `associate`, `social-profile`, `dob` (age band)
- **Empty/negative result looks like:** "no results" or a sparse card — broker coverage is patchy, so absence isn't proof; try a different axis (reverse the phone instead of the name) and other aggregators.

## Gotchas & OpSec
- Human-in-the-loop: none for the free data; watch for ad/upsell buttons that route to paid partner reports — the useful data is on the free page.
- Data is **broker-sourced and explicitly non-authoritative** (the site says so). Stale addresses and merged records are common — verify before acting.
- OpSec: passive; the subject is not alerted. Use a clean browser.

## Overlaps ("do both")
- Pairs with other US people-search aggregators (each broker has different coverage) and with reverse-phone/email tools — run several and triangulate, since no single aggregator is complete or fully current.

## Trust & verifiability
`trust: community` — a mainstream, long-established aggregator, but the underlying data is commercial broker data the site itself flags as needing verification; treat outputs as leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thatsthem-people-search |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, email, address → address, phone, email, associate, social-profile, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
