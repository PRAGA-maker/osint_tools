---
id: foxyrecon
name: FoxyRecon
description: Use when you have an indicator (email, `domain`, `ip-address`, hash, `phone`, ASN) and want to fan it out across 150+ OSINT resources from your Firefox context menu — returns pivots.
url: https://addons.mozilla.org/en-US/firefox/addon/foxyrecon/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: One-click routing of a selected indicator into dozens of OSINT lookup sites from the browser.
selectorsIn:
- email
- domain
- ip-address
- phone
selectorsOut:
- domain
- ip-address
- social-profile
status: live
pricing: free
costNote: Free and open-source (GPLv3) Firefox add-on; no account. Optional integrations (MISP, OpenCTI) need your own instances.
opsec: active
opsecNote: FoxyRecon opens queries against many third-party lookup services using the indicator you selected — each destination sees the query and your IP. That's active fan-out across many sites at once, so use a sock-puppet browser/VPN and be aware you're touching lots of services in quick succession.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: An open-source community add-on (marked experimental); it routes to reputable public tools but is small and self-maintained — audit its resource list and permissions.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FoxyRecon Firefox add-on
tags:
- toolkit
- browser-extension
- threat-intel
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# FoxyRecon

> A Firefox add-on that turns any selected indicator into a one-click launcher across 150+ OSINT/threat-intel lookup sites — highlight, right-click, and fan the same selector out everywhere.

## When to use
You have an indicator — an `email`, `domain`, `ip-address`, URL, file hash, `phone`, ASN, CVE — and want to run it through many OSINT and threat-intel services fast, without pasting it into each site by hand. FoxyRecon detects the indicator type from your selection/page and offers the relevant lookups via popup or context menu, can harvest indicators from a page and export them to CSV, and supports custom resources (MISP/OpenCTI). It accelerates pivoting; the underlying data comes from the services it launches.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install FoxyRecon from Mozilla Add-ons (Firefox).
2. Select an indicator on any page (or type one into the popup); FoxyRecon detects its type.
3. Right-click / use the popup to launch it against the relevant OSINT resources; results open in the destination sites.
4. Optionally harvest all indicators on a page and export to CSV, or wire in your MISP/OpenCTI.
5. Pivot: results from each service (`domain`/`ip-address`/`social-profile` links) feed the next round of enrichment.

## Inputs → Outputs
- **In:** an indicator — `email`, `domain`, `ip-address`, URL, hash, `phone`, ASN, CVE
- **Out:** the launched services' results — related `domain`s, `ip-address`es, `social-profile`s and threat-intel context
- **Empty/negative result looks like:** a destination service returns nothing, or the wrong indicator type is detected — adjust the selection/type and relaunch.

## Gotchas & OpSec
- OpSec: **active** and broad — it queries many third-party services at once, each seeing your IP and the indicator. Use a sock-puppet browser/VPN.
- It's a launcher, not a data source: quality/coverage come from the destination tools, some of which may be down or changed.
- Experimental community add-on — audit which resources and permissions it uses before trusting it on sensitive work.

## Overlaps ("do both")
- Complements automated enumeration frameworks — FoxyRecon is the fast manual/browser fan-out, CLI frameworks give scripted breadth. Do both: browser for quick interactive pivots, CLI for bulk.

## Trust & verifiability
`trust: community` — an open-source, self-maintained add-on; verifiable via its code/resource list, but the intel is only as good as the third-party services it routes to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | foxyrecon |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | email, domain, ip-address, phone → domain, ip-address, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
