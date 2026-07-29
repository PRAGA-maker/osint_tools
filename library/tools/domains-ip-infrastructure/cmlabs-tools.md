---
id: cmlabs-tools
name: CMLabs Tools
description: Use when you have a `domain` and want to fingerprint the site's technology stack (CMS, server, JS libraries, widgets) — returns the detected technologies and versions.
url: https://tools.cmlabs.co/en/technology-lookup
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Detecting what technologies a website is built on (CMS, server, frameworks, trackers).
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free for a few lookups; cmlabs free tools prompt a login/registration after ~5 uses.
opsec: passive
opsecNote: The lookup is run by cmlabs' servers against the target site, so your IP isn't what contacts the site. Passive from your side; note you may hit a login wall after several uses — use a research account if you sign in.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: unverified
trustNote: One of 30+ free SEO tools from cmlabs (an SEO agency); a convenience tech-fingerprint tool, comparable to Wappalyzer/BuiltWith and only as accurate as its signatures.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- cmlabs technology lookup
tags:
- Domain/IP/Links
- Website technology look up
- tech-fingerprint
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# CMLabs Tools

> cmlabs' Technology Lookup: paste a domain and see what CMS, server, libraries and widgets power the site — a free Wappalyzer-style fingerprint.

## When to use
You have a `domain` tied to your subject and want to know how the site is built — CMS (WordPress/Wix/etc.), web server, JavaScript libraries, analytics/tracker IDs, widgets. The stack, and especially reused analytics/ad IDs, can link a subject's site to other properties they run and hint at their technical sophistication.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tools.cmlabs.co/en/technology-lookup.
2. Enter the target `domain` and run the lookup.
3. Read the detected technologies (OS, server, CMS, JS libraries, widgets, versions).
4. Pivot: note any analytics/tracker IDs and reused components, then cross-search those IDs to find other sites by the same operator.

## Inputs → Outputs
- **In:** `domain`
- **Out:** detected technology stack (server, CMS, frameworks, libraries, widgets, versions)
- **Empty/negative result looks like:** few/no technologies detected — a heavily-custom, CDN-fronted, or JS-rendered site can hide its stack from signature detection.

## Gotchas & OpSec
- Signature-based, so it misses custom or obfuscated stacks and can misattribute versions.
- Free tier is capped (~5 uses before a login prompt) — use a research account if needed.
- Detection ≠ certainty; corroborate a key finding with a second fingerprint tool.

## Overlaps ("do both")
- Cross-check with Wappalyzer/BuiltWith — the real payoff is a **reused tracker/analytics ID**, which a dedicated "same-analytics" search turns into a list of the operator's other domains.

## Trust & verifiability
`trust: unverified` — a vendor convenience tool; results are heuristic signatures, so confirm anything load-bearing against an independent fingerprinter and the page source itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cmlabs-tools |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
