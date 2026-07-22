---
id: searchdorks
name: SearchDorks
description: Use when you want a ready-made search dork for Google/Shodan/Censys/FOFA/ZoomEye and want to describe your goal in plain English — returns copy-ready dork syntax.
url: https://kriztalz.sh/search-dorks/
category: search-engines
path:
- search-engines
bestFor: Turning a plain-English research goal into correct dork syntax for Google and the major internet-scan engines.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, browser-based, no sign-up and no data stored.
opsec: passive
opsecNote: Generating a dork is passive — it only writes query text in your browser. OpSec risk moves to wherever you then *run* the dork (Google, Shodan, etc.), which logs the search against your session/IP; run sensitive dorks from a sock-puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent single-developer utility; the value is the generated query, which you inspect and can correct before use, so trust rests on your own review of the output.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- domainrecon
- faviconhash
- githubrecon
- metadata-viewer
- pgpkeyanalyser
- traceroutevisualizer
aliases:
- Search Dorks
- kriztalz search-dorks
tags:
- google-dorks-tools
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# SearchDorks

> A natural-language dork generator: describe what you're trying to find, and it emits the correct advanced-search syntax for Google, Shodan, Censys, FOFA or ZoomEye.

## When to use
You know *what* you want to surface — exposed documents mentioning a name, cameras on a subnet, files of a type on a domain — but you don't want to hand-craft the operator soup for each engine. SearchDorks translates the intent into engine-specific dork syntax with a short explanation, so you can review and run it rather than memorising every operator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://kriztalz.sh/search-dorks/.
2. Type your research intent in plain English (e.g. "PDF resumes on example.com containing a phone number").
3. Pick the target engine (Google, Shodan, Censys, FOFA, ZoomEye).
4. Read the generated dork and its explanation; copy it with one click.
5. **Review before running** — confirm the operators match your intent, then paste it into the actual engine (from an appropriate/sock-puppet session).

## Inputs → Outputs
- **In:** a plain-English description of what you want to find + a chosen search engine
- **Out:** copy-ready dork syntax plus an explanation of each operator
- **Empty/negative result looks like:** a vague prompt yields an overly broad dork — tighten the description (add domain, filetype, keywords) and regenerate; the tool produces syntax, not results, so "no hits" happens only when you run the dork.

## Gotchas & OpSec
- It generates queries, it does not execute them — findings quality depends on the engine you paste into.
- Always sanity-check the generated syntax; an AI-generated dork can be subtly wrong or over-broad.
- OpSec: passive at generation; the real footprint is the search you subsequently run, so use a puppet account/IP for sensitive dorks.

## Overlaps ("do both")
- Pairs with any Google-dork collection or an internet-scan engine directly — SearchDorks helps you *author* the query, the engine returns the data; keep a static dork cheat-sheet for operators the generator omits.

## Trust & verifiability
`trust: community` — an independent utility whose output you can (and should) verify by reading the syntax before running it, so correctness is in your hands, not the tool's.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchdorks |
