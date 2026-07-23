---
id: view-rendered-source
name: View Rendered Source
description: Use when you have a `domain`/page and want to see its HTML after JavaScript has run — compares raw vs rendered DOM, exposing dynamically-injected links, trackers and content the plain source hides.
url: https://chrome.google.com/webstore/detail/view-rendered-source/ejgngohbdedoabanmclafpkoogegdpob
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Seeing the post-JavaScript rendered DOM of a page and diffing it against the raw source to find injected links/trackers.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free Chrome extension; no account.
opsec: active
opsecNote: To render the page it loads the target in your browser, so the site sees a normal visit from your IP — no different from browsing it directly. Use a VPN/sock-puppet browser for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Popular third-party developer extension; useful and widely used, but community-maintained rather than from a verified security vendor.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- View Rendered Source extension
tags:
- Domain/IP/Links
- Source Code Analyzes
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# View Rendered Source

> A browser extension that shows a page's HTML *after* JavaScript executes — and side-by-side with the raw source — revealing links, trackers and content injected at runtime that plain "View Source" never shows.

## When to use
You're examining a `domain`/page whose interesting content is built by JavaScript — a single-page app, a site that lazy-loads links, or one that injects tracking/affiliate code after load. Browser "View Source" shows only the raw server response; this extension shows the live DOM, and its three-way view (rendered vs raw vs diff) pinpoints exactly what the scripts added — often the outbound `domain`s, tracker IDs or hidden endpoints you're after.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "View Rendered Source" from the Chrome Web Store.
2. Navigate to the target page and let it fully load (scroll if content is lazy-loaded).
3. Click the extension — it shows Rendered, Raw (Serialized), and a Diff column.
4. Read the diff to see JS-injected markup: added links, iframes, tracker/analytics IDs, embedded endpoints.
5. Pivot: injected outbound `domain`s feed a link graph; a tracker/AdSense ID feeds a reverse-publisher lookup like `[[reverse-google-adsense]]`.

## Inputs → Outputs
- **In:** a loaded page on a `domain`
- **Out:** the rendered DOM and a raw-vs-rendered diff → JS-injected `domain`s, trackers, endpoints
- **Empty/negative result looks like:** rendered and raw are nearly identical — a static page with little/no JS, so there's nothing dynamically added to find.

## Gotchas & OpSec
- It renders in *your* browser, so you must actually visit the target — this is a real, attributable visit; use a sock-puppet browser/VPN for sensitive sites.
- Content behind interactions (clicks, logins) only appears if you trigger it before capturing.
- OpSec: active — indistinguishable from normally browsing the page.

## Overlaps ("do both")
- Pairs with `[[reverse-google-adsense]]` and network-tab inspection — this exposes the injected IDs/links, and reverse-tracker tools turn those IDs into the owner's wider network of sites.

## Trust & verifiability
`trust: unverified` — a handy, widely-used developer extension, but community-maintained; what it shows is your browser's real DOM, so the output itself is trustworthy even if the publisher isn't formally vetted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | view-rendered-source |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
