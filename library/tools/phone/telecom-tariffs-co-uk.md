---
id: telecom-tariffs-co-uk
name: Telecom Tariffs UK Code Look-up
description: Use when you have a UK phone number and want to identify its geographic area or network operator from the dialling code/number range — returns area and operator information.
url: http://www.telecom-tariffs.co.uk/codelook.htm
category: phone
path:
- phone
bestFor: Resolving a UK dialling code or mobile/number range to its geographic area or network operator.
selectorsIn:
- phone
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free look-up, no account. As of verification the codelook page 301-redirects to a bare server IP with a TLS-certificate mismatch, so it is currently awkward to reach in a normal browser.
opsec: passive
opsecNote: You look up a number range in a reference table — nothing is sent to the number's owner, so it is fully passive and non-alerting. Ofcom's own number-allocation data is the authoritative equivalent if this mirror is unreachable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-standing hobbyist UK telecoms reference; useful for code/range identification, but currently in a degraded/relocated state and not an official source.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- telecom-tariffs.co.uk codelook
- UK dialling code lookup
- UK number range lookup
tags:
- mobilephone
- Mobile & Phone Related
- uk
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Telecom Tariffs UK Code Look-up

> A UK number-range reference: paste a dialling code or number and learn which geographic area or network operator it belongs to — context that shapes how you investigate a UK phone number.

## When to use
You have a UK `phone` number and, before chasing the person, you want to know what the number *is*: which town/area an `01`/`02` geographic code maps to, or which mobile/VoIP operator an `07`/`03`/`08` range was allocated to. That range context tells you whether a "local" number really is local, flags non-geographic/premium/VoIP ranges, and narrows which UK carrier or region to pursue next.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.telecom-tariffs.co.uk/codelook.htm. (Note: it currently redirects to a bare server IP with a certificate warning — proceed manually, or use Ofcom's number-allocation data as the authoritative fallback.)
2. Enter the UK dialling code or the leading digits of the number.
3. Read the result: the geographic area for landline codes, or the originally-allocated operator for mobile/non-geographic ranges.
4. Treat operator as *allocation*, not current provider — UK number portability means a number may have moved networks since allocation.
5. Pivot: the area feeds local directory/electoral-roll searches; the range type (VoIP/premium) tells you whether normal reverse-lookup even applies.

## Inputs → Outputs
- **In:** a UK `phone` number or dialling code
- **Out:** `geolocation` (the geographic area for landline codes) plus the allocated network operator for mobile/non-geographic ranges
- **Empty/negative result looks like:** no match for the range, or the page failing to load (degraded state). If unreachable, use Ofcom's published telephone-numbering data, which is the authoritative source for the same information.

## Gotchas & OpSec
- **Portability caveat:** the operator shown is who the range was *allocated* to, not necessarily the current carrier — a ported number will mislead you.
- The site is currently degraded (redirects to a raw IP with a TLS mismatch); prefer Ofcom's numbering data for anything you need to rely on.
- Fully passive — a table lookup that never contacts the number's owner.
- This identifies the *range*, not the *subscriber*; it gives area/operator context, not a name or address.

## Overlaps ("do both")
- Pairs with reverse-phone and directory tools — establish the range/area here first so you apply the right lookup (geographic vs mobile vs VoIP).
- Complements Ofcom's official numbering data, which you should treat as the authoritative version of this same lookup.

## Trust & verifiability
`trust: unverified` — a hobbyist mirror of UK numbering allocations, currently in a degraded/relocated state; cross-check any range attribution against Ofcom's official telephone-numbering data before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telecom-tariffs-co-uk |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
