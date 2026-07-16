---
id: freecarrierlookup
name: FreeCarrierLookup
description: Use when you have a `phone` number and want to identify its carrier and whether it is mobile or landline — returns the carrier name, line type and (US/CA) email-to-SMS/MMS gateway.
url: https://freecarrierlookup.com/
category: phone
path:
- phone
bestFor: Free carrier and line-type (mobile vs landline) identification for a phone number.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: free
costNote: Completely free; no account or email required. A per-lookup CAPTCHA is the only gate.
opsec: passive
opsecNote: This performs a network/carrier database (HLR-style) lookup — it identifies the carrier but does NOT ring, text, or otherwise alert the subscriber. Passive toward the target; only your IP touches the site. Use a VPN if you don't want the query tied to you.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running free carrier-lookup service; carrier/line-type results are generally accurate for most countries, though number portability can make the "current carrier" lag.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Free Carrier Lookup
- freecarrierlookup.com
tags:
- phone-number-research
- carrier-lookup
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- carrier-lookup-2
- free-carrier-lookup
---

# FreeCarrierLookup

> A free carrier-lookup that tells you who operates a phone number and whether it is a mobile or landline — the first triage step on any phone selector.

## When to use
You have a `phone` number and need to know its carrier and line type before deciding how to pivot. Knowing it is a VoIP/landline vs. a real mobile changes your approach (a VoIP number suggests a burner or business line; a mobile is more likely tied to a personal identity). For US/Canada numbers it also yields the email-to-SMS/MMS gateway address, occasionally useful for corroboration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://freecarrierlookup.com/ in a clean/sock-puppet browser.
2. Select the country and enter the `phone` number.
3. Solve the CAPTCHA (a short word/number puzzle rendered as an image) and submit.
4. Read the output:
   - **Carrier** name (e.g. "T-Mobile USA", "EE").
   - **Line type** — wireless (mobile) vs landline.
   - **SMS/MMS gateway** — for US/CA, the `number@carrier-gateway` addresses.
5. Pivot: line type steers the next step — a mobile carrier supports messaging-app checks (WhatsApp/Telegram/Signal presence); VoIP/landline steers you toward business/records lookups. Feed the number into reverse-lookup people search.

## Inputs → Outputs
- **In:** `phone` (with country)
- **Out:** carrier name, line type (mobile/landline), US/CA email-to-SMS/MMS gateway — an enriched `phone`
- **Empty/negative result looks like:** "carrier not found" / a generic or blank carrier — common for some countries or for numbers that have been ported; not proof the number is invalid.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA is required on every lookup; solve it manually.
- **Number portability** means the reported carrier may be the original network, not the current one — treat carrier as indicative.
- Passive: the subscriber is never notified; this is a database lookup, not a call/text.

## Overlaps ("do both")
- Pairs with reverse phone people-search and messaging-app presence checks — FreeCarrierLookup classifies the line so you know which of those pivots are worth running.

## Trust & verifiability
`trust: community` — a widely used free service. Carrier/line-type data is generally reliable at the network level, but portability and VoIP re-assignment mean you should treat the carrier as a strong hint, not proof of the current provider.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | freecarrierlookup |
| category | phone |
| selectorsIn → selectorsOut | phone → phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
