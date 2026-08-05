---
id: change-detection
name: Change Detection
description: Use when you have a web page (domain/URL) you want watched and want alerts when its content changes — returns diffs and notifications on every update.
url: https://changedetection.io/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- change-detection
bestFor: Monitoring a specific web page for changes and getting notified with a diff.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Fully open-source and free to self-host (Docker); a hosted cloud plan (~$8.99/mo) exists for those who don't want to run it themselves.
opsec: active
opsecNote: Active — it makes recurring HTTP requests to the target page on your schedule, so the target's server sees repeated hits from your instance/IP. Widen the check interval, and route through a proxy/Tor (supported) if the watched site should not see a pattern tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Popular, actively maintained open-source project (Web Technologies s.r.o.); self-hosting means you control the data and can audit the code, so trust is high for the tooling itself.
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
- changedetect
- onwebchange
aliases:
- changedetection.io
tags:
- web-monitoring
- change-detection
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Change Detection

> Self-hostable web-page change monitoring: point it at a URL and it tells you — with a diff — whenever the content changes, so you don't have to keep reloading a page.

## When to use
You want to watch a page tied to your investigation — a subject's profile, a marketplace listing, a court/records page, a company site, a forum thread — and be alerted the moment it changes, without manually revisiting. Good for standing surveillance of a known `domain`/URL over days or weeks.

## How to use it (`bestInteractionPattern`: docker)
1. Self-host: `docker run -d -p 5000:5000 -v datastore:/datastore ghcr.io/dgtlmoon/changedetection.io` (or use the paid cloud instance to skip setup).
2. Open the web UI, "Add" the target URL (`domain`/page).
3. Optionally scope what to watch with a CSS/xPath selector (e.g. just a price or a status line), and set trigger/ignore text rules to cut noise.
4. Set the check interval and a notification channel (email, Discord, Slack, Telegram, webhook — 85+ supported). Enable the bundled Chrome fetcher for JS-heavy pages.
5. On each change you get a notification and a visual/text diff; review the diff to see exactly what moved.
6. Pivot: a detected change (new address, new listing, edited bio) is a fresh lead to chase in real time.

## Inputs → Outputs
- **In:** a `domain`/URL (plus optional selector and rules)
- **Out:** change notifications and content diffs for that page (`domain` activity signal)
- **Empty/negative result looks like:** no alerts — the page is static, or your selector/ignore rules filtered out the change. Verify the watch is actually fetching (check the last-checked timestamp) before concluding "nothing changed."

## Gotchas & OpSec
- It watches pages you specify; it does not discover pages. Feed it URLs from other recon.
- JS-rendered or login-gated pages need the Chrome fetcher / browser-steps configuration, or you'll diff an empty shell.
- Too-tight selectors miss real changes; too-loose ones spam you with cosmetic churn.
- OpSec: this is ACTIVE — repeated fetches hit the target's logs. Lengthen the interval and use the built-in proxy/Tor support for sensitive targets.

## Overlaps ("do both")
- Same job as hosted `[[onwebchange]]` and `[[changedetect]]`; choose self-hosted (this, for privacy/control) vs a hosted service (no setup). Running one is usually enough per target.

## Trust & verifiability
`trust: community` — a widely used, auditable open-source project; self-hosting keeps your watch list and captured data under your control, and the diffs are verifiable against the live page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | change-detection |
