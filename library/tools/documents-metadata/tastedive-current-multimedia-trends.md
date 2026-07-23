---
id: tastedive-current-multimedia-trends
name: TasteDive
description: Use when you have a target's stated interest (a band, film, book, game) or a TasteDive username and want related tastes or their public "Tastebuds" connections — returns social-profile and associate leads.
url: https://tastedive.com
category: documents-metadata
path:
- documents-metadata
bestFor: Mapping a subject's cultural interests to similar items, and surfacing their public TasteDive profile/Tastebuds connections.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to search recommendations and browse public profiles. A free API is available; heavy/commercial API use may require a key or paid plan.
opsec: passive
opsecNote: Browsing recommendations and public profiles is passive and doesn't notify anyone. If you register to view "Tastebuds"/social features, do so from a sock-puppet account — following or friending a target from a real account is an active, attributable action.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial recommendation service; useful as a soft interest/social pivot, not an authoritative identity source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- TasteDive
- Taste Kid
tags:
- interests
- recommendation-engine
- social-profile
- toddington
- curated-directory
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# TasteDive

> A media recommendation engine with light social features — pivot from a subject's known tastes (or a TasteDive handle) to related interests and their public connections.

## When to use
A niche, soft pivot. When you know a subject's cultural interests — a favorite band, film, author, or game — TasteDive maps them to similar items, which can help you predict communities/forums they'd frequent or seed search terms. If you have a TasteDive `username`, it can also surface a public profile and "Tastebuds" (followed accounts), giving weak `associate` leads. Low-signal for identity work; best as corroboration alongside stronger tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tastedive.com.
2. To profile interests: enter a known item the target likes (`name` of a band/film/book) and read the "you might also like" results — use these to guess adjacent communities/keywords.
3. To profile a person: navigate to a `username`'s public profile (if they have one) and view their listed tastes and Tastebuds connections (`selectorsOut`).
4. Pivot: matched interests feed forum/username searches; Tastebuds connections are candidate `associate` links to verify elsewhere.

## Inputs → Outputs
- **In:** `username` (a TasteDive handle) or `name` (an item/interest the subject likes)
- **Out:** `social-profile` (a matched TasteDive profile), `associate` (public Tastebuds/follows), related-interest lists
- **Empty/negative result looks like:** a generic recommendation list with no linked profile — meaning no reachable TasteDive account for that person, only content suggestions.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; social features need registration.
- OpSec: passive while reading; following/friending is active and attributable — use a sock puppet if you engage.
- Low fidelity: most users have no public profile, and interest-matching is probabilistic. Never treat a Tastebuds link as a confirmed relationship.

## Overlaps ("do both")
- Complements username-enumeration tools (e.g. [[whatsmyname-app]]-style checkers) — those find where a handle exists across sites, while TasteDive adds interest/social context if that handle is present here.

## Trust & verifiability
`trust: unverified` — a commercial recommendation product, not an identity registry. Its outputs are suggestive leads (interests, weak connections) that must be confirmed with stronger sources before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tastedive-current-multimedia-trends |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, name → social-profile, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
