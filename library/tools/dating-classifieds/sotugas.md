---
id: sotugas
name: SoTugas
description: Use when you have a `name` or `username` you suspect belongs to a Portuguese adult-content creator — returns their OnlyFans `social-profile` listing.
url: https://sotugas.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding and confirming Portuguese OnlyFans creators by name/handle.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to browse and search the directory; the OnlyFans profiles it links to are the creators' own paywalled accounts.
opsec: passive
opsecNote: Searching the directory is passive and anonymous. Do NOT click through and subscribe/message on the target's OnlyFans from an attributable account — that is active contact that alerts the creator. Use a clean, non-attributable browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party aggregator with no OnlyFans affiliation; listings are self-/community-submitted and unvetted, so confirm any match on the linked primary profile.
missingPersonsRelevance: low
coverage:
- pt
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- onlyfans-com
- search-onlyfans-profiles
- coomer-st
aliases:
- SoTugas
- SóTugas
- sotugas.com
tags:
- onlyfans
- portugal
- adult
source: osintambition-social
lastVerified: '2026-08-05'
enrichment: full
---

# SoTugas

> A Portuguese-language directory of OnlyFans creators ("contas portuguesas no OnlyFans") — a name/handle index into an adult platform that has no public search of its own.

## When to use
You have a `name` or `username` that may map to a Portuguese adult-content creator and you need to locate or confirm their OnlyFans presence — for example, linking an alias found elsewhere to a monetised profile, or confirming a creator is active. Because OnlyFans has no open profile search, a directory like this is one of the few ways to discover the account from a handle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sotugas.com/ in a clean/sock-puppet browser.
2. Use the search box for the `username`/`name`, or browse the Highlights, "free content", and Recently Updated sections.
3. Open a listing to see the creator's display name, handle, and link out to their OnlyFans `social-profile`; note whether it advertises free content.
4. STOP at discovery — record the profile URL/handle. Do not subscribe, tip, or message from an attributable account.
5. Pivot the confirmed `username` across `[[search-onlyfans-profiles]]` and general username tools to find the same handle on other platforms.

## Inputs → Outputs
- **In:** `name` / `username`
- **Out:** `social-profile` (the creator's OnlyFans account link and handle)
- **Empty/negative result looks like:** no matching listing. The directory only covers creators it has indexed (Portugal-focused), so absence is not evidence the person has no adult profile — it just isn't here.

## Gotchas & OpSec
- Scope is Portugal/Portuguese-language; a non-Portuguese creator won't be listed.
- Listings are unvetted and can be impersonations or stale — verify identity on the primary profile, not on the directory blurb.
- OpSec: browsing is passive, but any interaction on the linked OnlyFans (subscribe/DM) is active and attributable. Keep to observation.

## Overlaps ("do both")
- Pairs with `[[onlyfans-com]]` (the primary platform) and `[[search-onlyfans-profiles]]` for cross-checking a handle, and with `[[coomer-st]]` when you need to confirm a profile exists without contacting the creator.

## Trust & verifiability
`trust: unverified` — an unaffiliated community aggregator; a listing is only a lead until you confirm the handle and identity on the actual OnlyFans profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sotugas |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
