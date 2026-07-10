---
id: phone-validator-us
name: Phone Validator (US)
description: Use when you have a `phone` number and want to validate it and classify the line — returns line type (cell/landline/VoIP/invalid), carrier and geographic location.
url: https://www.phonevalidator.com
category: phone
path:
- phone
bestFor: Validating a phone number and classifying line type, carrier and location before deeper attribution.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: free
costNote: Free web search on the homepage (deliberately throttled to deter bots); larger/bulk validation is a paid API service.
opsec: passive
opsecNote: A database/numbering lookup — the number's device is not called or texted and the subject isn't notified. You disclose the number to PhoneValidator; use a sock-puppet browser. Results are metadata (line type/carrier/location), not the owner's identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial phone-data service; line-type/carrier data is generally reliable for US/Canada, weaker internationally, and the site itself disclaims accuracy guarantees and FCRA/TCPA use.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- PhoneValidator
- phonevalidator.com
tags:
- phone
- carrier-lookup
- line-type
- validation
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Phone Validator (US)

> A phone validator and line-type classifier: is this number real, is it a cell/landline/VoIP, which carrier, and where? The routing step before owner attribution.

## When to use
You have a `phone` number and, before attributing an owner, want to confirm it is valid and understand what it is: cell vs landline vs VoIP vs fake/invalid, plus carrier and geographic location. That classification drives strategy — a VoIP or invalid number signals disposability/spoofing, a mobile suggests personal use, and the carrier/location narrow where the subscriber is.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.phonevalidator.com in a sock-puppet browser.
2. Enter the `phone` number in the free homepage search and submit (expect deliberate throttling on the free tool).
3. Read the result: valid/invalid, line type (cell/landline/VoIP/invalid), carrier/phone company, and geographic location.
4. Route accordingly: valid mobile → owner-attribution tools; VoIP/invalid → treat as anonymised/spoofed; location → geographic context.
5. Pivot: a valid number with carrier/location feeds `[[whitepages-reverse-phone]]`, `[[thats-them]]`, and other reverse-phone attribution.

## Inputs → Outputs
- **In:** `phone`
- **Out:** validity, line type (cell/landline/VoIP/invalid), carrier, geographic location — number metadata, not an owner
- **Empty/negative result looks like:** "invalid" or "fake number" — the number isn't a valid assigned line (spoofed, mistyped, or unassigned). A valid classification with no name is expected: this tool doesn't name owners.

## Gotchas & OpSec
- Returns **line metadata, not identity** — it won't name the owner; pair it with reverse-phone people tools for that.
- Number portability can misreport the carrier as the original range holder; location is approximate (rate center, not the person).
- OpSec: **passive** — no call/text to the device; use a sock puppet since you feed a commercial service.

## Overlaps ("do both")
- Pairs with `[[textmagic-free-carrier-lookup]]` (another line-type/carrier classifier) and reverse-phone attribution (`[[whitepages-reverse-phone]]`, `[[thats-them]]`) — validate/classify here, attribute there. Cross-check line type across two validators for spoofed numbers.

## Trust & verifiability
`trust: community` — a commercial validator, reliable for US/Canada line-type/carrier data, with its own accuracy disclaimer. Treat classification as strong signal and attribution as a separate step.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phone-validator-us |
| category | phone |
| selectorsIn → selectorsOut | phone → phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
