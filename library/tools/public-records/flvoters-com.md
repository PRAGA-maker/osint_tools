---
id: flvoters-com
name: Flvoters.com
description: Use when you have a Florida subject's `name` and want their public voter record — returns registered name, address, DOB, party and (public) phone/email.
url: https://flvoters.com/
category: public-records
path:
- public-records
bestFor: Looking up Florida voter-registration records, where name, address, DOB, party and often phone/email are public record.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- dob
- phone
- email
status: live
pricing: freemium
costNote: Basic voter lookups are free; some detailed/bulk features may be gated. The underlying Florida voter file is public record.
opsec: passive
opsecNote: Florida voter data is public record by state law; the subject is not notified. Use responsibly — this is genuine PII (DOB, phone, email) and misuse (e.g. harassment) may be unlawful. Query from a research context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party interface to Florida's public voter file. The source data is authoritative state record, but a third-party mirror can lag official updates — cross-check the state system for anything decisive.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- melissa-us-2
aliases:
- FL Voters
- Florida voter records
tags:
- public-records
- voter-records
- florida
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Flvoters.com

> A window into Florida's unusually open voter file: a name can return registered address, DOB, party — and, because FL law makes them public, often phone and email.

## When to use
Your subject is (or was) in Florida and you have a `name` (or partial `address`). Florida is one of the most permissive states for voter-record disclosure: name, address, date of birth, party affiliation, and frequently phone and email are public record (SSN and driver's-license numbers are not). That makes this a high-yield US people-search pivot for Florida subjects — often confirming DOB and contact details that are hard to get elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://flvoters.com/.
2. Search by `name` (add a county/city or `address` to disambiguate common names).
3. Read the record: registered `name`, `address`, `dob`, party, and any public `phone`/`email`.
4. Disambiguate same-name registrants using DOB and precinct/address.
5. Pivot: a confirmed DOB + address strongly anchors identity for other searches; contact fields feed account-existence tools; cross-check against `[[melissa-us-2]]`.

## Inputs → Outputs
- **In:** `name` (± `address`/county)
- **Out:** `name`, `address`, `dob`, party, and public `phone`/`email`
- **Empty/negative result looks like:** no matching registrant. The subject may not be registered to vote in FL, may have moved out of state, or may use a name variant — absence is not proof they don't live in Florida.

## Gotchas & OpSec
- Covers **registered voters in Florida only** — non-voters and other states won't appear.
- A third-party mirror can lag the official file; verify a decisive record against the state's own lookup.
- This is real PII exposed by state law — use lawfully; harassment/commercial misuse can be illegal.
- OpSec: passive; public-record read, subject not notified.

## Overlaps ("do both")
- Pairs with `[[melissa-us-2]]` and other US people-search — voter records give an authoritative DOB/party that people-search aggregators often lack; cross-confirm the address between them.

## Trust & verifiability
`trust: community` — a third-party front-end over authoritative Florida public voter data. The underlying records are official, but confirm anything you'll act on against the state's own system, and treat contact fields as current-as-of-last-update.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flvoters-com |
</content>
