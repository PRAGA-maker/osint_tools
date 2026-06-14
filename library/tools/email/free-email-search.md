---
id: free-email-search
name: FREE Email Search
description: Use when you have an email address and want to find the linked name, possible phone, and addresses via a US people-search data broker.
url: https://www.spytox.com/email-search
category: email
path:
- email
bestFor: Reverse-email lookup against US consumer/people-search records (name, phone, address).
selectorsIn:
- email
selectorsOut:
- name
- phone
- address
- associate
status: live
pricing: freemium
costNote: Spytox shows teaser results free, then up-sells a paid report / redirects to a paid people-search partner.
opsec: passive
opsecNote: Server-side lookup against aggregated public/broker records; the subject is not notified. The address you search is disclosed to the broker.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Spytox is a known US people-search/data-broker site; coverage is US-centric and aggregated, so results vary in freshness and accuracy and should be corroborated.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Spytox
tags:
- email
relatedTools: []
source: metaosint
lastVerified: ''
enrichment: full
---

# FREE Email Search (Spytox)

> Reverse-email people-search broker that maps a US email address to a likely name, phone, and address.

## When to use
You have an `email` for a missing person or an associate and want to resolve it to a `name`, `phone`, `address`, or `associate` links. Best for US subjects; weak outside the US.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.spytox.com/email-search.
2. Enter the `email` address.
3. Read the teaser result — name and partial location/phone are usually shown free; full details are gated behind a paid report or a partner redirect.
4. Pivot: take the returned `name` + location into a dedicated people-search / public-records tool, and corroborate before trusting.

## Inputs → Outputs
- **In:** `email`
- **Out:** `name`, possible `phone`, `address`, `associate`
- **Empty/negative result looks like:** "no records found," or a generic landing page that only offers a paid search with no preview — treat as no match.

## Gotchas & OpSec
- Data-broker accuracy is uneven: records can be stale, merged across people, or wrong. Always corroborate with a second source.
- Human-in-the-loop: full detail is behind a partial paywall / partner redirect.
- OpSec: passive toward the subject; the searched address is logged by the broker.

## Overlaps ("do both")
- Run the same `email` through breach-search and other reverse-email brokers — coverage barely overlaps and each surfaces different identities.

## Trust & verifiability
`trust: community` — established but commercial US data broker; output is aggregated and not authoritative. Verify any identity it returns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-email-search |
| category | email |
| selectorsIn → selectorsOut | email → name, phone, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
