---
id: justfornurses-co-uk
name: Just for Nurses
description: Use when you have a `username`/`name` tied to UK nursing and want a niche nursing community forum and jobs board — returns forum posts, member `social-profile`s, and career/job leads.
url: http://www.justfornurses.co.uk/forum/
category: communities-forums
path:
- communities-forums
bestFor: Searching a UK nursing community forum and jobs board for a subject's posts, handle, and professional context.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free to read; a free account is needed to post and for some member areas.
opsec: passive
opsecNote: Reading public threads is passive. Registering or messaging members is active — use a sock-puppet account and never contact members from a real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A small, long-running UK nursing community site (forum + jobs board + advice); content is user-generated and unverified.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- JFN Nursing Forums
- justfornurses.co.uk
tags:
- forum
- nursing
- uk
- community
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Just for Nurses

> A niche UK nursing community — forums, a jobs board, and career advice — where a subject connected to nursing may post under a recognisable handle.

## When to use
Your subject plausibly works in or trains for UK nursing and you're hunting a `username`/`name` across niche communities. Just for Nurses hosts discussion forums, a nursing jobs board, and career threads; a matching handle can reveal self-disclosed workplace/specialty, location hints, career timeline, and other members they engage with — professional context you won't get from mainstream platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.justfornurses.co.uk/ and use the forum search, or run `site:justfornurses.co.uk "handle"` on a general engine for recall.
2. Read the member's posts and profile: specialty, region, join date, and interactions.
3. Some areas need a free login — register a puppet account only if necessary.
4. Pivot: a reused `username` feeds cross-platform checks; a disclosed employer/specialty (`employer-org`) feeds professional-registry lookups (e.g. NMC register).

## Inputs → Outputs
- **In:** `username`/`name` plausibly tied to UK nursing.
- **Out:** forum posts, member `social-profile`, self-disclosed `employer-org`/specialty, professional leads.
- **Empty/negative result looks like:** no matching member — the handle isn't used here (this is a small community). Absence proves nothing broader.

## Gotchas & OpSec
- Human-in-the-loop: some sections require a (free) account — use a puppet.
- Niche and UK-specific; only relevant when a subject's profession points here.
- User content is unverified; corroborate any professional claim against the official NMC register.

## Overlaps ("do both")
- Feed a reused handle into username-enumeration tools; cross-check a claimed nursing role against the UK NMC register for verification.

## Trust & verifiability
`trust: community` — an authentic but small hobby/professional forum. Posts are unverified; use it to find a persona and leads, then verify facts against authoritative registers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | justfornurses-co-uk |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
