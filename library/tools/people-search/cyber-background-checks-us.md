---
id: cyber-background-checks-us
name: Cyber Background Checks (US)
description: Use when you have a US `name` (or `phone`/`email`/`address`) and want a free people-search preview — returns `address`, `phone`, `email`, `associate`, `dob`, and `name`.
url: https://www.cyberbackgroundchecks.com/
category: people-search
path:
- people-search
bestFor: Free preview of a US person's current/past addresses, phones, emails, and relatives from aggregated public records.
selectorsIn:
- name
selectorsOut:
- address
- phone
- email
- associate
- dob
- name
status: live
pricing: freemium
costNote: The preview (current/past addresses, phones, relatives, aliases) is free to view. Detailed criminal/property/employment reports are handed off to paid partner services behind a paywall.
opsec: passive
opsecNote: A data-broker aggregator — searching is passive and the subject is not notified. The flip side is your own privacy: consider whether you want your searches/associations logged, and use appropriate separation for sensitive work. (These sites also honor opt-outs, which is why some records are missing.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial people-search/referral site (est. 2019) aggregating ~1B records from 2000+ sources; free tier is a preview, and data can be stale or conflate same-name individuals.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- CyberBackgroundChecks
- cyberbackgroundchecks.com
tags:
- people-search
- data-broker
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Cyber Background Checks (US)

> A free-preview US people-search aggregator — one name returns current/past addresses, phones, emails, and relatives, with deeper reports pushed to paid partners.

## When to use
You have a US subject and a `name` (or a `phone`/`email`/`address` to reverse) and want a quick, free read on their addresses, contact numbers, likely emails, and relatives — the kind of triage that gives you fresh selectors and relationship leads to chase. Its free tier is more generous than many brokers, making it a solid first stop before cross-checking against other sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.cyberbackgroundchecks.com/ and choose search by name (or reverse phone/email/address).
2. Enter the `name` with a state/city to disambiguate.
3. Read the free preview: current and previous `address`es, landline/cell `phone`s, `email`s, aliases, relatives/associates (`associate`), and approximate age (`dob`).
4. Ignore the upsell to paid criminal/property reports unless you specifically need them; carry the free leads elsewhere.
5. Pivot: relatives and prior cities feed other people-search and voter/property records; phones/emails feed reverse lookups and breach checks.

## Inputs → Outputs
- **In:** `name` (or `phone`/`email`/`address` to reverse)
- **Out:** `address` (current/past), `phone`, `email`, `associate` (relatives), age (`dob`), aliases (`name`)
- **Empty/negative result looks like:** no match, a same-name jumble, or a suppressed record (opt-outs) — broker data lags real moves and conflates common names. Every field is an unverified lead until corroborated.

## Gotchas & OpSec
- Free tier is a *preview*; "background check" branding oversells it — criminal/property depth is paywalled via partners.
- Data staleness and same-name conflation are the main failure modes; disambiguate by age + location.
- US-only.

## Overlaps ("do both")
- Pairs with `[[truepeoplesearch]]`, `[[fastpeoplesearch]]`, `[[thatsthem]]`, and `[[addresses-com]]` — run the same query across several free brokers; agreement across independent aggregators raises confidence in an address or relative.

## Trust & verifiability
`trust: unverified` — commercial aggregator; use it to generate leads (addresses, relatives, phones) and confirm them against authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyber-background-checks-us |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, email, associate, dob, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
