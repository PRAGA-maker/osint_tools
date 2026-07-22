---
id: linkfinder
name: LinkFinder
description: Use when you have a target's JavaScript files or a page (`domain`) and want to extract endpoints, paths and URLs referenced in the JS — returns discovered endpoints (`domain`).
url: https://github.com/GerbenJavado/LinkFinder
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Pulling hidden endpoints, paths and URLs out of a site's JavaScript with regex-based extraction.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (a Python tool); no account.
opsec: passive
opsecNote: Parsing JS you've downloaded is passive. If you point LinkFinder at a live URL, it fetches the site's JS from your IP — source files via an archive or a disposable IP if that contact should not be attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely-used open-source recon tool (GerbenJavado); output is reproducible against the same JS input.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- jsluice
aliases:
- LinkFinder
tags:
- Domain/IP/Links
- Source Code Analyzes
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# LinkFinder

> A Python recon tool that scrapes endpoints, paths and URLs out of JavaScript files using regex — the classic way to surface hidden API routes and links a site's front-end references.

## When to use
You're mapping a target `domain` and its JavaScript likely references endpoints, API paths and other URLs that aren't visible in the rendered page. LinkFinder parses one JS file, a page, or a whole set and lists the links it finds, widening your view of the site's structure and other hosts it talks to.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/GerbenJavado/LinkFinder && cd LinkFinder && pip install -r requirements.txt && python setup.py install`.
2. Run against a single file/URL with HTML output: `python linkfinder.py -i https://example.com/app.js -o cli`.
3. Or crawl a page's scripts: `python linkfinder.py -i https://example.com -d`.
4. Review the extracted endpoints/paths (`domain`/URLs).
5. Pivot: feed discovered endpoints into further recon; use a secrets-focused tool for API keys.

## Inputs → Outputs
- **In:** JavaScript file(s), a URL, or a domain (`domain`)
- **Out:** extracted endpoints, paths and URLs (`domain`) referenced in the JS
- **Empty/negative result looks like:** heavily minified/obfuscated or endpoint-free JS yields little — that's a clean/sparse codebase, not a failure; try more of the site's bundles.

## Gotchas & OpSec
- Regex-based: expect some noise (partial/relative paths, false matches) — verify endpoints before relying on them.
- Fetching live JS touches the target from your IP; parsing downloaded/archived files is fully passive.
- It finds *links*, not secrets — pair with a secrets scanner for API keys/tokens.

## Overlaps ("do both")
- Pairs with `[[jsluice]]` — LinkFinder is the classic endpoint extractor; jsluice adds structured URL and secret detection, so running both surfaces more than either alone.

## Trust & verifiability
`trust: community` — open source and widely used; its output is reproducible against the same JS, so any endpoint it reports can be confirmed by inspecting the source file.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkfinder |
