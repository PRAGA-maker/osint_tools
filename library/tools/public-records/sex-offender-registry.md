---
id: sex-offender-registry
name: Sex Offender Registry
description: Use when you have a `name` or `address` and want to check US sex-offender registry listings — returns a registrant's `address`, `physical-description` and offense record (aggregates state registries).
url: http://www.sexoffender.com/
category: public-records
path:
- public-records
bestFor: A single-entry point to search US state sex-offender registries by name or location.
selectorsIn:
- name
- address
selectorsOut:
- address
- physical-description
status: degraded
pricing: freemium
costNote: The registry search itself is free (registries are public by law); the site carries ads and may hand off to paid background-check brokers, but you do not need to pay to view registry listings.
opsec: passive
opsecNote: Passive — registry data is public and the search does not alert the registrant. For authoritative, non-commercial results prefer the government source (NSOPW.gov); use this aggregator only as a convenience layer, via a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party commercial aggregator of public registry data, not a government site; listings can be stale or incomplete, so confirm against the official state registry or NSOPW.gov.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- sexoffender.com
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Sex Offender Registry

> A commercial front-end for searching US sex-offender registries by name or location — convenient, but always confirm hits against the official government registry.

## When to use
You have a US `name` or `address` and want to check whether the person appears on a sex-offender registry — for risk assessment, corroborating a current address (registrants must report their address), or a `physical-description`/photo. This aggregator can be a quick single search box, but the **authoritative** source is the Department of Justice's NSOPW (nsopw.gov); use this only as a convenience and verify results officially.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.sexoffender.com/ in a sock-puppet browser (expect ads and occasional rate-limiting / 503s).
2. Search by name, or by location/ZIP to see registrants in an area.
3. Read a listing: registrant name, reported `address`, photo and `physical-description`, and offense details.
4. **Verify** any hit against the official state registry or nsopw.gov before relying on it — commercial aggregators lag and mis-match.
5. Pivot: a confirmed reported address (registrants are legally required to keep it current) is a strong lead for locating someone; the photo aids visual ID.

## Inputs → Outputs
- **In:** `name` or `address`/ZIP
- **Out:** registrant `address`, `physical-description`/photo, offense record
- **Empty/negative result looks like:** "no results" — the person isn't registered, isn't in this aggregator's copy, or the name is spelled differently; absence here is not proof, re-check NSOPW.

## Gotchas & OpSec
- **Not a government site** — it republishes registry data with ads and paid upsells; treat it as a pointer, not the record of authority.
- Same-name collisions are common; match on photo/DOB/location, not name alone.
- Registry inclusion and the reported address are legally maintained data, so a *verified* hit is unusually reliable for current-address purposes — but verify it at the source.

## Overlaps ("do both")
- Always cross-check against the official NSOPW.gov and the specific state registry; use this aggregator only to cast a first, single-box net.

## Trust & verifiability
`trust: unverified` — a commercial aggregator; the underlying registries are authoritative, so escalate every hit to the government source to confirm before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sex-offender-registry |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, physical-description |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
