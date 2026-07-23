---
id: umatrix
name: uMatrix
description: Use when you want to see and control every domain a page contacts at runtime — a matrix-based request blocker for observing a site's third-party connections and hardening your investigation browser.
url: https://chrome.google.com/webstore/detail/umatrix/ogfcmafjalglgifnmanfmnieipoejdcf/related
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Observing and blocking the third-party domains, trackers, and scripts a web page loads, per site.
selectorsIn:
- domain
selectorsOut:
- domain
status: degraded
pricing: free
costNote: Free and open source (GPLv3). No cost, no account.
opsec: passive
opsecNote: Runs locally in your browser; nothing is sent to the subject. It hardens your OWN session against trackers and lets you inspect what a target page tries to load — useful for spotting analytics/CDN domains tied to a site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Created by the uBlock Origin author (gorhill); well-regarded but development ceased in 2020, so it's stable-but-unmaintained and best on Firefox going forward.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- uMatrix
tags:
- Domain/IP/Links
- Source Code Analyzes
- request-control
source: cyb-detective
lastVerified: '2026-07-23'
---

# uMatrix

> A point-and-click matrix firewall for the browser: it shows every domain a page connects to at load time and lets you allow/block each by type (script, XHR, frame, cookie) — for both privacy hardening and infrastructure observation.

## When to use
Two OSINT uses. First, **observation**: open a target's site with uMatrix and read the matrix to see which third-party `domain`s it pulls in — analytics IDs, CDNs, ad networks, embedded widgets — which can link sites sharing the same infrastructure. Second, **OPSEC hardening**: lock down your investigation browser so pages can't silently phone home to trackers while you work.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install uMatrix (Firefox recommended; the Chrome listing still exists but is unmaintained).
2. Visit the target page and open the uMatrix panel — rows are the domains the page contacts, columns are request types.
3. Read the connections: note recurring third-party domains (trackers, CDNs, analytics) as infrastructure leads.
4. Block/allow cells to test what the page needs and to keep your session quiet.
5. Pivot: a shared analytics/CDN domain feeds "sites using the same tracker" pivots; blocking noise keeps your OPSEC footprint small.

## Inputs → Outputs
- **In:** the current page (`domain`)
- **Out:** the set of third-party `domain`s the page contacts, per request type
- **Empty/negative result looks like:** a page that contacts only its own domain — clean, but rare; most sites reveal several third parties.

## Gotchas & OpSec
- Unmaintained since 2020 (`status: degraded`): under Chrome's Manifest V3 it may stop working — prefer Firefox, or use uBlock Origin's advanced mode as the maintained successor.
- It's an observation/hardening aid, not a data source — it tells you what a page loads, not who owns it; combine with WHOIS/passive-DNS to attribute a domain.
- OpSec: **passive** — everything is local to your browser.

## Overlaps ("do both")
- Pairs with uBlock Origin (advanced mode) and passive-DNS/WHOIS tools — uMatrix surfaces the connected domains; WHOIS/DNS tools attribute them.

## Trust & verifiability
`trust: community` — from a highly respected author but no longer maintained; the connections it shows are directly observable and trustworthy, but keep a maintained alternative ready.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | umatrix |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
