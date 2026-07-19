---
id: fiddler
name: Fiddler
description: Use when you're investigating a website/app and want to see the HTTP(S) traffic it exchanges — returns captured requests/responses, headers, and hidden API calls you can inspect and save as evidence.
url: https://www.telerik.com/fiddler
category: evidence-capture
path:
- evidence-capture
- web-browsing
bestFor: Capturing and inspecting the underlying web traffic (APIs, redirects, tracking calls, embedded URLs) of a page you're examining, and preserving it as evidence.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Fiddler Classic is free (Windows desktop). The newer cross-platform "Fiddler Everywhere" is a paid product with a trial and requires an account; the free Classic build needs no subscription.
opsec: passive
opsecNote: Fiddler captures traffic from *your own* machine/browser as you load a site — it does not touch the target beyond the normal page requests your browser already makes, so it adds no extra footprint at the target. Still browse from a sock-puppet profile/IP, since loading the site is itself a visit the site can log.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A long-established web-debugging proxy from Telerik/Progress, widely used by developers and security researchers; a mainstream, reputable tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Fiddler Classic
- Telerik Fiddler
tags:
- web-debugging
- traffic-capture
- evidence
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Fiddler

> A web-debugging proxy — see the raw HTTP(S) requests a site or app makes, revealing hidden APIs, embedded URLs, and trackers, and capture it as evidence.

## When to use
You're examining a website or mobile app and the interesting data isn't in the visible page — it's in the background calls: a JSON API returning more fields than the UI shows, a redirect chain, an embedded media URL, an analytics/tracking beacon, or a request that leaks an ID. Fiddler sits as a local proxy and records every request your browser/app sends and receives, so you can inspect and preserve exactly what a site does under the hood.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install Fiddler Classic (free) from https://www.telerik.com/fiddler.
2. Launch it; it auto-configures as your system proxy and begins logging. Enable HTTPS decryption (Tools → Options → HTTPS) to see encrypted traffic — you'll install Fiddler's root cert on your own machine.
3. Browse the target site/app; watch the session list populate with requests.
4. Inspect a session's request/response — headers, cookies, JSON bodies, redirect targets, embedded URLs — and save sessions (.saz) as evidence.
5. Pivot: an exposed API field can hand you IDs/handles/`geolocation`; a hidden media URL feeds image/metadata analysis; a tracking ID feeds a `[[publicwww]]` code-fingerprint pivot.

## Inputs → Outputs
- **In:** your own browsing of a target site/app (you generate the traffic)
- **Out:** captured requests/responses — headers, cookies, JSON, hidden endpoints, redirect chains, saved as logs
- **Empty/negative result looks like:** a page that's fully static may make few background calls; if you see nothing interesting, the data really is in the HTML, or the app pins certificates and refuses Fiddler's HTTPS interception (common with mobile apps) — note the pinning rather than assuming no traffic.

## Gotchas & OpSec
- Human-in-the-loop: it's a `manual-review` tool — you read and interpret the captured sessions; installing it is a local desktop step.
- HTTPS decryption installs a root cert on *your* machine — fine for your own device, but understand what you're enabling and remove it when done.
- It captures *your* traffic to public sites; it is not a way to intercept someone else's connection. Loading the target still logs a normal visit at the site — use a sock-puppet browser/IP.
- Cert-pinned apps will block interception; that's an app defense, not a tool failure.

## Overlaps ("do both")
- Pairs with browser DevTools (Network tab) for quick in-page inspection and with `[[publicwww]]` for pivoting on IDs you find — Fiddler captures and preserves the full traffic; DevTools is faster for a quick look, and PublicWWW turns a discovered fingerprint into related sites.

## Trust & verifiability
`trust: trusted` — Fiddler is a mainstream, long-standing developer/security proxy from Telerik/Progress; it faithfully records real traffic, and the evidence is what your own browser actually sent and received.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fiddler |
| category | evidence-capture |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (manual-review) |
