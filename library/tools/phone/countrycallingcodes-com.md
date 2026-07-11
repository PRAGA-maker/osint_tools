---
id: countrycallingcodes-com
name: countrycallingcodes.com
description: Use when you have a `phone` number or a bare dialing prefix and want to identify the country/area it belongs to — returns the country (and often region) plus time-zone context.
url: http://www.countrycallingcodes.com/
category: phone
path:
- phone
bestFor: Resolving an international/area dialing code to its country and region (forward and reverse lookup).
selectorsIn:
- phone
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free reference site (running since 2000); no account or payment.
opsec: passive
opsecNote: Fully offline-style reference lookup — you type a code, not the target's full number, and nothing is sent to the subject or their carrier. No sock puppet needed; this is one of the safest first steps in phone OSINT.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing, single-purpose reference for international dialing codes; the underlying ITU code data is stable and easy to cross-check.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Country Calling Codes
tags:
- mobilephone
- Mobile & Phone Related
- dialing-codes
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# countrycallingcodes.com

> A stable reference for international and area dialing codes — use it to turn a raw `+NN` prefix (or an unknown number's leading digits) into a country and region, in both directions.

## When to use
You have a `phone` number or a fragment of one and need to know where it's from before doing anything else: which country the `+` prefix maps to, and for the US/Canada/other NANP countries, which region an area code covers. Establishing origin is the first triage step in phone OSINT — it tells you which national tools, carriers, and jurisdictions to point at next, and can immediately flag a number as foreign, VoIP-prefixed, or geographically inconsistent with your subject's claimed location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.countrycallingcodes.com/.
2. Forward lookup: pick or enter a country to get its calling code, or read the code lists directly.
3. Reverse lookup: use the "Reverse Country Code Lookup Tool" — enter a dialing code to see which country/area it belongs to.
4. Note the region and the time-zone info the site provides for that location.
5. Pivot: with the country pinned, route the full number to a country-appropriate carrier/HLR/number tool and check the area against the subject's known geography.

## Inputs → Outputs
- **In:** `phone` (or a bare dialing prefix/area code)
- **Out:** `address` (country/region), `geolocation` (region + time zone)
- **Empty/negative result looks like:** an ambiguous or unassigned code returns nothing meaningful — some prefixes are shared or reserved. It resolves geography of the *code*, not the live line; a ported/VoIP number's code may not reflect the user's real location.

## Gotchas & OpSec
- Human-in-the-loop: none; a static reference.
- It maps the **code's** country/region, not carrier or current location — mobile numbers roam and VoIP numbers can carry a code unrelated to where the person is. Use it for triage, not attribution.
- OpSec: passive and safe; nothing touches the subject.

## Overlaps ("do both")
- Pairs with number-validation/HLR and carrier-lookup tools — this establishes origin cheaply; those add line type, carrier, and validity once you know the country.

## Trust & verifiability
`trust: community` — a long-running single-purpose reference over stable ITU code data; any result is trivially cross-checkable against official code lists.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | countrycallingcodes-com |
| category | phone |
| selectorsIn → selectorsOut | phone → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
