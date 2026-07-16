---
id: freemaptools
name: FreeMapTools
description: Use when you have a `geolocation` or `address`/postcode and want to measure radius/distance, convert coordinates, or find places within an area — returns `geolocation`, `address` (coordinate/postcode conversions and area listings).
url: http://www.freemaptools.com
category: geolocation
path:
- geolocation
bestFor: Free browser map utilities — radius/area drawing, distance measurement, coordinate↔postcode conversion, and elevation lookups.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: All tools are free; an optional ad-free subscription exists but no feature is paywalled and no account is required.
opsec: passive
opsecNote: A client-side mapping utility — you enter coordinates/postcodes you already have, and it does no lookup against the target, so it leaks nothing about the subject. Standard browser hygiene only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-standing independent map-utilities site; results (distances, conversions, elevations) are computed from standard map data and are reliable for planning, not authoritative for legal boundaries.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Free Map Tools
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- free-map-tools
- freemaptools-com
---

# FreeMapTools

> A free suite of browser map utilities — draw radius/area circles, measure distances, convert coordinates↔postcodes, and find places within a zone.

## When to use
You have a `geolocation` (lat/long) or an `address`/postcode and need to do spatial reasoning around it: how far apart two points are, what falls within an X-km radius, the elevation of a spot, or converting between a UK/US postcode/ZIP and coordinates. In a missing-persons workflow, use it to define a search radius around a last-known location, list hospitals/towns inside that radius, or reconcile coordinates from photo EXIF with a street address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.freemaptools.com and pick the tool you need (Radius Around Point, Distance/Area, Elevation Finder, Postcode↔Lat/Long, Find Places, etc.).
2. Enter your `geolocation` or `address`/postcode, or click points on the map.
3. Set parameters (radius distance, units) and read the computed output.
4. Use country-specific tools (UK postcode/National Grid, US ZIP) where relevant.
5. Pivot: feed converted coordinates into imagery/mapping tools, or use the radius/place list to prioritize where to search next.

## Inputs → Outputs
- **In:** `geolocation` (lat/long) or `address`/postcode
- **Out:** `geolocation` (converted coordinates), `address` (postcode/place resolutions), plus computed distances, areas, elevations, and in-radius place lists
- **Empty/negative result looks like:** a postcode/coordinate that doesn't resolve (mistyped or unsupported country), or an empty "places within radius" list — meaning no matching features in that zone, not a tool failure.

## Gotchas & OpSec
- Computations are for planning/visualization, not legally authoritative boundaries or survey-grade positions.
- Coverage of postcode/place tools is best for UK, US, and a handful of listed countries; other regions are thinner.
- Fully passive and client-side — you only enter data you already hold.

## Overlaps ("do both")
- Pairs with EXIF/geolocation extractors and mapping platforms — FreeMapTools handles the measurement/conversion math, while dedicated geolocation tools verify and visualize the actual place.

## Trust & verifiability
`trust: unverified` — an independent utility site. Its geometric/conversion outputs are dependable for analysis, but treat any boundary or elevation figure as an estimate and confirm against an authoritative source when it matters.
