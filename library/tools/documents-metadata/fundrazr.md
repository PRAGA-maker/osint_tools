---
id: fundrazr
name: FundRazr
description: Use when you have a `name` and want their public crowdfunding campaigns — returns organiser identity, story details, location hints and beneficiary/associate links.
url: https://fundrazr.com
category: documents-metadata
path:
- documents-metadata
bestFor: Finding a person's public FundRazr fundraising campaigns and the identity, story and associates they reveal.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
- associate
- address
status: live
pricing: free
costNote: Free to browse campaigns; free to create (the platform takes a fee/tip, not an upfront charge).
opsec: passive
opsecNote: You browse public campaign pages; the organiser is not notified of a view. Do not donate to or message a subject's campaign — that is contact and may alert them or move money.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate crowdfunding platform; campaign details are self-published by organisers, so names, stories and locations are claims to corroborate, not verified facts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- fundrazr.com
tags:
- toddington
- curated-directory
- crowdfunding
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# FundRazr

> A crowdfunding platform whose public campaign pages can tie a `name` to a personal story, a location, named beneficiaries and supporters — a source of self-disclosed detail during a person search.

## When to use
Your subject may have run or benefited from a fundraiser — medical, memorial, legal, travel, community. FundRazr campaigns are often richly personal: organiser and beneficiary names, a narrative that fixes places, dates and relationships, photos, and a comment/donor trail of associates. Searching a `name` here can surface a candid, first-person account that corroborates identity, location or a life event.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search FundRazr (and a site-scoped web search: `site:fundrazr.com "name"`) for the subject's name or associated cause.
2. Open matching campaigns; read the organiser/beneficiary names, the story (for place/date/relationship detail), and public comments/supporters.
3. Capture the page (screenshot + timestamp) before it changes, and note associates from the supporter list.
4. Pivot: feed named organisers/beneficiaries/supporters into people- and social-search; use location clues in the story for geolocation.

## Inputs → Outputs
- **In:** `name` (organiser, beneficiary, or associated cause)
- **Out:** organiser/beneficiary `name`, story-derived `address`/location hints, supporter `associate`s, links to `social-profile`s
- **Empty/negative result looks like:** no campaigns, or a campaign with only a first name and no locating detail — organisers control disclosure and some share little.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; never donate or comment (that is contact and moves money).
- OpSec: passive — viewing a public campaign is not visible to the organiser.
- Verification: campaign narratives are self-authored and sometimes embellished or fraudulent; treat every detail as a claim to corroborate.

## Overlaps ("do both")
- Pairs with other crowdfunding platforms (GoFundMe, etc.) and social search because a person may fundraise on several, and supporters named here resolve into associates elsewhere.

## Trust & verifiability
`trust: community` — a real platform hosting self-published campaigns; the personal detail is valuable as leads but must be verified against independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
