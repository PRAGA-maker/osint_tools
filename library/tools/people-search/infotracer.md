---
id: infotracer
name: InfoTracer
description: Use when you have a `name`, `phone`, `email`, or `address` and want a US background/contact profile — returns addresses, phones, relatives (`associate`) and public-record hits behind a paywall.
url: https://infotracer.com/
category: people-search
path:
- people-search
bestFor: US people-search / background lookup aggregating contact, address, relatives, and public records.
selectorsIn:
- name
- phone
- email
- address
selectorsOut:
- address
- phone
- associate
- name
status: live
pricing: freemium
costNote: Free search shows a teaser/preview (that a record exists); the actual report — contact details, addresses, relatives, criminal/court records — is behind a paid subscription. No usable free full report.
opsec: passive
opsecNote: You query a data-broker aggregator, not the subject, so nothing reaches the target. But you must create an account and pay, associating the search with your payment identity — use a sock-puppet account and privacy-preserving payment. Note results are aggregated from brokers and can be stale or wrong.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial US data-broker/people-search aggregator. Convenient breadth, but broker data is frequently outdated or conflated across same-name individuals — corroborate every field before relying on it.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- truepeoplesearch
- spokeo
- beenverified
aliases:
- InfoTracer
- infotracer.com
tags:
- people-investigations
- data-broker
- background-check
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# InfoTracer

> A paid US people-search aggregator that bundles addresses, phones, relatives, and public-record hits into one background report from a name, number, email, or address.

## When to use
You have a US-context `name`, `phone`, `email`, or `address` and want a broad first-pass profile: current/past addresses, phone numbers, associated `associate`s (relatives, possible associates), and public-record flags (court, criminal, property). Useful for building a starting picture of a US subject or corroborating leads from free tools — with the strong caveat that it's a data broker whose accuracy is uneven.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://infotracer.com/ and choose the search type (name, phone, email, address, VIN).
2. Enter the selector and run the search — the free result confirms a record exists and previews limited fields.
3. To see the full report you must register and pay (subscription); use a **sock-puppet** account and privacy-conscious payment.
4. Read the report: addresses/history, phones, relatives/associates, and public-record hits.
5. Pivot: cross-check every field against free sources (`[[truepeoplesearch]]`) and other brokers (`[[spokeo]]`, `[[beenverified]]`); a relative/address is a lead, not a fact, until confirmed.

## Inputs → Outputs
- **In:** `name`, `phone`, `email`, or `address` (US)
- **Out:** address history, `phone`s, `associate`s (relatives), public-record hits, confirmed `name`
- **Empty/negative result looks like:** "no records" or a thin preview — the person may have little US broker footprint, or the selector is a variant. Broker gaps are common; absence isn't confirmation.

## Gotchas & OpSec
- Human-in-the-loop: **payment wall** — the useful output requires paying; budget and use a burner account.
- OpSec: **passive** toward the subject, but you disclose the query to a broker and tie it to your payment identity — sock puppet + private payment.
- Data quality is the big risk: broker aggregates conflate same-name people and carry stale addresses. Never treat a single InfoTracer field as ground truth.

## Overlaps ("do both")
- Pairs with free `[[truepeoplesearch]]` and other paid brokers (`[[spokeo]]`, `[[beenverified]]`) — run a free source first, then compare brokers, because each buys from different data suppliers and no single one is complete or reliable. Consensus across sources is what you trust.

## Trust & verifiability
`trust: community` — a legitimate commercial aggregator, not an authoritative record. Its breadth is useful for leads; verify each address/relative/record against an independent or primary source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | infotracer |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, email, address → address, phone, associate, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
