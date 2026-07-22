---
id: strava
name: Strava
description: Use when you have a `name`/`username` or a location of interest and want exercise-route patterns — returns public activities, segments and heatmap `geolocation` traces.
url: https://www.strava.com
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Finding where a subject runs/rides (home, gym, routine routes) via their public Strava activities, or reading a location's activity from the global heatmap.
selectorsIn:
- name
- username
- geolocation
selectorsOut:
- geolocation
- social-profile
- associate
status: live
pricing: freemium
costNote: Free account lets you view public profiles, activities and the global heatmap; street-level heatmap zoom and some map detail require a paid subscription.
opsec: passive
opsecNote: Viewing a public profile or the heatmap is passive, but Strava shows athletes who views their profile if you use a logged-in identifiable account — use a sock-puppet account. Following a private athlete sends them a request (active); never do that from an attributable account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party data from the subject's own device GPS; famously reliable enough that the heatmap exposed secret military bases and a president's bodyguards' routes.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- strava.com
- Strava heatmap
tags:
- geolocation
- fitness
- heatmap
source: bellingcat-toolkit
lastVerified: '2026-07-22'
enrichment: full
---

# Strava

> A fitness social network whose public GPS activities and global heatmap can reveal exactly where a person runs, rides and lives — the tool behind the military-base and Macron-bodyguard exposés.

## When to use
You have a subject's real `name` or a likely Strava `username`, or you have a `geolocation` of interest, and you want their movement patterns: regular routes, start/end points (often home or workplace), training times, and connected athletes (`associate`). Strava is one of the highest-yield location tools when the subject is a keen cyclist/runner who forgot to lock their profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet Strava account (needed to view the heatmap and many activities).
2. Search the athlete directory for the `name`/`username`; open a public profile for activities, routes, clubs and followers.
3. Inspect individual activities for the map trace — repeated start points frequently reveal home; commute routes reveal workplace.
4. For a location-first approach, open the Global Heatmap and zoom to the area of interest to see aggregated activity density (street-level zoom needs a subscription).
5. Pivot: start/end coordinates feed reverse-geocoding; club and follower lists feed `associate` mapping.

## Inputs → Outputs
- **In:** `name` / `username`, or a `geolocation` (for the heatmap)
- **Out:** `geolocation` traces, `social-profile` (activities, clubs), connected athletes (`associate`)
- **Empty/negative result looks like:** a profile marked private, "Only You"/"Followers" activities, or a subject with map-visibility hidden — excluded from the heatmap and profile view; absence of data ≠ absence of activity.

## Gotchas & OpSec
- Human-in-the-loop: an account is required for heatmap/weekly-map and full activity view — use a sock puppet, never your real identity.
- Privacy-zone and visibility settings hide home addresses on well-configured profiles; don't assume the shown start point is home.
- Never *follow* a private athlete to peek — that request notifies them (active/attributable).

## Overlaps ("do both")
- Pairs with reverse-geocoding and mapping tools (to resolve route endpoints to addresses) and with username-enumeration (the same handle often appears on other fitness/social apps).

## Trust & verifiability
`trust: trusted` — activities are the subject's own device GPS, so the location data is authoritative; the risk is over-reading (a start point isn't always home).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | strava |
