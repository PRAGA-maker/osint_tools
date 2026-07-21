---
id: wayback-archive
name: Wayback-Archive
description: Use when you have a Wayback Machine snapshot `domain`/URL and want to download it as a fully working offline copy — returns a local, self-contained rebuild of the archived site (evidence preservation, no selector output).
url: https://github.com/GeiserX/Wayback-Archive
category: archives-cache
path:
- archives-cache
bestFor: Downloading an archived web page/site from the Wayback Machine and reconstructing it (HTML, CSS, JS, images, fonts) for offline, self-contained viewing.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (pip install). Only cost is your bandwidth/disk.
opsec: passive
opsecNote: Passive with respect to the target — you pull from archive.org's Wayback Machine, not the subject's live server, so the subject gets no signal. Your requests hit the Internet Archive from your IP; route through normal research egress.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source Python tool (GeiserX/Wayback-Archive), actively maintained (v1.4.x, 2026); it re-fetches from the Internet Archive, so provenance traces to Wayback's captures.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- buscapaginasblancas
- website-diff
aliases:
- Wayback Archive downloader
tags:
- web-history-and-website-capture
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Wayback-Archive

> A CLI that pulls a Wayback Machine snapshot down as a fully-working offline copy — the way to freeze and locally preserve a page as it existed at a chosen point in time.

## When to use
A page that matters to your case has been deleted or altered, but the Wayback Machine has an old capture. Use this to download that capture — with all assets and rewritten relative links — into a self-contained local folder you can archive, hash, and browse offline as evidence. It reconstructs a *past* state, unlike a live crawler that captures the current site.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install` the tool per the repo README (Python required).
2. Find the exact Wayback snapshot URL for the page/date you want (via web.archive.org).
3. Set the `WAYBACK_URL` environment variable to that snapshot and run the CLI.
4. It recursively downloads HTML, CSS, JS, images and fonts, rewriting URLs to relative paths, and outputs a working site directory.
5. Serve locally (e.g. `python -m http.server`) to browse; keep the folder (and a hash) as your preserved record.
6. Pivot: mine the offline copy for `associate`, `employer-org`, contact details, or image `metadata-exif`.

## Inputs → Outputs
- **In:** a Wayback Machine snapshot `domain`/URL
- **Out:** a self-contained offline rebuild of that archived page/site (preservation artifact)
- **Empty/negative result looks like:** the download is sparse or broken — meaning the Wayback capture itself was incomplete (JS-heavy or partially crawled pages archive poorly); try a different snapshot date.

## Gotchas & OpSec
- Only as good as the Wayback capture — if the Internet Archive never captured the asset, this can't recover it.
- Heavily JavaScript-rendered pages reconstruct imperfectly.
- Watch disk on large sites (a real limit in ephemeral environments).
- OpSec: passive toward the subject; you touch archive.org, not their server.

## Overlaps ("do both")
- Pairs with `[[grab-site]]` and hosted archivers — grab-site captures the *live* site now, while Wayback-Archive recovers a *past* state; use both to bracket a change over time. Compare states with `[[website-diff]]`.

## Trust & verifiability
`trust: community` — open-source and actively maintained; output derives directly from Internet Archive captures, which are independently viewable at web.archive.org for corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayback-archive |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
