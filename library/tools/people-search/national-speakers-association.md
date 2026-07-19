---
id: national-speakers-association
name: National Speakers Association
description: Use when you have a `name` of a US professional/keynote speaker and want their member profile — returns bio, topics, location and credentials from NSA directories.
url: https://www.nsaspeaker.org
category: people-search
path:
- people-search
bestFor: Confirming and profiling a US professional speaker via NSA's member, CSP, and Hall of Fame directories — bio, expertise topics, and location.
selectorsIn:
- name
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free to search the "Find a Speaker"/member directories; full member-exclusive resources sit behind a login at portal.nsaspeaker.org, but public speaker profiles are viewable.
opsec: passive
opsecNote: You search a public professional directory; no subject is contacted and the query isn't tied to you. Passive — the member-only portal requires login, but you don't need it for basic profile lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The NSA is a long-standing US professional-speaking association; directory listings are member self-provided but tied to a real membership and credentials (e.g. CSP), lending some reliability.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NSA Speaker
- nsaspeaker.org
tags:
- expert-search
- professional-directory
- speakers
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# National Speakers Association

> The US professional-speaking association's member directories — a niche way to confirm and profile someone who works as a keynote/professional speaker.

## When to use
You have a `name` and reason to think the person is a professional or keynote speaker, trainer, or author-presenter, and want to confirm it and pull a profile: their speaking topics/expertise, bio, market/location, and any NSA credential (Certified Speaking Professional, CPAE Hall of Fame). It's a targeted expert-search for this profession — useful for corroborating a stated occupation, finding a professional bio, or identifying which market/city someone operates in.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.nsaspeaker.org and open the "Find a Speaker" / member directory (also the CSP and CPAE Hall of Fame directories).
2. Search by `name` (or by topic/expertise if you're identifying who speaks on a subject).
3. Read the profile: bio, speaking topics, business/`employer-org` name, market/location, and any credential.
4. Note member-exclusive resources need a login at portal.nsaspeaker.org — the public speaker profiles don't.
5. Pivot: a professional bio/business name feeds company and social-profile searches; the credential and topics corroborate identity and occupation.

## Inputs → Outputs
- **In:** `name` (or expertise topic)
- **Out:** speaker profile → business/`employer-org`, market/`address` (city/region), topics, credentials
- **Empty/negative result looks like:** no match — the person isn't an NSA member (most people aren't) or speaks outside the US; absence says nothing beyond "not an NSA member."

## Gotchas & OpSec
- Very narrow scope: only professional speakers who are NSA members — a small, US-focused population.
- Profiles are self-authored marketing bios — corroborate claimed expertise/roles elsewhere.
- Some content is member-only (portal login); basic profile lookups are public.
- OpSec: passive directory search.

## Overlaps ("do both")
- Complements general people-search and professional-network tools — NSA confirms the speaking profession and topics; those place the person in a broader identity/employment picture.

## Trust & verifiability
`trust: community` — a legitimate professional association, but listings are member-provided marketing. A verified credential (CSP/CPAE) is meaningful; still corroborate bio claims against independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | national-speakers-association |
| category | people-search |
| selectorsIn → selectorsOut | name → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
