---
id: flipboard
name: Flipboard
description: Use when you have a `username`/`name` and want a subject's Flipboard presence — returns their profile, curated magazines and shared articles, exposing interests and `social-profile` links.
url: https://flipboard.com/
category: search-engines
path:
- search-engines
- news-search
bestFor: Finding a subject's Flipboard profile and curated magazines to read their interests and shared content.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free to browse and search public profiles and magazines; an account is optional and only needed to curate your own content.
opsec: passive
opsecNote: Viewing public profiles and magazines is passive and does not notify the target. Browse logged-out or from a sock-puppet account so no follow/like leaks from your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Reputable content-curation platform; profile/magazine content is user-generated and unverified, useful as an interest and link source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Flipboard magazines
- flipboard.com
tags:
- news-search
- social-media
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Flipboard

> A social magazine / content-curation platform — a subject's public Flipboard profile and "magazines" reveal what they read, save and share, plus links to their other accounts.

## When to use
You have a `username` or `name` and want to profile a subject's interests, opinions and the topics they follow. Flipboard users build public "magazines" of flipped articles; the profile and those magazines are an interest-graph and often carry a bio and outbound links to the person's other `social-profile`s. Best as a lifestyle/interest enrichment source rather than a primary identity resolver.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the direct profile URL `https://flipboard.com/@<username>`, or use Flipboard's on-site search / a search-engine `site:flipboard.com "<name>"` query.
2. Open the profile: read the bio, list of magazines, and the articles they've flipped.
3. Note themes across magazines (hobbies, politics, profession, region) and any bio links to other accounts.
4. Pivot: bio/outbound links feed `social-profile` enrichment; the topic mix hints at profession, location or affiliations to confirm elsewhere.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (the Flipboard profile + linked accounts), `username`, plus interest context (magazines, flipped articles)
- **Empty/negative result looks like:** no matching profile or only unrelated same-name accounts — the person may not use Flipboard; absence isn't a finding.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; do not sign in to view public content.
- OpSec: passive — reading public profiles doesn't alert anyone; avoid following/liking, which is attributable.
- Name/handle collisions are common; corroborate that the interests and links match your subject before attributing.

## Overlaps ("do both")
- Pairs with username-enumeration and broad social-search tools — Flipboard confirms one platform and its curated interests, while a multi-platform username checker widens the net to accounts Flipboard alone won't show.

## Trust & verifiability
`trust: community` — Flipboard is a legitimate platform, but the magazines and bios are user-authored and unverified; treat interests and links as leads to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flipboard |
| category | search-engines |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
