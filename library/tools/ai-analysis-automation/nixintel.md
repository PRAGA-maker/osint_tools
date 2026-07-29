---
id: nixintel
name: NixIntel
description: Use when you need a technique or tool reference for an OSINT problem — returns tutorials, methodology write-ups, and a curated OSINT resource start page.
url: https://nixintel.info/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Learning the how-to method and finding the right tool for a specific OSINT task (SSL/infra attribution, social-media accounts, geolocation).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Blog and resource pages are free to read; the author also teaches paid SANS courses, but no paywall on the site content.
opsec: passive
opsecNote: You are reading a public blog — no target interaction. Apply the OpSec practices each individual article describes when you go on to run the tools it covers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by Steven Harris, a well-known OSINT practitioner and SANS instructor (SEC497/SEC587). Widely cited reference material; methodology-focused rather than a data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- osint-tools-yogsec
- bellingcat-online-investigation-toolkit
aliases:
- nixintel.info
- Steven Harris OSINT
tags:
- osint-blogs
- methodology
- reference
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# NixIntel

> A practitioner OSINT blog and resource hub — practical, reproducible technique write-ups plus a curated "OSINT Resources" start page.

## When to use
This is a reference, not a lookup: reach for it when you are stuck on *method* — how to attribute infrastructure from an SSL certificate, enumerate a target's social accounts (Telegram, Instagram, Snapchat, Kik), geolocate an image, or use tools like Spiderfoot, theHarvester, and Sherlock correctly. Also a good jumping-off directory when you need to discover the right tool for a selector you hold.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://nixintel.info/.
2. Search the site or browse categories for your problem (e.g. "SSL certificate", "Telegram", "geolocation").
3. Read the walk-through — articles are step-by-step with commands and screenshots you can follow against your own case.
4. Use the linked "OSINT Resources" start page to jump to the specific tools referenced.
5. Pivot: apply the method to your live case, then record the concrete tool you used (many map to other skills in this library).

## Inputs → Outputs
- **In:** none (a knowledge resource, not a selector-driven lookup)
- **Out:** methodology, tool recommendations, curated resource links
- **Empty/negative result looks like:** no article covers your exact niche — fall back to a broader OSINT directory or a different practitioner blog.

## Gotchas & OpSec
- It is educational content; techniques age. Check the post date and confirm a referenced tool is still live before relying on it.
- No data is returned here — value is in method and tool discovery, so pair it with the actual lookup tools it names.

## Overlaps ("do both")
- Pairs with `[[osint-tools-yogsec]]` and `[[bellingcat-online-investigation-toolkit]]` — those are tool directories; NixIntel adds the reproducible *how* behind the tools. Use NixIntel for method, the directories for breadth.

## Trust & verifiability
`trust: trusted` — authored by a recognised OSINT trainer with a strong track record; guidance is transparent and reproducible. Still verify any specific tool's current status yourself, since blog posts are snapshots in time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nixintel |
