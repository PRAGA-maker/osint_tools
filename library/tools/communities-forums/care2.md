---
id: care2
name: Care2
description: Use when you have a `name`/`username` and want to find a subject's activism footprint — petitions signed/created, causes, and member profile on a large activism network — returns `social-profile`, `associate`.
url: http://www.care2.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a subject's activism/advocacy footprint (petitions, causes, member profile) on a 40M+ member social-good network.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to browse petitions and public profiles; a free account is only needed to sign/create petitions, not to view.
opsec: passive
opsecNote: Browsing public petitions and member pages is passive. Signing a petition or messaging a member exposes your account and is active — stay logged out for research, and use a sock puppet if you ever need to sign in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A legitimate, long-running activism platform; profile data is self-reported by members, so treat names/locations as claims to corroborate, not verified facts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Care2 petitions
- thepetitionsite
tags:
- toddington
- curated-directory
- online-communities-blogs
- activism
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Care2

> One of the largest activism/petition social networks — a place to find a subject's causes, the petitions they signed or started, and connections around shared advocacy.

## When to use
Your subject is (or may be) engaged in activism, advocacy, animal welfare, environmental or human-rights causes, and you have a `name` or `username`. Care2 profiles and petition signatures can reveal a person's interests, cause affiliations, geographic hints, other handles, and `associate`s in the same campaigns — useful for building a lifestyle/interests picture or finding a community they'd resurface in.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.care2.com (and its petition arm, thepetitionsite.com).
2. Search for the target `name`/`username`; also try a search engine with `site:care2.com "<name>"` and `site:thepetitionsite.com "<name>"`, which often indexes signatures better.
3. Open matching member profiles and petitions; read stated location, causes, comments, and co-signers.
4. Stay logged out to keep browsing passive.
5. Pivot: co-signers/commenters are `associate` leads; stated causes and locations feed timeline and geolocation reasoning; a discovered handle feeds cross-platform username search.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (member page), `associate`s (co-campaigners/commenters), interests and location hints
- **Empty/negative result looks like:** no profile or signatures for the name — the subject isn't active here (most people aren't), which says little on its own.

## Gotchas & OpSec
- Profile fields are self-reported; corroborate any location/identity claim elsewhere.
- On-site search is weak; a search-engine `site:` query usually finds signatures and comments more reliably.
- OpSec: browse logged out; signing/messaging exposes your account.

## Overlaps ("do both")
- Pairs with broad username-search and other petition/activism platforms — cross-reference, since a person active on causes often appears on several such sites and each indexes different traces.

## Trust & verifiability
`trust: unverified` — the platform is genuine, but member-supplied data is unvetted; use hits as leads to corroborate, not as confirmed identity facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | care2 |
| category | communities-forums |
| selectorsIn → selectorsOut | name, username → social-profile, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
