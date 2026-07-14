---
id: inmobprefix
name: InMobPrefix
description: Use when you have an Indian mobile `phone` number and want to identify the original operator and telecom circle (region) from its prefix — returns geolocation (circle/state) and carrier without a paid lookup.
url: https://github.com/hstsethi/in-mob-prefix
category: phone
path:
- phone
bestFor: Offline mapping of an Indian mobile prefix to its telecom circle (region) and original operator.
selectorsIn:
- phone
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open-source; runs entirely offline against a bundled dataset (no API, no per-lookup cost).
opsec: passive
opsecNote: Fully local — the number is never sent to any third party, so this is the most OpSec-safe way to region-profile an Indian number. No target contact, no query leakage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source project using public data from Wikipedia, India's DoT, and TRAI, with a trained model for unknown prefixes. Mobile number portability means the *current* operator may differ from the original allocation.
missingPersonsRelevance: medium
coverage:
- in
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- phoneinfoga
aliases:
- in-mob-prefix
- Indian mobile prefix lookup
tags:
- phone-number-research
- india
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# InMobPrefix

> An offline lookup that maps an Indian mobile prefix (the leading 4 digits, 6xxx–9xxx) to its telecom circle/region and original operator — no paid API, no data leakage.

## When to use
You have an Indian mobile `phone` number and want to localise it — which telecom **circle** (roughly a state/region) it was issued in, and which operator originally held the range. This narrows a number's likely geographic origin, a useful early pivot when you have a phone but no location, and it runs fully offline so nothing about the number leaves your machine.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/hstsethi/in-mob-prefix` and set up Python.
2. Take the first 4 digits of the 10-digit Indian mobile number.
3. Run the lookup against the bundled CSV dataset; for prefixes not in the dataset, `predict-operator.py` uses a trained Gradient Boosting model to estimate the operator.
4. Read the returned operator + circle. Pivot: the circle gives a `geolocation` region to combine with other selectors; for broader carrier/format footprinting use `[[phoneinfoga]]`.

## Inputs → Outputs
- **In:** `phone` (Indian mobile, first 4 digits)
- **Out:** `geolocation` (telecom circle/region) + original operator name
- **Empty/negative result looks like:** prefix not found and a low-confidence model guess — treat predicted operators as tentative, and remember the range may have been reallocated.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** and local — the safest way to profile an Indian number; nothing is transmitted.
- Portability caveat: India has mobile number portability, so the **original** allocation this returns may not be the number's **current** operator — the circle/region is the more durable signal.
- India-only.

## Overlaps ("do both")
- Pairs with `[[phoneinfoga]]` — PhoneInfoga adds international carrier/line-type footprinting and web-footprint search; InMobPrefix gives precise Indian-circle geolocation offline.

## Trust & verifiability
`trust: community` — an open-source tool built on official Indian telecom data. Prefix-to-circle mappings from the dataset are reliable; model-predicted operators for unknown prefixes are estimates to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inmobprefix |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
