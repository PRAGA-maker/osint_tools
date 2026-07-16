---
id: yellowpages-people
name: YellowPages People
description: Use when you have a US `name` or `phone` and want a free directory match — returns name, phone and address, useful for reverse-phone confirmation.
url: https://people.yellowpages.com/
category: phone
path:
- phone
bestFor: Free US people/reverse-phone directory lookup to confirm a name↔phone↔address triangle.
selectorsIn:
- name
- phone
selectorsOut:
- name
- phone
- address
status: live
pricing: free
costNote: Free directory lookups; no account needed. Data draws on public/whitepages-style directory listings.
opsec: passive
opsecNote: Passive directory lookup; the subject is not notified. A data-broker/directory site, so it may show CAPTCHAs or push paid "background report" upsells — stay on the free listing data and treat results as leads.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free directory backed by whitepages-style listing data; coverage skews to landlines/older records and can be stale or partial.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- YellowPages People Search
- people.yellowpages.com
tags:
- phone
- directory
- people-search
- reverse-phone
source: inteltechniques-tools
lastVerified: '2026-07-16'
enrichment: full
---

# YellowPages People

> A free US people and reverse-phone directory: enter a name or phone number and get matching listing data — name, number, and address.

## When to use
A quick, free corroboration tool for US subjects. You have a `name` and want a listed `phone`/`address`, or you have a `phone` and want to know whose it is (reverse lookup). Best used to confirm the name↔phone↔address triangle from directory data before spending effort on paid brokers, or to add an address/number to a thin profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://people.yellowpages.com/.
2. Search by person name (with city/state to narrow) or enter a phone number for reverse lookup.
3. Read the listing: associated name, phone, and address.
4. Pivot: an address → reverse-address people-search (`[[fastpeoplesearch-com-reverse-address]]`); a confirmed number → messaging-app/carrier lookups; corroborate the pairing against another broker.

## Inputs → Outputs
- **In:** `name` or `phone`
- **Out:** directory `name`, `phone`, and `address` matches.
- **Empty/negative result looks like:** no listing / only paid-report prompts — the number is a mobile/unlisted line or the person isn't in directory data; try a dedicated people-search or caller-ID tool.

## Gotchas & OpSec
- Directory data favors landlines and older/listed records; many mobiles and younger subjects won't appear.
- Expect upsell prompts to paid "background reports" — the free listing is the useful part; ignore the rest.
- Results can be stale or partial; confirm against a second source before relying on them.
- US-only.

## Overlaps ("do both")
- Pairs with `[[fastpeoplesearch-com-reverse-address]]` and reverse-phone/caller-ID tools — cross-run to confirm, since directory and broker datasets differ in what they cover.

## Trust & verifiability
`trust: community` — a free directory aggregator; useful as a lead and cross-check, not authoritative — verify the name/number/address pairing elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yellowpages-people |
| category | phone |
| selectorsIn → selectorsOut | name, phone → name, phone, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
