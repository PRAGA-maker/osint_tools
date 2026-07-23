---
id: ipinfo-map
name: IPinfo map
description: Use when you have one or many `ip-address`es and want to see where they geolocate — returns a plotted world map with per-IP `geolocation`.
url: https://ipinfo.io/map
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Bulk-plotting a list of IP addresses on a map to spot clustering or a rough geographic origin.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The paste-and-map tool is free and needs no account; full-accuracy datasets, the API, and large-volume enrichment sit behind IPinfo's paid/free-API-key tiers.
opsec: passive
opsecNote: "You are pasting IPs into ipinfo.io — you never contact the hosts themselves, so the map step is passive toward any target. IPinfo does log the addresses you submit. If the IPs came from your own logs (e.g. who visited a honeypot), remember you're disclosing them to a third party."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: IPinfo is a well-known commercial IP-data provider; free-tier geolocation is city-level and approximate, best treated as a region hint rather than a precise location.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- ipinfo.io map
- IPinfo bulk IP map
tags:
- Domain/IP/Links
- Domain/IP investigation
- ip-geolocation
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# IPinfo map

> Paste a list of IP addresses and IPinfo plots each one on a world map — a fast visual read on where a set of IPs sits.

## When to use
You have one or many `ip-address`es — from email headers, server logs, a login-history export, or a reverse-DNS pivot — and you want a quick geographic picture: are they clustered in one city/country, or scattered (VPN/proxy churn)? Useful for corroborating a claimed location or triaging which IP to investigate further. It geolocates IPs only; it will not identify a person, so missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ipinfo.io/map.
2. Paste up to 500,000 `ip-address`es (one per line) into the box and submit — no account needed.
3. Read the plotted map: each IP appears at its city/country centroid; hover/zoom to see counts and clustering.
4. Pivot: take a single interesting IP into IPinfo's per-IP page (or another IP tool) for ASN/ISP/hostname detail, or cross-check against the subject's claimed `address`.

## Inputs → Outputs
- **In:** `ip-address` (single or bulk list)
- **Out:** `geolocation` per IP plotted on a map (city/country level), cluster view
- **Empty/negative result looks like:** IPs dropping to a country centroid or not plotting — private/reserved ranges and some VPN exit IPs geolocate poorly; a pin is an estimate, not a home address.

## Gotchas & OpSec
- Free-tier geolocation is approximate (often city or ISP POP, not the user's actual location); never treat a pin as a precise physical `address`.
- VPN/proxy/mobile-carrier IPs will map to the provider's infrastructure, not the person — clustering at a datacenter city is a tell.
- OpSec: passive toward the target, but IPinfo logs the IPs you paste.

## Overlaps ("do both")
- Pairs with passive-DNS/reverse-IP tools like [[dns-dumpster]] (which surfaces the IPs behind a domain) and with bulk triage like [[cyberbro]] — resolve or extract IPs there, then visualize their spread here.

## Trust & verifiability
`trust: trusted` — IPinfo is an established commercial IP-intelligence provider, so the data pipeline is reliable; the caveat is precision, not honesty. Confirm any location that matters against a second geolocation source.
