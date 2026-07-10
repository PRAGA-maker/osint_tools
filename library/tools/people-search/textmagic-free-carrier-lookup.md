---
id: textmagic-free-carrier-lookup
name: TextMagic Free Carrier Lookup
description: Use when you have a `phone` number and want to know its carrier and line type — returns carrier name, mobile/landline/VoIP classification, country and network codes.
url: https://www.textmagic.com/free-tools/carrier-lookup
category: people-search
path:
- people-search
bestFor: Free HLR-style carrier and line-type lookup to classify a phone number before deeper reverse-phone work.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: free
costNote: Free tool with no signup (part of TextMagic's free-tools suite); TextMagic sells bulk SMS/lookup APIs, but the single web lookup is free.
opsec: passive
opsecNote: The lookup queries carrier/numbering databases, not the phone itself — the target's device is never contacted and receives no notification. You disclose the number to TextMagic; use a sock-puppet browser. This is a metadata/HLR-style check, not a call or SMS.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by TextMagic, an established commercial SMS provider; carrier/line-type data is reliable, though it identifies the number's carrier — not its owner.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- TextMagic carrier lookup
- textmagic phone checker
tags:
- people-search
- carrier-lookup
- phone-metadata
- hlr
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# TextMagic Free Carrier Lookup

> A free carrier/line-type classifier: tell whether a number is mobile, landline or VoIP and which carrier holds it — the triage step before reverse-phone attribution.

## When to use
You have a `phone` number and, before spending effort on owner attribution, want to know what *kind* of number it is: mobile vs landline vs VoIP, which carrier/network, and which country. That classification shapes strategy — a VoIP number hints at a disposable/anonymised line, a mobile suggests personal use, and the carrier can matter for legal process or for choosing the right reverse-phone tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.textmagic.com/free-tools/carrier-lookup (redirects to freetools.textmagic.com/carrier-lookup).
2. Paste the `phone` number and select its country.
3. Click "Check Carrier."
4. Read the result: carrier name, phone type (mobile/landline), national format, time zone, mobile country code (MCC) and network code (MNC).
5. Pivot: a mobile number → reverse-phone tools (`[[whitepages-reverse-phone]]`, `[[cell-revealer-telephone-number-lookup]]`); a VoIP flag → treat as possibly anonymised; the country/timezone → geographic context.

## Inputs → Outputs
- **In:** `phone`
- **Out:** carrier name, line type (mobile/landline/VoIP), country, time zone, MCC/MNC — i.e. number metadata, not an owner
- **Empty/negative result looks like:** invalid-number error or "unknown carrier" — usually a malformed number or wrong country selection, not necessarily a dead line. Ported numbers may show the original range holder.

## Gotchas & OpSec
- This returns the **carrier, not the owner** — it does not name a person. Use it to classify and route, then attribute elsewhere.
- Number portability can make the reported carrier the historical range owner rather than the current one.
- OpSec: **passive** — a database lookup, no contact with the device; still use a sock puppet since you hand the number to TextMagic.

## Overlaps ("do both")
- Pairs with `[[whitepages-reverse-phone]]` and `[[cell-revealer-telephone-number-lookup]]` — this tool classifies the line; those attempt to name the owner. Classify first, then attribute.

## Trust & verifiability
`trust: community` — TextMagic is a legitimate commercial SMS/telephony vendor, so carrier/line-type output is dependable numbering-plan data. It says nothing about identity, so never infer an owner from it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | textmagic-free-carrier-lookup |
| category | people-search |
| selectorsIn → selectorsOut | phone → phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
