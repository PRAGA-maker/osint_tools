---
id: peek-you-user-name
name: PeekYou - Username Search
description: Use when you have a `username` and want the real person behind it — returns linked social-profiles, a probable name, and aggregated identity leads.
url: https://www.peekyou.com/username
category: username
path:
- username
bestFor: Resolving a username to a real identity by aggregating the profiles and public content tied to that handle.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free to search 300M+ profiles by username; deep contact detail may push toward paid partner reports.
opsec: passive
opsecNote: Searching aggregates public data and does not notify the subject, but PeekYou is itself a data broker that logs queries. Use a clean session; note PeekYou also lets people be searched — consider your own footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A large commercial people-search aggregator; identity links are algorithmic guesses from public data — strong leads, but conflation happens, so verify.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- PeekYou
tags:
- username
- people-search
- data-broker
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- peekyou
- peekyou-people-search
---

# PeekYou - Username Search

> A people-search engine that runs the other direction: give it a handle, get the human — the profiles, name, and identity threads tied to a username.

## When to use
You have a `username` (from a forum, a chat, another platform) and want to know who is behind it. PeekYou aggregates public web content and correlates a handle across sites, so it's a fast way to jump from an anonymous username to a probable real `name` and a cluster of linked `social-profile`s — the core username→identity pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.peekyou.com/username and enter the handle.
2. Review the aggregated result: linked social profiles, a probable name, photos, and other associated content.
3. **Verify the correlation** — open the linked profiles and confirm they're the same person (photo, bio, cross-links), since aggregators conflate same-handle strangers.
4. Pivot: a confirmed real name feeds people-search/records; additional linked profiles feed deeper SOCMINT; a photo feeds face/reverse-image search.

## Inputs → Outputs
- **In:** `username`
- **Out:** linked `social-profile`s, a probable real `name`, associated photos/content
- **Empty/negative result looks like:** no aggregated identity, or a scattered set of unrelated profiles for a common handle. A thin result is common for privacy-conscious or non-US subjects; don't force-fit unrelated profiles into one person.

## Gotchas & OpSec
- Conflation risk: PeekYou links by handle/name similarity and can merge different people — every correlation is a hypothesis to confirm.
- Freemium: broad results are free; detailed contact data may route to paid partners.
- Not FCRA-compliant — no employment/tenant/credit use.
- OpSec: **passive**; searching doesn't notify the subject.

## Overlaps ("do both")
- Pairs with username enumerators like `[[findme-0xsaikat]]` and with `[[social-media-osint-tools-collection]]` — enumerators check where a handle exists, PeekYou attempts the who; run both and reconcile.

## Trust & verifiability
`trust: unverified` — a commercial aggregator whose identity links are algorithmic; treat a hit as a lead and verify each linked profile against the live source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peek-you-user-name |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
