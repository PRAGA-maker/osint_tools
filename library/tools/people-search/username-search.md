---
id: username-search
name: UserSearch.org
description: Use when you have a `username` and want to find where it exists across social, dating, gaming, forum, and crypto platforms — returns matching social-profile links and profile details.
url: https://usersearch.org/
category: people-search
path:
- people-search
bestFor: Reverse username lookup across 3,000+ social, dating, forum, gaming and crypto platforms.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Username search is free with no signup; deeper features (email, phone, breach, image search) are paid via the sister service UserSearch.ai.
opsec: passive
opsecNote: The service queries third-party platforms on its own infrastructure, so your IP is not exposed to each target site, and profile owners are not notified. Still treat any account you then visit directly with normal sock-puppet hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (since 2012) commercial username-search service; results are automated public-web matches and include false positives, so verify each hit.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- usersearch.org
- reverse username lookup
tags:
- username
- people-search
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# UserSearch.org

> A fast reverse-username lookup across thousands of platforms: paste a handle and find where that same username exists — social, dating, gaming, forums, crypto.

## When to use
You have a `username`/handle and want to map a subject's online footprint quickly — the same handle reused across sites is one of the strongest cross-platform links in OSINT. UserSearch checks 3,000+ platforms (including dating and forum sites that generic tools miss) and returns candidate profile links, which can surface a real `name`, photos, and further selectors on the matched profiles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://usersearch.org/ and enter the target `username` (no signup needed).
2. Choose a search depth tier (from a fast ~10-site scan to a full 300+-site sweep).
3. Read the returned list of platforms where the handle exists; open promising `social-profile` links.
4. Verify each: confirm the profile is actually the same person (handles get reused by different people) before treating it as a match.
5. Pivot: matched profiles feed name/photo/associate extraction; for email/phone/image reverse lookups, escalate to the paid UserSearch.ai or dedicated tools.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` links across many platforms, and via those, a possible real `name`
- **Empty/negative result looks like:** few or no hits — the handle may be unique to one site, the person may vary handles per platform, or matches may be stale/deleted accounts. Expect **false positives** (same handle, different person).

## Gotchas & OpSec
- Automated matches include false positives and stale accounts — always confirm each hit belongs to your subject.
- The free tier covers username only; email/phone/breach/image lookups are paid (UserSearch.ai).
- OpSec: the service queries sites for you (shielding your IP from targets), but visiting a matched profile directly is on you — use a sock puppet.

## Overlaps ("do both")
- Do both with other username enumerators (Sherlock, WhatsMyName, `[[names-directory]]` for name variants) — coverage differs per tool, and cross-confirming a hit across two engines reduces false positives.

## Trust & verifiability
`trust: community` — a reputable long-running commercial service, but outputs are automated public-web matches; each profile is a lead to verify, not a confirmed identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | username-search |
| category | people-search |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
