---
id: edge
name: Microsoft Edge
description: Use when you need an investigator browser with InPrivate windows, DevTools device/geo emulation and Collections — a free Chromium browser for compartmentalised OSINT sessions.
url: https://www.microsoft.com/en-us/windows/microsoft-edge/microsoft-edge
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A free Chromium-based browser usable as a disposable/compartmentalised investigation environment.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free from Microsoft; bundled with Windows and available for macOS/Linux. No account required (signing in syncs profiles but is optional).
opsec: passive
opsecNote: The browser itself is a neutral tool, but it is your OpSec surface — sign OUT, use a dedicated InPrivate/guest profile per investigation, and route through a VPN so sessions aren't linked to your identity or to each other. Signing into a Microsoft account defeats compartmentalisation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: First-party Microsoft browser built on open-source Chromium; the browser is genuine, though as a Microsoft product it phones home telemetry you should harden.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Microsoft Edge browser
- Chromium Edge
tags:
- browsers
- investigator-tooling
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Microsoft Edge

> A free Chromium-based browser you can run as a compartmentalised investigation environment — InPrivate windows, DevTools emulation, and Collections for gathering evidence.

## When to use
You need a browser to actually do the investigating, and want one you can keep separate from your day-to-day identity. Edge is Chromium under the hood (so it renders like Chrome and runs Chrome extensions) but is worth listing for a few investigator-friendly features: InPrivate windows and guest profiles for throwaway sessions, per-investigation profiles, DevTools device/geolocation/user-agent emulation to see a site as another device or location would, and the built-in Collections feature for clipping and organising evidence as you go.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Edge (or use the bundled Windows copy). Do **not** sign into a personal Microsoft account for investigation work.
2. Create a dedicated profile (or use InPrivate/guest) per case so cookies, history and logins stay compartmentalised.
3. For location/device-sensitive checks, open DevTools → device toolbar / Sensors to override user-agent and geolocation.
4. Use Collections to clip pages, images and notes into a per-case bundle as you browse.
5. Harden: disable sync/telemetry where possible, add your OSINT extensions, and route the profile through a VPN.

## Inputs → Outputs
- **In:** n/a — it's the environment you run other tools/lookups in, not a selector-in tool.
- **Out:** n/a — it renders and captures what other sources return.
- **Empty/negative result looks like:** n/a. Judge it as a workspace, not a data source.

## Gotchas & OpSec
- OpSec: the browser is your exposure surface. Signed-in sync, saved logins, and telemetry can link sessions — keep profiles clean, sign out, and use a VPN.
- It is not an OSINT data source; it finds nothing on its own. Don't over-rate it — it's plumbing.
- As Chromium, it runs Chrome extensions, so most `browser-extension` tools in this library work here too.

## Overlaps ("do both")
- Interchangeable with other investigator browsers (`[[tor-browser]]` for anonymity, a hardened Firefox/Chromium profile) — pick per need: Tor for anonymity, Edge/Chromium for compatibility and Collections-based evidence capture.

## Trust & verifiability
`trust: trusted` — genuine first-party Microsoft software built on open-source Chromium; the tool is trustworthy, but harden its telemetry/sync for OpSec.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | edge |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
