---
id: seosly-com
name: seosly.com (Google Search Operators guide)
description: Use when you have a `name` or other selector and want to build precise Google dork queries to find it — returns a reference of 50+ working search operators, not data itself.
url: https://seosly.com/google-search-operators/
category: search-engines
path:
- search-engines
bestFor: Looking up the exact, currently-working Google search operator syntax for building people-search dorks.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free article; no paywall or account to read the full operator list.
opsec: passive
opsecNote: This is a reference article you read — it queries nobody. The dorks you then run in Google touch Google (not the target); use a logged-out/sock-puppet browser for the actual searches if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authored and maintained by named SEO practitioner Olga Zarr; a widely-cited, regularly-updated operator reference. It is documentation, not a data source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Google search operators
- Google dorks cheat sheet
tags:
- searchengines
- Search Engines
- dorking
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- seosly-com-2
---

# seosly.com (Google Search Operators guide)

> A maintained, free reference of 50+ currently-working Google search operators — the syntax layer you use to build precise people-finding dorks.

## When to use
You are about to run a Google search for a subject and want it tight, not noisy — narrowing to one site, one filetype, a title match, or an exact phrase. This page is the lookup for *which operators still work* (Google has quietly deprecated several), so you build a correct `site:` / `intitle:` / `filetype:` / `"exact phrase"` query instead of guessing. It is a technique reference, not a database — it returns no data about a person; it teaches you the query that will.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://seosly.com/google-search-operators/ and skim the four sections: basic operators, advanced commands, deprecated ones, and worked examples.
2. Pick operators for your goal, e.g. to find a subject's professional profile: `site:linkedin.com OR site:bayt.com "Full Name" "City"`; to find leaked documents: `filetype:pdf "Full Name"`; to pin a phrase: wrap it in quotes.
3. Note the "deprecated/unreliable" section so you do not waste time on operators Google no longer honours.
4. Run the assembled query in Google (logged-out/sock-puppet browser) and iterate.
5. Pivot: dork hits → the actual profiles/documents feed the rest of your workflow.

## Inputs → Outputs
- **In:** `name` (or any selector you are searching for) — as the value you drop into an operator
- **Out:** `name`, `social-profile` (via the precise Google queries you build; the page itself outputs syntax)
- **Empty/negative result looks like:** N/A for the page (it always loads); an over-narrow dork returns zero Google hits — loosen an operator or drop a term.

## Gotchas & OpSec
- This is documentation: it finds nothing on its own — the leverage is in the queries you then run.
- Google deprecates operators over time; trust this page's "still works" labelling over older cheat-sheets.
- OpSec: reading the guide is passive; run the resulting dorks from a sock-puppet browser so the searches are not tied to you.

## Overlaps ("do both")
- Pairs with every `site:`-style stub in the library (e.g. `[[google-com-62]]` for Bayt.com) — this teaches the syntax those pre-built dork URLs apply.

## Trust & verifiability
`trust: trusted` — a named, maintained practitioner reference that is accurate about current operator behaviour; it is guidance, so verify the *results* of your dorks separately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seosly-com |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
