---
id: the-dots
name: The Dots
description: Use when you have a `name` or `username` for someone in the creative/media industries and want their professional profile — returns a `social-profile` with work history, portfolio and current employer.
url: https://the-dots.com/
category: social-networks
path:
- social-networks
bestFor: Finding a creative-industry professional's portfolio, work history and current employer — a "LinkedIn for creatives".
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
- image
status: live
pricing: freemium
costNote: Free to browse many public profiles; some features and full network access require a free account/login.
opsec: passive
opsecNote: Public profiles are viewable without login and browsing does not notify the subject. If you create an account to see more, use a sock-puppet and avoid connecting/messaging, which would alert them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate professional network for creative industries; profile content is self-reported, so treat employment/portfolio claims as user-supplied.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- peekyou
aliases:
- The-Dots
- thedots
tags:
- toddington
- curated-directory
- social-media
- professional-network
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# The Dots

> A professional network for the creative and media industries — think "LinkedIn for creatives" — a good place to find portfolios, employers, and career trails that don't appear on LinkedIn.

## When to use
You have a `name` or `username` for someone who works in design, film, fashion, marketing, media, or the arts, and you want their professional footprint: portfolio work, past and current employers, collaborators, and a photo. Creative professionals often maintain a strong presence here while keeping LinkedIn thin, so it fills a gap for that demographic.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://the-dots.com/.
2. Search the subject's `name` or reused `username`.
3. Read the profile: display `name`, photo (`image`), bio, portfolio/work samples, and listed employers/collaborators (`employer-org`).
4. Pivot: a current employer feeds corporate/LinkedIn checks; portfolio imagery feeds reverse-image search; a reused `username` feeds cross-network search.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile`, `employer-org` (work history), `image`, portfolio/collaborators
- **Empty/negative result looks like:** no matching profile — expected for anyone outside the creative industries, or who uses a different handle here. Absence just means "not on The Dots."

## Gotchas & OpSec
- Skewed to creative/media professionals and UK-centric; a non-match is uninformative for people in other fields.
- Some detail requires a login — use a puppet account and never connect/message the subject.
- OpSec: **passive** for public-profile viewing.

## Overlaps ("do both")
- Pairs with `[[peekyou]]` and LinkedIn-style tools — The Dots covers the creative-industry career trail that mainstream professional aggregators often miss.

## Trust & verifiability
`trust: community` — a real professional network, but profiles are self-reported; corroborate employment and portfolio claims before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-dots |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
