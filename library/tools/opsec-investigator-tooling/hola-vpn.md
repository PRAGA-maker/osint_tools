---
id: hola-vpn
name: Hola VPN
description: Use when you want to change your apparent egress country for casual geo-unblocking — but note it is a peer-to-peer network with a poor privacy record, so it is NOT recommended for investigative OpSec.
url: https://hola.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Casual geo-location switching in a browser — with heavy caveats; not for sensitive investigative traffic.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier (browser extension) plus a paid "Hola VPN Plus" tier. The free tier is peer-to-peer — your device can be used as an exit node for other users.
opsec: active
opsecNote: Do NOT use Hola for investigative anonymity. The free tier routes traffic through other users' devices (and historically sold idle bandwidth via the Luminati/Bright Data network), so your traffic may exit through a stranger's IP and other traffic may exit through yours. Prefer a reputable no-logs commercial VPN or Tor for sock-puppet work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Commercial consumer product with a documented history of privacy/security controversies (bandwidth resale, exit-node exposure); listed here mainly so investigators recognise and avoid it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Hola
- Hola Free VPN
- Hola Unblocker
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Hola VPN

> A free peer-to-peer browser "VPN" for geo-unblocking — included here as a cautionary entry: convenient, but the wrong tool for investigator OpSec.

## When to use
Only for low-stakes, non-attributable geo-unblocking where you understand and accept that your traffic may route through other users' devices. For any real investigative OpSec — masking your origin while touching a subject's infrastructure or accounts — **do not use Hola**; reach for a reputable no-logs VPN or Tor instead.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Hola extension from your browser's web store (or the desktop/mobile app) from https://hola.org.
2. Pick a country to appear to browse from; Hola routes your request through its network.
3. Understand the trade-off: on the free tier your own connection can serve as an exit node for others, and their traffic can exit through you.
4. Better path: uninstall after casual use, or skip entirely in favour of a trusted VPN/Tor for anything sensitive.

## Inputs → Outputs
- **In:** none (it is an egress/proxy tool, not a lookup)
- **Out:** none (changes your apparent location; produces no investigative data)
- **Empty/negative result looks like:** N/A — success is simply your traffic appearing to originate from the chosen country.

## Gotchas & OpSec
- Human-in-the-loop: none, but the real "gotcha" is the privacy model itself.
- Peer-to-peer exit routing means unpredictable, shared IPs — the opposite of controlled attribution.
- Historic bandwidth-resale controversy (Luminati/Bright Data) means "free" has a cost you may not want to pay in an investigation.

## Overlaps ("do both")
- Contrast with any reputable commercial VPN entry in this category, or Tor: those give controlled, single-tenant egress. Hola is the example of what to avoid.

## Trust & verifiability
`trust: unverified` — a consumer product with a well-documented privacy track record; catalogued so investigators can identify and steer clear of it rather than as a recommended tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hola-vpn |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
