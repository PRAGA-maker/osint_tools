---
id: addresssearch-email-and-address-lookup-united-states
name: AddressSearch Email & Address Lookup (United States)
description: Use when you have an `email` (or `name`) in the US and want the linked mailing address, or a reverse-email match — returns address and email from a large opt-in-style index.
url: http://addresssearch.com
category: email
path:
- email
bestFor: Free US email-to-mailing-address and reverse-email lookups across a large consumer index.
selectorsIn:
- email
- name
selectorsOut:
- address
- email
status: degraded
pricing: free
costNote: Advertised as a free lookup service (email and mailing-address search, reverse email). No payment claimed; the site was intermittently unreachable at last check, so treat availability as flaky.
opsec: passive
opsecNote: Passive — you query a third-party consumer-data index, not the subject, so no notification reaches them. The site says it protects the searched person's privacy, but assume your query is logged; use a clean/sock browser and do not enter your own identifiers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial US consumer-data lookup harvested via Toddington's directory; data provenance and freshness are not independently verified, so treat hits as leads to corroborate.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- AddressSearch
- addresssearch.com
tags:
- toddington
- curated-directory
- email-addresses
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# AddressSearch Email & Address Lookup (United States)

> A free US consumer-data lookup that maps an email to a mailing address (and back) across a claimed ~95M email / ~140M address index.

## When to use
You have a US subject's `email` and want to tie it to a current or past mailing `address`, or you have an address/name and want a matching email. It's a broad consumer-data index, so it's best as an early, cheap enrichment step that hands you an address or email to verify against stronger sources — not as authoritative proof on its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://addresssearch.com in a clean/sock browser. If it doesn't load, retry later — availability has been flaky.
2. Choose the search type: email → mailing address, name/address → email, or reverse email.
3. Enter the `email` (or `name`) and submit.
4. Read the output: a matched mailing `address` and/or `email`. A confident hit is a specific address tied to the input; a weak result is a generic or empty match.
5. Pivot: a returned address feeds property/records and people-search tools; a returned email feeds breach-check and account-existence checks like [[account-live-com]].

## Inputs → Outputs
- **In:** `email` (or `name`/`address`)
- **Out:** `address` (mailing), `email`
- **Empty/negative result looks like:** "no results" or only a broad city/state with no street — meaning the identifier isn't in the index, not that the person has no address.

## Gotchas & OpSec
- US-only consumer data; irrelevant for non-US subjects.
- Data can be stale or conflated between people sharing a name — corroborate before relying on it.
- OpSec: passive; subject is not alerted. Availability is unreliable, so don't treat a failed load as a negative result.

## Overlaps ("do both")
- Pairs with [[account-live-com]] and other email tools — this returns a physical address for an email, those confirm the email is a live account. Run both to move from "email exists" to "email → real-world address."

## Trust & verifiability
`trust: unverified` — a commercial consumer-data broker surfaced through a curated directory. Its matches are investigative leads to confirm against authoritative records, not standalone facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | addresssearch-email-and-address-lookup-united-states |
| category | email |
| selectorsIn → selectorsOut | email, name → address, email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
