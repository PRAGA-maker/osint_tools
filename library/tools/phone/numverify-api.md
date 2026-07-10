---
id: numverify-api
name: Numverify API
description: Use when you have a `phone` number and want to validate it and learn its country, carrier, and line type — returns validity, country/region, carrier, and number format (not the owner's name).
url: https://numverify.com/
category: phone
path:
- phone
bestFor: Programmatic global phone-number validation — confirming a number is real and identifying its country, carrier, and line type.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: freemium
costNote: Free tier (100 lookups/month) after signing up for an API key; paid plans raise the quota. No per-lookup name/owner data at any tier — it validates and enriches, it doesn't identify.
opsec: passive
opsecNote: The number is sent to numverify's (apilayer's) API for validation, not to the subject — the target is never contacted or notified. You do expose the queried number to a third-party API; use a dedicated API key and avoid logging sensitive numbers in shared code.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: trusted
trustNote: Operated by apilayer, an established API provider; validation/carrier/line-type data is reliable, though carrier can be stale for ported numbers.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- numverify
- apilayer phone validation
tags:
- Phone numbers
- phone-validation
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Numverify API

> A global phone-number validation API — confirm a number is real and get its country, carrier, and line type programmatically (it does not return the owner's identity).

## When to use
You have one or many `phone` numbers and need to validate them and learn structural facts: is the number valid, what country/region is it, which carrier, and is it mobile or landline. Ideal as an early triage/enrichment step over a batch of numbers before deeper (owner-identifying) lookups, and for confirming the country of an unfamiliar international number.

## How to use it (`bestInteractionPattern`: api)
1. Register at https://numverify.com/ for a free API key (100 lookups/month).
2. Call the endpoint, e.g. `http://apilayer.net/api/validate?access_key=KEY&number=14158586273&country_code=&format=1`.
3. Read the JSON: `valid`, `country_code`/`country_name`, `location`, `carrier`, `line_type` (mobile/landline), and normalized/international formats.
4. Batch-validate a list to drop invalid numbers and group by country/carrier.
5. Pivot: take valid numbers into owner-identifying tools (`[[thatsthem-phone-search]]`, carrier/HLR lookups); use country/carrier to inform which regional tools to try next.

## Inputs → Outputs
- **In:** `phone` number (E.164 or with country code)
- **Out:** validity boolean, country/region, `carrier`, line type (mobile/landline), normalized `phone` formats
- **Empty/negative result looks like:** `valid: false` (malformed or non-assigned number) or missing carrier/location for some regions. Note carrier can be wrong for ported numbers — validation ≠ identification.

## Gotchas & OpSec
- **Validation, not attribution** — it never returns a name or address; don't expect owner identity.
- Carrier data can be stale for ported numbers.
- Free tier is small and rate-limited; guard your API key.

## Overlaps ("do both")
- Pairs with `[[thatsthem-phone-search]]` and carrier/HLR lookups — numverify confirms *that a number is valid and where it's from*, those attempt *who it belongs to*.

## Trust & verifiability
`trust: trusted` — a reputable commercial validation API; the format/country/line-type data is dependable, with the usual caveat that carrier can lag number portability.
