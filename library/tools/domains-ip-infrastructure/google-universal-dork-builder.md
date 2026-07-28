---
id: google-universal-dork-builder
name: Google (universal) Dork Builder
description: Use when you have a `domain`/target and want to quickly assemble advanced search-operator "dork" queries for Google/Bing/Yandex — returns crafted queries that surface exposed pages (`domain`).
url: https://addons.mozilla.org/en-US/firefox/addon/google-dork-builder/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Building and saving advanced-operator search dorks (site:, filetype:, intitle:) across engines, with Google Hacking Database import.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free Firefox add-on (small user base, last updated ~2021); no account.
opsec: passive
opsecNote: The extension only assembles query strings locally. Running the resulting searches is ordinary passive web search — logged by the engine and tied to your IP, so use a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A small community Firefox add-on that just constructs query strings, so the risk is minimal; the value is convenience, not data — verify every hit at the source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Google Dork Builder
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- google-dorking
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Google (universal) Dork Builder

> A Firefox helper that assembles advanced-operator "dork" queries for you, imports known dorks from the Google Hacking Database, and saves your own — so you spend time reading results, not remembering operator syntax.

## When to use
You're searching around a `domain` (or a person/org tied to one) and want to squeeze more out of general search engines using operators — `site:`, `filetype:`, `intitle:`, `inurl:` — to surface exposed documents, directories, login pages, or mentions that a plain query buries. The builder speeds up composing and reusing these queries and pulls proven patterns from the Google Hacking Database.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Google Dork Builder" from https://addons.mozilla.org/en-US/firefox/addon/google-dork-builder/ in Firefox.
2. Compose a query by picking operators and filling in values (target domain, file types, title/URL terms); or import a dork template from the Google Hacking Database.
3. Run it against Google/Bing/Yandex; save useful dorks to your library and sync across devices.
4. Iterate — narrow with more operators, swap engines to compare indexes.
5. Pivot: exposed files (`filetype:pdf/xls/doc`) can carry `metadata-exif`/author fields; discovered subdomains/paths feed infrastructure mapping.

## Inputs → Outputs
- **In:** a `domain`/target plus the operators you choose
- **Out:** crafted search queries → engine results (exposed pages, files, subpaths on that `domain`)
- **Empty/negative result looks like:** a well-formed dork returning nothing — either the target genuinely exposes little, or the operator combination is too narrow; loosen it or try another engine.

## Gotchas & OpSec
- It builds queries; it does **not** find anything by itself — results (and their reliability) come from the search engine you run them on.
- Aggressive automated dorking can trip engine rate limits/CAPTCHAs; this add-on runs your queries interactively, which keeps that low.
- OpSec: passive; standard search traffic — use a clean/VPN session for sensitive targets.

## Overlaps ("do both")
- Complements dedicated GitHub/code dorking (e.g. [[gitdorker]]) — this covers general web engines, that covers source repositories.

## Trust & verifiability
`trust: community` — a minor but harmless utility; because it only formats queries, trust rests entirely on verifying each search result at its source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-universal-dork-builder |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
