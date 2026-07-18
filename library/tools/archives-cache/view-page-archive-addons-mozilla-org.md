---
id: view-page-archive-addons-mozilla-org
name: Web Archives (View Page Archive)
description: Use when you have a URL that changed or vanished and want archived/cached copies across many services at once — returns document-id-style snapshots to recover deleted content.
url: https://addons.mozilla.org/en-US/firefox/addon/view-page-archive/
category: archives-cache
path:
- archives-cache
bestFor: One-click lookup of a page's archived/cached versions across Wayback, Archive.today, Google cache, and more, from the browser.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free, open-source browser extension (Firefox and Chrome); optional donations. No account.
opsec: passive
opsecNote: The extension opens archive services in your browser; each archive you open sees your IP/request, but the target site itself is not contacted (you view cached copies, not the live page). Use a clean browser for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: "Mozilla-'Recommended' open-source add-on (a.k.a. Web Archives) with a strong review history; source is public and auditable."
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Web Archives
- View Page Archive & Cache
- web-archives-extension
tags:
- archives-cache
- browser-extension
- web-archiving
- cached-pages
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Web Archives (View Page Archive)

> A Firefox/Chrome extension (now published as "Web Archives") that checks a URL against many archive and cache services at once — the fastest way to recover a page that was edited or deleted.

## When to use
A `domain`/URL that mattered to your case has changed, gone 404, or been scrubbed — a taken-down profile, an edited listing, a deleted article. Instead of pasting the URL into each archive by hand, this extension queries Wayback Machine, Archive.today, Google/Bing caches, and others from a right-click, surfacing every preserved snapshot (`document-id`) so you can read what the page used to say and when.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from https://addons.mozilla.org/en-US/firefox/addon/view-page-archive/ (a Chrome Web Store version exists too).
2. On the dead/changed page — or by pasting a custom URL into the extension — right-click and pick an archive source, or open all sources.
3. The extension opens each service's copy; compare snapshots across dates to see how the content evolved.
4. Pivot: capture the relevant snapshot (screenshot + snapshot URL/timestamp) for evidence, and feed recovered details (names, emails, images) back into your investigation. For a permanent private copy, also run the URL through `[[archivebox]]`.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** `document-id` (archived snapshots across services, with dates)
- **Empty/negative result looks like:** every source returns "no archived version" — the page may be too new, robots-blocked from archiving, or never crawled; try submitting it to an archive yourself.

## Gotchas & OpSec
- Human-in-the-loop: none beyond installing the extension and clicking a source.
- OpSec: passive toward the target — you read cached copies, not the live site. Each archive service does see your request/IP; use a clean browser for sensitive work.
- Coverage varies by service and date; always check more than one archive, since Wayback and Archive.today often hold different snapshots.

## Overlaps ("do both")
- Pairs with `[[archivebox]]` — this finds existing third-party snapshots fast, while ArchiveBox lets you make a fresh, private, self-controlled capture before content disappears.

## Trust & verifiability
`trust: trusted` — it is a Mozilla-Recommended, open-source add-on that merely links to reputable archive services; the snapshots it surfaces are third-party-attested and verifiable at each service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | view-page-archive-addons-mozilla-org |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
