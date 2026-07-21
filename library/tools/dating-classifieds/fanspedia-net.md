---
id: fanspedia-net
name: fanspedia.net
description: Use when you have a `username`, creator name or location and want to check a third-party OnlyFans directory for a matching creator profile — returns a `social-profile`, category and location leads.
url: https://fanspedia.net/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching an independent OnlyFans creator directory to link a handle/name/location to an adult-content profile.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
- geolocation
status: live
pricing: free
costNote: Free to search and browse the directory; individual creators' OnlyFans subscriptions are separate and out of scope.
opsec: passive
opsecNote: Browsing a public directory is passive. This is sensitive adult-content OSINT — handle any finding with care, restrict use to a legitimate, authorized investigation, and avoid subscribing/contacting (that becomes active and identifying).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party directory explicitly "not affiliated with OnlyFans"; listings are scraped/aggregated and unverified, and such adult-directory sites change hosts frequently.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- fanspedia
tags:
- onlyfans
- OnlyFans Related Sites
- adult
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# fanspedia.net

> An independent, searchable OnlyFans creator directory — a way to link a handle, display name, or location to an adult-content `social-profile`.

## When to use
You have a `username`, a display name, or a stated location and want to check whether it maps to an OnlyFans creator. Adult-platform presence can corroborate an identity, reveal a stated city/region, or connect a reused handle to other accounts. Because OnlyFans itself isn't openly searchable, third-party directories like this fill the gap. This is sensitive: use only within an authorized, legitimate investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://fanspedia.net/.
2. Search by `username`/name, or filter by category and location.
3. Inspect a matching listing for the creator's handle, stated location, and linked profile.
4. Cross-check the handle against other platforms to confirm it's the same person.
5. Pivot: a confirmed handle feeds cross-platform username-search; a stated location feeds geolocation/people-search.

## Inputs → Outputs
- **In:** `username`, creator `name`, or location
- **Out:** directory listing → `social-profile`, matching `username`, stated `geolocation`
- **Empty/negative result looks like:** no listing — the person may simply not be a creator, or the directory (an incomplete third-party scrape) may not have indexed them; absence proves nothing.

## Gotchas & OpSec
- Unaffiliated & unverified: it's a scraped directory, not OnlyFans; listings can be wrong, stale, or impersonations — corroborate before attributing.
- Sensitivity: adult-content findings carry real privacy/harm risk; confine to authorized use, and never subscribe or message (that's active and identifying).
- Site volatility: adult directories change domains/hosts often — verify you're on the live site.
- OpSec: passive for browsing only.

## Overlaps ("do both")
- Pairs with general username-search and other creator-directory tools — run the handle across several so a single directory's gaps don't cause a false negative.

## Trust & verifiability
`trust: unverified` — an unaffiliated third-party aggregator of unvetted listings; every hit is a lead to confirm on the actual platform, and every miss is inconclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fanspedia-net |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name → social-profile, username, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
