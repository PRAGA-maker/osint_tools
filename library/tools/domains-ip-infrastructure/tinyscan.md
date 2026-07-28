---
id: tinyscan
name: TinyScan
description: Use when you have a `domain`/URL and want a safe remote scan — screenshot, resolved IP/geolocation, tech stack, DNS/SSL/headers — without visiting it yourself; returns ip-address, domain.
url: https://www.tiny-scan.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Remotely inspecting a suspicious URL (screenshot + IP + tech + DNS/SSL) without touching it from your own browser.
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
- geolocation
status: live
pricing: freemium
costNote: Free plan scans URLs and returns basic info (screenshot, IP, DNS, headers); premium adds advanced features. No account needed for a basic scan.
opsec: active
opsecNote: TinyScan's servers load the target URL, so the visit hits the target's site — but from TinyScan's infrastructure and IP, not yours, which shields your identity. You can set a custom User-Agent/Referer/Accept-Language for the scan. Never open a suspected malware/phishing URL directly; let the scanner take the hit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A urlscan-style third-party URL analysis service. Results are machine-collected from a single fetch and reflect one point in time; corroborate for anything critical.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- urlscan-io
- domain-dossier
- urlquery
tags:
- domain-and-ip-research
- url-scanner
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# TinyScan

> A remote URL scanner (urlscan.io-style): submit a link and get a screenshot, resolved IP/location, tech stack, DNS/SSL, and headers — so you inspect a hostile site without loading it yourself.

## When to use
You have a `domain` or full URL — a suspicious link, a phishing page, a subject's site — and want to see what it is and where it's hosted without exposing your own browser/IP. Returns hosting `ip-address` and `geolocation`, technology fingerprints, and a rendered screenshot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tiny-scan.com and paste the URL.
2. (Optional) set a custom User-Agent / Referer / Accept-Language to mimic a target visitor or evade cloaking.
3. Run the scan and read the report: desktop/mobile screenshots, resolved IP and server location, detected tech stack, DNS records, SSL cert, HTTP headers, cookies, and extracted links/JS.
4. Note IP + hosting → for infrastructure pivots; screenshot → to confirm content without visiting.
5. Pivot: the IP → `[[domain-dossier]]`/reverse-IP for co-hosted sites; extracted links → follow the redirect/phishing chain safely.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** `ip-address` and `geolocation` (server), `domain` (resolved host, linked domains), tech stack, DNS/SSL/headers, screenshot
- **Empty/negative result looks like:** the scan fails to load the page (dead site, geo/UA cloaking, or bot-blocking) — try a different User-Agent, or cross-check with another scanner before concluding the site is down.

## Gotchas & OpSec
- The scan **visits the target** from TinyScan's servers; this protects you, but the target's logs will show the scanner's hit (and cloaking sites may serve it different content).
- Single-fetch snapshot — dynamic/cloaked sites can look different to real visitors.
- Community service; verify critical findings with a second scanner.

## Overlaps ("do both")
- Pairs with `[[urlscan-io]]` / `[[urlquery]]` — run the URL through more than one scanner to defeat cloaking and fill gaps, and with `[[domain-dossier]]` for the WHOIS/DNS side.

## Trust & verifiability
`trust: community` — a third-party scanner; its screenshot and IP data are reliable for the moment of the scan but reflect one fetch. Corroborate before acting on a high-stakes verdict.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tinyscan |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → ip-address, domain, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
