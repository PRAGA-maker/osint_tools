---
id: find-people-search-us
name: Find People Search (US)
description: Use when you have a `name` and want a free first-pass US people-search that surfaces addresses, phones, relatives and possible social profiles — returns address, phone, email, associate, social-profile, dob.
url: https://findpeoplesearch.com
category: people-search
path:
- people-search
bestFor: A free name-first sweep of US public-records aggregations for contact info and a relative graph.
selectorsIn:
- name
selectorsOut:
- address
- phone
- email
- associate
- social-profile
- dob
status: live
pricing: freemium
costNote: Basic name/state lookups and teaser results are free; full contact details, exact-name reports and background-style detail sit behind a paid report (positioned as a cheaper alternative to BeenVerified/Spokeo/Intelius).
opsec: passive
opsecNote: Searching is passive against the subject — they are not notified. But you are handing the target's name to a commercial data broker that logs queries and may retarget you with ads; use a sock-puppet browser/session and never enter your own identifying details.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial people-search aggregator; data is scraped/licensed from public records and marketing databases, so results are lead-quality and need corroboration, not proof.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- FindPeopleSearch
- findpeoplesearch.com
tags:
- people-search
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Find People Search (US)

> A free-to-start US people-search aggregator: type a name, get a candidate list of addresses, phones, and relatives to triage.

## When to use
You have a `name` (ideally plus a US city/state or approximate age) and want a quick, no-account first pass to generate `address`, `phone`, `associate` (relatives/known associates) and possible `social-profile` leads. Best as an early triage step to decide which candidate is your subject before spending on a paid report or a more authoritative source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://findpeoplesearch.com in a clean/sock-puppet browser.
2. Enter the subject's `name`; narrow with city/state, approximate age, or a prior address when the free form allows it.
3. Read the free result list — usually name, age band, current/previous cities, and partial phones/relatives — and match against what you already know to isolate the right person.
4. Treat the paywall as a decision point: the free teaser is often enough to confirm identity and hand off; only pay if the full report is worth it and you accept the broker interaction.
5. Pivot: a relative (`associate`) name feeds another people-search or `[[os-divorce-records]]`; a prior `address` anchors timeline; a surfaced `social-profile` feeds username enumeration.

## Inputs → Outputs
- **In:** `name` (+ optional city/state, age, prior address, email)
- **Out:** `address`, `phone`, `email`, `associate`, `social-profile`, `dob`/age band
- **Empty/negative result looks like:** no matching candidates, or only generic "records may exist, buy report" upsells with no distinguishing teaser — treat as unconfirmed, not as "person doesn't exist." Common US names produce many false candidates; do not assume the first result is your subject.

## Gotchas & OpSec
- Human-in-the-loop: the useful detail is frequently gated behind a paid report; know when the free teaser already answered your question.
- Data-broker quality: addresses/phones can be stale or misattributed to a same-named person. Corroborate before acting.
- Not an FCRA-permissible source — do not use for employment, tenancy, or credit decisions.

## Overlaps ("do both")
- Pairs with `[[os-divorce-records]]` because this gives the relative/associate graph and prior addresses while the divorce directory pins the authoritative court record behind an associate link.

## Trust & verifiability
`trust: community` — a commercial aggregator with unaudited sourcing; every hit is a lead to verify against a primary record, not an authoritative fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-people-search-us |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, email, associate, social-profile, dob |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
