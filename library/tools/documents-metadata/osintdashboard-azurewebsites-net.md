---
id: osintdashboard-azurewebsites-net
name: OSINT Dashboard
description: Use when you have a `domain`, `image`, or `phone` and want a quick combined lookup — returns URL/IP/DNS details, image EXIF/GPS, and phone carrier/location.
url: https://osintdashboard.azurewebsites.net/
category: documents-metadata
path:
- documents-metadata
bestFor: A single-page multi-tool for URL/IP analysis, image EXIF extraction, and phone-number lookup.
selectorsIn:
- domain
- image
- phone
selectorsOut:
- ip-address
- domain
- geolocation
- metadata-exif
status: degraded
pricing: free
costNote: Free student/community project; hosted on a free Azure App Service tier, so it may sleep or be slow on first load.
opsec: passive
opsecNote: URL/phone lookups query public data sources server-side, and EXIF is parsed from the image you upload — none of this contacts the subject. Uploading an image sends it to a third-party server, so strip anything sensitive you don't want stored, or use a local EXIF tool for sensitive files.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open-source project (source on GitHub) by named student authors; it aggregates third-party lookups, so accuracy — especially phone "user information" — is only as good as its upstream sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- sn-radar-vk-photo-search
- snradar
aliases:
- OSINT Dashboard
- osintdashboard.azurewebsites.net
tags:
- multi-tool
- exif
- phone-lookup
source: uk-osint
lastVerified: '2026-07-29'
enrichment: full
---

# OSINT Dashboard

> A lightweight, open-source single-page toolkit bundling three common lookups — URL/IP analysis, image EXIF extraction, and phone-number carrier/location — behind one interface.

## When to use
You want a fast first pass on a mixed lead without opening three separate tools: a `domain`/URL to profile (IP, server, DNS), an `image` to strip for EXIF/GPS, or a `phone` number to check carrier, likely location, and whether it's VoIP. Good for quick triage; corroborate anything important with dedicated tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the dashboard (allow a moment — free Azure hosting may cold-start).
2. Pick a module: URL Analysis, Exif Viewer, or Phone Lookup.
3. Enter/upload the input (`domain`, `image`, or `phone`).
4. Read the output: IP/server/DNS for URLs; camera/timestamp/GPS for images; carrier/location/VoIP flag for phones.
5. Pivot: GPS from EXIF → mapping; IP/DNS → infrastructure tools; carrier/location → phone-OSINT follow-up.

## Inputs → Outputs
- **In:** `domain`/URL, `image`, or `phone`
- **Out:** `ip-address`/`domain`/DNS details, `metadata-exif` (incl. GPS `geolocation`), phone carrier/location/VoIP flag
- **Empty/negative result looks like:** blank fields or an error — the image had EXIF stripped (common on social-media downloads), the number is unlisted, or the site cold-started/timed out; retry or use a specialist tool.

## Gotchas & OpSec
- Free-tier hosting: expect occasional slowness, sleeping, or downtime (`status: degraded`).
- Phone "user information" from aggregators is often generic or wrong — treat carrier/region as indicative, not identity.
- Social-media images usually have EXIF removed by the platform, so a blank EXIF result is normal, not a tool failure.

## Overlaps ("do both")
- Pairs with dedicated EXIF viewers and phone-intel tools for depth — this dashboard is a quick triage front-end, not a replacement for specialist lookups.

## Trust & verifiability
`trust: community` — a small open-source student project aggregating third-party data; verify any load-bearing result (especially phone attribution) against a primary or specialist source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintdashboard-azurewebsites-net |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain, image, phone → ip-address, domain, geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
