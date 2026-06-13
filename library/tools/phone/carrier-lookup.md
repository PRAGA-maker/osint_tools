---
id: carrier-lookup
name: carrier lookup
description: Use when you have a US phone number and need its carrier and line type (mobile vs landline) to qualify the number before deeper phone OSINT.
url: https://www.carrierlookup.com/
category: phone
path:
- phone
bestFor: US phone number to carrier name and line type (mobile/landline), with an API.
selectorsIn:
- phone
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: A limited free lookup exists; bulk/API access requires registration and prepaid credits (~1¢ per lookup, $50 minimum for 1,000).
opsec: passive
opsecNote: Carrier/line-type lookup reads numbering and ported (LRN) data; it does not call or ping the target handset.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial carrier-detection service; carrier/line-type results are generally reliable for US numbers but it's a third-party aggregator, not a carrier itself.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: true
localInstall: false
registration: true
aliases:
- carrierlookup.com
- CarrierLookup
tags:
- phone
- carrier
- us
source: osint4all
lastVerified: '2026-06-13'
enrichment: full
---

# carrier lookup

> US carrier-detection service — enter a US number to get the carrier name and whether it's mobile or landline, via web or API.

## When to use
You have a US `phone` number and need its carrier and line type (`metadata-exif`) to qualify the number: is it mobile, landline, or VoIP, and which carrier? Do this before subscriber-finding so you choose the right downstream tools and recognise disposable/VoIP numbers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.carrierlookup.com/.
2. Run a free single lookup with the 10-digit US `phone` number.
3. Read the result: carrier name and line type (mobile/landline). For volume or programmatic use, register, buy credits (~1¢/lookup), and use the API.
4. Pivot: line type/carrier informs the next move — a VoIP/prepaid number suggests different OSINT than a contract mobile; feed into reverse-lookup tools like `[[advanced-background-checks]]`.

## Inputs → Outputs
- **In:** `phone` (US)
- **Out:** `metadata-exif` (carrier name, mobile/landline line type)
- **Empty/negative result looks like:** "unknown carrier"/invalid number, or a free-tier rate-limit/registration prompt before you get the answer.

## Gotchas & OpSec
- Human-in-the-loop: free lookups are rate-limited; meaningful volume needs an account and prepaid credits.
- US carriers only — not for international numbers.
- It reports carrier/line type, not subscriber identity.
- OpSec: passive; LRN/numbering-data lookup with no contact to the handset.

## Overlaps ("do both")
- Pairs with `[[advanced-background-checks]]` (free US reverse phone → name/address) — carrierlookup qualifies the number, the reverse lookup names it. For UK carrier use `[[aql-com]]`.

## Trust & verifiability
`trust: community` — a commercial third-party carrier-detection aggregator; line-type/carrier results are generally reliable for US numbers but should be sanity-checked against a second source for edge cases (recent ports, VoIP).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | carrier-lookup |
| category | phone |
| selectorsIn → selectorsOut | phone → metadata-exif (carrier, line type) |
| pricing / cost | freemium (free limited; API ~1¢/lookup) |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (login, rate-limit) |
