---
id: thatsthem
name: ThatsThem
description: Use when you have an email, phone, name, or address and want to pivot to a full US contact profile — returns name, address, phone, and linked details.
url: https://thatsthem.com/reverse-email-lookup
category: email
path:
- email
- email-search
bestFor: Free reverse lookups across email, phone, name, address, and IP for US residents.
selectorsIn:
- email
- phone
- name
- address
- ip-address
selectorsOut:
- name
- address
- phone
- email
- associate
status: live
pricing: freemium
costNote: Web lookups are free; bulk/API access and append data are paid.
opsec: passive
opsecNote: Queries ThatsThem's public aggregated database; the target is not notified. Use a sock-puppet browser session if you want to avoid tying the search to your account/cookies.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing free US people-search aggregator widely cited in OSINT frameworks; data is consumer-marketing grade and can be stale or partial.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- venacus
- usersearch-ai
aliases:
- thatsthem.com
tags:
- email
- people-search
- reverse-lookup
source: arf-seed
lastVerified: ''
enrichment: full
---

# ThatsThem

> A free US-focused reverse-lookup aggregator: start from one identifier (email, phone, name, address, or IP) and pull a linked contact profile.

## When to use
You have one selector for a US subject — an `email`, `phone`, partial `name` + city, a known `address`, or even an `ip-address` — and want to expand it into a fuller picture: full `name`, current/prior `address`, other `phone` numbers, and sometimes associated people. Strong early-pivot tool because reverse-email and reverse-phone are both free.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://thatsthem.com/` and pick the matching reverse tab (email/phone/name/address/IP).
2. Enter the selector; solve any CAPTCHA.
3. Read the result cards: each card is a candidate person with name, addresses, phones, and sometimes age range, IP, or device hints.
4. Pivot: feed a recovered `phone`/`address` back in to confirm, or push a recovered `name` into broader people search and social tools.

## Inputs → Outputs
- **In:** `email`, `phone`, `name`, `address`, `ip-address`
- **Out:** `name`, `address`, `phone`, `email`, `associate`
- **Empty/negative result looks like:** "No results found" or a generic page with no contact cards — common for non-US, very young, or privacy-scrubbed subjects.

## Gotchas & OpSec
- Human-in-the-loop: CAPTCHA appears on repeated queries.
- US-centric; weak-to-absent coverage outside North America.
- Marketing-grade data: addresses/phones can be years out of date — corroborate before acting.
- OpSec: passive; target not alerted. Use a clean/sock-puppet session to avoid linking searches to you.

## Overlaps ("do both")
- Pairs with [[venacus]] (breach-sourced data fills gaps in aggregator data) and [[usersearch-ai]] (turns the same email into social/username hits).

## Trust & verifiability
`trust: community` — a well-known free aggregator referenced across OSINT framework lists; reliable as a lead generator but verify specifics independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thatsthem |
| category | email |
| selectorsIn → selectorsOut | email, phone, name, address, ip-address → name, address, phone, email, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
