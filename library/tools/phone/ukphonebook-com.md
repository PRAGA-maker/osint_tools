---
id: ukphonebook-com
name: ukphonebook.com
description: Use when you have a UK `phone`, `name` or partial `address` and want the matching listing — returns name, current/previous address, other occupants and linked connections.
url: https://www.ukphonebook.com/
category: phone
path:
- phone
bestFor: Resolving a UK landline/name to an address (and co-occupants) using directory, PAF, electoral-roll and Companies House data.
selectorsIn:
- phone
- name
- address
selectorsOut:
- name
- address
- associate
- phone
status: live
pricing: freemium
costNote: 5 free searches/day returning limited detail; full records cost credits (~£10 for 40 credits, ~£30 for 100). A full record unlock is ~4 credits.
opsec: passive
opsecNote: This is a records lookup against aggregated directory/electoral data; the subject is not notified. Register and pay (if buying credits) under a research identity, since the account ties queries to you.
humanInLoop: true
humanInLoopReason:
- rate-limit
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running UK directory aggregator sourcing from directory enquiries, Royal Mail PAF, the UK Electoral Roll and Companies House. Data can be stale or opt-out-suppressed; corroborate.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- epieos
aliases:
- UK Phone Book
- ukphonebook electoral roll
tags:
- mobilephone
- Mobile & Phone Related
- uk
- reverse-lookup
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ukphonebook.com

> The UK's long-standing online phone/electoral-roll directory: resolve a UK number or name to an address, co-occupants and linked people.

## When to use
You are working a UK subject and have a `phone` (landline), a `name`, or a partial `address`/postcode and want to fill in the rest — current and previous `address`, the other occupants at that address (`associate` links), and listed `phone` numbers. Strong for confirming that a name maps to a specific UK household and for building a family/co-resident graph.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ukphonebook.com/ and pick the relevant search: reverse phone, find-a-person, residential directory, or electoral-roll search.
2. Enter what you have — a UK number for reverse lookup, or a `name` plus a location (city/town/postcode, even partial).
3. Read the free result: a limited listing (name + rough location). You get 5 free searches per day.
4. To see the full record (all listed numbers, current/previous addresses, other occupants, potential connections) unlock it with credits.
5. Pivot: feed a confirmed `address` into mapping/property tools; feed co-occupant names back in as new `name` searches to expand the household graph.

## Inputs → Outputs
- **In:** `phone`, `name`, or partial `address`
- **Out:** `name`, current/previous `address`, `associate` (other occupants / linked connections), listed `phone`
- **Empty/negative result looks like:** "no results" or a listing with no address detail. UK numbers/addresses can be ex-directory or electoral-roll opt-out, so absence is not proof the person doesn't live there.

## Gotchas & OpSec
- Human-in-the-loop: free tier is capped at 5 searches/day and shows only partial data; full records require buying credits (partial pay-wall).
- Coverage is UK-only and skews to landlines and electoral-roll-listed adults; mobiles and opt-outs are often missing.
- Data can lag reality by months to years — treat a hit as a lead and date-check it.
- OpSec: passive; the subject is not alerted. If you register to buy credits, use a research identity.

## Overlaps ("do both")
- Pairs with `[[epieos]]` — Epieos works the online/account side of a person while ukphonebook works the offline UK directory/electoral side; together they cross-confirm identity.

## Trust & verifiability
`trust: community` — an established commercial UK aggregator drawing on authoritative sources (PAF, Electoral Roll, Companies House), but the compiled data can be stale or suppressed, so verify any address before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukphonebook-com |
</content>
