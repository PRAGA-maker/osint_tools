---
id: about-maps-and-satellites
name: About Maps and Satellites (Bellingcat Toolkit)
description: Use when you have a `geolocation`/`address` and need to choose the right mapping or satellite tool for it — returns a curated, categorized guide to map/imagery resources.
url: https://bellingcat.gitbook.io/toolkit/more/all-tools/about-maps-and-satellites
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Deciding which map, satellite, or historical-imagery tool fits a geolocation task, from Bellingcat's vetted toolkit.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, openly published section of Bellingcat's Online Investigation Toolkit (hosted on GitBook); no account needed.
opsec: passive
opsecNote: Reading a curated guide — no target is queried. The tools it points to have their own OpSec profiles; the guide itself leaks nothing about a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Bellingcat, a leading open-source investigation organization, as part of their widely used and regularly updated toolkit; entries are practitioner-vetted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bellingcat-meta-content-library
- bellingcat-s-online-investigation-toolkit-2
- china-related-resources
- license-plate-maps
aliases:
- Bellingcat Maps and Satellites guide
tags:
- bellingcat-toolkit
- maps
source: bellingcat-toolkit
lastVerified: '2026-08-05'
enrichment: full
---

# About Maps and Satellites (Bellingcat Toolkit)

> Bellingcat's curated orientation to mapping and satellite-imagery tools — the index that tells you which imagery resource to reach for on a given geolocation problem.

## When to use
You have a `geolocation` or `address` to verify, geolocate, or monitor and you're unsure which map/satellite tool fits — current high-res imagery, historical imagery for change-over-time, oblique/street-level views, or specialist regional providers. This section of Bellingcat's toolkit categorizes the options with practitioner notes, so you pick the right instrument instead of trial-and-error across a dozen sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the guide at the Bellingcat toolkit URL.
2. Read the categorized entries: base mapping/satellite providers, historical-imagery archives, and specialist/regional tools, each with what it's good for.
3. Match your task (verify a photo's location, watch a site over months, find older imagery) to the recommended tool class.
4. Follow the link to the actual tool and run the geolocation there.
5. Pivot: confirmed coordinates → cross-check with a second imagery source and with ground-level photos; feed dates from historical imagery into a timeline.

## Inputs → Outputs
- **In:** a `geolocation`/`address` problem to solve (the guide helps you choose the tool)
- **Out:** a curated shortlist of map/satellite tools and when to use each → leads to confirmed `geolocation`
- **Empty/negative result looks like:** the guide is static reference — "nothing found" isn't a state; if your niche (e.g. a specific country's cadastral imagery) isn't covered, consult Bellingcat's regional resource pages.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a reading resource.
- It's an index, not an imagery engine — the actual geolocation happens in the tools it links to, each with its own limits and OpSec.
- Freshness: Bellingcat updates the toolkit periodically, but always confirm a linked tool is still live before relying on it.

## Overlaps ("do both")
- Pairs with [[bellingcat-s-online-investigation-toolkit-2]] (the full toolkit) and [[china-related-resources]] / [[license-plate-maps]] — this narrows to maps/imagery; the others cover adjacent geospatial and regional needs.

## Trust & verifiability
`trust: trusted` — curated by Bellingcat, a reputable open-source investigation body; the guidance is practitioner-vetted, though it points to third-party tools whose individual reliability you should still confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | about-maps-and-satellites |
