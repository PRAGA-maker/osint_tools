---
id: public-email-records
name: Public Email Records
description: Use when you want to try a reverse-email lookup for an owner name/location — an obscure aggregator site that typically funnels to a paid people-search.
url: http://publicemailrecords.com
category: email
path:
- email
bestFor: A last-resort reverse-email-to-identity guess; in practice usually a lead-gen funnel to a paid people-search vendor.
selectorsIn:
- email
selectorsOut:
- name
- address
- phone
status: unknown
pricing: freemium
costNote: Advertised as free but typically gates real results behind a paid third-party people-search subscription.
opsec: passive
opsecNote: Searching is passive against the target, but you submit the query (and possibly your IP) to an unknown operator — use a VPN and a clean browser.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Obscure site with no verifiable provenance; HTTP-only, name implies a public-records reverse lookup but data quality and operator are unknown. Treat any "hit" with heavy skepticism.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
source: metaosint
lastVerified: ''
enrichment: full
---

# Public Email Records

> An obscure reverse-email-lookup site that claims to map an address to its owner; in practice it behaves like a lead-generation funnel to paid people-search products.

## When to use
You have only an `email` and want to attempt a reverse pivot to a `name`, `address`, or `phone`. Reach for this only as a low-confidence, last-resort check after better-known reverse-email tools, because the operator and data sourcing are unverified.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site over a VPN / clean browser (it is HTTP-only, no TLS).
2. Enter the target email in the lookup field.
3. Expect a teaser result that then prompts payment or redirects to a third-party people-search.
4. Treat any preview "match" as a lead to corroborate elsewhere — never as fact.

## Inputs → Outputs
- **In:** `email`
- **Out:** claimed `name` / `address` / `phone` (unverified, often paywalled).
- **Empty/negative result looks like:** "no records found," or a generic upsell page with no specific data.

## Gotchas & OpSec
- Human-in-the-loop: payment-wall-partial — real data is usually gated.
- OpSec: HTTP-only and operator-unknown; do not submit your real identity, use a VPN. Passive toward the subject but you trust an unknown party with your query.

## Overlaps ("do both")
- Cross-check any claim against `[[reverse-whois]]` and mainstream reverse-email tools before believing it.

## Trust & verifiability
`trust: unverified` — no clear ownership, HTTP-only, likely an affiliate funnel. Data accuracy cannot be confirmed; do not rely on it as a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | public-email-records |
| category | email |
| selectorsIn → selectorsOut | email → name, address, phone |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
