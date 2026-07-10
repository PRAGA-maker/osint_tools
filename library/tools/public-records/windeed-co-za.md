---
id: windeed-co-za
name: windeed.co.za
description: Use when you have a `name` or ID/registration number in South Africa and want official property, deeds, company, and directorship records — returns `address` (property ownership), `employer-org` (CIPC directorships), `associate`, `name`.
url: https://beta.windeed.co.za/company
category: public-records
path:
- public-records
bestFor: Authoritative South African deeds-office, property-ownership, and CIPC company/director searches on a person or company.
selectorsIn:
- name
- document-id
- employer-org
selectorsOut:
- address
- employer-org
- associate
- name
status: live
pricing: freemium
costNote: Registration is free with no subscription or monthly fee, but every search is paid via prepaid "search vouchers" — there is no free-search tier, so you must buy credit before any result is returned.
opsec: passive
opsecNote: Requires a registered, paid account tied to your identity and payment method, so all searches are attributable to you — use a dedicated research account. The searches query official registries, not the target, so nothing is leaked to the subject; but Lexis/WinDeed retains an audit trail of who searched what.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by LexisNexis South Africa (Lexis WinDeed); pulls from official Deeds Office and CIPC registries, making results authoritative.
missingPersonsRelevance: high
coverage:
- za
auth: account
api: false
localInstall: false
registration: true
aliases:
- Lexis WinDeed
- WinDeed
tags:
- companysites
- Company Related Sites
- deeds-office
- property-records
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# windeed.co.za

> LexisNexis's South African search platform — pay-per-search access to official Deeds Office property ownership and CIPC company/director records on a person or company.

## When to use
You have a South African subject — a `name`, an ID/registration number (`document-id`), or a company (`employer-org`) — and you need authoritative ownership and corporate links: what property they own (with `address`), what companies they direct, and who the co-directors are. Strong for asset/association mapping and confirming identity via official registries in South Africa.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free (research) Lexis WinDeed account at windeed.co.za and buy a prepaid search voucher.
2. Log in and pick the search type: Deeds Office Person/Property, Company, or Director search.
3. Enter the `name`, ID/registration number, or company name across one of the 11 Deeds Offices / CIPC as prompted.
4. Spend voucher credit to run the search and read results.
5. Read out property `address`es, co-owners/co-directors (`associate`), and `employer-org` links; pivot ID numbers and company names into further WinDeed or CIPC lookups.

## Inputs → Outputs
- **In:** `name`, `document-id` (SA ID / company registration no.), or `employer-org`
- **Out:** `address` (property ownership), `employer-org` (CIPC directorships), `associate` (co-owners/co-directors), confirmed `name`
- **Empty/negative result looks like:** a paid search that returns no registered property/directorship for the identifier — meaning nothing on record under those exact details (verify spelling/ID before concluding absence). You still spend voucher credit on empty searches.

## Gotchas & OpSec
- **No free-search tier:** you pay per query via vouchers even for nil results — budget before searching.
- South Africa-only registries.
- Account and payment are attributable; LexisNexis keeps a searched-by audit trail — use a dedicated research identity and stay within a lawful basis (POPIA applies).
- The `beta.` and main `windeed.co.za` / `search.windeed.co.za` hosts front the same service.

## Overlaps ("do both")
- Pairs with CIPC direct company lookups and SA people-search tools — WinDeed is authoritative and paid, so use free sources first to scope the target, then spend a voucher to confirm property/directorships here.

## Trust & verifiability
`trust: trusted` — a LexisNexis South Africa product sourcing official Deeds Office and CIPC data. Results are authoritative registry extracts; the main caveat is cost, not accuracy.
