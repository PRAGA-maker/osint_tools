---
id: username-search-tool
name: Username search tool (Aware Online)
url: https://www.aware-online.com/en/osint-tools/username-search-tool/
category: username
path:
- username
description: Use when you have a `username` and want a fast dashboard of search links across engines and people/username databases — returns pivot links to `social-profile`s and mentions.
bestFor: One page that fans a username out to Google/Bing/Yandex plus username databases (KnowEm, PeekYou, UserSearch) as ready-made search links.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
- email
status: live
pricing: free
costNote: Free browser tool; it only builds and opens search URLs on third-party services, so no account or payment on Aware Online itself.
opsec: passive
opsecNote: Aware Online generates links client-side and does not itself query the target; attribution risk comes from the destination services you click through to (Google, Yandex, KnowEm). Use a sock-puppet browser when following the generated links.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Aware Online, a reputable Dutch OSINT training provider; it is a link-builder, so the underlying results come from the third-party engines it points to.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Aware Online username search
- aware-online username tool
tags:
- username-enumeration
- osint-dashboard
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Username search tool (Aware Online)

> A free "custom search" dashboard: type one username and it hands you ready-made search links across the major engines and the main username/people databases.

## When to use
You have a `username` and want to sweep it across many services without hand-crafting each query. The page builds search URLs for Google, Bing and Yandex plus username databases (KnowEm, PeekYou, UserSearch, etc.) and email lookups — a fast, low-effort first pass to see where a handle appears before reaching for automated enumerators.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.aware-online.com/en/osint-tools/username-search-tool/.
2. Enter the target `username` in the on-page field.
3. Click the generated buttons/links to run the search on each engine or database (each opens the third-party service).
4. Work through the results per service, noting where the handle resolves to a real profile.
5. Pivot: confirmed `social-profile`s feed avatar reverse-image search; handles that embed a real name/DOB feed name-based people search.

## Inputs → Outputs
- **In:** `username`
- **Out:** search links resolving to `social-profile`s, `name`s and `email` mentions across engines/databases
- **Empty/negative result looks like:** the linked searches all return nothing relevant — the handle isn't indexed on those services. This is a link-builder, so "no result" is really the destination engine's answer, not Aware Online's.

## Gotchas & OpSec
- It generates links, it does not run checks itself — you still click through and read each service manually.
- Coverage equals whatever engines/databases it links; pair with a live enumerator for platform-existence checks.
- OpSec: the link-building is passive, but following the links queries third parties tied to your session — use a puppet browser.

## Overlaps ("do both")
- Pairs with `[[deepfind-me]]` and `[[whatsmyname-app]]` — those actively check platform existence, while this hands you broad search-engine and database queries the automated tools skip.

## Trust & verifiability
`trust: community` — built by a well-regarded OSINT training provider; it is only as good as the third-party engines it points to, so verify each hit on the destination service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | username-search-tool |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
