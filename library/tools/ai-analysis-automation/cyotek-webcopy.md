---
id: cyotek-webcopy
name: Cyotek WebCopy
description: Use when you want a full offline mirror of a `domain`/website for analysis or preservation — returns a local copy of the site's pages and assets with links remapped.
url: http://www.cyotek.com/cyotek-webcopy
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Downloading a whole website locally (offline mirror) for analysis and evidence preservation.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free Windows application (requires .NET Framework 4.6); no account.
opsec: active
opsecNote: WebCopy CRAWLS the target site to mirror it, sending many requests that appear in the site's logs (from your IP). Only mirror sites you're authorised to, throttle the crawl, and route through a VPN; a fast full-site copy is noisy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Established free tool from Cyotek; it faithfully mirrors what the HTTP server returns (no JS rendering), so dynamic sites copy incompletely.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- WebCopy
- Cyotek WebCopy
tags:
- ai-analysis-automation
- website-mirror
- preservation
- offline
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Cyotek WebCopy

> A free Windows site-copier — mirror an entire website to disk (with links rewritten for offline use) to analyse or preserve it before it changes.

## When to use
You have a `domain`/website you want to study or preserve offline: to review its full structure at your own pace, keep a snapshot before it's altered/taken down, or work with its content without repeatedly hitting the live site. WebCopy downloads pages and assets and remaps links so the copy browses locally.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Cyotek WebCopy (Windows, .NET 4.6) from https://www.cyotek.com/cyotek-webcopy.
2. Create a project: set the site URL (`domain`) and the local save folder; configure rules (what to include/exclude, depth, throttling).
3. Run the copy; review the results map (downloaded, skipped, errors).
4. Browse the local mirror offline. Pivot: the offline copy feeds content review, link extraction, and archiving; combine with a hash for provenance.

## Inputs → Outputs
- **In:** a website `domain`/URL (+ crawl rules)
- **Out:** a local, link-remapped copy of the site (no selector output)
- **Empty/negative result looks like:** a thin/broken copy — the site is JavaScript-rendered (WebCopy doesn't run JS), auth-walled, or blocked the crawler; dynamic sites mirror poorly.

## Gotchas & OpSec
- Active crawling — leaves a footprint in the target's logs; throttle and get authorisation.
- No JavaScript execution — SPA/dynamic sites won't copy fully; use a headless-browser archiver for those.
- Windows-only; large sites need disk space and time.

## Overlaps ("do both")
- Complements `[[auto-archiver]]`/wget and `[[wayback-machine]]` — WebCopy makes a browsable offline mirror; Auto Archiver/Wayback give hash-verified, dynamic-capable preservation. Use both for a defensible record.

## Trust & verifiability
`trust: trusted` — a reputable, long-standing free tool; the mirror reflects exactly what the server returned (minus JS), so note dynamic gaps when relying on the copy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyotek-webcopy |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
