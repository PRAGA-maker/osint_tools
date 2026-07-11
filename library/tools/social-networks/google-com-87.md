---
id: google-com-87
name: Google site-search for Snapchat Places
description: Use when you have a location or place name and want Snapchat public "Place" pages Google has indexed — returns Snap Map place pages and associated public snaps via a `site:snapchat.com/place/` dork.
url: https://www.google.com/search?q=site%3Asnapchat.com%2Fplace%2F+inurl%3A
category: social-networks
path:
- social-networks
bestFor: Surfacing Snapchat public Place pages (Snap Map) for a location through Google's index.
selectorsIn:
- name
- geolocation
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free; plain Google web search with site:/inurl: operators. No account needed.
opsec: passive
opsecNote: Queries hit Google, not Snapchat, so no subject is notified and you avoid Snapchat's app-level logging. Google logs your searches — use a sock-puppet/logged-out browser. Opening Snap Map / snapchat.com place pages afterwards is a separate, slightly more exposing step.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: This is Google web search with site:/inurl: operators — a first-party engine indexing public Snapchat Place pages. Reliability is bounded by Google's crawl of Snapchat's public place URLs.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Snapchat Places Google dork
- site:snapchat.com/place dork
tags:
- snapchat
- Snapchat
- google-dork
- snap-map
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Google site-search for Snapchat Places

> A Google dork (`site:snapchat.com/place/ inurl:…`) that surfaces Snapchat public "Place" pages — a way into Snap Map location content that Snapchat's app doesn't let you search by text.

## When to use
You want public Snapchat content tied to a location — a venue, neighbourhood or event a subject may have posted from. Snapchat's Snap Map has public "Place" pages, but you can't keyword-search them in-app. Using Google's index with `site:snapchat.com/place/` finds indexed place pages, which can lead to public snaps and story content associated with a spot.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a logged-out/sock-puppet browser, run `site:snapchat.com/place/` on Google, adding the place name or keyword (e.g. `site:snapchat.com/place/ "Venue Name"`).
2. Read the result titles/URLs — each is a public Snap Map Place page.
3. Open a place page to view associated public snaps/stories and the geographic context.
4. Cross-reference the location against a subject's known haunts/events.
5. Pivot: a public snap can reveal a `social-profile`, faces, or scene detail for geolocation; the place ties content to a `geolocation`.

## Inputs → Outputs
- **In:** a place `name` or `geolocation` context
- **Out:** Snapchat Place `social-profile`/`geolocation` pages and associated public snaps
- **Empty/negative result looks like:** no indexed place pages — Google hasn't crawled that place URL, or Snapchat serves the content only in-app. Absence in Google doesn't mean no Snap activity; complement with the Snap Map web/app directly.

## Gotchas & OpSec
- Snapchat is heavily app-centric; Google's coverage of place pages is partial and changes as Snapchat alters its public web surface.
- Public snaps are ephemeral — a page may point to content that's since expired.
- Combine with the Snap Map (map.snapchat.com) directly, which shows live public snaps by area that Google won't index.

## Overlaps ("do both")
- Pairs with the Snap Map web interface and other `site:` dorks (`[[google-com-53]]`, `[[google-com-48]]`) — the dork finds indexed pages; the live map shows current geotagged snaps the index misses.

## Trust & verifiability
`trust: trusted` — plain Google search; the mechanism is sound and first-party. The caveat is Snapchat's limited/indexed public web surface, not data authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-87 |
| category | social-networks |
| selectorsIn → selectorsOut | name, geolocation → social-profile, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
