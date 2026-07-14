---
id: cnam-and-caller-name-lookup-service-provider-cid-name-professional-cnam-service-provider-for-asterisk-freeswitch-ope
name: CID(name) — CNAM Caller Name Lookup
description: Use when you have a US/Canada `phone` number and want the CNAM (registered caller-ID name) via a live SS7 dip — returns the name (person or business) on the line.
url: http://www.cidname.com
category: phone
path:
- phone
bestFor: Resolving the CNAM (caller-ID name) registered to a US/Canada phone number via a live per-dip SS7 query.
selectorsIn:
- phone
selectorsOut:
- name
- employer-org
status: live
pricing: freemium
costNote: Requires a paid account; each lookup is a billable "dip" (small per-query fee) delivered over an HTTP API. No meaningful free browsing — the value is behind signup and per-dip charges.
opsec: passive
opsecNote: A CNAM dip queries the carrier's SS7 record, not the subscriber; the number's owner is not contacted or notified. Your account/billing identifies you to the provider, so use a dedicated account for investigative work.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: A specialist commercial CNAM provider for VoIP platforms (Asterisk/FreeSWITCH/OpenSIPS); data comes live from the number owner's carrier via SS7 rather than a stale private database, so it is fresh but only as accurate as the carrier's CNAM record.
missingPersonsRelevance: high
coverage:
- us
- ca
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- cidname.com
- CID(name)
- CNAM lookup
tags:
- phone
- cnam
- caller-id
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# CID(name) — CNAM Caller Name Lookup

> A commercial CNAM (caller-ID name) service: given a US/Canada number, it dips the carrier's SS7 record live and returns the registered name on the line.

## When to use
You have a US or Canadian `phone` number and want the CNAM — the person or business `name` the carrier associates with it (the text that shows on a caller ID). This turns a bare number into an attributed name, a high-value pivot in missing-persons and identity work for North American landlines and many mobiles. Because CID(name) performs a live SS7 dip rather than reading a cached database, results reflect the current carrier record.

## How to use it (`bestInteractionPattern`: api)
1. Sign up at https://www.cidname.com and fund the account (billing is per dip).
2. Issue a lookup via the HTTP API, passing the target `phone` (E.164/North American format).
3. Read the returned CNAM string — a personal `name`, a business `employer-org` name, or a generic label.
4. Pivot: a returned name feeds people-search and public-records lookups; a business name feeds corporate-registry checks. Corroborate before relying on it.

## Inputs → Outputs
- **In:** `phone` (US/Canada number)
- **Out:** CNAM string — person `name` or business `employer-org` name
- **Empty/negative result looks like:** a blank CNAM, "WIRELESS CALLER"/"UNKNOWN", or a city/state placeholder — common for mobiles and numbers whose carriers don't publish a subscriber name; absence of a name is not proof of anything.

## Gotchas & OpSec
- **Coverage is US/Canada only**, and many mobile numbers return generic labels ("WIRELESS CALLER") rather than a real name.
- CNAM reflects what the *carrier* has on file, which can be outdated, a business trunk name, or a prior subscriber — treat as a lead to verify.
- **Human-in-the-loop:** paid account and API integration required; there is no free web search box.
- OpSec: passive toward the target (the subscriber isn't contacted); your provider account identifies you.

## Overlaps ("do both")
- Do both with `[[numbering-plans]]` (validate/geo-locate the number first) and other reverse-phone/people-search tools — CNAM gives the carrier-registered name, while people-search adds address/associate context and cross-checks the name.

## Trust & verifiability
`trust: community` — a specialist commercial provider with fresh live-dip data; reliable as a carrier record, but CNAM accuracy is bounded by what the terminating carrier registered, so corroborate the name independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cnam-and-caller-name-lookup-service-provider-cid-name-professional-cnam-service-provider-for-asterisk-freeswitch-ope |
| category | phone |
| selectorsIn → selectorsOut | phone → name, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
