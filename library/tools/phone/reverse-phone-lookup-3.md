---
id: reverse-phone-lookup-3
name: Reverse Phone Lookup
description: Use when you have a `phone` number and want the registered owner's name — returns a caller/subscriber name via a free reverse lookup (ZLookup).
url: https://www.zlookup.com/
category: phone
path:
- phone
bestFor: Free, no-signup reverse lookup of a phone number to a subscriber name, including mobile and international numbers.
selectorsIn:
- phone
selectorsOut:
- name
status: live
pricing: free
costNote: Free with no signup or payment; ad-supported. Claims to query operator/CNAM databases directly.
opsec: passive
opsecNote: The lookup is passive from the subject's side — ZLookup states the phone owner is not notified. You are disclosing the target number to a third-party service that logs queries; use a sock-puppet browser/IP. Do not enter your own number.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Popular free reverse-lookup site. Results derive from CNAM/carrier data and public listings; coverage and accuracy vary widely, especially for mobiles and outside the US.
missingPersonsRelevance: high
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- truecaller
- phoneinfoga
aliases:
- ZLookup
- zlookup.com
tags:
- phone
- reverse-phone
- caller-id
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Reverse Phone Lookup

> ZLookup: a free, no-signup reverse phone lookup that returns the subscriber/caller name behind a number.

## When to use
You have a `phone` number (from a listing, a leaked record, a message) and want to attach a `name` to it — the first identity pivot on an unknown number. It handles US numbers (including toll-free and Google Voice) and claims international coverage, so it's a quick free first pass before paid enrichment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.zlookup.com/ in a sock-puppet browser.
2. Enter the number in full international format (e.g. `+1 555 123 4567`) and submit.
3. Read the result: it may return the owner's full name and, for business/employer lines, a business name.
4. Pivot: feed a returned `name` into people-search and social tools; if it returns nothing, escalate to `[[truecaller]]` (crowd-sourced caller ID) or profile the number's metadata with `[[phoneinfoga]]`.

## Inputs → Outputs
- **In:** `phone`
- **Out:** `name` (subscriber/caller name; sometimes business/carrier name)
- **Empty/negative result looks like:** "no name found" / blank — the number is unlisted, prepaid, ported, or outside covered databases; absence is not proof the number is inactive.

## Gotchas & OpSec
- Human-in-the-loop: none, though ad interstitials appear.
- OpSec: **passive** — the subject is not alerted; but you hand the target number to a third party. Use a sock puppet and never look up your own number.
- Accuracy is uneven: CNAM often shows a stale or carrier-generic name, and mobile/international hit rates are lower than landline/US. Always corroborate.

## Overlaps ("do both")
- Pairs with `[[truecaller]]` (crowd-sourced names catch what CNAM misses) and `[[phoneinfoga]]` (carrier/line-type/format footprint rather than a name) — run all three; they miss different numbers.

## Trust & verifiability
`trust: community` — a free ad-supported service with opaque data sourcing. Treat a returned name as a lead to confirm against a second source, not as identification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reverse-phone-lookup-3 |
| category | phone |
| selectorsIn → selectorsOut | phone → name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
