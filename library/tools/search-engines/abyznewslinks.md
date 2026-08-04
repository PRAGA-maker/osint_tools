---
id: abyznewslinks
name: ABYZ News Links
description: Use when you have a `geolocation`/`address` and want local news outlets covering it — returns a directory of newspapers, broadcasters and press agencies by country and region.
url: http://www.abyznewslinks.com
category: search-engines
path:
- search-engines
bestFor: Finding the local newspapers and news media for a place, so you can search them for a person or event.
selectorsIn:
- geolocation
- address
selectorsOut: []
status: live
pricing: free
costNote: Free directory; no account or payment required.
opsec: passive
opsecNote: A static link directory — you browse a list of outlet URLs; nothing about your subject is submitted. The subsequent searches happen on the outlets' own sites.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running, manually curated directory of news outlets; links are hand-maintained so some rot over time, but the geographic organisation is reliable for finding local media.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ABYZNewsLinks
- abyznewslinks.com
tags:
- news
- news-directory
- local-media
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# ABYZ News Links

> A worldwide directory of newspapers, broadcasters and press agencies organised by country and region — the fast way to find the *local* outlets that would have covered a person or event.

## When to use
You have a `geolocation`/`address` — a town, region or country tied to your subject — and need the local media that might carry an obituary, court report, arrest notice, business item or community story about them. ABYZ indexes news outlets geographically down to the state/province level, so you can jump from "the subject is from X" to a list of X's newspapers and broadcasters, then search each for the person's name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.abyznewslinks.com and drill down by continent → country → region/state.
2. Read the listed outlets (newspapers, broadcast stations, magazines, press agencies), each with an outbound link.
3. Open the relevant local outlets and search their sites for your subject's name/event; combine with a site-scoped web search (`site:outlet.com "name"`).
4. Pivot: local coverage often yields associates, addresses, employers and dates that feed the rest of your investigation.

## Inputs → Outputs
- **In:** `geolocation`/`address` (place of interest)
- **Out:** a curated list of local news-outlet websites for that place (the tool itself returns no subject data)
- **Empty/negative result looks like:** a region with only a handful of outlets, or dead outlet links — expect some link rot in a hand-maintained directory.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a browse-and-click directory.
- OpSec: passive — no subject query touches this site; be mindful only when you go on to interact with individual outlets.
- Coverage varies: dense for the US/UK/Canada, thinner for some regions; some listed links may be defunct.

## Overlaps ("do both")
- Pairs with general and news-specific search engines because ABYZ tells you *which* local outlets exist while the search engine finds *what* they published about your subject.

## Trust & verifiability
`trust: community` — a manually curated directory; the value is the geographic index of outlets, and each outlet's reporting is verified on its own site, not here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
