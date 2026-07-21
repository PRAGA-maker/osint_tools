---
id: eroticbeauties-net
name: eroticbeauties.net (OnlyFans directory)
description: Use when you have a `username` and want to check whether it maps to a listed adult-content (OnlyFans) creator — returns the linked `social-profile` and profile metadata.
url: https://www.eroticbeauties.net/onlyfans/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Resolving whether a username or handle corresponds to a catalogued OnlyFans creator and pivoting to that public profile.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free directory listing. Individual creator content on OnlyFans itself is paywalled; this index of profiles is not.
opsec: passive
opsecNote: Browsing an aggregator's public directory does not touch the target's account or notify them. It is an adult site — expect trackers/ads; browse in a hardened sock-puppet session with an ad-blocker and never log in or subscribe from an investigative machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party adult-content aggregator that scrapes/indexes public OnlyFans profiles; listings are unofficial and can be stale, mislabelled or promotional. Confirm any match on the primary platform.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- eroticbeauties onlyfans directory
tags:
- onlyfans
- OnlyFans Related Sites
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# eroticbeauties.net (OnlyFans directory)

> A third-party directory that indexes public OnlyFans creator profiles — usable as a username-to-profile lookup for adult-content accounts.

## When to use
You have a `username`/handle that may belong to an adult-content creator and want to confirm the link and reach the public-facing profile (bio, display name, linked socials, country, post/photo counts) without paying for or logging into OnlyFans. Relevant when a subject's online identity overlaps with sex-work platforms and you need to establish that connection or find corroborating profile details.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.eroticbeauties.net/onlyfans/ in a hardened sock-puppet browser with an ad/tracker blocker.
2. Use the on-page sort/filter controls (by name, username, newest, popular, country, subscription price) or search for the handle.
3. Open a matching listing to read the public metadata: display name, country, subscriber/post/photo/video counts, and any linked socials.
4. Verify the match against the creator's actual OnlyFans URL and linked social accounts before treating it as confirmed.
5. Pivot: a linked handle or display name feeds cross-platform username tools (`[[sherlock]]`, `[[whatsmyname]]`) and reverse-image/face tools for any avatar.

## Inputs → Outputs
- **In:** `username` (or partial handle)
- **Out:** `social-profile` (OnlyFans + any linked socials), profile metadata
- **Empty/negative result looks like:** no listing for the handle — the creator may not be indexed here (coverage is partial), may use a different name, or may not exist; absence is not proof.

## Gotchas & OpSec
- Aggregator data is scraped and may be outdated, promotional, or wrongly attributed — never rely on it as sole confirmation.
- Adult site: heavy ads/trackers and affiliate links; keep it fully isolated from any real identity and never subscribe/log in from an investigative session.
- Coverage is a subset of OnlyFans; treat it as one index among several, not authoritative.

## Overlaps ("do both")
- Pairs with cross-platform username tools like `[[sherlock]]` / `[[whatsmyname]]` — those enumerate the handle everywhere, while this specifically confirms and enriches the adult-platform footprint.

## Trust & verifiability
`trust: unverified` — an unofficial adult-content scraper with no accountable maintainer; use only as a lead generator and always confirm on the primary platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eroticbeauties-net |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
