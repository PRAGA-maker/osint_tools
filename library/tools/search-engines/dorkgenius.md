---
id: dorkgenius
name: DorkGenius
description: Use when you have a target (a `name`, `domain`, filetype, or keyword) and want ready-made advanced search-engine dorks for Google/Bing/DuckDuckGo — returns dork query strings to run.
url: https://dorkgenius.com/
category: search-engines
path:
- search-engines
bestFor: Generating advanced search-engine dork queries from a plain description of what you want to find.
selectorsIn:
- name
- domain
selectorsOut:
- document-id
- social-profile
status: live
pricing: freemium
costNote: Free dork generation on the site; some AI-assisted/advanced features are gated behind paid credits.
opsec: passive
opsecNote: DorkGenius only builds the query strings — it does not run them, so it sees only your prompt, not the target. Running the generated dorks exposes your searches to the search engine, so run them behind a VPN/sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party dork generator; the queries it emits are standard search-operator syntax you can read and verify before running.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Dork Genius
tags:
- google-dorks-tools
- dorking
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# DorkGenius

> A dork builder — describe what you want to surface (exposed documents, a person's profiles, a filetype on a domain) and it returns advanced search-operator queries for Google, Bing, and DuckDuckGo.

## When to use
You know *what* you want to find but not the exact operator syntax: exposed PDFs mentioning a `name`, login pages on a `domain`, indexed directories, a filetype across a site. DorkGenius turns the intent into ready-to-run dorks so you do not hand-craft `site:`/`filetype:`/`intitle:` chains.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dorkgenius.com/.
2. Describe the goal (e.g. "PDFs on example.com mentioning John Smith") and/or pick the target engine.
3. Copy the generated dork string(s).
4. Run them in the chosen engine from a sock-puppet browser; iterate on the wording to refine.
5. Pivot: `document-id` and `social-profile` hits feed document-metadata and profile-enrichment tools.

## Inputs → Outputs
- **In:** `name`/`domain`/keyword/filetype intent
- **Out:** search-engine dork query strings that, when run, surface `document-id`s and `social-profile`s
- **Empty/negative result looks like:** a generated dork that returns nothing when run — refine the operators/terms; the generator gives syntax, not guaranteed hits.

## Gotchas & OpSec
- It generates queries but does not execute them — you still run and vet the dorks yourself.
- Freemium: basic generation is free; advanced/AI features may need credits.
- OpSec: generation is **passive**, but *running* dorks is visible to the engine — use a VPN and pace to avoid CAPTCHAs.

## Overlaps ("do both")
- Pairs with `[[site-dorks]]` (which fans a term across many sites) — use DorkGenius to craft a precise query, sitedorks to broadcast one.

## Trust & verifiability
`trust: community` — a query generator; every dork is transparent operator syntax you can read, verify, and adjust before running.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dorkgenius |
| category | search-engines |
| selectorsIn → selectorsOut | name, domain → document-id, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
