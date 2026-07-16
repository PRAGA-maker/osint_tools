---
id: us-phonebook
name: US Phonebook
url: https://www.usphonebook.com/
category: phone
path:
- phone
description: Use when you have a US `phone`, `name` or `address` and want the person behind it — returns owner `name`, `address`, relatives and phone type, free.
bestFor: Free US reverse phone lookup (and name/address search) returning owner name, address, relatives and line type.
selectorsIn:
- phone
- name
- address
selectorsOut:
- name
- address
- associate
status: live
pricing: free
costNote: Advertised as 100% free reverse phone/name/address lookups; the site monetises via ads and upsell links to paid background-check partners, but core lookups need no payment.
opsec: passive
opsecNote: A passive query against a consumer data-broker index; the subject is not notified. The site is ad-heavy with "is this you?" upsell traps — use a clean/sock-puppet browser and avoid the partner background-check funnels.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A popular free US reverse-lookup aggregator; data is broker-sourced and can be stale or conflate same-name people, so treat results as leads to confirm.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- USPhonebook
- usphonebook.com
tags:
- phone
- reverse-phone
- people-search
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- usphonebook
---

# US Phonebook

> A free US reverse-phone and people-search aggregator — enter a number, name or address and get the owner, their address, relatives and line type.

## When to use
You have a US `phone` (or a `name`/`address` to search forward) and want a free identification: owner name, current/associated address, listed relatives, and whether the line is mobile/landline. A good no-cost first pass on a US number before paying for a deeper report, and useful for turning a number into a name plus a household network to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.usphonebook.com/ and choose reverse-phone, name, or address search.
2. Enter the selector (10-digit number for reverse phone).
3. Read the result: owner name, address, phone type, and listed relatives/associates.
4. Ignore the paid "background check" upsell partners; the core lookup is free.
5. Pivot: an owner `name` feeds people/social search; relatives feed `associate` mapping; cross-check the name in `[[switchboard]]`/`[[spydialer-reverse-phone-lookup]]`.

## Inputs → Outputs
- **In:** `phone`, `name`, or `address`
- **Out:** owner `name`, `address`, `associate` (relatives), phone type
- **Empty/negative result looks like:** no owner / carrier-only data — common for privacy-registered, prepaid, VOIP, or newly-issued numbers. A blank name doesn't prove the number is unused, and same-name collisions require disambiguation.

## Gotchas & OpSec
- US-only, broker-sourced data — can be stale or conflate different same-name individuals; verify before acting.
- Heavy ads and upsell funnels to paid partners; stay on the free lookup.
- OpSec: passive toward the subject; use a clean browser and avoid entering your own data into "is this you?" prompts.

## Overlaps ("do both")
- Pairs with `[[spydialer-reverse-phone-lookup]]` and `[[ipqualityscore-com-2]]` — different brokers hold different records, and IPQS characterises the line (VOIP/active) before you trust an owner attribution.

## Trust & verifiability
`trust: community` — a widely-used free reverse-lookup with useful reach, but aggregated broker data of variable accuracy; corroborate any owner attribution against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-phonebook |
| category | phone |
| selectorsIn → selectorsOut | phone, name, address → name, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
