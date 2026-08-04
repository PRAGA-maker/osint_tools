---
id: findr-fans
name: Findr.fans
description: Use when you have a `username`, `name` or location and want to check for an OnlyFans presence — a third-party search engine indexing OnlyFans creators by handle, location and category.
url: https://findr.fans/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching for a subject's possible OnlyFans creator profile by username, name or location.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to search; it indexes public OnlyFans profile metadata, not paid content.
opsec: passive
opsecNote: Searching is passive and doesn't notify the creator. This is adult-industry data — handle findings with care: confirming or exposing someone's sex-work presence carries real safety, legal and dignity risks. Only pursue when relevant to a legitimate investigation, use a puppet browser, and never republish or out a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: One of several third-party OnlyFans search indexes; its database is smaller than rivals (OnlyFinder etc.), so it's a partial, unofficial mirror — not authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- findr.fans
- Findr fans
tags:
- onlyfans
- adult
- creator-search
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Findr.fans

> A third-party OnlyFans search engine — filter creators by username, name, location, gender and category to check whether a subject maintains an adult-platform profile.

## When to use
You have a `username`, `name` or location and, for a legitimate reason, need to determine whether the subject has an OnlyFans presence (e.g. a reused handle links to a creator account, or you're confirming an income source or an exploitation concern). OnlyFans has almost no native search; findr.fans and similar indexes fill that gap by mirroring public profile metadata.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://findr.fans/ in a sock-puppet browser session.
2. Search a `username` (best signal — handles are often reused across platforms), or filter by name/location/category.
3. Review results — profile handles, display names, locations and links to the public OnlyFans page (not paywalled content).
4. Corroborate before asserting identity: match profile photos, bio, linked socials and reused handle against your other findings.
5. Pivot: a confirmed handle feeds cross-platform username search; a linked social/name feeds people-search.

## Inputs → Outputs
- **In:** `username` / `name` / location
- **Out:** candidate OnlyFans `social-profile`(s) — handle, display name, location, public page link
- **Empty/negative result looks like:** no match — meaning nothing in *this* index (which is comparatively small); check a larger OnlyFans search engine before concluding the subject has no such profile.

## Gotchas & OpSec
- Human-in-the-loop: none, but adult content may appear; work in an appropriate environment.
- OpSec: **passive** — no notification to the creator; use a puppet session. Ethically/legally sensitive: never out, republish, or weaponize a person's sex-work presence; confine use to a justified investigation.
- Its database is partial and unofficial; a hit needs corroboration and an absence proves nothing.

## Overlaps ("do both")
- Cross-check with other OnlyFans indexes (OnlyFinder, etc.) and general username tools — coverage differs per index, and a reused handle elsewhere strengthens attribution.

## Trust & verifiability
`trust: community` — an unofficial third-party mirror of public OnlyFans metadata; treat results as leads to corroborate, not confirmed identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findr-fans |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
