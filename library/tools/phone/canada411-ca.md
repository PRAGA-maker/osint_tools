---
id: canada411-ca
name: canada411.ca
description: Use when you have a Canadian phone number and need the listed subscriber's name and address via Canada411 reverse phone search.
url: https://www.canada411.ca/search/reverse.html
category: phone
path:
- phone
bestFor: Canadian reverse phone lookup — number to listed name and address.
selectorsIn:
- phone
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Free directory search; ad-supported (operated by Yellow Pages Canada).
opsec: passive
opsecNote: Queries published Canadian directory listings; does not contact the subscriber.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Canada411 is Canada's main online phone directory, operated by Yellow Pages (YP) Canada, sourcing listings from Bell, Telus, MTS and other carriers.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Canada411
- canada411.ca
tags:
- mobilephone
- Mobile & Phone Related
- canada
- reverse-lookup
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# canada411.ca (reverse phone)

> Canada's main online phone directory — enter a Canadian number to get the listed subscriber's name and address.

## When to use
You have a Canadian `phone` number and need to identify the subscriber: their `name` and `address`. First stop for Canadian number identification in missing-persons work. You can search the full 10 digits for a specific listing, or the last 7 digits to see all listings containing that fragment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.canada411.ca/search/reverse.html.
2. Enter the Canadian `phone` number (10 digits for a specific match; last 7 for a broader fragment search). Solve any captcha.
3. Read the result: subscriber `name` and `address` for listed numbers.
4. Pivot: take the name/address into the address search (`[[canada411-ca-2]]`) to find co-residents, or into people-search/social tools.

## Inputs → Outputs
- **In:** `phone` (Canadian)
- **Out:** `name`, `address`
- **Empty/negative result looks like:** "no listings found." Mobile and unlisted numbers usually won't resolve — absence is not proof the number is invalid.

## Gotchas & OpSec
- Human-in-the-loop: occasional captcha on repeated lookups.
- Listed landlines dominate; many mobiles and ex-directory numbers are absent.
- Canada only.
- OpSec: passive; published-directory query with no contact to the subscriber.

## Overlaps ("do both")
- Pairs with `[[canada411-ca-2]]` (reverse address → residents at a location) — run the phone lookup, then expand the address to find associates.

## Trust & verifiability
`trust: trusted` — Canada411 is the authoritative Canadian online directory (Yellow Pages Canada) drawing on carrier listings; listed-subscriber results are reliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canada411-ca |
| category | phone |
| selectorsIn → selectorsOut | phone → name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
