---
id: stealthy-proxy-server-extension-chrome
name: Stealthy Proxy Server Extension (Chrome)
description: Use when you need one-click proxy browsing to reach geo-blocked sites — a free Chrome proxy extension; convenient, but a weak-anonymity, trust-the-provider option.
url: https://chrome.google.com/webstore/detail/stealthy/ieaebnkibonmpbhdaanjkmedikadnoje
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Quickly viewing geo-restricted/censored web content from another apparent location during OSINT browsing.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension (100k+ users). A free proxy — no paid tier required, which itself is a caution (see OpSec).
opsec: active
opsecNote: A free browser proxy routes your traffic through a third party who can see and log it — it changes your apparent location but is NOT trustworthy anonymity. Never send credentials or sensitive investigation traffic through it, don't log into real accounts while it's on, and prefer a reputable VPN or Tor for genuine OpSec. Use it only for low-stakes "view what a geo-blocked page shows" checks, ideally in a throwaway profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A third-party free proxy extension; free proxies have inherent trust problems (traffic visibility, unknown logging). Functional for geo-unblocking, but not a vetted privacy tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Stealthy extension
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- proxy
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Stealthy Proxy Server Extension (Chrome)

> A one-click Chrome proxy for reaching geo-blocked/censored sites. Handy for a quick "what does this page show from elsewhere" check — but a free proxy, so treat its anonymity as near-zero.

## When to use
You want to see content that's blocked in your country or region — a site, video, or page that geo-gates by IP — and need a fast way to appear elsewhere for a low-stakes look. Stealthy toggles a proxy on/off in the browser. Reach for it only for casual geo-unblocking; for any target-facing or sensitive work, use a proper VPN or Tor instead (see OpSec).

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Stealthy into a **throwaway** Chrome profile — never your personal/investigation-critical one.
2. Toggle it on to route browser traffic through its proxy.
3. Load the geo-blocked page to see the version served to the proxy's location.
4. Toggle it off when done; don't log into any real account while it's active.
5. For genuine anonymity or anything sensitive, switch to a trusted VPN/Tor — this is a convenience unblocker, not protection.

## Inputs → Outputs
- **In:** none (a browsing aid, not a selector lookup)
- **Out:** access to geo-restricted content from another apparent location — no subject `selectorsOut`
- **Empty/negative result looks like:** the site still blocks you (proxy IP also blacklisted) or fails to load — try a different exit or a real VPN.

## Gotchas & OpSec
- **Free proxy = trust the operator with your traffic.** It can see/log what you route through it; assume no confidentiality.
- Not real anonymity — don't send credentials, don't log in, keep it to low-stakes viewing.
- Browser extensions with proxy/traffic access are a risk surface — isolate to a disposable profile.

## Overlaps ("do both")
- Overlaps with VPN/Tor-based OpSec tools (which are the right choice for sensitive work) and with `[[guardian-project]]`'s Orbot; use those instead of a free proxy whenever anonymity actually matters.

## Trust & verifiability
`trust: unverified` — a functional but unvetted free proxy; adequate for casual geo-unblocking, unsuitable as a privacy/anonymity control given the inherent trust problems of free proxies.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stealthy-proxy-server-extension-chrome |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
