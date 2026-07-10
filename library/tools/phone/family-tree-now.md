---
id: family-tree-now
name: Family Tree Now
description: Use when you have a `phone`, `name` or `address` and want free US household and relative links — returns person records, addresses, ages and likely relatives/associates.
url: https://www.familytreenow.com/
category: phone
path:
- phone
bestFor: Free US people/genealogy search that maps a name/phone/address to addresses, ages and probable relatives.
selectorsIn:
- phone
- name
- address
selectorsOut:
- address
- associate
- name
- dob
status: live
pricing: free
costNote: Genuinely free — no paywall on core records (name/age, address history, relatives). No account needed to search.
opsec: passive
opsecNote: A data-broker/genealogy lookup — you query FamilyTreeNow, not the subject, and nobody is notified. Use a sock-puppet browser. FamilyTreeNow offers a record opt-out, so a missing person may be suppressed rather than absent.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A free US people-search/genealogy aggregator; strong for relative/household links but accuracy is uneven — inferred relatives and old addresses are common, so it's a lead source, not proof.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- FamilyTreeNow
- familytreenow.com
tags:
- people-search
- genealogy
- relatives
- data-broker
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Family Tree Now

> A free US people-and-genealogy search that's unusually generous with relatives and address history — a strong opening move for building a subject's household graph.

## When to use
You have a `name`, `phone`, or `address` for a US subject and want, for free, their address history, age, and — its standout feature — a list of likely relatives and household associates. Excellent early in a missing-person workflow to reconstruct the family/associate network and find living relatives to approach, without hitting a paywall.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.familytreenow.com/ in a sock-puppet browser.
2. Search by `name` (add city/state or age to narrow), or use the phone/address entry points.
3. Open the matching person record.
4. Read: current/prior `address`es, age/`dob`, and the **Possible Relatives / Associates** list (`associate`s) — the most valuable part.
5. Pivot: relatives feed the associate graph and their own searches; an address feeds property/voter records; a phone feeds `[[whitepages-reverse-phone]]`/`[[thats-them]]`.

## Inputs → Outputs
- **In:** `phone`, `name`, or `address`
- **Out:** `address` history, age/`dob`, and `associate`/relatives (its strength), plus name variants
- **Empty/negative result looks like:** no matching record or a bare entry — young, private, or opted-out subjects. FamilyTreeNow honors opt-outs, so absence can mean suppression, not non-existence.

## Gotchas & OpSec
- **"Relatives" are inferred** — the relative/associate list mixes true kin with co-residents and coincidental links; treat each as a lead to verify.
- Addresses can be stale; corroborate current location against a second source.
- OpSec: **passive** to the subject; use a sock puppet. (You may also want to opt yourself out — it exposes a lot.)

## Overlaps ("do both")
- Pairs with `[[thats-them]]`, `[[radaris-people-and-business-search-north-america]]`, and `[[peoplefinders-united-states]]` — FamilyTreeNow's relative graph complements the others' contact data; cross-check inferred relatives across brokers before trusting them.

## Trust & verifiability
`trust: unverified` — a free aggregator with no per-record provenance; its relative/address links are leads, not facts. Verify against authoritative records (property, voter, obituaries) before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | family-tree-now |
| category | phone |
| selectorsIn → selectorsOut | phone, name, address → address, associate, name, dob |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
