---
id: wikitravel-org
name: Wikitravel — Phone Numbers
description: Use when you have a `phone` number and want to interpret its country/dialing format — returns reference context (country, trunk/international prefixes), not a subscriber identity.
url: https://wikitravel.org/en/Wikitravel:Phone_numbers
category: phone
path:
- phone
bestFor: Understanding how a phone number's country code, trunk prefix, and dialing format work when normalizing an unfamiliar international number.
selectorsIn:
- phone
selectorsOut: []
status: degraded
pricing: free
costNote: Free public wiki page. No account, no lookup service — it is documentation, not a database.
opsec: passive
opsecNote: Reading a static wiki page reveals nothing about the target and does not touch any phone network. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-edited travel wiki page; Wikitravel is largely frozen/abandoned in favor of Wikivoyage, so content may be dated.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Wikitravel Phone Numbers
tags:
- mobilephone
- Mobile & Phone Related
- reference
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- wikitravel
---

# Wikitravel — Phone Numbers

> A reference page on how international phone numbers and dialing conventions work — context for reading a number, not a reverse-lookup tool.

## When to use
You have a `phone` number in an unfamiliar international format and need to make sense of it before running any actual lookup: which country the code points to, how trunk ("0") and international ("+"/"00") prefixes are added or dropped, and how to normalize it into E.164 for other tools. This is a *reference* stop, not a data source — it will not tell you who owns a number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wikitravel.org/en/Wikitravel:Phone_numbers.
2. Read the conventions: country calling codes, the difference between the international access prefix and the national trunk prefix, and how local vs. international dialing differ.
3. Apply it to your number — strip/normalize the prefix, confirm the country, and rewrite into a clean `+<country><number>` form.
4. Pivot: take the normalized `phone` to an actual lookup/enrichment tool (carrier/HLR lookup, messaging-app checks, reverse directories) — that is where an identity would come from.

## Inputs → Outputs
- **In:** `phone` (as a mental/reference exercise — nothing is submitted)
- **Out:** none — this yields *understanding* (country, format), not selectors about a person.
- **Empty/negative result looks like:** the page is documentation, so there is no "result"; if the wiki is unreachable, use any standard country-calling-code reference instead.

## Gotchas & OpSec
- This is NOT a reverse phone lookup — despite living in the `phone` category, it returns no name, address, or profile. Set expectations accordingly.
- Wikitravel is largely dormant (superseded by Wikivoyage); treat details as a rough guide and confirm current dialing rules elsewhere if precision matters.
- OpSec: fully **passive** — reading a wiki reveals nothing.

## Overlaps ("do both")
- Use before, not instead of, real phone-OSINT tools: normalize the number here, then run it through an actual lookup service for identity/carrier data.

## Trust & verifiability
`trust: community` — an editable wiki, so accuracy depends on contributors and freshness; cross-check any specific dialing rule against a current source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikitravel-org |
| category | phone |
| selectorsIn → selectorsOut | phone → — |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
