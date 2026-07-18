---
id: the-globe-and-mail
name: The Globe and Mail
description: Use when you have a `name` connected to Canada and want national/local news coverage, quotes or obituaries — returns social-profile and associate.
url: http://www.theglobeandmail.com
category: communities-forums
path:
- communities-forums
bestFor: Searching Canada's national newspaper archive for a subject's mentions, obituaries, bylines and affiliations.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Headlines and search are free; many full articles are behind a metered/subscription paywall. Archives and syndication often expose the text.
opsec: passive
opsecNote: Reading/searching published journalism is invisible to any subject. Avoid signing in with a real account; a login is unnecessary to read most search results.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Canada's leading national newspaper (edited, bylined journalism of record); attributable and citable.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Globe and Mail
- theglobeandmail.com
tags:
- news-journalism
- curated-directory
- canada
- toddington
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# The Globe and Mail

> Canada's national newspaper of record — the go-to news source when a subject, family, or case has a Canadian connection.

## When to use
The subject has a Canadian dimension and you want reported detail: a news mention, a quote, an obituary or death notice, a court report, or a byline. Canadian obituaries in particular are rich for missing-person and next-of-kin work — they name surviving relatives (`associate`), locations, and employers. A hit ties a `name` to coverage (`social-profile`) and to the people named around them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use Globe and Mail search, or a scoped engine query: `site:theglobeandmail.com "Jane Doe"`. For obituaries, also check its death-notices section.
2. For paywalled hits, read the excerpt, check an archived copy (`[[wayback]]`-style), or news syndication to recover the text.
3. Note dates, places, employers, family members, and co-named people.
4. Pivot: relatives from an obituary → `associate`/next-of-kin tracing; employer → `employer-org`; court/case references → Canadian public-records search.

## Inputs → Outputs
- **In:** `name` (optionally place/employer to disambiguate)
- **Out:** `social-profile` (coverage/mentions), `associate` (relatives/co-named people, esp. from obituaries)
- **Empty/negative result looks like:** no articles reference the subject — expected for most private individuals; means no Globe and Mail footprint.

## Gotchas & OpSec
- Paywall: assume full text is metered; recover via archive/syndication rather than subscribing under your real identity.
- Common-name collisions — anchor on place, date, or family before attributing.
- OpSec: passive read; safe.

## Overlaps ("do both")
- Run inside a broader Canadian news sweep (local papers, CBC) and obituary aggregators — the Globe gives national coverage and strong obituaries, while local outlets catch community-level detail it omits.

## Trust & verifiability
`trust: trusted` — edited, bylined journalism of record; mentions are attributable and citable, with obituaries and court reports being especially reliable leads to corroborate against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-globe-and-mail |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
