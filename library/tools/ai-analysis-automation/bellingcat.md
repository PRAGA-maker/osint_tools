---
id: bellingcat
name: Bellingcat
description: Use when you need OSINT methodology, case studies, or vetted tool/technique guides — Bellingcat's investigations and how-to articles are a reference knowledge base, not a lookup tool.
url: https://www.bellingcat.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Learning proven OSINT techniques and following published investigations from a leading open-source research collective.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to read; a non-profit funded by grants/donations. No account.
opsec: passive
opsecNote: Reading articles is passive. Note that visiting from an attributable browser reveals your interest in specific topics/techniques; use a clean session if your research interest itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Bellingcat is a respected, methodologically rigorous open-source investigation collective; its guides and case studies are widely cited and reproducible.
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
- bellingcat-com
- bellingcat-openstreetmap-search
- these-are-the-tools-open-source-researchers-say-they-need
- xblog-bellingcat-a-beginner-s-guide-to-flight-tracking-bellingcat
aliases:
- Bellingcat
tags:
- osint-blogs
- methodology
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Bellingcat

> The Bellingcat site: not a search tool but a reference library of OSINT methodology, tool guides, and worked investigations from a leading open-source research collective.

## When to use
When you need *how* rather than *who* — a technique for geolocation, chronolocation, flight/ship tracking, image verification, or archival research, or a case study to model your own investigation on. Bellingcat's articles and its online investigation toolkit are a trusted starting point for choosing methods and tools. It teaches and documents; it returns no selectors itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.bellingcat.com/ and use the site search or the "Resources"/toolkit section.
2. Find a guide matching your task (e.g. verifying a video, tracking a flight) or a comparable published case.
3. Follow the method; jump to the specific tools it recommends (many are catalogued here as their own entries).
4. Pivot: apply the technique to your actual selectors using the linked tools.

## Inputs → Outputs
- **In:** a topic/technique/case you want to learn (not an OSINT selector)
- **Out:** methodology articles, tool guides, and investigation write-ups
- **Empty/negative result looks like:** no article on your exact need — the method may live under a different name, or in the community toolkit rather than the blog.

## Gotchas & OpSec
- It's a knowledge base, not a data source — you still execute the technique with other tools.
- Some published techniques rely on tools/sites that have since changed; verify a tool is still live before depending on it.
- Reading is passive, but your topic interest is visible to your network/ISP — use a clean session if that matters.

## Overlaps ("do both")
- Pairs with its own toolkit entries (`[[bellingcat-openstreetmap-search]]`, the tools list) — read the method here, then use the specific catalogued tools to do the work.

## Trust & verifiability
`trust: trusted` — a rigorous, widely-cited collective whose methods are documented to be reproducible; still, confirm any referenced third-party tool's current status yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bellingcat |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
