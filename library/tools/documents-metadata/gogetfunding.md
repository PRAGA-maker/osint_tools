---
id: gogetfunding
name: GoGetFunding
description: Use when you have a `name` and want to find their public crowdfunding campaign — returns fundraiser text with name, location, associates and photos.
url: http://gogetfunding.com
category: documents-metadata
path:
- documents-metadata
bestFor: Locating a person's public fundraiser to mine story, location, contacts and images.
selectorsIn:
- name
selectorsOut:
- name
- geolocation
- associate
- image
status: live
pricing: free
costNote: Free to browse and search public campaigns; only creating/donating to a campaign involves money.
opsec: passive
opsecNote: Passive — you read publicly-posted campaign pages; the subject isn't contacted. Browse logged out; do not donate or message from a real account, as organisers can see donor/comment identities.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established crowdfunding platform (operating since ~2011); campaign content is self-reported by organisers and unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- gogetfunding.com
tags:
- toddington
- curated-directory
- crowdfunding
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# GoGetFunding

> A global crowdfunding platform whose public campaign pages can reveal a person's story, location, associates and photos.

## When to use
You have a `name` (or a cause/event) and want to check whether the person has run a public fundraiser — medical, funeral, travel, personal emergency. Crowdfunding pages are rich, self-published bios: they often name the organiser and beneficiary, give a town/region, list family/friends in updates and comments, and include photos — useful corroboration and pivot material. Also a channel scammers exploit, so it supports fraud checks too.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to gogetfunding.com and use its search, or run a site-scoped web search: `site:gogetfunding.com "Full Name"`.
2. Open matching campaigns and read the full story, updates and public comments.
3. Extract leads: organiser/beneficiary `name`, stated `geolocation`, named `associate`s (family/friends), and `image`s.
4. Cross-check the story's details (dates, places, other people) against independent sources.
5. Pivot: a photo feeds reverse-image search; named associates feed people-search; a location narrows other queries.

## Inputs → Outputs
- **In:** `name` (or cause/keyword)
- **Out:** `name`, `geolocation`, `associate`s, `image`s from the campaign page
- **Empty/negative result looks like:** no campaign for the name (most people never run one) — absence here says nothing about the person.

## Gotchas & OpSec
- Human-in-the-loop: none to browse.
- OpSec: passive — but never donate/comment/message from a real identity; organisers see donor and commenter names.
- Content is self-reported and unverified; treat the story as claims, and be alert to fraudulent or exaggerated campaigns.

## Overlaps ("do both")
- Run alongside other crowdfunding sites (GoFundMe, JustGiving) and general search — coverage differs per platform, so a person absent on one may have a campaign on another.

## Trust & verifiability
`trust: community` — an established platform, but each campaign is user-authored and unverified; corroborate names, locations and relationships elsewhere before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gogetfunding |
| category | documents-metadata |
| selectorsIn → selectorsOut | name → name, geolocation, associate, image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
