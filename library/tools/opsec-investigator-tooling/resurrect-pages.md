---
id: resurrect-pages
name: Resurrect Pages
description: Use when you hit a dead link or removed page (`domain`/URL) and want an archived copy — returns one-click lookups across Wayback, archive.is, Google Cache, and more.
url: https://addons.mozilla.org/en-US/firefox/addon/resurrect-pages
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: One-click access to cached/archived copies of a dead page across several archive services at once.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open-source (MIT); a lightweight Firefox add-on.
opsec: passive
opsecNote: "Resurrect Pages just builds and opens lookup URLs at archive services (Wayback, archive.is, etc.), so you query the archive — not the dead page's original server. That makes it passive toward the target. The archive services see the request; use a sock-puppet browser session for sensitive research, and note archive.is may show a CAPTCHA."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source Firefox add-on (Anthony Lieuallen), 4.6★ and maintained (updated 2026); it only constructs archive-lookup URLs, so there's minimal trust surface.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Resurrect Pages
- Firefox Resurrect Pages
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- archives
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Resurrect Pages

> A Firefox add-on that, on any dead or removed page, offers one-click lookups across multiple archive/cache services (Wayback Machine, archive.is, Google Cache, WebCite) to recover the content.

## When to use
You've hit a 404, a deleted post, or a page a subject took down (`domain`/URL) and want to see what it said — fast, without hand-typing each archive service's query. It fans the current URL out to several caches at once, maximizing the chance one has a snapshot. Recovery/archival tooling, so low direct missing-persons relevance, though recovering a deleted profile/post can be pivotal.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Resurrect Pages" from https://addons.mozilla.org/en-US/firefox/addon/resurrect-pages (Firefox).
2. On a dead page (or by right-clicking a broken link), invoke it via the context menu, toolbar, or Ctrl-Shift-U.
3. Pick an archive service (or open several): Wayback Machine, archive.is, Google Cache, WebCite.
4. Read the recovered snapshot; note its capture date to establish *when* the content existed.
5. Preserve the snapshot (`document-id` = the archived URL/timestamp) as dated evidence, and pivot on what it reveals.

## Inputs → Outputs
- **In:** a dead/removed `domain`/URL
- **Out:** archived copies of the page (`document-id` = archive URL + capture date)
- **Empty/negative result looks like:** every service returns "not archived" — no cache captured it before removal; try the parent URL, a Google `cache:`/site search, or accept it wasn't archived.

## Gotchas & OpSec
- It only *finds* existing archives — if no service ever crawled the page, there's nothing to resurrect.
- Different services have different capture dates; check timestamps to reconstruct a timeline, and prefer the closest-to-relevant snapshot.
- archive.is sometimes rate-limits/CAPTCHAs; solve manually.

## Overlaps ("do both")
- Complements direct archive tools and change-monitors like [[visualping]]/[[followthatpage]] — those preserve pages going forward, Resurrect Pages recovers ones already gone; use both for full before/after coverage.

## Trust & verifiability
`trust: community` — a small, auditable, maintained open-source add-on that only routes you to reputable archives; the recovered content's authority comes from the archive service (cite the snapshot URL + date), not the add-on.
