---
id: onlyfam
name: OnlyFam
description: Use when you have a `username`, `name`, or `geolocation` and want to find or confirm a person's OnlyFans creator presence — returns social-profile links and profile metadata.
url: https://onlyfam.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Locating or confirming a subject's OnlyFans creator account and pivot handles by name, username, or location.
selectorsIn:
- username
- name
- geolocation
selectorsOut:
- social-profile
- username
- geolocation
status: live
pricing: freemium
costNote: Browsing and keyword/location search of the public index is free with no signup; deeper analytics/filters are gated behind a paid tier, but the free search is enough for lookup and confirmation.
opsec: passive
opsecNote: This is a third-party index of public OnlyFans profile data; searching it does not touch OnlyFans or notify the creator. Do not log into or subscribe to any account you find from your own identity — that would deanonymize you and pay the target. Treat the adult-content context with care and use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent third-party scraper of OnlyFans public data, not affiliated with OnlyFans; coverage and freshness are self-claimed (600k+ creators) and unaudited, so treat hits as leads to verify on the real profile.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OnlyFam.com
- OnlyFans finder
tags:
- onlyfans
- creator-search
- adult
source: osintambition-social
lastVerified: '2026-07-22'
enrichment: full
---

# OnlyFam

> A no-signup search index over public OnlyFans creator profiles — use it to find or confirm whether a subject has an OnlyFans presence and to harvest their linked handles.

## When to use
You have a `username` (or display `name`, or an approximate `geolocation`) and want to know whether the subject runs an OnlyFans account, or you already suspect a handle and want to confirm and enrich it. A hit corroborates that a username is in active adult-content use and often exposes the same handle, display name, bio, and stated location the person reuses elsewhere — all pivotable back into mainstream social search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onlyfam.com in a clean/sock-puppet browser session.
2. Enter the target `username`, `name`, or a `geolocation` filter and run the search — no account is required for the public index.
3. Read the results: each hit shows the creator handle, display name, avatar, bio snippet, and often a stated location and links.
4. Confirm before trusting: open the corresponding `onlyfans.com/<handle>` page (or reverse-search the avatar) to verify the third-party index isn't stale or mismatched.
5. Pivot: reuse the confirmed handle/display name in a broad username sweep and reverse-image tools; a stated city feeds geolocation work.

## Inputs → Outputs
- **In:** `username`, `name`, or `geolocation`
- **Out:** `social-profile` (OnlyFans handle/URL), reused `username`, bio text, sometimes stated `geolocation`
- **Empty/negative result looks like:** no matching creators returned — meaning this index has no public OnlyFans profile under that term, NOT proof the person has no account (private/renamed creators and index gaps are common).

## Gotchas & OpSec
- Third-party index: data can be stale, mislabelled, or conflate different people who share a handle — always verify on the real profile before attributing.
- Never subscribe or message from an identifiable account; that both alerts and pays the target and burns your investigation.
- The paid tier adds bulk filters/analytics, but single-subject lookup works fully on the free search — don't pay for a one-off.

## Overlaps ("do both")
- Pairs with broad username-enumeration tools: OnlyFam confirms the adult-content account specifically, while a general handle sweep maps the same username across mainstream platforms the two indexes miss for each other.

## Trust & verifiability
`trust: unverified` — an unaffiliated scraper of OnlyFans public data with self-reported coverage; useful as a discovery lead but every hit must be confirmed against the genuine OnlyFans profile before it is treated as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onlyfam |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name, geolocation → social-profile, username, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
