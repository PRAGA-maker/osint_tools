---
id: bool
name: Bool
description: Use when you have a name/username/employer and want to construct precise Boolean search strings (AND/OR/NOT, quotes, site:) for Google/LinkedIn people-sourcing — a query builder, not a data source.
url: https://chromewebstore.google.com/detail/bool-boolean-search-assis/cfpmoigmhcehoegokjllchipdiindpkc
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Building and refining Boolean search strings for people-sourcing across search engines and LinkedIn.
selectorsIn:
- name
- username
- employer-org
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free Chrome/Edge extension; no account required.
opsec: passive
opsecNote: The extension only assembles a query string in your browser — it does not send anything anywhere until you run the search. Running the resulting query is passive against Google/Bing (the target isn't contacted), but LinkedIn searches can leave viewer traces, so run those from a sock-puppet LinkedIn account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A third-party productivity extension aimed at recruiters/sourcers; it constructs queries only, so there is no data-quality risk — just vet the extension's permissions before installing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- advanced-search-operators-list
- dorks-collections-list
aliases:
- Bool Boolean Search Assistant
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Bool

> A browser extension that helps you assemble precise Boolean search strings (AND/OR/NOT, quotes, `site:`) — turning a fuzzy person-search into a surgical query.

## When to use
You have partial identity data — a `name`, `username`, `employer-org`, job title, location — and want to find the subject's profiles/mentions without wading through noise. Bool helps you build the exact Boolean query (grouping synonyms with OR, excluding false positives with NOT, pinning to a domain with `site:`) that a plain keyword search can't express. Especially handy for LinkedIn/X-ray sourcing.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store into a sock-puppet browser profile.
2. Open its query-builder panel and enter your terms — required terms, synonym groups (OR), and exclusions (NOT).
3. Let it produce the assembled Boolean string with correct operators/quoting.
4. Run that string in Google/Bing (or a LinkedIn X-ray via `site:linkedin.com/in`).
5. Pivot: matching results surface `social-profile`s and corroborating `name`/employer details; refine the query and repeat.

## Inputs → Outputs
- **In:** `name`, `username`, `employer-org`, and other partial identifiers
- **Out:** a precise search query that surfaces `social-profile` / `name` results
- **Empty/negative result looks like:** the built query returns nothing — usually over-constrained (too many ANDs); loosen terms or add OR synonyms.

## Gotchas & OpSec
- It builds queries; it finds nothing by itself — the results depend entirely on the engine you run them in.
- Over-tight Boolean logic silently hides real matches; iterate from broad to narrow.
- LinkedIn X-ray results can be viewed via search without logging in, but clicking through logged-in can register a profile view — use a sock-puppet account.

## Overlaps ("do both")
- Pairs with reference lists like `[[advanced-search-operators-list]]` and `[[dorks-collections-list]]` — Bool builds the syntax interactively, those catalogs give you the operator/dork patterns to feed it.

## Trust & verifiability
`trust: community` — a third-party query-builder with no data of its own, so there is no accuracy risk in its output; just confirm the extension's publisher/permissions before installing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bool |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, username, employer-org → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
