---
id: yourclassifieds-ca-canada
name: Yourclassifieds.ca (Canada)
description: Use when you have a `name`, `phone` or locale and want a subject's classified ads across Ontario — returns ad contact details, address hints and associates.
url: http://yourclassifieds.ca
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a person's buy/sell, real-estate or services ads across Ontario's Metroland community papers.
selectorsIn:
- name
- phone
selectorsOut:
- phone
- address
- name
status: live
pricing: free
costNote: Free to browse and search ads; posting or managing your own ads needs a (free) registered account. Searching does not.
opsec: passive
opsecNote: Browsing/searching ads is passive and discloses nothing to the poster. If you contact an advertiser, use a sock-puppet identity — that step is active and reveals you to the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legitimate classifieds network for Metroland's ~113 Ontario community newspapers; ad content is self-posted, so contact details are user-supplied and unverified.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- YourClassifieds.ca
- Metroland classifieds
tags:
- toddington
- curated-directory
- classifieds
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Yourclassifieds.ca (Canada)

> The online classifieds arm of Metroland's ~113 Ontario community newspapers — a regional place to find a subject's for-sale, real-estate, garage-sale or services ads and the contact details attached to them.

## When to use
You have a `name`, a `phone` number, or a locale for someone in Ontario and want to see whether they post classified ads. People routinely leave a phone number, a first name, a neighbourhood, or a business name in an ad, so a matching listing can hand you fresh contact details, an approximate location, or evidence of activity/interests — a useful pivot when a subject is otherwise thin online.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://yourclassifieds.ca and use the keyword/category search.
2. Search the `name`, a business name, or a `phone` number; browse by region + category (real estate, buy/sell, services, garage sales) to narrow to a locale.
3. Read matching ads for self-supplied contact details: `phone`, first `name`, neighbourhood/town (`address` hint), and item/service specifics.
4. Pivot: run the ad's phone number through phone-OSINT, and the locale/name through people-search and property records.

## Inputs → Outputs
- **In:** `name`, `phone`, or region + category
- **Out:** ad `phone`, poster `name`/handle, town/neighbourhood (`address` hint), item/service context
- **Empty/negative result looks like:** no matching ads (the person simply hasn't posted, or posted on a different platform) — classifieds are opt-in, so absence proves nothing about the subject.

## Gotchas & OpSec
- All content is **self-posted and unverified** — a phone number or name in an ad is a lead to corroborate, not a confirmed fact; sellers often use burner numbers or partial names.
- Coverage is **Ontario-centric** (Metroland footprint); it won't help outside that region.
- OpSec: searching is passive. **Contacting** an advertiser is active and reveals you — always use a sock-puppet if you take that step.

## Overlaps ("do both")
- Pair with Kijiji and other Canadian classifieds plus phone-OSINT — different platforms carry different ads, and a phone number recovered here often resolves an identity elsewhere.

## Trust & verifiability
`trust: unverified` — a legitimate, established regional classifieds network, but the actual ad data is user-generated and unverified; always confirm any contact detail against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yourclassifieds-ca-canada |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone → phone, address, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
