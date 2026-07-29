---
id: changedetection-io-open-source
name: ChangeDetection.io (Open Source)
description: Use when you have a `domain`/URL and want to be alerted when its content changes — returns diffs of monitored pages over time.
url: https://github.com/dgtlmoon/changedetection.io
category: archives-cache
path:
- archives-cache
bestFor: Self-hosted monitoring of web pages for changes, with alerts and visual/text diffs over time.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (self-host via Docker/pip). The maintainers also offer a paid hosted version, but the OSS self-hosted tool is fully free.
opsec: passive
opsecNote: Self-hosted monitoring fetches the target page on a schedule from wherever you run it, so your server's IP repeatedly requests the subject's page — set a realistic interval and route through a proxy if the recurring pattern matters. Nothing is disclosed to the page owner beyond normal web requests. Optional browser/JS rendering fetches more like a real user.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Popular, actively maintained open-source project by dgtlmoon (tens of thousands of GitHub stars). Self-hosted, so you control the data; reliability is high.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- visualping
- urlwatch
aliases:
- changedetection.io
- dgtlmoon changedetection
tags:
- change-monitoring
- web-monitoring
- self-hosted
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# ChangeDetection.io (Open Source)

> Self-hosted "watch this web page" monitoring — point it at a URL and get diffs and alerts whenever the content changes.

## When to use
When you want to keep watching a subject's web presence over time: a profile page, a company site, a listing, a court/records page, or any URL where a *future change* is the intelligence. Instead of manually re-checking, ChangeDetection.io polls the page and shows exactly what changed, alerting you via email, webhook, or chat.

## How to use it (`bestInteractionPattern`: docker)
1. Self-host: `docker run -d -p 5000:5000 -v datastore-volume:/datastore dgtlmoon/changedetection.io` (or `pip install changedetection.io`).
2. Open the web UI, **Add** the target `domain`/URL, and set a check interval.
3. Optionally add a CSS/xPath selector to watch only a page region, and enable the Playwright/browser fetcher for JS-heavy pages.
4. Configure notifications (email/webhook/Discord/etc.); when the watched content changes, you get the diff.
5. Pivot: a detected change (new address, new listing, edited bio) is a fresh lead — capture it and feed the new selector into the relevant lookup tool.

## Inputs → Outputs
- **In:** `domain`/URL to monitor
- **Out:** timestamped diffs of the page and change alerts (a monitoring stream, not a one-shot lookup)
- **Empty/negative result looks like:** "no change" over many checks — the page is static or the change happens in a region/format your selector or fetcher misses (e.g. JS-rendered); switch on the browser fetcher or widen the watched area.

## Gotchas & OpSec
- JS-heavy pages need the browser (Playwright) fetcher; the default HTTP fetch misses client-rendered changes.
- Recurring fetches from one IP form a pattern — pace intervals and proxy if monitoring a sensitive target.
- Self-hosting means you run and secure the instance; keep it updated and access-controlled.

## Overlaps ("do both")
- Compare with `[[visualping]]` (hosted, no-setup change monitoring) and `[[urlwatch]]` (CLI, config-file driven). Choose ChangeDetection.io for a self-hosted UI with diffs and selectors; Visualping for zero-setup; urlwatch for pure command-line pipelines.

## Trust & verifiability
`trust: community` — a widely used, actively maintained open-source project you self-host, so you control and can audit the data. Diffs are directly verifiable against the live page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | changedetection-io-open-source |
