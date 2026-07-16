---
id: itp-infotrack
name: InfoTrackPeople
description: Use when you have a `name` (optionally a US `address` or `phone`) and want a free people-search preview — returns name, address, phone, age/dob and possible associate links.
url: https://infotrackpeople.org/
category: messaging
path:
- messaging
bestFor: Quick free-tier US people lookup returning current address, phone and associates.
selectorsIn:
- name
- phone
- address
selectorsOut:
- name
- address
- phone
- associate
- dob
status: live
pricing: freemium
costNote: Free tier previews name, approximate age, locations and possible associates; full/background reports (criminal, detailed contact) are gated behind a paid report.
opsec: passive
opsecNote: You query a third-party aggregator, not the subject, so the subject is not alerted — but the site logs your searches and may retarget you with ads. Search from a clean/sock-puppet browser and do not enter your own real contact details.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial US people-search aggregator (one of many near-identical services); free-tier data is broad-strokes and error-prone, so corroborate before relying on it.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- InfoTrackPeople.org
- ITP Infotrack
tags:
- people-search
- background-check
- usa
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# InfoTrackPeople

> A free-to-preview US people-search aggregator: type a name and get current address, phone, approximate age and likely associates, with fuller reports behind a paywall.

## When to use
You have a `name` for a US subject (optionally narrowed by a known `address` or `phone`) and want a fast first-pass on where they live now, their phone numbers, rough age, and who they're connected to. Best as an early triangulation step to generate leads (addresses, associates) you then confirm in authoritative records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://infotrackpeople.org/ in a clean/sock-puppet browser and go to the people search.
2. Enter the subject's `name`; add a US state/city, `address`, or `phone` to disambiguate common names.
3. Read the free preview: matched `name`(s), approximate age (`dob` bracket), current/prior `address` list, `phone` numbers, and possible `associate`/relative names.
4. STOP at the free tier for triage — do not pay for a "full report" unless you've confirmed it's the right person; the same fields are usually obtainable from cheaper/authoritative sources.
5. Pivot: an address feeds county/property records; associate names feed relationship mapping; a phone feeds reverse-phone tools.

## Inputs → Outputs
- **In:** `name` (plus optional `address` / `phone` to narrow)
- **Out:** `name`, `address` (current + historical), `phone`, `associate` (relatives/known associates), approximate `dob`/age
- **Empty/negative result looks like:** "no records found" or a list of same-name strangers you can't disambiguate — treat as inconclusive, since coverage is US-consumer-data-only and stale.

## Gotchas & OpSec
- Human-in-the-loop: a partial paywall — the free preview teases, and detailed reports require payment; don't assume the paid data is more accurate.
- OpSec: **passive** toward the subject (no alert), but the site tracks your searches; use a throwaway browser session.
- These aggregators recycle the same broker feeds, so data is often outdated and mixes people with similar names — always corroborate an address/associate before acting on it.

## Overlaps ("do both")
- Run alongside other US people-search aggregators and authoritative county records: cross-checking two brokers plus a primary source is the only way to trust a free-tier address or associate.

## Trust & verifiability
`trust: unverified` — a commercial data-broker front (not an official record), so treat every field as a lead to confirm elsewhere, not as established fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | itp-infotrack |
| category | messaging |
| selectorsIn → selectorsOut | name, phone, address → name, address, phone, associate, dob |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
