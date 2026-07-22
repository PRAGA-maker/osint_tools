---
id: witchdoctor-new-zealand
name: WitchDoctor (New Zealand)
description: Use when you have a `name` and want to check a long-running NZ technology-review publication's byline/quote archive — returns `social-profile` / author attribution.
url: https://witchdoctor.co.nz
category: dark-web
path:
- dark-web
bestFor: Searching a New Zealand consumer-tech review site's archive for a person's byline, review or quote.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to read; ad-supported. No account required.
opsec: passive
opsecNote: Reading and Google-dorking a public news/review site is passive and reveals nothing to any subject; only your requests reach the publisher.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An independent NZ tech-review publication (bylined journalism), not an investigative database; useful only as a searchable media archive.
missingPersonsRelevance: medium
coverage:
- nz
auth: none
api: false
localInstall: false
registration: false
aliases:
- Witchdoctor.co.nz
tags:
- toddington
- curated-directory
- specialty-search
- media-archive
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# WitchDoctor (New Zealand)

> A long-running independent New Zealand consumer-technology and music/lifestyle review site — a niche media archive, not an OSINT database.

## When to use
Low direct value for missing-persons work; treat it as one small searchable New Zealand media source. It becomes relevant only when a subject has a footprint in NZ tech/music journalism: a byline (contributor/reviewer), a quoted expert or interviewee, or a mention in a product/event write-up. In those narrow cases the archive can confirm a name-to-role link, a rough date, and sometimes an author profile you can pivot from.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use the site's own search, or Google-dork it: `site:witchdoctor.co.nz "<name>"`.
2. Open matching articles and read for the connection — is the `name` an author byline, a quoted source, or an incidental mention?
3. Follow an author byline to their contributor page/bio, which may link social handles or other outlets.
4. Pivot: a confirmed byline feeds journalist/author enumeration; a quote establishes the person's presence in NZ at the article's date and their claimed expertise.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile` (author/contributor page), byline/quote attribution and article date
- **Empty/negative result looks like:** no dorked hits or on-site matches — the person has no footprint in this publication (the common case).

## Gotchas & OpSec
- This is journalism, not a lookup service — expect zero hits for most subjects; do not over-read a single incidental mention.
- Same-name collisions are likely; confirm identity from article context before linking.
- Passive throughout; no subject notification.

## Overlaps ("do both")
- Pairs with broader news/media-archive search and journalist-enumeration tools — this only covers one NZ outlet, so use it to corroborate, not as a primary sweep.

## Trust & verifiability
`trust: unverified` — a legitimate independent NZ publication, but it is editorial media, so treat its content as reporting/opinion, not as verified record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | witchdoctor-new-zealand |
| category | dark-web |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
