---
id: anonymox
name: anonymoX
description: Use when you need a quick browser-level IP/location change for light sock-puppet browsing — a proxy extension returning a foreign `ip-address`; not a substitute for a trusted VPN/Tor.
url: https://www.anonymox.net/en
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: One-click, in-browser proxy to mask your IP or appear in another country for casual research.
selectorsIn: []
selectorsOut:
- ip-address
status: live
pricing: freemium
costNote: Free tier offers a handful of proxy identities/countries with bandwidth caps; premium unlocks more locations and speed.
opsec: active
opsecNote: This is an anonymity aid for YOU, not a target action — but a free third-party proxy extension is a weak one. It can see and log your traffic, leaks via WebRTC/DNS are common, and browser-only proxying does not cover other apps. For anything sensitive use a trusted VPN or Tor, not this. Treat it as light obfuscation only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A commercial German browser-extension proxy; closed-source and free-proxy-based, so its handling of your traffic cannot be independently verified — do not trust it with sensitive activity.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- mullvad-vpn
- tor-browser
aliases:
- AnonymoX
- anonymox.net
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
- proxy
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# anonymoX

> A one-click browser proxy extension to change your apparent IP/country — convenient for low-stakes obfuscation, but a free third-party proxy you should not trust with anything sensitive.

## When to use
You want to quickly view a site from a different country, dodge a light geo-block, or add a thin layer of IP obfuscation to casual sock-puppet browsing — without configuring a full VPN. anonymoX swaps your browser's apparent `ip-address` in a couple of clicks. For any operation where attribution actually matters, use a trusted VPN or Tor instead; this is convenience-grade only.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the anonymoX extension from https://www.anonymox.net/en (Firefox/Chrome).
2. Enable it and pick an available identity/country from the free list.
3. Browse; the sites you visit see the proxy's IP and country, not yours.
4. Verify the change on an IP-geolocation checker, and test for WebRTC/DNS leaks before relying on it.
5. Pivot: for real anonymity, escalate to `[[mullvad-vpn]]` or `[[tor-browser]]`; use anonymoX only for throwaway, low-risk viewing.

## Inputs → Outputs
- **In:** — (you pick a country/identity)
- **Out:** a substitute browser `ip-address`/geolocation for your session
- **Empty/negative result looks like:** free identities exhausted/rate-limited, or an IP check still showing your real location (a leak) — stop and switch to a trusted tool.

## Gotchas & OpSec
- Free, closed-source, third-party proxy: it can log your traffic. Never send credentials or sensitive queries through it.
- Browser-only — other apps and system traffic are unaffected; WebRTC/DNS leaks routinely expose the real IP.
- Not a security tool. For genuine OpSec use a reputable VPN or Tor; treat anonymoX as light geo-shifting only.

## Overlaps ("do both")
- Contrast with `[[mullvad-vpn]]` and `[[tor-browser]]` — those are the trustworthy options for real anonymity; anonymoX trades trust for one-click convenience.

## Trust & verifiability
`trust: unverified` — a closed-source commercial proxy extension routing you through free proxies; there is no way to verify what it does with your traffic, so keep sensitive activity off it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | anonymox |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → ip-address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
