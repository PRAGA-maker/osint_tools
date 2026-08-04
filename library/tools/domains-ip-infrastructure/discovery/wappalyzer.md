---
id: wappalyzer
name: Wappalyzer
description: Use when you have a `domain`/website and want to fingerprint its technology stack — CMS, frameworks, analytics IDs, hosting — returning tech signals and sometimes pivotable `metadata-exif`-style identifiers.
url: https://www.wappalyzer.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Identifying the technologies, analytics/tracking IDs and platforms behind a website to fingerprint and link sites.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free browser extension and single-site lookups; bulk lookups, lead/contact data and the API are paid. Core fingerprinting is free.
opsec: active
opsecNote: The browser extension and the "look up a website" feature load the target site to fingerprint it, so your request reaches the target's server (and any analytics on it). Use a sock-puppet browser/VPN when fingerprinting a subject's own infrastructure; the paid technology-lookup runs server-side and is less exposing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Widely-used, well-established tech-profiling product with an open-source fingerprint ruleset heritage; detections are directly checkable against page source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- wappalyzer.com
tags:
- domains-ip-infrastructure
- tech-fingerprinting
- discovery
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Wappalyzer

> The standard "what is this site built with?" fingerprinter — CMS, frameworks, analytics, ad networks, hosting — and a source of tracking IDs that can link sites to a common owner.

## When to use
You have a `domain` and want to know its technology stack: CMS/e-commerce platform, JS frameworks, CDNs, analytics and advertising tags, payment processors, and more. Beyond satisfying "what runs this," the real OSINT value is the identifiers it surfaces — a shared Google Analytics/AdSense ID, Facebook Pixel, or unique platform footprint can tie a subject's separate sites together. Use it in infrastructure attribution and when clustering a network of related sites.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Wappalyzer browser extension (Chrome/Firefox) in a sock-puppet profile, or use "Look up a website" on wappalyzer.com.
2. Navigate to (or enter) the target `domain`.
3. Read the detected technology categories: CMS, frameworks, analytics, ads, hosting, payment, etc.
4. Note any tracking/analytics IDs (UA-/G- Analytics, AdSense pub-, FB Pixel) — these are the cross-linking gold.
5. Pivot: run a shared analytics/AdSense ID through reverse-analytics tools (e.g. reverse-lookup services) to find other domains using the same ID and cluster the owner's estate.

## Inputs → Outputs
- **In:** `domain` / website URL
- **Out:** technology stack + platform/tracking identifiers (which enable finding related `domain`s)
- **Empty/negative result looks like:** few or generic detections (a bare static site, or a WAF/proxy masking the origin). Sparse detections don't mean "no tech" — they can mean the fingerprints are hidden behind a CDN.

## Gotchas & OpSec
- Human-in-the-loop: none, though interpreting which IDs are pivotable is manual.
- OpSec: **active** for the extension/single-site lookup — it loads the target and can appear in the site's own analytics. Fingerprint sensitive targets via a sock-puppet browser/VPN, or the server-side lookup.
- Detections are heuristic and can miss or misattribute; confirm a critical fingerprint against the raw page source/headers.

## Overlaps ("do both")
- Pairs with reverse-analytics / shared-ID tools and with WHOIS/DNS lookups — Wappalyzer surfaces the tracking IDs and stack, and those tools turn a shared ID or registrant into the wider set of linked domains.

## Trust & verifiability
`trust: trusted` — a mature, widely-used product whose detections you can verify yourself by inspecting page source, scripts and headers. The identifiers it reports are objective facts on the page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wappalyzer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
