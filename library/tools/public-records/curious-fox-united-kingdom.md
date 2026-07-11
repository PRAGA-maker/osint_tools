---
id: curious-fox-united-kingdom
name: Curious Fox (United Kingdom)
description: Use when you have a `name`/surname tied to a UK or Irish village and want to reach people researching that family/place — returns village-linked genealogy posts and a way to contact the researchers behind them.
url: http://www.curiousfox.com
category: public-records
path:
- public-records
bestFor: Village-by-village UK/Ireland genealogy contact board — connecting to others researching a surname or locality.
selectorsIn:
- name
- address
selectorsOut:
- name
- associate
- address
status: live
pricing: freemium
costNote: Free members can post entries but cannot initiate contact; only paid members can message others. Searching/browsing entries is free.
opsec: passive
opsecNote: Passive research board — no email addresses are exposed (anti-spam by design), and contact is mediated through the site. Posting your own query reveals your research interest to other members, so use a sock-puppet handle if the enquiry is sensitive.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running community genealogy contact site; content is user-submitted research queries, not authoritative records — treat leads as tips to verify.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: true
aliases:
- CuriousFox
- curiousfox.com
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Curious Fox (United Kingdom)

> A village-by-village contact board for UK and Ireland family history — you find others researching the same surname or place and open a line to them, rather than querying a record set.

## When to use
You have a `name`/surname anchored to a specific UK or Irish village, town, or county and want to reach living researchers (often relatives or local historians) who may know the family. Valuable in a missing-person or long-lost-relative case for finding people who can supply context, older addresses, and family connections that no database holds.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.curiousfox.com and search by surname, location/village, or keyword; the geosearch expands to surrounding areas.
2. Read matching posts: research queries naming ancestors with dates, places, occupations, and the questions the poster is chasing.
3. To make contact, note that only paid members can message posters — upgrade, or post your own (free) entry and wait for replies.
4. Exchange information through the site (no email addresses are shown by design).
5. Pivot: a responding researcher can yield `associate`/family links and historic `address`es to feed records tools.

## Inputs → Outputs
- **In:** surname/`name` + village/locality (`address`)
- **Out:** village-linked genealogy posts, named ancestors/`associate`s, historic locations, and a mediated contact route to the poster
- **Empty/negative result looks like:** no posts for the surname/village — common for less-researched families; absence means no one has posted, not that the family isn't from there.

## Gotchas & OpSec
- Contact is paywalled: free accounts can post but not message; budget for a paid tier if you need to reach someone.
- User-generated: entries are hobbyist research, sometimes speculative — corroborate any "fact" against records.
- OpSec: passive; no emails exposed. Use a sock-puppet handle if you don't want your enquiry linked to you.

## Overlaps ("do both")
- Pairs with genealogy/BMD sources like `[[myfamilyannouncements-co-uk]]` and `[[thegazette-co-uk]]` — Curious Fox finds *people* who know the family, while those find the *records* to verify what they tell you.

## Trust & verifiability
`trust: community` — a user-driven contact board, not a record authority; its value is the human connections it brokers, all of which need independent verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | curious-fox-united-kingdom |
| category | public-records |
| selectorsIn → selectorsOut | name → name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
