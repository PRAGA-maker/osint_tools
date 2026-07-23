---
id: wideband-shortware-radio-receiver-map
name: KiwiSDR Receiver Map
description: Use when you want to listen to radio from a specific place (or geolocate a transmission) — a world map of public online SDR receivers you can tune in-browser, returning geolocation context.
url: http://rx.linkfanel.net/
category: communities-forums
path:
- communities-forums
bestFor: Finding and using public online SDR (KiwiSDR) receivers near a location to monitor radio, or to TDoA-geolocate a transmitter.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
opsec: passive
opsecNote: You listen through volunteers' public receivers; the receiver operator can see that a client connected, but no target person is contacted. Tuning to a frequency alerts no transmitter. TDoA geolocation and simple "listen from near a place" are passive intelligence gathering; note some KiwiSDRs restrict frequencies or connections.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running community map of public KiwiSDR/WebSDR receivers; availability of any given receiver varies and the map can be briefly unavailable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- KiwiSDR map
- rx.linkfanel.net
- shortwave receiver map
tags:
- sdr
- radio
- signals
- tv-radio
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# KiwiSDR Receiver Map

> A live world map of public online SDR receivers — pick one near any location and tune the radio spectrum in your browser, or use several together to geolocate a transmitter by time-difference-of-arrival.

## When to use
A niche SIGINT-flavored tool. Two uses: (1) **listen from a place** — tune a receiver physically near a `geolocation` of interest to hear local shortwave/HF/utility/amateur traffic you couldn't receive remotely; (2) **geolocate a transmission** — many KiwiSDRs support TDoA, letting you fix the approximate location of an unknown HF transmitter using multiple receivers. Useful for radio-signals investigations and situational awareness around a region.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://rx.linkfanel.net/ — a map of currently-online public SDR receivers worldwide (green = available).
2. Click a receiver near your area of interest (`selectorsIn`) to open its web interface; tune frequency/mode in the browser.
3. To geolocate: use a KiwiSDR's TDoA extension, selecting several receivers that can hear the same signal, to estimate the transmitter's `geolocation`.
4. Pivot: what you hear (languages, callsigns, content) and any TDoA fix feed the broader investigation.

## Inputs → Outputs
- **In:** `geolocation` (a place to receive from / around)
- **Out:** live audio/spectrum from that area, and (via TDoA) an estimated transmitter `geolocation`
- **Empty/negative result looks like:** no online receivers near the target area, or all busy/offline — coverage is volunteer-dependent and sparse in some regions; try nearby receivers or later.

## Gotchas & OpSec
- Human-in-the-loop: none, though receivers have limited concurrent slots.
- OpSec: passive listening; the receiver host sees a client connection but no target is involved. Respect each receiver's usage limits and local radio laws.
- Availability is fluid: receivers go on/offline constantly and the map itself can be briefly unavailable (retry).

## Overlaps ("do both")
- Pairs with WebSDR networks, aircraft/marine signal tools, and frequency databases — use the map to reach a receiver, and reference/decoding tools to interpret what you hear; TDoA complements other geolocation methods for HF sources.

## Trust & verifiability
`trust: community` — a well-known community map of volunteer-run receivers. The receivers genuinely work, but coverage and uptime vary; treat a TDoA fix as an estimate to corroborate, and confirm anything heard against other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wideband-shortware-radio-receiver-map |
| category | communities-forums |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
