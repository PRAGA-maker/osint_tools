---
id: trace-my-ip
name: Trace My IP (tracemyip.org)
description: Use when you want to confirm your own visible `ip-address`/`geolocation` before operating, or to generate a tracking link — returns the visitor's IP, geolocation and connection details.
url: https://www.tracemyip.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Verifying what IP/geolocation you are exposing (VPN/proxy self-check), and optionally creating tracking links/pixels that log visitors.
selectorsIn: []
selectorsOut:
- ip-address
- geolocation
status: live
pricing: freemium
costNote: Free to see your own IP/geo and to sign up for basic visitor tracking; advanced tracking (many sites, alerts, history) is paid.
opsec: active
opsecNote: Visiting logs YOUR IP — that is the point when self-checking, but only visit through the setup you intend to use operationally. Its tracking-link feature, if you deploy it against a target, is ACTIVE and legally sensitive — sending someone a logging link to grab their IP can be unlawful/entrapment-adjacent depending on jurisdiction and consent; do not use it without authorisation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running commercial IP-info and visitor-tracking service. Reliable for showing your own connection details; geolocation of any IP is ISP-level approximate, not a precise address.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- user-agent-string-decoder
aliases:
- TraceMyIP
- tracemyip.org
tags:
- vpn-test
- ip-lookup
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# Trace My IP (tracemyip.org)

> An IP-reveal and visitor-tracking service — primarily an OpSec self-check to confirm what IP and location you are exposing before you start work.

## When to use
Two distinct uses. (1) **Self-check (primary, safe):** before running any active OSINT, open it to confirm your VPN/proxy is up and that the IP, ISP, and geolocation you present are what you expect — not your real ones. (2) **Visitor tracking (advanced, sensitive):** it can generate tracking links/pixels that log the IP and details of whoever opens them — a powerful but legally fraught technique that must only be used with proper authorisation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Route your browser through your intended VPN/proxy/Tor setup, then open https://www.tracemyip.org/.
2. Read the displayed IP, ISP, country/region/city, and connection type; confirm none of it maps back to your real identity or location.
3. Repeat after switching servers to verify the IP actually changes and no leak (WebRTC/DNS) exposes the real address — corroborate with a dedicated leak-test tool.
4. (Only if authorised) use the account features to create a tracking link and monitor visitor IPs — understand the legal constraints first.
5. Pivot: a confirmed-clean setup greenlights active steps; a leak means fix the tooling before proceeding.

## Inputs → Outputs
- **In:** none (it reads your current connection) — or a deployed tracking link for the advanced use
- **Out:** `ip-address`, `geolocation` (ISP-level), ISP/connection details
- **Empty/negative result looks like:** it shows your **real** IP/location — meaning your anonymisation is not working; stop and fix before doing anything active.

## Gotchas & OpSec
- **Active:** visiting logs your IP — only ever visit through the exact setup you plan to operate behind.
- Geolocation is ISP/region-level and often imprecise — do not treat it as a street address.
- The tracking-link feature is legally sensitive; using it to grab a target's IP without consent/authorisation can be unlawful. Treat self-check as the default use.

## Overlaps ("do both")
- Pairs with a dedicated leak-test (WebRTC/DNS) and `[[user-agent-string-decoder]]` — this shows the IP/geo you present, those catch leaks and fingerprinting your IP check alone would miss.

## Trust & verifiability
`trust: unverified` — a real commercial service, reliable for reporting your own connection details; any IP geolocation it reports (yours or a visitor's) is approximate and must not be read as a precise location.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trace-my-ip |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → ip-address, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
