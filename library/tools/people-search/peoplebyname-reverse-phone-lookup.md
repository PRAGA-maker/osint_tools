---
id: peoplebyname-reverse-phone-lookup
name: PeopleByName Reverse Phone Lookup
description: Use when you have a `phone` (or a `name`) and want the owner's name, address, age, and relatives for the US/Canada — returns contact and household details, free.
url: http://www.peoplebyname.com/search.php
category: people-search
path:
- people-search
bestFor: Free reverse phone lookup (US/Canada) that resolves a number to a name, address, age, and associated relatives — and vice versa by name.
selectorsIn:
- phone
- name
selectorsOut:
- name
- address
- associate
- dob
status: live
pricing: freemium
costNote: Core reverse-phone and name lookups are free; the site upsells deeper paid partner reports (background/full history), but you don't need to pay for the basic name/address result.
opsec: passive
opsecNote: A data-broker query that does not notify the number's owner. Data is aggregated from public records/directories and is not authoritative — verify before acting. Search from a clean browser; ignore paid upsell prompts unless needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established reverse-lookup provider (operating since 2008) with a large US/Canada record set; broker-sourced, so treat outputs as leads to confirm, not verified facts.
missingPersonsRelevance: high
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- PeopleByName
tags:
- toddington
- curated-directory
- people-search
- reverse-phone
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- peoplebyname-us
---

# PeopleByName Reverse Phone Lookup

> A free US/Canada reverse-phone (and name) directory: drop in a number to get the likely owner's name, address, age, and relatives — a fast way to turn a bare phone into a person.

## When to use
You have a `phone` number and need to know who it belongs to — name, current/prior address, approximate age, and associated relatives (`associate`s) — or you have a `name` and want their listed number/address. This is a quick enrichment step to attach identity to a phone, disambiguate a namesake by address/age, or open a relatives list to work outward from. Reach for it early in US/Canada locate work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.peoplebyname.com/search.php.
2. Enter the 10-digit `phone` in the reverse-phone box (or use the name search), and submit — no login.
3. Read the result: owner name, address (and history), age/DOB, and associated relatives.
4. Ignore the paid "full report" upsells unless you specifically need them — the basic name/address is on the free result.
5. Pivot: an `associate` becomes a new subject; the `address` feeds reverse-address tools; confirm the identity against another aggregator.

## Inputs → Outputs
- **In:** `phone` (or `name`)
- **Out:** `name`, `address` (+ history), `associate` (relatives), `dob` (age)
- **Empty/negative result looks like:** "no results" or a sparse record — broker coverage is uneven (unlisted/new/ported numbers often miss). Not proof; reverse the number on another service and cross-check.

## Gotchas & OpSec
- Human-in-the-loop: none for the free data; watch for upsell buttons routing to paid partner reports.
- Data is **broker-aggregated and non-authoritative** — stale addresses and merged records happen; verify before relying.
- OpSec: passive; the owner is not alerted.

## Overlaps ("do both")
- Pairs with `[[thatsthem-people-search]]` and other reverse-phone tools — each broker has different coverage, so triangulate a phone across several rather than trusting one.

## Trust & verifiability
`trust: community` — a long-running reverse-lookup provider with broad coverage, but the underlying data is commercial broker data; treat every field as a lead to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peoplebyname-reverse-phone-lookup |
| category | people-search |
| selectorsIn → selectorsOut | phone, name → name, address, associate, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
