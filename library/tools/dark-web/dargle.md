---
id: dargle
name: Dargle
description: Use when you have a `domain` or keyword and want to search an index of onion/dark-web sites and their metadata — returns matching `domain`s, titles, and timestamps.
url: http://www.dargle.net/search
category: dark-web
path:
- dark-web
bestFor: Keyword/domain searching a crawled index of dark-web sites with title, domain-source, and timestamp columns.
selectorsIn:
- domain
- username
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free web search interface; no account required.
opsec: passive
opsecNote: You query Dargle's own crawled index from the clearnet — you are not visiting the onion sites directly, so this is passive reconnaissance. As with any dark-web search, use a compartmentalised browser/IP and do not enter sensitive case identifiers you wouldn't want logged by a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Small independent dark-web index (listed by uk-osint) with no published methodology; coverage, freshness, and operator are unknown, so treat results as leads only.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Dargle dark web search
tags:
- darkweb
- Dark Web Links
- search
source: uk-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Dargle

> A small clearnet-accessible search interface over a crawled index of dark-web sites, organised by domain, title, source, and timestamp.

## When to use
You want to check whether a `domain`, keyword, or handle appears on indexed dark-web sites without going onto Tor yourself. Dargle's index exposes tables of domains, timestamps, and domain-sources, so it works as a passive first look for dark-web mentions before you commit to visiting anything over Tor. Niche and unverified — use it to surface leads, not to draw conclusions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.dargle.net/search.
2. Enter a `domain`, keyword, or handle in the "Dargle It" box.
3. Review results by Title / Domain / hit-count, and browse the Domains / Timestamps / Domain Sources tables for context on when a site was seen.
4. Pivot: a promising onion `domain` goes to a Tor browser (in a safe environment) or another dark-web index for corroboration.

## Inputs → Outputs
- **In:** `domain`, keyword, or `username`
- **Out:** matching dark-web `domain`s, page titles, sources, and timestamps
- **Empty/negative result looks like:** "0 results" — Dargle's crawl simply hasn't indexed a match; absence says little given its unknown, likely partial coverage.

## Gotchas & OpSec
- Coverage, crawl freshness, and the operator are undocumented — treat every hit as an unverified lead.
- The homepage often shows a blank/0-result state; that's the empty search view, not an error.
- Passive by design (you search the index, not the onions), but keep dark-web hygiene when you follow a lead onto Tor.

## Overlaps ("do both")
- Cross-check against other dark-web search/indexes (Ahmia, Tor66-style directories) — no single dark-web crawler is comprehensive, so run the same selector across several.

## Trust & verifiability
`trust: unverified` — an independent index with no published methodology or provenance; useful only as a lead generator, with every result confirmed elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dargle |
| category | dark-web |
| selectorsIn → selectorsOut | domain, username → domain, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
