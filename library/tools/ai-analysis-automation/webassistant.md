---
id: webassistant
name: WebAssistant (MM3 Proxy Offline Browser)
description: Use when you have a domain/URL and want a local, timestamped offline copy of a site's pages captured as you browse — returns an archived copy of web content for later analysis, not new selectors.
url: http://www.proxy-offline-browser.com/download.html
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Capturing and preserving a browsed website locally (via a local proxy) so pages survive takedown/edits.
selectorsIn:
- domain
selectorsOut:
- metadata-exif
status: degraded
pricing: free
costNote: MM3-WebAssistant is free/open-source (GPL) Java software; no purchase or account required, though the project is long-standing and not actively marketed.
opsec: active
opsecNote: It works by proxying your live browsing to the target site to cache each page, so the target's server does see your requests in real time — this is active collection. Route it through a VPN/sock-puppet and avoid logging in to the target while capturing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: A veteran open-source Java project (MM3-WebAssistant); legitimate but niche and infrequently updated, so test on a current OS/JRE before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- MM3-WebAssistant
- Proxy Offline Browser
tags:
- offline-browsing
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# WebAssistant (MM3 Proxy Offline Browser)

> A local caching proxy that saves every page you browse to disk — evidence-preservation for web content you visit during an investigation.

## When to use
You are examining a `domain`/website that might change or vanish (a suspect's site, a marketplace listing, a social page) and want a **local, offline copy** you can revisit and reference later. WebAssistant sits as a proxy between your browser and the web, caching each page as you view it, so you build an archive simply by browsing. It captures content and page `metadata-exif`; it does not extract new identifiers.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install MM3-WebAssistant from http://www.proxy-offline-browser.com/download.html (requires a Java runtime).
2. Start the local proxy and point your browser's proxy settings at it (typically `localhost` + a port).
3. Browse the target site normally over a VPN/sock-puppet connection — every page you load is cached locally.
4. Later, switch to offline mode to re-open the archived pages without hitting the live site.
5. Pivot: the preserved pages become referenceable evidence; extract any selectors from them with your normal tooling.

## Inputs → Outputs
- **In:** `domain`/URL (whatever you browse)
- **Out:** a local offline archive of those pages (`metadata-exif` and content preserved)
- **Empty/negative result looks like:** pages that fail to cache (heavy JS/SPA sites, auth walls) — the proxy captures classic HTML far better than modern dynamic apps.

## Gotchas & OpSec
- **Active:** capture happens by fetching the live site through the proxy, so your requests reach the target in real time. Use a VPN/sock-puppet and don't authenticate.
- Old-school tech: it handles static/classic pages well but struggles with modern single-page apps and streamed media.
- Requires a Java runtime and some proxy configuration; test it works on your current OS first (status is degraded/niche).

## Overlaps ("do both")
- Complements web-archive services: this gives you a private, timestamped local copy you control, whereas public archives (Wayback) give an independent third-party record. Capturing both strengthens an evidence chain.

## Trust & verifiability
`trust: community` — it is a legitimate long-running open-source project, but niche and rarely updated; the archive it produces is only as trustworthy as your own capture process, so document when and how you captured each page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webassistant |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
