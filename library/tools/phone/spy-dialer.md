---
id: spy-dialer
name: Spy Dialer
description: Use when you have a US `phone` number and want the owner and context — returns the subscriber `name`, line type, carrier, general `geolocation`, spam flags and any voicemail greeting.
url: http://spydialer.com/
category: phone
path:
- phone
bestFor: Free reverse lookup of a US phone number to a name, line type, carrier and city/state, plus hearing the voicemail greeting.
selectorsIn:
- phone
- name
- email
selectorsOut:
- name
- geolocation
status: live
pricing: free
costNote: Completely free, no account or card; up to ~50 lookups per day, ad-supported.
opsec: passive
opsecNote: Searches are anonymous and the number's owner is not notified. Note the voicemail feature works by actually reaching the carrier's voicemail — using it is closer to active; the record/name lookup itself is passive. Use a sock-puppet browser for sensitive numbers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running free reverse-lookup aggregator of public records and proprietary data; coverage is US-centric and can be incomplete or stale — treat a name hit as a lead, not proof.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- free-reverse-phone-lookup
- spydialer
- spydialer-reverse-phone-lookup
- www-spydialer-com
aliases:
- spydialer.com
- SpyDialer
tags:
- phone-number-research
- reverse-phone
- us
source: awesome-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Spy Dialer

> A free, no-signup reverse-lookup for US phone numbers — name, line type, carrier and city, and uniquely, the account's voicemail greeting.

## When to use
You have a US `phone` number and want to attach a person and context to it: who the subscriber is, whether it's a cell/landline/VOIP, the carrier, the general city/state, and whether it's flagged as spam. It also supports reverse lookups by `name` and `email`. The voicemail-greeting feature can reveal a first name or voice when records are thin.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://spydialer.com/ and choose the search type (phone / name / email / address).
2. Enter the 10-digit US number (or other selector) and submit.
3. Read the result: owner `name` (if in records), line type, carrier, city/state (`geolocation`), and spam indicators.
4. Optionally play the voicemail greeting to catch a name/voice.
5. Pivot: a name feeds people-search and social lookups; carrier + line type inform further phone-OSINT; city/state narrows geography.

## Inputs → Outputs
- **In:** US `phone` (or `name` / `email` / address)
- **Out:** subscriber `name`, line type, carrier, `geolocation` (city/state), spam flags, voicemail greeting
- **Empty/negative result looks like:** "no name found" with only carrier/line-type — common for well-guarded, prepaid, or recently-ported numbers; absence of a name is not proof the number is inactive.

## Gotchas & OpSec
- US-only and record-dependent — international numbers and privacy-conscious owners often return nothing beyond carrier.
- Daily lookup cap (~50) and ads; data can be outdated.
- The voicemail feature actually dials into voicemail — treat that specific action as more intrusive than a passive record lookup.

## Overlaps ("do both")
- Pairs with carrier/line-type validators and people-search — Spy Dialer gives a fast free name+voicemail angle; validators confirm the technical metadata and people-search deepens the identity.

## Trust & verifiability
`trust: community` — a free aggregator; useful and widely used, but confirm any name against an independent source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spy-dialer |
