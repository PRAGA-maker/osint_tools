---
id: ioa
name: Information Operations Archive (IOA)
description: Use when you have a `username` or account handle and want to know whether it belongs to a documented state-linked disinformation campaign — returns attribution and associated social-profile data.
url: https://www.io-archive.org/
category: people-search
path:
- people-search
bestFor: Checking whether a social-media account/handle is part of a known, attributed information operation (troll farm) and pulling its archived posts/media.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Free to search the archive of publicly released, attributed IO datasets; bulk dataset access/downloads may require request or registration.
opsec: passive
opsecNote: You query a static research archive, not a live platform, so nothing reaches the account or its operators. Fully passive; ordinary browsing hygiene through a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A researcher-maintained archive of platform-released, rigorously attributed information-operations datasets (Twitter/X and Reddit takedowns since 2018); attribution comes from the platforms' own disclosures.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- IOA
- Information Operation Archive
- io-archive.org
tags:
- disinformation
- information-operations
- attribution
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Information Operations Archive (IOA)

> A searchable archive of attributed disinformation campaigns — check whether an account is a known state-linked troll and read its archived activity.

## When to use
You have a `username`/handle (or a campaign, country, or narrative) and need to know whether it is part of a documented information operation. IOA aggregates the datasets platforms release when they take down state-backed influence networks — 15+ countries, 54,000+ accounts, 160M+ posts, and 8 TB of media. If a subject's account appears here, that is strong, platform-sourced evidence it was an inauthentic/state-linked asset, not a real person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.io-archive.org/ in a sock-puppet browser.
2. Search by account `username`/ID, country of origin, or keyword.
3. Review matches: which attributed operation the account belongs to, plus its archived tweets/posts and media.
4. Pivot: a match tells you the account is attributed to an IO — flag it as inauthentic; associated accounts in the same dataset feed `associate`/network mapping; archived media feeds reverse-image/geolocation.

## Inputs → Outputs
- **In:** `username`/account handle (or country/keyword)
- **Out:** attribution (which IO), `social-profile` (archived account + posts/media), `associate` (co-attributed accounts in the operation)
- **Empty/negative result looks like:** no match — the account is not in any *released* takedown dataset. That is not proof of authenticity; only disclosed operations are archived, and recent/undisclosed ones won't appear.

## Gotchas & OpSec
- Absence ≠ genuine: only platform-released, attributed datasets are here; a real-but-not-yet-caught IO account won't show. Use a match as strong positive evidence, a miss as inconclusive.
- Datasets are historical snapshots at takedown time — accounts are already suspended on the live platform.
- OpSec: passive; a static archive with no target contact.

## Overlaps ("do both")
- Pairs with live social-account analysis and bot-detection tools — IOA confirms *known* inauthentic accounts, while behavioural analysis flags *suspected* ones not yet in any dataset.

## Trust & verifiability
`trust: trusted` — attribution derives from the platforms' own state-actor takedown disclosures, curated by disinformation researchers; the data is authoritative for the operations it covers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ioa |
| category | people-search |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
