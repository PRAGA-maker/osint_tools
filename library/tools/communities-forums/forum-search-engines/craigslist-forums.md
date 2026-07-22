---
id: craigslist-forums
name: Craigslist Forums
description: Use when you have a `username` or keyword and want to read a person's public Craigslist forum posts and regional community chatter — returns `social-profile` handle activity and posting `geolocation`/timing.
url: https://forums.craigslist.org/
category: communities-forums
path:
- communities-forums
- forum-search-engines
bestFor: Reading public Craigslist community/forum discussions and a handle's regional posting activity.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free to read; a Craigslist account is only needed to post, not to browse.
opsec: passive
opsecNote: Reading public forum threads is passive and does not contact users. Do not reply or message a poster from an attributable account; browse in a clean/sock-puppet session if the subject is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Public user-generated forum content; handles are pseudonymous and posts are self-reported, so treat everything as claims, not fact.
missingPersonsRelevance: medium
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- craigslist
- craigslist-classified-ads-worldwide
aliases:
- forums.craigslist.org
tags:
- forums
- craigslist
- community
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Craigslist Forums

> The long-running Craigslist message boards — a place to trace a pseudonymous handle's public posts and regional community chatter.

## When to use
You have a Craigslist `username`/handle (from a classified ad or a prior lead) or a keyword/region of interest, and want to read that account's public forum activity or community discussion. In an investigation this can reveal a subject's interests, locale, timing patterns, and writing style behind a handle, and surface leads in regional boards (e.g. a "rideshare," "missed connections," or local-issues thread).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://forums.craigslist.org/ and pick a forum category (or region).
2. Browse or search threads for the `username`/handle or keyword. For deeper coverage, run a site: search on a web engine (`site:forums.craigslist.org "handle"`), since native search is limited.
3. Open a handle's posts to read content, timestamps, and any region/board context.
4. Note posting times (timezone hints) and recurring interests; cross-reference the handle against other platforms.
5. Pivot: the handle feeds username-search tools; a linked classified ad or region feeds `[[craigslist]]` and geolocation reasoning.

## Inputs → Outputs
- **In:** `username`/handle or keyword
- **Out:** `social-profile` (public forum posts under the handle), `geolocation` (board region / stated location), posting timestamps
- **Empty/negative result looks like:** no matching posts — the handle may be inactive, deleted, or only used in classifieds (which live outside the forums). Craigslist handles are easily discarded, so absence is weak evidence.

## Gotchas & OpSec
- Native search is weak; prefer an external `site:forums.craigslist.org` query.
- Handles are pseudonymous and disposable — the same person may use many; don't over-attribute.
- OpSec: passive reading only. Never reply to or message a poster from an attributable identity.

## Overlaps ("do both")
- Pairs with `[[craigslist]]` / `[[craigslist-classified-ads-worldwide]]` for the classifieds side, and with username-search tools to link the handle to other platforms.

## Trust & verifiability
`trust: unverified` — anonymous user-generated content; posts are self-reported claims by pseudonymous accounts. Corroborate any identity or location signal elsewhere before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | craigslist-forums |
| category | communities-forums |
