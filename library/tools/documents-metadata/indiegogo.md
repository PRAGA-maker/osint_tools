---
id: indiegogo
name: Indiegogo
description: Use when you have a `name`, `username`, or project and want their crowdfunding footprint — returns campaigns exposing `employer-org`, `associate`, and location leads.
url: https://www.indiegogo.com
category: documents-metadata
path:
- documents-metadata
bestFor: Finding a subject's crowdfunding campaigns (as creator or backer) and the people/place details they reveal.
selectorsIn:
- name
- username
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free to search and read public campaigns; backing a project costs money but is never needed for research.
opsec: passive
opsecNote: Browsing and searching public campaigns is passive. Do NOT back a campaign, comment, or message the creator from an attributable account — that is active contact. Reading a public profile page doesn't notify the owner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major, established crowdfunding platform; campaign pages are self-published by creators, so treat their claims as claims, but the account/activity metadata is authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- kickstarter
- gogetfunding
- fundrazr
aliases:
- indiegogo.com
tags:
- crowdfunding
- financial-footprint
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Indiegogo

> A major crowdfunding platform — a place a subject may have launched or backed a campaign, leaving behind names, employers, locations, and a dated activity trail.

## When to use
Your subject may have run a crowdfunding campaign (a product, film, cause, or personal fundraiser) or backed one. A campaign page is a rich disclosure: the creator's `name`/handle, often a business (`employer-org`) and team members (`associate`), a location, contact links, an update history with dates, and comments that can reveal a network. Useful for confirming a professional venture, a timeline, or a place tie.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.indiegogo.com and use the search box for the `name`, `username`, project name, or brand.
2. Also run a site-scoped engine query — `site:indiegogo.com "Full Name"` — since on-site search misses profile/comment mentions.
3. Open matching campaigns and profiles: read the creator/team names, linked company and socials, stated location, funding dates, and updates.
4. Pivot: team members → `associate`; linked company → `employer-org`; external links/socials → new `social-profile`/`domain` selectors; comments → connected accounts.

## Inputs → Outputs
- **In:** `name` / `username` / project or brand name
- **Out:** campaigns → `employer-org`, `associate`, location and dated activity
- **Empty/negative result looks like:** no campaigns or only unrelated same-name projects. Most people have never run one — absence means nothing beyond "not a crowdfunder here." Try `[[kickstarter]]` and other platforms too.

## Gotchas & OpSec
- Creator claims (location, affiliations) are self-reported marketing — corroborate before relying on them.
- On-site search is weak for people; lean on site-scoped search-engine queries.
- OpSec: passive for viewing. Backing/commenting/messaging is active and attributable — don't.

## Overlaps ("do both")
- Run the same name across `[[kickstarter]]`, `[[gogetfunding]]`, and `[[fundrazr]]` — a subject may have used a different platform, and personal-fundraiser sites in particular carry location and family/`associate` detail.

## Trust & verifiability
`trust: trusted` — Indiegogo is a legitimate, well-known platform, so account existence and activity dates are reliable; the narrative content of a campaign is self-published and needs corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | indiegogo |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, username → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
