---
id: httrack
name: HTTrack
description: Use when you have a `domain`/website URL and want a complete offline copy for preservation and analysis — returns a local mirror of the site's pages and assets.
url: https://www.httrack.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Mirroring an entire website locally (offline browsing) to preserve and analyze it before it changes or disappears.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (GPL); Windows (WinHTTrack) and Linux/CLI builds.
opsec: active
opsecNote: HTTrack crawls the target site directly from your machine — the site's server sees your IP and a recognizable HTTrack user-agent, and an aggressive mirror generates heavy, obvious traffic. Route through a VPN/sock-puppet connection, throttle the crawl, and set a custom user-agent if you don't want the visit attributed to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-established open-source website copier; widely used and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- WinHTTrack
- httrack.com
tags:
- offline-browsing
- website-mirror
- preservation
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# HTTrack

> A free website copier: point it at a site and it downloads the pages, images, and assets into a browsable local mirror — for preserving evidence before it's edited or taken down.

## When to use
You have a `domain` or specific site (a subject's blog, a business site, a page you expect to change or vanish) and want a durable offline copy to preserve and analyze at leisure — walking the structure, grepping the HTML, keeping a timestamped snapshot for your record. It captures the site; it doesn't extract selectors on its own.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install HTTrack from https://www.httrack.com (WinHTTrack GUI on Windows, or `httrack` CLI on Linux).
2. Start a new project, enter the target site URL(s), and set scope limits (depth, domains, file types) so you don't crawl the whole internet.
3. Set crawl limits/throttling and a user-agent; run the mirror.
4. Browse the local copy offline; search the saved HTML for emails, names, links, and hidden content.
5. Pivot: mined emails/handles/links feed selector-specific tools; keep the mirror as a preserved artifact.

## Inputs → Outputs
- **In:** `domain` / site URL(s)
- **Out:** a local, browsable mirror of the site (the source you then analyze — not a selector itself)
- **Empty/negative result looks like:** an empty or tiny mirror — the site blocks crawlers, requires login, is JavaScript-rendered (HTTrack won't run JS), or robots/scope limits stopped it; adjust settings or use a headless-browser capture instead.

## Gotchas & OpSec
- OpSec: **active** — the crawl hits the site from your IP with an HTTrack user-agent and can be noisy; use a VPN/sock-puppet, throttle, and mask the user-agent.
- It does **not execute JavaScript**, so modern SPA/dynamic sites mirror poorly — use a browser-based archiver for those.
- Respect scope limits or you'll pull far more than intended; mind legal/ToS constraints on bulk copying.

## Overlaps ("do both")
- Do both with web-archive/snapshot tools: HTTrack gives you a full local, greppable copy under your control, while an archive service (Wayback/archive.today) provides an independent, citable timestamped record.

## Trust & verifiability
`trust: community` — a mature, open-source, auditable tool. It faithfully saves what the server returns; the completeness of the mirror depends on your scope settings and the site's anti-crawl measures.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | httrack |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
