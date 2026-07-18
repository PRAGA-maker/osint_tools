---
id: shopperapproved
name: Shopper Approved
description: Use when you have a merchant/store name and want to read its collected customer reviews — returns reviewer first-name + location fragments and review text, occasionally pivotable.
url: https://www.shopperapproved.com
category: search-engines
path:
- search-engines
bestFor: Reading a specific online store's public review wall to surface reviewer names/locations and buyer sentiment.
selectorsIn:
- employer-org
selectorsOut:
- name
- address
status: live
pricing: freemium
costNote: Free to read published review pages; the paid product is the merchant-side collection service (free 15-day trial), not review browsing.
opsec: passive
opsecNote: Passive — you read published review pages; no query is tied to a person and nothing is sent to a subject. Reviewer data shown is limited (first name + coarse location), so treat fragments as leads, not confirmed identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial review-collection platform (100M+ reviews across 10k+ stores); reviews are merchant-solicited, so selection is skewed positive and reviewer identity is only partial.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- shopperapproved.com
tags:
- toddington
- curated-directory
- reviews
- e-commerce
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Shopper Approved

> A merchant review-collection platform whose public review walls occasionally expose reviewer first names and locations — a thin, sideways OSINT source, not a people-search.

## When to use
You are investigating a specific online store/merchant (as an employer, a scam vendor, or a business a subject is tied to) and want to read the customer reviews it has collected — both for reputation/sentiment and to see whether any review exposes a reviewer's first name + city that you can cross-reference. It is best treated as a corroboration source: it will not let you search by a person, and reviewer identity is deliberately partial.

## How to use it (`bestInteractionPattern`: web-manual)
1. Find the store's Shopper Approved certificate/review page — usually linked from the merchant's own site, or search `site:shopperapproved.com <store name>`.
2. Read the review wall: star ratings, review text, and the reviewer label (typically first name + last initial + a coarse location like city/state).
3. If a review mentions specifics (a name, a location, a purchase detail) relevant to your case, note it as a lead.
4. Pivot: a reviewer's first name + city is a weak selector — combine it with the merchant/product context and feed it into a broader name or social-profile search.

## Inputs → Outputs
- **In:** a merchant / store `employer-org` name
- **Out:** review text plus partial reviewer identity — first `name` fragment and coarse `address`/location
- **Empty/negative result looks like:** a store that doesn't use Shopper Approved has no page here; and even where a page exists, reviewer identity is minimal — expect fragments, not full names.

## Gotchas & OpSec
- **Merchant-side skew:** reviews are solicited by the store, so the sample runs positive and is not a neutral record.
- Reviewer identity is intentionally partial (first name + last initial + city); do not treat a match as confirmation without corroboration.
- The site's own product is the paid collection service for merchants — that paywall does not affect reading already-published review pages.

## Overlaps ("do both")
- Pairs with general review/reputation and name-search tools — this surfaces a merchant's own review wall, and those broaden a partial reviewer identity into a person.

## Trust & verifiability
`trust: community` — a commercial platform hosting merchant-solicited reviews at scale; the content is real but selection-biased and identity-thin, so use it for context and leads rather than as authoritative identity data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shopperapproved |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → name, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
