---
id: fixmystreet
name: FixMyStreet
description: Use when you have an `address`/`geolocation` (or a reporter's `name`) and want public local-problem reports tied to that spot — returns `name` (reporter), `geolocation`, photos and dated activity.
url: https://www.fixmystreet.com
category: people-search
path:
- people-search
bestFor: Reading public street-problem reports pinned to an address, including reporter names, photos and timestamps.
selectorsIn:
- address
- geolocation
- name
selectorsOut:
- name
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free civic service run by mySociety; no account needed to browse reports.
opsec: passive
opsecNote: Public report map; browsing is passive and needs no login. To *file* a report you must register, but for OSINT you only read — stay in read-only mode.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by mySociety, a reputable UK civic-tech charity; reports are user-submitted so individual content is as reliable as its reporter.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Fix My Street
- mySociety FixMyStreet
tags:
- address
- civic
- geolocation
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# FixMyStreet

> A UK civic-reporting map where residents flag local problems (potholes, fly-tipping, broken lights) at a precise location — public reports often carry the reporter's name, a photo and a timestamp.

## When to use
You have an `address` or `geolocation` and want to see who has been active around it, or you have a reporter `name` and want to place them at a location and time. Reports are pinned to exact points and frequently show the reporter's display name, an uploaded photo, and dated updates — a niche way to tie a person to a neighbourhood, corroborate presence at a place/time, or surface a photo.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.fixmystreet.com and enter the `address`/postcode, or browse "All reports" and pan the map to the area.
2. Open individual reports at the location: read the reporter's display name, description, uploaded photos, and the report/update timestamps.
3. To search by person, use the site/Google to find reports under a display name.
4. Capture photos (which may carry EXIF or show recognisable surroundings) and dates.
5. Pivot: reverse-image report photos, place the reporter via the location/time, and enumerate the display name as a possible handle.

## Inputs → Outputs
- **In:** `address`/`geolocation`, or reporter `name`
- **Out:** reporter `name`/display name, `geolocation` (exact point), photos and `metadata-exif`-style timestamps
- **Empty/negative result looks like:** no reports at the location, or reports filed anonymously (some reporters hide their name) — absence of reports says nothing about who lives there.

## Gotchas & OpSec
- Not everyone uses their real name; display names are self-chosen — treat as a lead, not an identity.
- Some reports are filed anonymously or with names hidden by the council body.
- UK-focused (mySociety runs sister sites in other countries under different names/domains).

## Overlaps ("do both")
- Pairs with general people-search and reverse-image tools — FixMyStreet supplies a location/time/photo anchor that those turn into an identity.

## Trust & verifiability
`trust: trusted` — the platform (mySociety) is reputable, but each report is user-submitted, so verify any name/photo against a second source before asserting identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fixmystreet |
| category | people-search |
| selectorsIn → selectorsOut | address, geolocation, name → name, geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
