---
id: loot-com-classified-ads-united-kingdom
name: Loot.com Classified Ads (United Kingdom)
description: Use when you have a `name`, `phone` or UK locale and want a subject's classified ads — returns ad contact details, location hints and item context.
url: https://www.loot.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a person's buy/sell, property, jobs or services ads across the UK with the contact details attached.
selectorsIn:
- name
- phone
selectorsOut:
- phone
- address
- name
status: live
pricing: free
costNote: Free to browse and search ads across the UK. Posting/managing ads needs a free account; searching does not.
opsec: passive
opsecNote: Searching and reading ads is passive and discloses nothing to the poster. Contacting an advertiser is active and reveals you — use a sock-puppet identity for any outreach.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A live UK classifieds marketplace (successor to the historic Loot listings brand); ad content is user-submitted and unverified.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Loot
- loot.com
tags:
- toddington
- curated-directory
- classifieds
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Loot.com Classified Ads (United Kingdom)

> A live UK-wide buy-and-sell classifieds site — a place to find a subject's ads across property, vehicles, jobs and services and pull the phone number, name, and location they left behind.

## When to use
You have a `name`, a `phone` number, or a UK locale for a subject and want to see whether they post classified ads. Ads are self-posted, so a match can hand you fresh contact details (`phone`, a name, a town), plus evidence of activity, possessions, or a job — a useful pivot when someone is otherwise thin online.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.loot.com and use the keyword/category/location search.
2. Search the `name`, a business name, or a `phone` number; narrow by UK region and category (Cars & Vehicles, Property, Jobs, Services, Community, etc.).
3. Read matching ads for self-supplied details: `phone`, poster `name`/handle, town/area (`address` hint), item/service specifics.
4. Pivot: run the ad's phone number through UK phone-OSINT and the locale/name through people-search and the electoral roll.

## Inputs → Outputs
- **In:** `name`, `phone`, or location + category
- **Out:** ad `phone`, poster `name`/handle, town/area (`address` hint), item/service context
- **Empty/negative result looks like:** no matching ads — the person hasn't posted here or used another platform (Gumtree, Facebook Marketplace); classifieds are opt-in, so absence proves nothing.

## Gotchas & OpSec
- All content is **self-posted and unverified**; treat a phone number or name in an ad as a lead to corroborate, not a confirmed fact — sellers often use burner numbers or partial names.
- Coverage is UK-wide but activity is uneven versus dominant platforms like Gumtree/Facebook Marketplace — search those too.
- OpSec: searching is passive; **contacting** an advertiser is active and reveals you — always use a sock-puppet for outreach.

## Overlaps ("do both")
- Pair with Gumtree, Facebook Marketplace and UK phone-OSINT — different platforms carry different ads, and a phone number found in one often resolves an identity in another.

## Trust & verifiability
`trust: unverified` — a legitimate live UK classifieds site, but the ad data itself is user-generated; confirm any contact detail against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | loot-com-classified-ads-united-kingdom |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone → phone, address, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
