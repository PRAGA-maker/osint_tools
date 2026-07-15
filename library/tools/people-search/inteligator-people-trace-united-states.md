---
id: inteligator-people-trace-united-states
name: Inteligator People Trace (United States)
description: Use when you have a `name` (optionally + state) and want a US background-style report — returns address, phone, email, relatives and public-records hits, behind a paid subscription.
url: http://www.inteligator.com/home/index.php?tab=4
category: people-search
path:
- people-search
bestFor: Aggregated US background reports (address history, phones, relatives, criminal/records hits) from a single name query.
selectorsIn:
- name
selectorsOut:
- address
- phone
- email
- associate
- dob
status: live
pricing: freemium
costNote: "Not usably free: the name search runs and shows a teaser, but viewing the report requires a subscription — commonly a $1/day trial that rolls into ~$19.95/month. Treat as paid; the free step only confirms a record may exist."
opsec: passive
opsecNote: You query an aggregator's database, not the subject — the person is not notified. But you must create an account and enter payment to see results, so your own identity/payment is exposed to Inteligator; use a dedicated investigative account, not personal details.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial background-check aggregator (claims 2B+ records, 50 states); reviewers report broad coverage but frequent stale/incorrect relatives, emails and profiles — corroborate everything.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- Inteligator
- inteligator.com
tags:
- toddington
- curated-directory
- people-search
- background-check
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# Inteligator People Trace (United States)

> A commercial US people/background aggregator: one name (plus state) fans out into address history, phones, relatives and public-records hits — but the report sits behind a paid subscription.

## When to use
You have a US subject's `name` (ideally narrowed by state) and want a fast, one-stop aggregation of address history, phone numbers, likely relatives/associates, and record hits (criminal, marriage/divorce, property) to build a lead list. Best when you already expect to pay for at least one report and want breadth in a single pass rather than stitching free sources together.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the People Search tab at http://www.inteligator.com/ and enter the subject `name`; add the U.S. state to cut down on same-name collisions.
2. Submit — the free step returns a teaser indicating whether records appear to exist (often a count of possible matches, states, ages).
3. To see the actual `address`/`phone`/`associate`/records data you must register and start a paid trial/subscription. Use a dedicated investigative account and payment method, not personal details.
4. Read the report critically: relatives, emails, and social profiles are the fields reviewers most often find wrong — treat each as a lead to verify, not a fact.
5. Pivot: confirmed addresses/phones feed reverse-lookup and mapping; relatives feed `[[usa-official-com]]` and other people-search cross-checks.

## Inputs → Outputs
- **In:** `name` (+ optional state)
- **Out:** `address` history, `phone`, `email`, `associate`/relatives, `dob`/age, records hits
- **Empty/negative result looks like:** teaser shows zero possible matches, or the paid report returns only sparse/no records — for a common name this often means the subject is buried under namesakes, not absent.

## Gotchas & OpSec
- Human-in-the-loop: registration + a payment wall gate every real result; the "free search" is only a bait teaser.
- Data quality: reviewers consistently flag stale addresses and misattributed relatives/emails — never present an Inteligator field as confirmed without a second source.
- OpSec: passive toward the subject, but you expose your own account/payment to a data broker; compartmentalize.

## Overlaps ("do both")
- Pairs with `[[usa-official-com]]` — that is a free records aggregator you can run first to decide whether paying Inteligator for depth is worth it, and to cross-check any relatives/addresses it returns.

## Trust & verifiability
`trust: community` — it is an established commercial aggregator, but it is a reseller of bulk public-records data with well-documented accuracy problems, so its output is corroboration-grade, not authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inteligator-people-trace-united-states |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, email, associate, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, account-login) |
