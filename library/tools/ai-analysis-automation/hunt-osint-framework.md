---
id: hunt-osint-framework
name: Hunt Osint Framework
description: Use when you have any selector and want a categorised map of free online OSINT tools by investigation type (email, phone, IP/domain, geolocation, image forensics) to find the right tool fast — returns links to pivot into, not data itself.
url: https://nitinpandey.in/ihunt/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A free, category-organised directory (iHunt) of online OSINT tools across investigation stages.
selectorsIn:
- email
- phone
- ip-address
- domain
- image
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free directory (iHunt, by Nitin Pandey); every linked resource is free/open-source or has a free tier.
opsec: passive
opsecNote: Browsing the framework is passive. Your actual OpSec depends on whichever linked tool you launch — some are active/logged. Use a sock-puppet browser and read each destination before submitting a selector.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A maintained community OSINT-tool directory (iHunt) aimed at researchers and LE; curation is credible but the linked tools' quality is their own.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- analyst-research-tools
aliases:
- iHunt
- iHunt OSINT Framework
tags:
- Tools collections/toolkits
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Hunt Osint Framework

> iHunt — a free, category-organised directory of online OSINT tools spanning email, phone, IP/domain, geolocation, and image-forensics investigations.

## When to use
When you have a selector and want to quickly find the right free tool for it. iHunt groups dozens of online resources by investigation type — email investigation, phone analysis, IP & domain, geolocation, image forensics, crime/threat analysis — so you can jump from "I have a `phone`" or "I have an `image`" to a shortlist of relevant tools without searching around. It's a navigation aid, not a data source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nitinpandey.in/ihunt/ in a sock-puppet browser.
2. Pick the category matching your selector (Email, Phone, IP/Domain, Geolocation, Image, etc.).
3. Launch one of the listed tools and run your query there.
4. Check that tool's own OpSec/pricing before submitting anything.
5. Pivot: results feed the next selector back into another iHunt category.

## Inputs → Outputs
- **In:** `email`, `phone`, `ip-address`, `domain`, `image` (any selector — you're choosing a category)
- **Out:** routes to tools returning `social-profile`, `geolocation`, and forensic data
- **Empty/negative result looks like:** N/A for the directory itself; a dead end appears only in the linked tool. If a category's tools all miss, switch selector/category.

## Gotchas & OpSec
- **Directory, not a database** — it holds no data; all results come from the linked services.
- Some links may be stale or now paywalled; verify on use.
- OpSec is inherited from the destination tool, which may be active/logged.

## Overlaps ("do both")
- Same role as `[[analyst-research-tools]]` and OSINT Framework; consult more than one portal since each curator lists a different tool set.

## Trust & verifiability
`trust: community` — a credible maintained directory, but trust the *curation*, not the underlying tools; confirm each tool's output independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hunt-osint-framework |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | email, phone, ip-address, domain, image → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
