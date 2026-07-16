---
id: carrier-lookup-2
name: Carrier Lookup
description: Use when you have a `phone` number and want its carrier and line type (mobile vs landline) plus the email-to-SMS gateway — returns enriched `phone` metadata.
url: http://freecarrierlookup.com/
category: people-search
path:
- people-search
bestFor: Identifying the current carrier and whether a number is wireless or landline, plus the US/CA email-to-SMS gateway.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: free
costNote: Free for interactive lookups on the website; each query requires solving a CAPTCHA. No official API (third-party screen-scraper wrappers exist).
opsec: passive
opsecNote: The lookup queries carrier/portability databases, not the subject — the number's owner is not notified. It is passive against the target, though you disclose the number to freecarrierlookup's operator; use a clean browser if the association matters.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party service, not independently verified here; carrier data is generally accurate for most countries but reflects the current carrier after any porting, not the original one.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FreeCarrierLookup
- freecarrierlookup.com
tags:
- toddington
- curated-directory
- people-search
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- free-carrier-lookup
- freecarrierlookup
---

# Carrier Lookup

> FreeCarrierLookup.com — paste a phone number, get its current carrier, whether it's mobile or landline, and (for US/CA) the email-to-SMS/MMS gateway.

## When to use
You have a `phone` number and need to characterise it before deeper work: which carrier serves it now, whether it's a wireless or landline number, and — for US/Canada — the email-to-SMS gateway address. That line-type/carrier signal helps distinguish a real personal mobile from a VoIP/landline/burner and guides which reverse-lookup approach to try next.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.freecarrierlookup.com/ (note the stub's `http` URL redirects to `https`; the `www` host is canonical).
2. Select the country and enter the `phone` number.
3. Solve the CAPTCHA (required on every lookup) and submit.
4. Read the result: carrier name, line type (wireless/landline), and — for US/CA numbers — the SMS/MMS gateway domain (e.g. `number@vtext.com`).
5. Pivot: line type steers next steps (VoIP → check number-provisioning services like `[[twilio-lookup]]`; mobile → carrier-aware reverse lookups). The email-to-SMS gateway is itself an `email`-style selector.

## Inputs → Outputs
- **In:** `phone` (with country selected)
- **Out:** enriched `phone` metadata — carrier, line type (mobile/landline), email-to-SMS/MMS gateway (US/CA)
- **Empty/negative result looks like:** "carrier not found" / blank line type — common for some international ranges and newly-ported numbers. It returns the **current** carrier only; a ported number won't reveal its original carrier, and this tells you nothing about the owner's identity.

## Gotchas & OpSec
- CAPTCHA on every query — no clean bulk/API path from the official site (scraper wrappers exist but break often and violate ToS).
- Carrier reflects post-porting state; do not infer the number's origin from it.
- Accuracy is strong for US/CA and major markets, patchier for smaller countries.

## Overlaps ("do both")
- Pairs with `[[twilio-lookup]]`/`[[numverify]]`-style carrier APIs and reverse-lookup directories — this gives a quick free carrier/line-type read, while API tools give structured, bulk, or portability data and the directories attempt owner identification.

## Trust & verifiability
`trust: unverified` — third-party service with generally reliable carrier data, but no first-party guarantee; corroborate line-type conclusions with a second carrier tool before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | carrier-lookup-2 |
| category | people-search |
| selectorsIn → selectorsOut | phone → phone |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
