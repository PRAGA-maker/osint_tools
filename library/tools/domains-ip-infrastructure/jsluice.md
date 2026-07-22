---
id: jsluice
name: JSLUICE
description: Use when you have a target's JavaScript files (`domain`) and want to extract URLs, paths and hard-coded secrets/API keys from them — returns endpoints and leaked `domain`s.
url: https://github.com/BishopFox/jsluice
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Mining a site's JavaScript for hidden endpoints, paths and accidentally committed API keys/secrets.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (MIT) from Bishop Fox; a Go library and CLI.
opsec: passive
opsecNote: Parsing JS you have already downloaded is passive analysis. Fetching the JS from the live site (to feed jsluice) touches the target's server from your IP — pull files via an archive or a disposable IP if that contact should not be attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Published by Bishop Fox (a reputable security firm) and authored by tomnomnom; open source with an active user base.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- gitgot
aliases:
- jsluice
tags:
- Domain/IP/Links
- Website's files metadata analyze and files downloads
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# JSLUICE

> A Go CLI/library that reads JavaScript and pulls out the "juicy" bits — URLs, API paths, and hard-coded secrets developers left in client-side code.

## When to use
You're mapping a target's web infrastructure and its front-end JavaScript is a goldmine: it often references internal API endpoints, hidden paths, and sometimes hard-coded keys or tokens that never appear in the visible site. Run jsluice over those JS files to enumerate endpoints and catch leaked secrets that widen your view of the target's `domain` footprint.

## How to use it (`bestInteractionPattern`: cli)
1. Install (Go): `go install github.com/BishopFox/jsluice/cmd/jsluice@latest`.
2. Collect the target's JS files (download them, or pull from an archive to stay off the live host).
3. Extract URLs/paths: `cat app.js | jsluice urls` — lists endpoints and their HTTP methods.
4. Extract secrets: `cat app.js | jsluice secrets` — flags likely API keys/tokens with a severity guess.
5. Pivot: discovered endpoints/subdomains (`domain`) feed further recon; treat any flagged secret carefully and lawfully — surfacing it is OSINT, using it is not.

## Inputs → Outputs
- **In:** JavaScript file(s) from a target `domain`
- **Out:** extracted URLs/paths (endpoints, other `domain`s) and candidate secrets/API keys
- **Empty/negative result looks like:** minified or well-scrubbed JS yields few endpoints and no secrets — that's a clean codebase, not a tool error; try more of the site's bundles.

## Gotchas & OpSec
- Secret detection is heuristic: expect false positives (public keys, sample tokens) — verify before treating anything as a live credential.
- OpSec: parsing is passive; the act of downloading JS from the live site is what touches the target — source files via archives or a disposable IP when needed.
- Never use a discovered secret to access systems you're not authorised to — extraction is research, exploitation is not.

## Overlaps ("do both")
- Pairs with `[[gitgot]]` and other secret scanners — jsluice works on client-side JS, while repo/secret scanners cover source control; together they cover both places credentials leak.

## Trust & verifiability
`trust: trusted` — open source from Bishop Fox; its output is reproducible against the same JS files, so findings can be independently confirmed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jsluice |
