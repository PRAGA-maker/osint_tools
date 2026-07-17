---
id: google-maps-timeline-exporter
name: Google Maps Timeline Exporter
description: Use when you have access to a subject's Google `geolocation` history (their logged-in session or a Takeout export) and want to convert it into analysable CSV — returns structured location/movement rows.
url: https://chrome.google.com/webstore/detail/timeline-exporter/afalbippddliaaomolohcbfogogbjpkk
category: geolocation
path:
- geolocation
bestFor: Turning a Google Maps Timeline (or Takeout location export) into CSV rows of places, times, and mileage for offline analysis.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- address
status: degraded
pricing: free
costNote: Free Chrome extension; processes data locally in the browser, no server or subscription.
opsec: active
opsecNote: Requires being logged into the target's own Google account (or holding their Takeout export) — this is consent/authorization-gated data, not open-source intel. Only run against an account you are lawfully authorized to access (e.g. the reporting family's own device with permission). It reads the private Timeline, so treat the output as sensitive personal data.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Open-source extension by reinzor (github.com/reinzor/timeline-exporter); community tool with no official Google affiliation. Reliability degraded since Google moved Timeline to on-device storage.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- google-maps
aliases:
- Timeline Exporter
- Google Timeline CSV export
tags:
- Maps, Geolocation and Transport
- Tools
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Google Maps Timeline Exporter

> A Chrome extension that scrapes a logged-in Google Maps Timeline into CSV — for turning a subject's own (authorized) location history into a movement analysis.

## When to use
You have lawful access to a subject's Google account — for example a missing person's family authorizing you to work from their relative's logged-in device — and want to convert the Google Maps **Timeline** into a spreadsheet of visited places, timestamps, and travel legs. This is not open-source intel: it only works when you can reach the account's private location history. Use it to reconstruct a last-known-movements timeline.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the "Timeline Exporter" extension from the Chrome Web Store (source: github.com/reinzor/timeline-exporter).
2. In the same browser, sign in to the Google account you are authorized to examine.
3. **Important since late 2024:** Google discontinued the web Timeline at timeline.google.com and moved history onto the device. If the web Timeline is unavailable, instead pull the data via Google **Takeout** (Location History / "Timeline") and use the extension/companion to parse that export.
4. Set the date range, run the export, and download the CSV.
5. Pivot: geocode the CSV rows into a map, cross-reference addresses against `[[google-maps]]`, and align timestamps with other timeline evidence.

## Inputs → Outputs
- **In:** authorized access to a Google account's Timeline, or its Takeout export (`geolocation`)
- **Out:** CSV rows of visited places, coordinates, timestamps, and mileage → derives `geolocation` and candidate `address` points
- **Empty/negative result looks like:** an empty CSV or an export error — Location History was never enabled on that account, or Google's UI/API changed and the scrape blocked (common now).

## Gotchas & OpSec
- **Active & authorization-gated:** you must be logged into the account. Only do this with clear legal authority; accessing someone's Google account without consent is unlawful.
- Reliability is degraded — Google's move to on-device Timeline and bot protections frequently break large date-range exports. The Takeout route is more dependable.
- All processing is local (no third-party server sees the data), but the CSV itself is highly sensitive; store it accordingly.

## Overlaps ("do both")
- Pairs with `[[google-maps]]` — export the raw points here, then plot and street-view each stop in Google Maps to interpret the movements.

## Trust & verifiability
`trust: unverified` — community open-source extension, not a Google product. The data it exports is authoritative (it's Google's own Timeline), but the extension itself is unaudited and its reliability now depends on Google's changing UI.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-maps-timeline-exporter |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
