---
id: addmes
name: AddMeS
description: Use when you have a Snapchat `username` (or want to find one by demographics) and want to confirm/discover Snapchat accounts — returns self-posted Snapchat usernames and profile links.
url: https://addmes.io/
category: username
path:
- username
bestFor: Confirming a Snapchat username exists in a public "add me" directory, or browsing self-listed users by age/gender.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: 100% free, no registration needed to search or submit; ad-supported.
opsec: passive
opsecNote: You search a public directory of self-submitted Snapchat handles — you do NOT contact anyone via Snapchat, so no alert is sent by searching. Only entries people posted themselves appear. If you go on to add someone on Snapchat, that IS active contact — use a sock-puppet Snapchat account and reconsider the intrusion.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An anonymous, ad-supported third-party directory of self-submitted handles; no verification that a listing belongs to a real/identified person, and the audience skews young.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- AddMeS
- addmes.io
- Snapchat add me directory
tags:
- username
- snapchat
- social-media
source: osintambition-social
lastVerified: '2026-07-29'
enrichment: full
---

# AddMeS

> A public "add me" directory of self-posted Snapchat usernames, searchable/filterable by demographics — a way to check whether a Snapchat handle is publicly listed.

## When to use
You have a candidate `username` and want to see if it appears as a self-listed Snapchat handle, or you're working a lead where someone advertised their Snapchat publicly. AddMeS aggregates handles that users themselves submitted to be discoverable, with filters for gender and age band. It only ever contains *self-posted* handles, so it's a narrow confirmatory/discovery tool, not a comprehensive Snapchat lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://addmes.io/.
2. Search a `username`, or browse using the gender and age-range filters (13-17, 18-20, … 50+).
3. Check whether a matching Snapchat handle is listed and read any self-provided details.
4. Treat a hit as "this handle was publicly posted here" — corroborate identity elsewhere before acting.
5. Any actual Snapchat contact = active; use a sock-puppet account, and weigh the ethics (the pool skews young).

## Inputs → Outputs
- **In:** `username` (or demographic filters)
- **Out:** self-listed Snapchat `username`/`social-profile` handles
- **Empty/negative result looks like:** no listing — the vast majority of Snapchat users never post here, so absence means almost nothing. A hit is a weak, unverified signal.

## Gotchas & OpSec
- **Tiny, self-selected slice of Snapchat** — non-listing is not evidence of absence; a listing is not proof of identity.
- **Minors:** the directory includes teen age bands — take special care; do not contact minors, and escalate to appropriate authorities in a real case.
- OpSec: searching is **passive**; adding someone on Snapchat is active contact — use a sock-puppet and justify the intrusion.

## Overlaps ("do both")
- Complements broad username-enumeration tools — those check a handle across many platforms; AddMeS specifically covers self-posted Snapchat handles, a surface general enumerators don't index.

## Trust & verifiability
`trust: unverified` — anonymous, unmoderated, self-submitted data with no identity verification; use only as a weak lead and corroborate everything.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | addmes |
| category | username |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
