---
id: changedetect
name: changedetection.io
description: Use when you have a web page (profile, listing, notice) and want to be alerted when its content changes — returns dated change diffs/snapshots for monitoring a subject's online footprint.
url: https://changedetection.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- change-detection
bestFor: Automated monitoring of a web page for content changes, with diffs, snapshots, and alerts.
selectorsIn:
- domain
- social-profile
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Open-source and free to self-host (Docker/pip); an optional paid hosted plan runs the checks for you.
opsec: active
opsecNote: Each check fetches the target page, so it repeatedly touches the subject's server from your monitoring host. Self-host to control the source IP/User-Agent (and route via proxy) — hosted mode fetches from the provider's infrastructure instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Popular open-source project (widely deployed, active repo); self-hosting means you can audit exactly what it does.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- change-detection
aliases:
- changedetection.io
- ChangeDetect
tags:
- change-monitoring
- surveillance
- automation
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# changedetection.io

> Open-source web-page change monitoring: watch a URL and get a diff/alert whenever its content changes — self-hosted so you control the request.

## When to use
You have a page that matters to an investigation — a subject's public profile, a marketplace/rental listing, a company "team" page, a court/notice board — and you want to know the moment it changes (a new post, a removed item, an updated phone number) instead of re-checking by hand. It's an active-monitoring/surveillance utility over a page you already know; it doesn't discover new subjects.

## How to use it (`bestInteractionPattern`: docker)
1. Self-host it: `docker run -d -p 5000:5000 -v datastore:/datastore dgtlmoon/changedetection.io` (or pip install), then open the local UI.
2. Add the target URL as a watch; optionally set a CSS/xpath selector to monitor just one region, and a check interval.
3. For JS-heavy sites, enable the bundled Playwright/browser fetcher so dynamic content renders.
4. Configure notifications (email, webhook, Discord/Telegram) to fire on change; review the visual/text **diff** and stored snapshots.
5. Pivot: a detected change (new `social-profile` link, added contact) becomes a fresh selector to chase.

## Inputs → Outputs
- **In:** a page URL (`domain`/`social-profile`) and optional element selector + interval.
- **Out:** dated change diffs and snapshots, plus alerts; the changed content itself (new links, numbers, listings).
- **Empty/negative result looks like:** no notifications because the page is static, or noisy false-positive alerts from rotating ads/timestamps — tighten the selector to the region you actually care about.

## Gotchas & OpSec
- **Active by nature:** repeated fetches hit the target's server on a schedule and can be fingerprinted — self-host, set a sane interval, and proxy if the source IP matters.
- Dynamic/anti-bot sites need the browser fetcher and may still block automated checks or serve you differently.
- Over-broad watches spam you with irrelevant changes; scope to a selector.

## Overlaps ("do both")
- Overlaps with [[change-detection]] and with archive tooling: changedetection.io alerts you to a change in near-real-time, while an archive service preserves the before/after states for evidence.

## Trust & verifiability
`trust: community` — mature, widely-used open-source project; self-hosting lets you audit its behavior and keep full custody of the captured snapshots.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | changedetect |
