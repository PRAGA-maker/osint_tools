---
id: osint-investigation-assistant-lambda-black
name: OSINT Investigation Assistant (lambda.black)
description: Use when you have a name, username, or email and want a single page that generates ready-to-run search queries and tool links across many sources — returns pre-built pivots, not data itself.
url: https://lambda.black/osint.html
category: search-engines
path:
- search-engines
bestFor: Turning one selector into a batch of pre-built search queries/tool links to work through quickly.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free single-page web tool; no account, nothing to install.
opsec: passive
opsecNote: The page builds query URLs in your browser; you decide which to open. Nothing is sent to the subject by the page itself, but each generated query you click hits that third-party engine — apply normal OpSec (sock-puppet session, clean IP) when you follow the links.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A personal/community single-page assistant (a link-and-query generator). It runs no analysis and stores no data — it just constructs searches, so trust concerns are minimal, but coverage depends on whatever links the author maintains.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- lambda.black osint
- lambda black OSINT assistant
tags:
- tool-collection
- query-helper
source: ultimate-osint
lastVerified: '2026-07-21'
enrichment: full
---

# OSINT Investigation Assistant (lambda.black)

> A single self-contained web page that takes one selector and spits out a batch of ready-to-click search queries and tool links across many platforms — a fast "fan-out" launcher, not a data source of its own.

## When to use
You have a starting selector — a `name`, `username`, or `email` — and want to blitz it across many search engines and OSINT sites without hand-typing each query. Paste the selector and the page generates the corresponding pre-built searches (social platforms, search engines, breach/username checkers, etc.), which you open and review. Use it early in an investigation to seed a wide sweep quickly; it saves keystrokes, it doesn't do the analysis.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://lambda.black/osint.html.
2. Enter your selector (name/username/email) into the relevant field.
3. The page builds a set of query links; click through the ones relevant to your case, reviewing each source's results yourself.
4. Treat it as a launchpad — cross off dead ends, keep hits, and move confirmed leads into dedicated tools.
5. Pivot: any `social-profile`/handle you confirm feeds username-enumeration and people-search tooling.

## Inputs → Outputs
- **In:** `name`, `username`, or `email`.
- **Out:** a set of pre-built search/tool links (`social-profile` leads once you open them). The page returns *queries*, not results.
- **Empty/negative result looks like:** the generated searches themselves return nothing — that's the underlying engines' answer, not the assistant's; the tool always builds links regardless.

## Gotchas & OpSec
- Human-in-the-loop: every generated query needs you to open and read it — this is a launcher, so the review work is entirely manual.
- OpSec: **passive** at the page (it builds URLs client-side), but each link you click hits a third-party engine — use a sock-puppet session/clean IP for the actual searches.
- Coverage is only as current as the author's link list; some generated queries may point at moved or dead endpoints. Verify with maintained tools.

## Overlaps ("do both")
- Pairs with dedicated username-enumeration and people-search tools — this fans a selector out fast, while those tools go deep on the hits it surfaces.

## Trust & verifiability
`trust: community` — a lightweight personal/community query-generator with no data of its own and no analysis. Reliability depends on the destination engines; confirm every lead in the source it came from.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-investigation-assistant-lambda-black |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
