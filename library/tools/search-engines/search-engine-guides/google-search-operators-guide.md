---
id: google-search-operators-guide
name: Google Search Operators Guide
description: Use when you have any selector (`name`, `username`, `email`, `phone`, `domain`) and want to build precise Google dorks to surface it — returns operator syntax that sharpens searches into `social-profile`, `document-id`, `email` hits.
url: https://www.googleguide.com/advanced_operators_reference.html
category: search-engines
path:
- search-engines
- search-engine-guides
bestFor: Reference for constructing precise Google dorks (site:, intitle:, filetype:, inurl:, quotes) around a subject selector.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- document-id
- email
status: live
pricing: free
costNote: Free static reference page; the Google searches you then run are also free.
opsec: passive
opsecNote: The guide itself is a static document — reading it leaks nothing. The searches you construct from it are run against Google; use a sock-puppet/logged-out session and avoid clicking through to target-controlled pages that could log your visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing third-party reference (Google Guide by Nancy Blachman); accurate on core operators but last updated in 2022, so some undocumented operators listed may no longer work.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- google-guide-cheat-sheet
aliases:
- Google Guide advanced operators
- googleguide.com
tags:
- google-dorking
- search-operators
- technique-reference
source: arf-seed
lastVerified: '2026-07-20'
enrichment: full
---

# Google Search Operators Guide

> A reference cheat-sheet for Google's advanced operators — the raw material for turning a thin selector into a precise dork.

## When to use
You have a selector (`name`, `username`, `email`, `phone`, `domain`, or a distinctive string) and a plain Google search is too noisy. This page is the operator reference you consult to build a *precise* query — restricting to a site, a file type, a title, or an exact phrase — so the subject's footprint (profiles, leaked documents, cached pages) rises above the noise. It's a technique reference, not a lookup tool: you read it, then run the resulting dork on Google yourself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.googleguide.com/advanced_operators_reference.html.
2. Find the operator you need. Core ones for OSINT:
   - `site:` — restrict to a domain (e.g. `site:linkedin.com "Jane Doe"`).
   - `"..."` — exact phrase (a full name, a rare username, an address line).
   - `filetype:` / `ext:` — surface `document-id`-bearing PDFs/XLS (`filetype:pdf "resume" "Jane Doe"`).
   - `intitle:` / `inurl:` — match handles or names in page titles/URLs.
   - `-term` and `OR` — exclude noise or widen aliases.
3. Compose the dork around your selector and run it on Google (logged-out/sock-puppet session).
4. Iterate: tighten with `site:`/`filetype:`, widen with `OR` across alias spellings.
5. Pivot: hits feed profile enumeration, document review, and reverse-lookups.

## Inputs → Outputs
- **In:** any text selector — `name`, `username`, `email`, `phone`, `domain`
- **Out:** sharper Google result sets pointing to `social-profile`, `document-id` (files), `email` and other footprint
- **Empty/negative result looks like:** a well-formed dork returning nothing usually means the selector isn't indexed under that constraint — loosen the operators before concluding absence.

## Gotchas & OpSec
- Last updated 2022; Google retires/undocuments operators over time, so some listed (e.g. `ext:`, `allinanchor:`, `+`) may behave differently or fail — verify against live Google behavior.
- Over-tight dorks silently return zero; treat empty results as "query too narrow," not "subject not found."
- OpSec: the reference is passive, but run the actual searches from a clean session and be wary of clicking through to pages the target controls.

## Overlaps ("do both")
- Pairs with `[[google-guide-cheat-sheet]]` — this is the full reference; the cheat-sheet is the quick-glance version for rapid dork construction.

## Trust & verifiability
`trust: community` — an authoritative-but-aging third-party reference; the operator concepts are sound, but confirm any exotic operator still works before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-search-operators-guide |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile, document-id, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
