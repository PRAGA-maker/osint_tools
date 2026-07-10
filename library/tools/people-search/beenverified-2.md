---
id: beenverified-2
name: BeenVerified
description: Use when you have a US `name`, `phone`, `email` or `address` and want an aggregated background report — returns `address`, `phone`, `associate` (relatives) and record leads.
url: https://beenverified.com
category: people-search
path:
- people-search
bestFor: US background checks combining address history, relatives, phones, emails and public records.
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
costNote: Searching is free (you see that a report exists and a teaser), but viewing full reports requires a paid subscription. Effectively paywalled for the useful detail.
opsec: passive
opsecNote: Passive — BeenVerified queries aggregated public records; the subject is not notified. A subscription requires account + payment, a trail on your side — use appropriate billing hygiene. FCRA-restricted: must NOT be used for employment, tenant, or credit decisions.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A major commercial US data broker; coverage is broad but records are frequently stale or conflated across same-name individuals — corroborate before acting.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: true
aliases:
- BeenVerified
- beenverified.com
tags:
- background-check
- public-records
- people-search
source: gh-topic-footprinting
lastVerified: '2026-07-10'
enrichment: full
---

# BeenVerified

> A mainstream US background-check aggregator: feed it a name, phone, email, or address and it assembles address history, relatives, contact numbers, and public-record hits into one report.

## When to use
You have a US `name`, `phone`, `email`, or `address` and want a consolidated background picture — prior addresses, relatives and associates (`associate`), phone/email links, and pointers to court/criminal/property records. Strong as a paid "one report" step in a US locate/missing-persons trace when free tools (FamilyTreeNow, PeekYou) have taken you as far as they can.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://beenverified.com and search by `name` (+ state), `phone`, `email`, or `address`.
2. The free search confirms a report exists and teases its contents; the full report needs a subscription.
3. Subscribe (account + payment) to open the report: address history, relatives/associates, phones, emails, and record flags.
4. Cross-check disambiguation cues (age, middle name, address timeline) — brokers conflate same-name people.
5. Pivot: relatives feed `[[familytree]]`; phones/emails feed reverse-lookup and breach tools; record flags feed court searches like `[[iowa-courts-online-search]]`.

## Inputs → Outputs
- **In:** US `name` (+ state), `phone`, `email`, or `address`
- **Out:** `address` history, `phone`, `associate` (relatives/associates), emails, public-record pointers, confirmed `name`/aliases
- **Empty/negative result looks like:** "no records" or a mismatched report — the subject has little US public-record footprint, or the identifier is wrong/too common. Absence isn't proof; data can be stale.

## Gotchas & OpSec
- Human-in-the-loop: **payment-wall-partial** — the useful detail is subscription-gated.
- OpSec: **passive** to the target; your subscription is a trail — use billing hygiene.
- **FCRA:** not for employment/tenant/credit decisions. Records are often stale/conflated — verify.

## Overlaps ("do both")
- Pairs with `[[familytree]]` and `[[peekyou-people-search]]` (free coverage) — run the free tools first, then BeenVerified to consolidate and add record pointers. Confirm cross-tool before trusting.

## Trust & verifiability
`trust: community` — a large, reputable-brand broker, but aggregated and error-prone (staleness, same-name conflation). Treat every field as a lead to confirm against a primary record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | beenverified-2 |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, email, address → address, phone, associate, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
