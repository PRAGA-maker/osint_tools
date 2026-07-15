---
id: google-com-86
name: "Snapchat public places Google dork (site:snapchat.com/place/)"
description: Use when you have a `geolocation`/place name or want to enumerate Snapchat public "place" pages — a Google dork that returns Snapchat place `social-profile`/location URLs.
url: https://www.google.com/search?client=firefox-b-d&q=site%3Asnapchat.com%2Fplace%2F
category: social-networks
path:
- social-networks
bestFor: Surfacing Snapchat public place/location pages via a Google site: dork.
selectorsIn:
- geolocation
- name
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free — it is just a Google search with a `site:` operator.
opsec: passive
opsecNote: The dork runs against Google, not Snapchat, so it is passive toward the target. Clicking through into Snapchat itself is where you may be logged/observed — do that logged out or via a sock-puppet. Volume dorking can trigger Google CAPTCHAs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: This is a saved Google query, not a tool with its own data — reliability depends on Google's current index of Snapchat place pages, which changes over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- searchenginejournal-com
aliases:
- Snapchat place dork
- site:snapchat.com/place
tags:
- snapchat
- Snapchat
- google-dorking
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Snapchat public places Google dork (site:snapchat.com/place/)

> A pre-built Google dork — `site:snapchat.com/place/` — that enumerates Snapchat's public "place" pages, which aggregate public Snaps posted at a location.

## When to use
You want to find Snapchat public place/location pages, either to browse public content posted at a `geolocation` or to add a place term to narrow results. Snapchat place pages surface publicly-shared Snaps tied to a venue/area, which can put activity at a location on the map. Combine the base dork with a place `name` (e.g. add `"Denver"` or a venue name) to target a specific area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL, or run `site:snapchat.com/place/` in Google.
2. Append a place/venue term to focus it, e.g. `site:snapchat.com/place/ "central park"`.
3. Review the indexed Snapchat place-page URLs in the results.
4. Open a place page (logged out / sock-puppet) to view publicly-shared content tied to that location.
5. Pivot: public Snaps/handles seen there feed username enumeration and geolocation corroboration; the place URL itself is a durable pointer to that location's public feed.

## Inputs → Outputs
- **In:** `geolocation` / place `name`
- **Out:** Snapchat place-page URLs (`social-profile`/`geolocation` pages), and public content reachable from them
- **Empty/negative result looks like:** few or no results — Snapchat frequently changes which place pages are indexable, so a thin result set reflects Google's index, not necessarily an absence of the place. Try a broader term or Snap Map directly.

## Gotchas & OpSec
- Index-dependent: Google's coverage of `snapchat.com/place/` fluctuates; treat a null result as inconclusive.
- The dork finds pages; actually viewing content still means visiting Snapchat — do so without your real account.
- For live location content, Snap Map (map.snapchat.com) is the more direct source; this dork is for indexed/durable place pages.

## Overlaps ("do both")
- Pairs with `[[searchenginejournal-com]]` (to extend/modify the dork) and with Snap Map — the dork finds durable place pages, Snap Map shows live public Snaps by area.

## Trust & verifiability
`trust: community` — it is a search recipe, not a data source; verify anything found by opening the actual Snapchat page and corroborating with a second location signal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-86 |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation, name → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
