---
id: numbering-plans
name: Numbering Plans
description: Use when you have a `phone` number and want to validate it and resolve its country, area, and network/operator from published numbering-plan data — returns geolocation and carrier/line context.
url: https://www.numberingplans.com/?page=analysis&sub=phonenr
category: phone
path:
- phone
- international
bestFor: Validating a phone number and resolving its country, area, and network/operator from official numbering plans.
selectorsIn:
- phone
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Basic number analysis is free (some daily query limits for anonymous use); a free account and paid subscriptions unlock heavier use and additional numbering databases.
opsec: passive
opsecNote: A reference lookup against published numbering-plan data; nothing is sent to the target number and the owner is not notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running independent telephony-numbering reference site; its plan data mirrors public/regulatory allocations and is reliable for structure/geography, less so for post-porting carrier ownership.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- numberingplans.com
- number analysis tool
tags:
- phone
- numbering-plan
- validation
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Numbering Plans

> A telephony numbering-plan reference: paste any phone number and get its validity, country, area/region, and the network/operator range it belongs to.

## When to use
You have a `phone` number in an unknown or ambiguous format and want to (a) confirm it is structurally valid, (b) pin its country and geographic area, and (c) identify the network/operator range it was originally allocated to. This is a foundational normalisation and geolocation step before deeper phone OSINT — it tells you *where* a number lives and *which carrier block* it came from, narrowing follow-up and flagging VOIP/special ranges.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.numberingplans.com/?page=analysis&sub=phonenr.
2. Enter the target `phone` in international format (other notations are tolerated) and analyse.
3. Read the result: validity, country, area/city, and the allocated network/operator for that number range.
4. Pivot: the country/area (`geolocation`) narrows people-search scope; an operator/line-type signal informs whether to try mobile-messaging tools (`[[whatsapp-osint]]`) or a burner check (`[[receive-sms-online-3]]`).

## Inputs → Outputs
- **In:** `phone` (international format preferred)
- **Out:** number validity plus country/area and network/operator (`geolocation` + carrier context)
- **Empty/negative result looks like:** "invalid/unallocated" — a mistyped number, a non-existent range, or a very new allocation; and note that ported numbers still show their *original* operator block, not the current carrier.

## Gotchas & OpSec
- Number **portability** means the displayed operator is the original range holder, not necessarily the current carrier — treat carrier as a lead.
- Heavy/automated use hits query limits without an account; the anonymous free tier is for occasional lookups.
- OpSec: passive; a static data lookup with no contact to the target.

## Overlaps ("do both")
- Precedes `[[howtocallabroad-com]]` (dialing format) and pairs with line-type/HLR lookups and `[[receive-sms-online-3]]` — do both, since this gives structure/geography while those give ownership/liveness signals.

## Trust & verifiability
`trust: community` — an independent reference whose plan data reflects public numbering allocations; reliable for structure and geography, with portability the main caveat on carrier attribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | numbering-plans |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
