---
id: ghostery
name: Ghostery
description: Use when you want to see and block the trackers and analytics a webpage loads — reveals third-party tracker/ad IDs on a site and blocks tracking on your own investigation browsing.
url: https://www.ghostery.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Enumerating the trackers/analytics a site loads (for fingerprinting/attribution) and blocking tracking during OSINT browsing.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open-source browser extension (Chrome/Firefox/Edge/Safari); an optional paid privacy suite exists but the tracker-blocker is free.
opsec: passive
opsecNote: Defensive/observational — it inspects and blocks trackers in YOUR browser. Enabling it on investigation browsing reduces the trackers that fingerprint you. When used to enumerate a site's trackers, you're just loading a public page; nothing extra is sent to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Well-known, open-source anti-tracking extension with a long track record; the tracker list is transparent and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Ghostery
- ghostery.com
tags:
- privacy
- trackers
- browser-extension
- anti-tracking
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Ghostery

> An open-source browser extension that detects, lists and blocks the trackers and analytics on any page — useful both as OpSec and as a way to fingerprint a site's tracking stack.

## When to use
Two uses. **OpSec:** run it in your investigation browser to block third-party trackers/ads so the sites you visit collect less about you. **Analysis:** open a target site and use Ghostery's panel to enumerate which trackers, analytics and ad networks it loads — the specific tracker/analytics IDs can fingerprint the site and, cross-referenced with reverse-analytics tools, help attribute it to the same operator as other sites.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Ghostery from your browser's store (Chrome/Firefox/Edge/Safari) or ghostery.com.
2. Browse to the target `domain`.
3. Open the Ghostery panel to see the list of detected trackers, analytics, and ad services on the page.
4. Note distinctive IDs/services (e.g. a specific Analytics or ad-network account) for correlation.
5. Pivot: feed a Google Analytics/AdSense ID into a reverse-analytics tool to find sibling sites.

## Inputs → Outputs
- **In:** a `domain`/page you visit
- **Out:** the list of trackers, analytics and ad services (and their IDs) loaded by that page
- **Empty/negative result looks like:** few or no trackers detected — a privacy-clean or static site; that's a finding, not a failure.

## Gotchas & OpSec
- It shows what loads in *your* session; some trackers are conditional (consent walls, geolocation) and may not fire.
- Blocking can break site functionality — toggle per-site when a page misbehaves.
- For rigorous tracker attribution, confirm IDs in the page source rather than relying solely on the panel.

## Overlaps ("do both")
- Pairs with reverse-analytics tools (e.g. `[[spyonweb]]`) — Ghostery surfaces the tracker IDs on a page; reverse-analytics turns an ID into the list of other sites sharing it.

## Trust & verifiability
`trust: trusted` — a mature, open-source anti-tracking tool with a transparent, auditable tracker database.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghostery |
