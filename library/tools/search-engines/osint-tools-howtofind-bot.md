---
id: osint-tools-howtofind-bot
name: osint-tools (HowToFind-bot)
description: Use when you've exhausted your known tools for a selector and want more options — a categorised catalog of 300+ OSINT tools/scripts to pull additional techniques from.
url: https://github.com/HowToFind-bot/osint-tools
category: search-engines
path:
- search-engines
bestFor: Discovering additional OSINT tools for a given selector or task, organised by category.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free GitHub repository; no account needed to read.
opsec: passive
opsecNote: Passive — it is a static list of links to other tools; browsing it exposes nothing about any target. OpSec considerations belong to whichever downstream tool you pick from it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-curated GitHub catalog (~1.3k stars) pointing to ~308 third-party repos across 24+ categories; it is a signpost, not vetted software, so evaluate each linked tool independently.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- yaseeker
aliases:
- HowToFind-bot osint-tools
tags:
- catalog
- reference
- directory
source: gh-topic-osint-framework
lastVerified: '2026-08-05'
enrichment: full
---

# osint-tools (HowToFind-bot)

> A categorised GitHub catalog of ~300 open-source OSINT tools and scripts — a place to find *more* tooling when your current kit runs dry for a selector.

## When to use
You're stuck on a selector — a `phone`, `username`, `email`, image, plate, wallet, domain — and want to see what other tools exist for it. This is a meta-resource: not a lookup itself, but an index that maps categories (account recon, phone, domains/IPs, crypto, plates, files, network) to concrete tool repositories you can then try.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/HowToFind-bot/osint-tools and read the README.
2. Jump to the category matching your selector/task (e.g. "phone numbers", "usernames", "cryptocurrency").
3. Scan the listed repos; open the ones that fit and evaluate them (activity, stars, last commit) before use.
4. Note the README tip to swap a pinned commit hash for `master` to view the latest version of the list.
5. Pivot: adopt a suitable tool from the list into your workflow — this catalog's output is *other tools*, not data.

## Inputs → Outputs
- **In:** none — you browse by category/need, it takes no selector
- **Out:** links to third-party OSINT tool repositories organised by category
- **Empty/negative result looks like:** a category with only stale/archived repos, or nothing matching your niche need — fall back to a broader awesome-list or a live tool search. Being a static list, it can lag on the newest tools.

## Gotchas & OpSec
- It's a signpost, not vetted software; some linked repos are unmaintained, dead, or of unknown quality — vet each before running.
- Coverage reflects when the list was last updated; brand-new tools may be absent.
- No selector input — don't expect it to "search" anything for you.
- OpSec: passive; the real OpSec assessment happens on whichever downstream tool you choose.

## Overlaps ("do both")
- Complements other tool indexes (awesome-osint, OSINT Framework) — each curator picks a different set, so consult more than one when hunting for a tool for an unusual selector.

## Trust & verifiability
`trust: community` — a popular but crowd-curated catalog; treat every linked repo as unverified until you assess it yourself, and confirm a tool is live and maintained before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-tools-howtofind-bot |
