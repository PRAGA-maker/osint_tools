---
id: beenverified-com
name: BeenVerified
description: Use when you have a `name` (or phone/email/address) and want a consolidated US person report — returns address history, phone, email, relatives, and social-profile links behind a paywall.
url: https://www.beenverified.com/
category: people-search
path:
- people-search
bestFor: Consolidated US background report (addresses, relatives, contacts) from a name or phone/email.
selectorsIn:
- name
- phone
- email
- address
selectorsOut:
- address
- phone
- email
- social-profile
- associate
- dob
status: live
pricing: freemium
costNote: Searching is free and shows a teaser (locations, relatives count), but viewing the full report requires a paid subscription (monthly membership, often with auto-renew).
opsec: passive
opsecNote: A commercial data-broker report; the subject is not notified. You disclose the searched selectors and your payment identity to the broker. Under US FCRA this data must NOT be used for employment, tenancy, or credit decisions.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Aggregated data-broker records (public records + marketing data); convenient but error-prone (mixed people, stale addresses). Not a consumer reporting agency.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- truepeoplesearch
- advancedbackgroundchecks
- spokeo
aliases:
- beenverified.com
tags:
- peoplesearch
- People Search Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# BeenVerified

> A subscription US people-search aggregator that compiles a person's addresses, phones, emails, relatives, and linked profiles into one report — powerful but paywalled and error-prone.

## When to use
You have a `name` (ideally with a US state/city) or a `phone`/`email`/`address` and want a broad first sweep of everything a mainstream broker holds: address history, current/past phones and emails, likely relatives and associates, and social-profile links. Good for quickly generating leads (relatives to contact, addresses to check) on a US subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.beenverified.com/ and search by name (+ state), phone, email, or address.
2. Read the free teaser: cities lived, and a count of relatives/phones — enough to judge if it's your subject.
3. To see full details you must start a paid membership; be aware of auto-renew and cancel promptly if doing a one-off.
4. Treat every field as a lead — brokers routinely mix records of similarly-named people.
5. Pivot: relatives feed an associate map; a current address feeds property/neighbor tools; a free-people-search cross-check confirms fields without paying.

## Inputs → Outputs
- **In:** `name`, `phone`, `email`, or `address`
- **Out:** `address` (history), `phone`, `email`, `associate` (relatives), `social-profile`, `dob`/age
- **Empty/negative result looks like:** a thin report or "no records" — common for young people, recent movers, or privacy opt-outs. Absence is weak evidence; try free aggregators.

## Gotchas & OpSec
- Human-in-the-loop: full data is behind a paid, auto-renewing subscription.
- OpSec: **passive** toward the subject; you disclose selectors + payment to the broker.
- Legal: FCRA-prohibited uses (employment/tenant/credit screening) — do not use it for those.

## Overlaps ("do both")
- Pairs with `[[truepeoplesearch]]` and `[[advancedbackgroundchecks]]` — free aggregators that often show the same addresses/relatives without paying; use them to confirm BeenVerified's teaser before subscribing.
- Pairs with `[[spokeo]]` — different broker blend; cross-check to catch records one misses.

## Trust & verifiability
`trust: unverified` — a commercial broker aggregating public + marketing data; useful for lead generation but prone to record-mixing and staleness, so corroborate every field.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | beenverified-com |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, email, address → address, phone, email, social-profile, associate, dob |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
