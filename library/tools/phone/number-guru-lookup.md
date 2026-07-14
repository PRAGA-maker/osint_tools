---
id: number-guru-lookup
name: NumberGuru Lookup
description: Use when you have a `phone` number and want the likely owner name, carrier, line type and spam reputation — returns name and phone metadata.
url: https://www.numberguru.com
category: phone
path:
- phone
bestFor: Fast reverse-phone triage — is this US number a real line, who might own it, and is it a spam/robocall source.
selectorsIn:
- phone
selectorsOut:
- name
status: live
pricing: freemium
costNote: Basic reverse lookup (caller name, location, carrier, spam score) is free; full owner reports, people/email/property lookups run on paid BeenVerified-backed records.
opsec: passive
opsecNote: You submit only the phone number; the number's owner is not notified by a lookup. The service (owned by BeenVerified) logs your queries — use a sock-puppet account/app install and avoid tying a lookup to your real identity.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A consumer reverse-phone/caller-ID service (BeenVerified-owned) that aggregates public and crowd-sourced records; results are probabilistic and must be corroborated.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- NumberGuru
- Number Guru reverse phone
tags:
- toddington
- curated-directory
- telephone-numbers
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# NumberGuru Lookup

> A consumer reverse-phone and caller-ID service — enter a US number and get the likely owner, carrier, line type, and spam reputation.

## When to use
You have a `phone` number (from a contact list, a message, a flyer) and need quick triage: is it a live number, who is it plausibly registered to, what carrier and line type, and is it a known spam/robocall source. Good first-pass on US numbers before committing to deeper, paid record pulls.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.numberguru.com (or the NumberGuru app) and enter the `phone` number.
2. Read the free report: possible owner name, caller location, carrier, and spam/community reputation.
3. For a fuller owner report (linked people/email/property records), the site hands off to paid BeenVerified data — decide whether to pay.
4. Pivot: a candidate `name` feeds people-search and social tooling; carrier/line-type informs whether the number is a mobile, VoIP, or landline for further phone-OSINT.

## Inputs → Outputs
- **In:** `phone` (best coverage for US numbers)
- **Out:** candidate `name` (owner) + `metadata` (carrier, line type, location, spam score)
- **Empty/negative result looks like:** "no information found" or only carrier/location with no name — common for mobile, prepaid, and VoIP numbers. A blank owner is not proof the number is unassigned.

## Gotchas & OpSec
- Human-in-the-loop: the free tier stops at basic data; owner detail is a paywalled BeenVerified upsell — the free result is a teaser.
- US-centric; weak or empty for non-US numbers.
- Aggregated/crowd-sourced data is often outdated or wrong — always corroborate an owner name before acting on it.
- OpSec: passive toward the owner; the service logs your searches.

## Overlaps ("do both")
- Pairs with other reverse-phone tools (carrier/HLR lookups, Truecaller-style apps) — coverage and owner guesses differ per source, so cross-check before trusting a name.

## Trust & verifiability
`trust: unverified` — a commercial aggregator; treat the owner name and metadata as leads to confirm, not as authoritative subscriber records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | number-guru-lookup |
| category | phone |
| selectorsIn → selectorsOut | phone → name, metadata |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
