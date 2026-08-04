---
id: web-archives
name: Web Archives
description: Use when you have a `domain`/URL and want to pull up its archived or cached versions across many providers at once — returns links to Wayback, cache and archive snapshots.
url: https://github.com/dessant/web-archives
category: archives-cache
path:
- archives-cache
bestFor: One-click lookup of a page's archived/cached copies across Wayback Machine, archive.today, cached views and more.
selectorsIn:
- domain
selectorsOut:
- domain
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (GPLv3); install from your browser's extension store, no account.
opsec: passive
opsecNote: The extension queries public archive/cache providers, not the live target site, so you can read a deleted or altered page without hitting the subject's own server. Note the archive providers (and Google/Bing caches) see your request; use a clean browser profile if that matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Open-source, actively maintained extension by Armin Sebastian, distributed through the official Chrome/Edge/Firefox/Safari/Opera stores; it only orchestrates queries to reputable public archives.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- web archives extension
- dessant web-archives
tags:
- bellingcat-toolkit
- archives
- wayback
- cache
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# Web Archives

> A browser extension that, from any page or link, checks a dozen archive and cache providers at once — the fastest way to find a saved copy of content that's been deleted or changed.

## When to use
A profile, listing, forum post, or news page relevant to your case has been deleted, edited, or taken down — or you simply want to see what a `domain` looked like at an earlier date. Web Archives lets you right-click a link (or the current page) and jump straight to its snapshots across the Wayback Machine, archive.today, cached views and other sources, so you can recover the original content and any details (contact info, images, `metadata-exif`) that were later scrubbed.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Web Archives" from your browser's store (Chrome/Edge/Firefox/Safari/Opera) — the extension repo is https://github.com/dessant/web-archives.
2. In the toolbar/options, enable and reorder the archive & cache sources you want to query.
3. Right-click a link or the current page → **Web Archives** → pick a provider (or "all") to open its snapshot(s).
4. Read the recovered page for the content that's now missing from the live site; note dates to establish when something changed.
5. Pivot: recovered handles/emails/images feed the relevant selector tools; a snapshot date anchors a timeline.

## Inputs → Outputs
- **In:** a `domain`/URL (current page or a link)
- **Out:** links to archived/cached copies; within them, recovered content and `metadata-exif`
- **Empty/negative result looks like:** "no archived versions" across providers — the page may never have been captured; try submitting it to an archive now, or search the content string in a general engine.

## Gotchas & OpSec
- It's an orchestrator: coverage depends on whether the underlying archives captured the page. A miss at one provider isn't a miss everywhere — check several.
- Passive to the target, but the archive/cache providers log your queries.
- Some caches (e.g. Google) have been deprecated; the extension's live source list reflects what's currently working.

## Overlaps ("do both")
- Complements direct Wayback Machine / archive.today use — the extension just makes the multi-provider check one click; for deep timelines, still open the Wayback calendar directly. Pairs with `[[darkweb-archive]]` for onion pages the clearnet archives don't cover.

## Trust & verifiability
`trust: trusted` — open-source, widely used, and it only relays to reputable public archives; the recovered content's reliability is that of the underlying archive, which is generally strong for evidentiary use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | web-archives |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
