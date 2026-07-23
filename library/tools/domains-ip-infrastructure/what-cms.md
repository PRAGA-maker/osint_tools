---
id: what-cms
name: What CMS
description: Use when you have a `domain`/URL and want to identify its CMS and web tech stack — returns the detected platform, frameworks and hosting.
url: https://whatcms.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fingerprinting the CMS, framework and technologies a website runs on.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free single-site detections on the web (light rate limit); batch detection and an API are paid.
opsec: passive
opsecNote: WhatCMS fetches/fingerprints the site from its own servers, not yours, so the target sees WhatCMS's requests rather than your IP. Only WhatCMS sees the domain you queried. (If you'd rather leave no third-party trace at all, fingerprint locally with Wappalyzer instead.)
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Popular tech-detection service. Fingerprinting is heuristic — it can miss or misidentify heavily customised/proxied sites; treat the stack as probable, not certain.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WhatCMS
- whatcms.org
tags:
- bellingcat-toolkit
- websites
- tech-fingerprinting
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# What CMS

> A web-technology fingerprinter — enter a site and it reports the CMS (WordPress, Drupal, Shopify…), frameworks, languages, and hosting powering it, from a database of 1,200+ technologies.

## When to use
You have a target `domain` and want to know what it's built on — the CMS/platform, JS frameworks, server software, and hosting. Useful for infrastructure profiling, spotting a shared build across a subject's multiple sites (same theme/stack = possible same author), or narrowing how a site might be probed or corroborated.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://whatcms.org/ and enter the `domain`/URL.
2. Read the detected stack: CMS + version hints, frameworks, programming language, web server, CDN, and hosting provider, shown as tags.
3. Note distinctive combos (a specific CMS + theme + analytics ID) — these become fingerprints to match against other sites.
4. Mind the free-tier rate limit; space out queries or use the paid API/batch for volume.
5. Pivot: a shared stack/theme across sites supports a common-owner hypothesis (confirm via `[[whoisology]]`); hosting/CDN feeds infrastructure mapping.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** detected CMS, frameworks, language, server, CDN, hosting (a technology profile of the `domain`)
- **Empty/negative result looks like:** "unknown" / sparse results — common for custom-built, static, or CDN/proxy-fronted sites that hide their backend. Absence of a CMS ≠ error.

## Gotchas & OpSec
- Human-in-the-loop: free web lookups are **rate-limited**; heavy use needs the paid API.
- Detection is heuristic and can be fooled by proxies, CDNs, or customisation — a wrong/blank result doesn't mean the fingerprint failed maliciously.
- OpSec: **passive** for you — WhatCMS does the fetching; your IP isn't exposed to the target.

## Overlaps ("do both")
- Complements the Wappalyzer browser extension (local, no third party) and BuiltWith — cross-check, since each detects a slightly different technology set.

## Trust & verifiability
`trust: community` — a widely used fingerprinter. Reliable for mainstream CMSs; treat detections of customised or proxied sites as probable, and confirm version/stack details before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | what-cms |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
