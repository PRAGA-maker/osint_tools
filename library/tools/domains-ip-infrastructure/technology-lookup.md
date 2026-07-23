---
id: technology-lookup
name: Technology Lookup
description: Use when you have a `domain` and want to know its web tech stack — returns detected CMS, frameworks, analytics IDs, servers and libraries the site runs.
url: https://osint.sh/stack/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fingerprinting a website's technology stack (CMS, frameworks, analytics, server) from its domain.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free tool on the osint.sh toolkit; no account required for the web lookup.
opsec: passive
opsecNote: Passive from your side — osint.sh fetches and fingerprints the target site, so your IP typically does not directly hit the target (the service does). Only osint.sh sees your query; the target may see the service's requests, not yours.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: One of the free tools in the osint.sh suite; detection is heuristic (like Wappalyzer/BuiltWith) and can miss or misreport technologies, so corroborate.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- osint.sh stack
- osint.sh technology lookup
tags:
- domain-and-ip-research
- tech-stack
- fingerprinting
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Technology Lookup

> A free web-technology fingerprinter (part of the osint.sh toolkit): enter a domain and see the CMS, frameworks, analytics, server, and libraries it runs.

## When to use
You have a `domain` and want to know what it's built on — WordPress vs a custom stack, which analytics/tag IDs it embeds, what server and JS libraries it uses. Reach for this to profile a site's technology, and especially to grab shared identifiers (Google Analytics/AdSense IDs, common frameworks) that can link a target site to *other* sites run by the same operator. It's a fingerprinter, not a vulnerability scanner.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/stack/ and enter the target `domain`.
2. Read the detected technologies: CMS/platform, JS frameworks/libraries, analytics/marketing tags, web server, CDN, and more.
3. Note any shared analytics or ad IDs — these are gold for connecting sites under common ownership.
4. Corroborate with a second fingerprinter, since detection is heuristic and can be incomplete.
5. Pivot: feed analytics/ad IDs into "reverse analytics" tools to find sibling domains; feed the server/CDN into infrastructure analysis.

## Inputs → Outputs
- **In:** `domain`
- **Out:** detected tech stack — CMS, frameworks, analytics/ad IDs, server, CDN, libraries (which can link to other `domain`s)
- **Empty/negative result looks like:** few or no detections — a heavily custom, obfuscated, or Cloudflare-fronted site can hide its stack; absence isn't proof of a bare site.

## Gotchas & OpSec
- Heuristic detection (like Wappalyzer/BuiltWith): it can miss technologies or report stale ones — verify anything you rely on.
- The most valuable output is often shared IDs (analytics/ad), which enable ownership pivots — look for those specifically.
- OpSec: passive for you; the osint.sh service does the fetching.

## Overlaps ("do both")
- Pairs with BuiltWith/Wappalyzer-style tools (run more than one; they disagree) and with reverse-analytics-ID lookups — this tool *finds* the IDs, those *pivot* on them to sibling sites. Combine with WHOIS/passive-DNS for a full infrastructure picture.

## Trust & verifiability
`trust: community` — a free heuristic fingerprinter; treat detections as leads to confirm (especially shared IDs) rather than definitive facts, and cross-check with a second detector.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | technology-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
