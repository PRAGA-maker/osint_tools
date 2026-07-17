---
id: ahmia-list-of-onion-domains
name: Ahmia (Tor onion search)
description: Use when you have a keyword, `username` or `domain` and want to find Tor hidden services (.onion) mentioning it — returns onion `domain` addresses to investigate.
url: https://ahmia.fi/
category: search-engines
path:
- search-engines
bestFor: Searching the Tor network's .onion hidden services from the clearnet by keyword or selector.
selectorsIn:
- username
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free clearnet search engine (ahmia.fi); no account. Viewing the .onion results themselves requires the Tor Browser.
opsec: passive
opsecNote: Searching ahmia.fi over clearnet is passive and doesn't touch the hidden services. If you then OPEN an onion result, do it only through Tor Browser (and consider a VM/Tails) — visiting hidden services directly can expose you and is where real risk begins.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, reputable independent Tor search project that filters abuse material; its index is a crawl, so coverage is partial and results should be verified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ahmia
- ahmia-link-graph
aliases:
- ahmia.fi
- Ahmia onion search
tags:
- toddington
- curated-directory
- search-engines
- tor
- darkweb
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Ahmia (Tor onion search)

> A clearnet search engine for Tor's .onion hidden services — the front door for finding dark-web pages by keyword without crawling Tor yourself.

## When to use
You're checking whether a subject, `username`, brand, `domain`, email, or leaked dataset surfaces on the dark web — a marketplace listing, a doxx/paste, a forum handle, a data dump. Ahmia lets you search indexed .onion services from the normal web, so you can scope dark-web exposure before deciding whether to open anything in Tor.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ahmia.fi/ (its verified clearnet address — beware phishing clones).
2. Search a keyword, `username`, `domain`, email, or other distinctive selector.
3. Read the results: titles, snippets, and the onion `domain` addresses where the term appears.
4. To view a result, copy the .onion address into **Tor Browser** (ideally from a hardened VM/Tails), not a normal browser.
5. Pivot: an onion address/handle → cross-reference against other dark-web indexes and your clearnet findings; a matched dataset → breach-analysis workflow.

## Inputs → Outputs
- **In:** keyword, `username`, `domain`, email, or other selector
- **Out:** onion `domain` addresses (hidden-service URLs) plus title/snippet context
- **Empty/negative result looks like:** no results — Ahmia only indexes what its crawler has reached and it deliberately excludes abuse material, so absence is not proof the term isn't on Tor. Try alternate spellings and other onion search engines.

## Gotchas & OpSec
- Coverage is partial and skewed by Ahmia's crawl and content policy; treat "no hits" as inconclusive.
- **Only open onion links through Tor Browser**, and preferably a disposable/VM environment — this is where the real OpSec risk sits, not in the search itself.
- Always start from the verified ahmia.fi address; fake clones exist to phish dark-web searchers.

## Overlaps ("do both")
- Do both with `[[ahmia]]` and `[[ahmia-link-graph]]` (same project, other views) and with other Tor indexes/paste-site searches — each crawler sees a different slice of the network, so run several before concluding a term is absent.

## Trust & verifiability
`trust: community` — a reputable, independently run Tor search project; results are crawler-derived leads (with an anti-abuse filter), so verify any hit by examining the actual hidden service in Tor rather than trusting the snippet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ahmia-list-of-onion-domains |
| category | search-engines |
| selectorsIn → selectorsOut | username, domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
