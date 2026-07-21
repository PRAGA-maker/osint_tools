---
id: pinterest
name: Pinterest
description: Use when you have a `username`, `name` or `image` and want interest/lifestyle profiling — returns `social-profile`, boards/pins, `geolocation` cues and `associate` links.
url: https://www.pinterest.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- social-networking
bestFor: Building an interest, lifestyle, and location profile of a subject from their boards, pins, and follows.
selectorsIn:
- username
- name
- image
selectorsOut:
- social-profile
- geolocation
- associate
status: live
pricing: free
costNote: Free to browse; some profile/board browsing is possible without login, but full access and search work best with a (sock-puppet) account.
opsec: passive
opsecNote: Reading public boards/pins is passive and less aggressively surfaced to users than Facebook/LinkedIn. If you log in to search, use a sock-puppet account — following or messaging would create a footprint. Avoid interacting; just read.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A genuine platform; boards reflect self-curated interests, not verified facts. Useful for behavioural/lifestyle inference and image leads, weak for hard identity confirmation.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- pinterest-trends
- uk-pinterest-com
aliases:
- Pinterest
- pinterest.com
tags:
- social-networking
- Social Media
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# Pinterest

> An interest-curation platform where users assemble boards of things they love — quietly revealing lifestyle, plans, tastes, and sometimes location, with less scrutiny than the big social networks.

## When to use
Your subject has (or may have) a Pinterest account, or you have a photo you want to trace. Boards and pins profile a person's interests, aspirations, and life stage — wedding planning, home renovation of a specific house, baby boards, hobbies, travel wishlists — which can yield `geolocation` cues (a named venue, a home under renovation), a partner/associate, and behavioural context. Pinterest is also a strong reverse-image target because images are richly indexed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try `https://www.pinterest.com/<username>/` directly; browse public boards and pins (some viewing works without login).
2. From a sock-puppet account (for full search), search the subject's name/handle and look for their boards and follows.
3. Read boards for lifestyle/location signals — venue names, "our new home," local businesses, event dates — and note followed/collaborating accounts as `associate`s.
4. For a photo lead, use Pinterest's visual search and reverse-image tools to find where an image appears.
5. Pivot: a username feeds `[[sherlock]]`/`[[whatsmyname]]`; a named venue/place feeds mapping; a partner/associate feeds people-search; images feed `[[pimeyes-com]]`.

## Inputs → Outputs
- **In:** `username` / `name` / `image`
- **Out:** `social-profile`, boards/pins (interests), `geolocation` cues, `associate` (follows/collaborators)
- **Empty/negative result looks like:** no profile for the handle, or a private/empty account — the person may not use Pinterest or keeps boards secret. Absence is not proof, and interest inference is soft evidence at best.

## Gotchas & OpSec
- Interests are self-curated aspiration, not fact — infer lifestyle carefully and corroborate any location cue.
- Passive to read; logging in for search means using a sock puppet — never follow/message from it.
- Handles are often reused elsewhere — a Pinterest username is a good cross-platform pivot even when the boards are thin.

## Overlaps ("do both")
- Pairs with `[[pinterest-trends]]` and cross-platform username tools — the profile gives lifestyle/location leads, those extend the identity and confirm the handle across the web.

## Trust & verifiability
`trust: unverified` — an authentic platform whose content is self-curated interest, not verified identity data; excellent for behavioural/location leads and image tracing, weak as standalone identity proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pinterest |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, name, image → social-profile, geolocation, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
