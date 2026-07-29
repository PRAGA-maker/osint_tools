---
id: update-scanner-add-on
name: Update Scanner
description: Use when you have a `domain`/webpage and want to be alerted when its content changes — returns highlighted diffs of a monitored page over time.
url: https://addons.mozilla.org/en-US/firefox/addon/update-scanner/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Watching a specific webpage (a profile, listing, or notice) for changes when it offers no RSS/Atom feed.
selectorsIn:
- domain
selectorsOut: []
status: degraded
pricing: free
costNote: Free, open-source Firefox add-on; no account. Last updated ~2019, so unmaintained but functional.
opsec: active
opsecNote: Update Scanner re-fetches the monitored page on a schedule FROM YOUR BROWSER, so the target's server sees repeated hits from your IP at regular intervals — a pattern that can stand out. Monitor from a sock-puppet browser/VPN, and set a sensible (not aggressive) scan frequency to stay low-noise.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A long-standing, well-rated Firefox add-on (thousands of users); simple and reliable, but no longer actively maintained.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- visualping
aliases:
- Update Scanner
tags:
- monitoring
- change-detection
- browser-extension
source: sinwindie-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Update Scanner

> A Firefox add-on that watches a webpage and highlights what changed since last visit — the simple way to monitor a page that has no RSS/Atom feed.

## When to use
You have a `domain`/specific page that matters to a case — a subject's profile bio, a classified/marketplace listing, a court or agency notice, a "last seen" page — and you want to know the moment it changes without checking manually. Update Scanner scans chosen pages on a schedule, highlights additions/edits, and lets you ignore trivial changes. Persistent monitoring, not discovery.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Update Scanner from Firefox Add-ons.
2. On a target page, add it to the scan list; set a per-page scan frequency (keep it modest).
3. When the page changes, the add-on flags it and highlights the diff.
4. Tune the sensitivity to ignore insignificant tweaks (ads, counters).
5. Capture/preserve the changed content when it matters (pair with a full-page capture for evidence).

## Inputs → Outputs
- **In:** `domain` / a specific page URL to monitor
- **Out:** change alerts with highlighted diffs of the page over time
- **Empty/negative result looks like:** "no change" scans — expected most of the time; a page behind a login or one rendered entirely by JavaScript may not diff reliably.

## Gotchas & OpSec
- **Repeated polling from your IP:** scheduled re-fetches create a regular-interval footprint on the target — use a sock-puppet/VPN and a non-aggressive frequency.
- **Unmaintained (~2019)** and Firefox-only; JS-heavy/login-walled pages diff poorly. For those, a hosted service may work better.
- OpSec: **active** — you are repeatedly requesting the target page.

## Overlaps ("do both")
- Compare with `[[visualping]]` — VisualPing is a hosted change-monitor that polls from *its* servers (no IP footprint for you) and handles more complex pages; Update Scanner is the free, local, no-account option for simple pages you don't mind polling yourself.

## Trust & verifiability
`trust: community` — a real, well-established add-on; the diffs it shows are directly verifiable against the live page, though it's no longer actively maintained.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | update-scanner-add-on |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | domain →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
