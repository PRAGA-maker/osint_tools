---
id: ipqualityscore-com-2
name: ipqualityscore.com
url: https://www.ipqualityscore.com/phone-number-validator
category: phone
path:
- phone
description: Use when you have a `phone` and want to validate it — returns carrier, line type (mobile/VOIP/landline), active status, country/region and a fraud-risk score.
bestFor: Vetting a phone number's nature — real vs VOIP/burner, active vs disconnected, carrier and fraud risk — before trusting it as a contact point.
selectorsIn:
- phone
selectorsOut:
- name
- address
status: live
pricing: freemium
costNote: A free web validator and a free trial (~1,000 lookups) exist; sustained/bulk use and the reverse-name field require an account and paid API plans.
opsec: passive
opsecNote: Validation is a passive metadata/carrier lookup that does not contact or notify the subscriber. The reverse-name feature needs a login, which ties queries to your account — use a sock-puppet registration. No call is placed to the number.
humanInLoop: true
humanInLoopReason:
- rate-limit
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: A widely-used commercial fraud-prevention provider with direct carrier relationships in 75+ countries; line-type/carrier/active-status data is high-quality, though owner-name coverage is limited.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- IPQualityScore
- IPQS phone validator
tags:
- mobilephone
- Mobile & Phone Related
- phone-validation
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ipqualityscore.com

> IPQS's phone validator — a real-time check of what a number actually *is*: carrier, line type, active status, location and fraud risk, across 150+ countries.

## When to use
You have a `phone` and need to judge its nature before relying on it: is it a real mobile or a disposable VOIP/burner, is the subscriber active or disconnected, which carrier and country, and how risky/abusive does it score? Essential for triaging a number in a trace — a VOIP/high-risk result reframes whether a "contact" is genuine, and line-type guides which reverse-lookup tools are worth running.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ipqualityscore.com/phone-number-validator.
2. Enter the `phone` in international format and run the free lookup (rate-limited; a free trial adds ~1,000 lookups with an account).
3. Read the result: carrier, line type (mobile/landline/VOIP), active/disconnected, prepaid/ported flags, city/region, and fraud score.
4. For the reverse-name field, log in (account required); expect "unknown" for many numbers.
5. Pivot: line-type/active status tells you whether to spend on `[[spydialer-reverse-phone-lookup]]`-style owner lookups; country/carrier narrows the subject's location.

## Inputs → Outputs
- **In:** `phone`
- **Out:** carrier, line type, active status, country/region (`address`-level), fraud score; sometimes owner `name` (login)
- **Empty/negative result looks like:** valid-but-unattributed — you almost always get carrier/line-type/risk, but the owner `name` is frequently "unknown." An "invalid/inactive" verdict is itself a strong signal the number is fake or dead.

## Gotchas & OpSec
- It excels at number *characterisation*, not owner identification — don't expect a name for most numbers.
- Free use is rate-limited; volume and reverse-name need an account/paid API.
- OpSec: passive — no call is placed. Logging in for reverse-name is attributable; use a puppet account.

## Overlaps ("do both")
- Pairs with `[[spydialer-reverse-phone-lookup]]` — IPQS says what the number *is* (VOIP/mobile/active/risky), SpyDialer tries to say *who* owns it. Run IPQS first to avoid wasting effort on dead/VOIP numbers.

## Trust & verifiability
`trust: trusted` — a reputable commercial fraud-prevention service with direct carrier data, so line-type/carrier/active-status is high-confidence; treat the fraud score as a signal and note owner-name coverage is thin.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipqualityscore-com-2 |
| category | phone |
| selectorsIn → selectorsOut | phone → name, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit, account-login) |
