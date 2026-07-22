---
id: jewish-virtual-library-online
name: Jewish Virtual Library
description: Use when you have a `name` of a notable figure and want a biographical/reference entry — returns `social-profile`-style biography, dates and `associate` links.
url: https://www.jewishvirtuallibrary.org
category: search-engines
path:
- search-engines
bestFor: Looking up biographies and reference entries on notable Jewish figures, Israel and Jewish history.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free online reference library; no account or payment required.
opsec: passive
opsecNote: A public reference site; reading it is passive and reveals nothing to any subject. Only the site's server logs your visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large online reference library published by the American-Israeli Cooperative Enterprise (AICE); an editorial/advocacy encyclopedia — useful reference, not a neutral primary source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Jewish Virtual Library
- jewishvirtuallibrary.org
- JVL
tags:
- reference
- encyclopedia
- biography
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Jewish Virtual Library

> A large online reference encyclopedia on Jewish history, Israel and notable figures — a biographical/context lookup, not a people-search database.

## When to use
Low direct value for tracing an ordinary subject; useful when your case touches a *notable* person, organisation or historical event in Jewish or Israeli history and you need quick biographical context. Entries give dates, life/career summaries, related figures (`associate` links) and source references — helpful for identifying a public figure, confirming a name-to-role link, or building background on an organisation a subject is tied to. The old `/jsource/Bible/...` URL is one corner of a much larger reference site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.jewishvirtuallibrary.org and use its search, or Google-dork `site:jewishvirtuallibrary.org "<name>"`.
2. Open the biography/topic entry and read for dates, roles, affiliations and linked people/organisations.
3. Follow internal cross-links to related figures and events to widen context.
4. Pivot: named `associate`/organisations feed further biographical and archival research; confirmed dates anchor a historical timeline.

## Inputs → Outputs
- **In:** `name` (of a notable figure), or a topic/organisation
- **Out:** biographical `social-profile`-style entry, dates, `associate`/organisation links, source citations
- **Empty/negative result looks like:** no entry — the person/topic isn't notable enough to be covered (the common case for private individuals).

## Gotchas & OpSec
- Covers notable/public subjects only — no use for tracing private individuals.
- Editorial/advocacy encyclopedia (AICE); treat framing as a secondary, potentially partial source and corroborate facts.
- Passive reference lookup; no subject exposure.

## Overlaps ("do both")
- Pairs with Wikipedia and archival/biographical databases — cross-check entries, since coverage, dates and framing differ between reference works.

## Trust & verifiability
`trust: community` — a substantial reference library, but editorially curated with an advocacy remit; good for leads and context, corroborate specifics against primary or neutral sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jewish-virtual-library-online |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
