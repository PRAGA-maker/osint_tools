---
id: gtmetrix-website-performance
name: GTmetrix Website Performance
description: Use when you have a `domain`/URL and want to see how a site is built — returns its resource waterfall, third-party hosts/CDNs, tech, and a rendered screenshot.
url: https://gtmetrix.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Profiling a website's performance and technical makeup — resource waterfall, third-party requests, CDN/hosting hints, and a page screenshot.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free tests without an account (limited); a free account adds history, more test locations, and settings; paid plans for volume/API.
opsec: passive
opsecNote: GTmetrix loads the target site from its OWN servers, not yours — so the analysis traffic hits the site from GTmetrix's IP, not you. That means running a test does put a real request on the target's logs (from GTmetrix), which is low-attribution to you but not zero-touch. Fine for public sites; note it for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established, reputable web-performance service. Its technical readout (requests, hosts, timings) is accurate; it's a performance tool repurposed for light infrastructure recon, not a dedicated OSINT engine.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- gtmetrix.com
- GTmetrix
tags:
- toddington
- website-analysis
- performance
- tech-fingerprint
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# GTmetrix Website Performance

> A web-performance tester that doubles as light infrastructure recon — its waterfall exposes every host, CDN, and third-party a site calls, plus a screenshot of the page.

## When to use
You have a `domain`/URL and want to understand how the site is built and hosted without touching it yourself. GTmetrix renders the page from its own servers and reports the full request waterfall: every resource URL, third-party domain, CDN, analytics/ad host, load timings, and a screenshot. Useful for fingerprinting a target's tech/hosting, spotting linked infrastructure and trackers, and capturing how a page looked at test time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://gtmetrix.com and enter the `domain`/URL (a free account unlocks test-location choice and saved history).
2. Run the test and open the **Waterfall** tab: read every requested host — CDNs, third-party scripts, analytics/ad domains, API endpoints.
3. Check the **Structure/Summary** for tech hints and the captured **screenshot** of the rendered page.
4. Note shared third-party IDs/hosts as pivots toward related sites and the hosting/CDN provider.
5. Pivot: discovered hosts/domains feed WHOIS/DNS and source-code search (e.g. [[nerdydata-source-code-search-engine]]); the screenshot archives the page state.

## Inputs → Outputs
- **In:** `domain`/URL
- **Out:** resource waterfall (third-party `domain`s, CDNs, hosts), tech hints, load metrics, `ip-address`/hosting clues, page screenshot
- **Empty/negative result looks like:** the test errors or times out — the site is down, blocks automated agents, or requires auth; a failed test isn't proof the site is dead.

## Gotchas & OpSec
- The request comes from GTmetrix's IP, not yours — low-attribution, but it does put a real hit on the target's logs.
- It's a performance tool: infra signals are a by-product, so pair it with dedicated DNS/WHOIS/source-search tools for depth.
- Free tier is rate-limited; an account helps for repeated tests.

## Overlaps ("do both")
- Pairs with WHOIS/DNS and [[nerdydata-source-code-search-engine]] — GTmetrix reveals which hosts/third-parties a page calls, and those tools resolve who owns them and which other sites share them.

## Trust & verifiability
`trust: trusted` — a reputable performance service; its technical readout is accurate. Treat inferred hosting/tech as leads to confirm with authoritative DNS/WHOIS data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gtmetrix-website-performance |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
