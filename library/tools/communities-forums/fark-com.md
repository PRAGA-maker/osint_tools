---
id: fark-com
name: Fark.com
description: Use when you have a `username` and want to read a long-time Fark member's comment history and interests — a veteran news-commentary community searchable by handle.
url: http://www.fark.com
category: communities-forums
path:
- communities-forums
bestFor: Reading a Fark member's accumulated comments and the topics/links they submit as interest and disclosure leads.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to read and search. A paid "TotalFark" tier exists for extra features but is not needed to research public comments.
opsec: passive
opsecNote: Browsing public member pages and comment threads leaks nothing to the subject. Do not register or reply to interact with the target; if you must sign up to view something, use a sock-puppet identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An established (since 1999) news-aggregation community; content is user-generated commentary, so treat personal claims as self-reported and unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Fark
- fark.com
tags:
- toddington
- curated-directory
- news-journalism
- forum
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Fark.com

> A long-running news-link community whose persistent member handles make it a place to read a subject's accumulated comments and interests — if they're a Farker.

## When to use
You have a `username` (Fark handles are stable and often reused elsewhere) and want to read that member's public comment history and the news links they submit. People reveal locations, jobs, politics, and personal anecdotes in years of casual commentary, so it can corroborate a persona or connect a handle across sites. Treat it as an interest/corroboration source, not a locator — most people have no Fark presence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.fark.com. Use the site search, or a search engine with `site:fark.com "<username>"` or their phrases.
2. Open the member's profile/comment view to see their handle history, submitted links, and comment archive.
3. Read the comments for self-disclosed details (city, employer, relationships, events) and links they care about.
4. Pivot: a reused handle feeds cross-platform username search; disclosed details are leads to verify elsewhere.

## Inputs → Outputs
- **In:** `username` (Fark handle)
- **Out:** `social-profile` (member page), comment/submission history, interest and disclosure leads
- **Empty/negative result looks like:** no member page and no `site:fark.com` hits — the handle isn't active here; Fark is niche, so absence is the norm.

## Gotchas & OpSec
- Human-in-the-loop: none for reading.
- Content is self-reported community banter — corroborate any personal detail before relying on it.
- OpSec: passive. Do not comment at or message the subject; that would be active and alerting.

## Overlaps ("do both")
- Behaves like other legacy-community handle searches (e.g. `[[metafilter]]`) — run the same `username` across several long-lived forums, since a person's disclosures are scattered and each site holds a different slice.

## Trust & verifiability
`trust: unverified` — a reputable old community, but the value here is user-generated commentary, which is self-reported. Verify any fact you extract against independent evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fark-com |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
